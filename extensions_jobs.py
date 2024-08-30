import time
from datetime import datetime

from flask import session
from sqlalchemy import desc, or_, exists, and_
from sqlalchemy.orm import load_only, selectinload

from extensions_locations import string_to_location
from extensions_string import clean_search_string, clean_location_string
from models.postgres.api_source import APISource
from models.postgres.company import Company
from models.postgres.experience_level import ExperienceLevel
from models.postgres.listed_job import ListedJob

from extensions_sql import db
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

from models.postgres.listed_job_experience_level import \
    ListedJobExperienceLevel
from models.postgres.locations.listed_job_location import ListedJobLocation
from models.postgres.locations.location import Location
from routines.parsing.find_location import (
    delimit_string,
    find_locations_within_distance_miles,
    order_listed_jobs_location,
    order_listed_jobs_by_location,
    find_locations_within_distance_miles_all_remote,
    find_all_locations_for_country,
    find_all_locations_for_state,
    find_all_locations_for_city,
)
from user_jobs.user_limits import (
    max_jobs_unauthenticated,
    max_jobs_authenticated
)


def clear_previous_job_search():
    if session.get('job_view_id'):
        session.pop('job_view_id', None)

    if session.get('job_company_id'):
        session.pop('job_company_id', None)

    if session.get('job_location_query'):
        session.pop('job_location_query', None)

    if session.get('job_location_distance'):
        session.pop('job_location_distance', None)

    if session.get('job_search_query'):
        session.pop('job_search_query', None)

    if session.get('job_page_number'):
        session.pop('job_page_number', None)


def save_new_search_job(
        job_id: int = None,
        page_number: int = None,
        search_keyword: str = None,
        location_keyword: str = None,
        distance: int = None,
        company_id: int = None):

    clear_previous_job_search()

    if job_id is not None:
        session['job_view_id'] = job_id

    if page_number is not None:
        session['job_page_number'] = page_number

    if search_keyword is not None:
        session['job_search_query'] = search_keyword

    if location_keyword is not None:
        session['job_location_query'] = location_keyword

    if distance is not None:
        session['job_location_distance'] = distance

    if company_id is not None:
        session['job_company_id'] = company_id


def get_listed_job_by_id(job_id: int):
    """
    Query database and get a specific job based on ID.
    """
    if (job_id is None or
            not isinstance(job_id, int) or
            job_id < 0):
        return None

    # Performance check
    start_time = time.time()

    # Database methods are enclosed in a try-except block.
    try:
        # Access ListedJob Table and get row
        result = (
            db.session.query(ListedJob)
            .filter(ListedJob.id == int(job_id))
            .options(
                load_only(
                    ListedJob.id,
                    ListedJob.name,
                    ListedJob.description,
                    ListedJob.salary_currency,
                    ListedJob.min_salary,
                    ListedJob.max_salary,
                    ListedJob.expiration_time_utc,
                    ListedJob.posted_time_utc,
                    ListedJob.api_source_id,
                    ListedJob.company_id
                ),

                selectinload(ListedJob.api_source)
                .load_only(APISource.name),

                selectinload(ListedJob.listed_job_experience_levels)
                .selectinload(ListedJobExperienceLevel.experience_level)
                .load_only(ExperienceLevel.name),

                selectinload(ListedJob.company)
                .load_only(Company.name),

                selectinload(ListedJob.listed_job_location)
                .load_only(ListedJobLocation.location_id)
                .selectinload(ListedJobLocation.listed_job_location)
                .load_only(
                    Location.country_id,
                    Location.state_id,
                    Location.city_id,
                    Location.remote,
                ),

                selectinload(ListedJob.listed_job_location)
                .selectinload(ListedJobLocation.listed_job_location)
                .selectinload(Location.country),

                selectinload(ListedJob.listed_job_location)
                .selectinload(ListedJobLocation.listed_job_location)
                .selectinload(Location.state),

                selectinload(ListedJob.listed_job_location)
                .selectinload(ListedJobLocation.listed_job_location)
                .selectinload(Location.city),
            )
            .first()
        ) if db.session.query(exists().where(
            ListedJob.id == int(job_id))).scalar() else None

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        print(
            f"Process Time: {elapsed_time:.6g} ms", flush=True)

        return result if result is not None else None

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        # raise e
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        # raise e
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        # raise e
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        # raise e
        return None


def get_listed_jobs_paginate(
        page_number: int = 1,
        include_expired: bool = False):
    """
    Query database and get Listed Jobs
    Paginates with n items per request.
    """

    # Unauthenticated users are limited to n items per page.
    max_jobs_per_page = (
        max_jobs_unauthenticated
        if not session.get('user_id', False)
        else max_jobs_authenticated
    )

    # paginate from page number
    if page_number is None or page_number == 0:
        page_number = 1

    if max_jobs_per_page is None or max_jobs_per_page < 2:
        # print("Increasing item count to 2.", flush=True)
        max_jobs_per_page = 2

    sql_offset = (max_jobs_per_page * page_number) - max_jobs_per_page

    # Performance check
    start_time = time.time()

    # Database methods are enclosed in a try-except block.
    try:
        # Access ListedJob Table and get rows
        result = (
            db.session.query(ListedJob)
            .filter(
                ((ListedJob.expiration_time_utc >=
                  datetime.today().date())
                 if not include_expired else True)
            )
            .options(
                load_only(
                    ListedJob.id,
                    ListedJob.name,
                    ListedJob.description,
                    ListedJob.salary_currency,
                    ListedJob.min_salary,
                    ListedJob.max_salary,
                    ListedJob.posted_time_utc,
                    ListedJob.api_source_id,
                    ListedJob.company_id
                ),

                selectinload(ListedJob.api_source)
                .load_only(APISource.name),

                selectinload(ListedJob.listed_job_experience_levels)
                .selectinload(ListedJobExperienceLevel.experience_level)
                .load_only(ExperienceLevel.name),

                selectinload(ListedJob.company)
                .load_only(Company.name),

                selectinload(ListedJob.listed_job_location)
                .load_only(ListedJobLocation.location_id)
                .selectinload(ListedJobLocation.listed_job_location)
                .load_only(
                    Location.country_id,
                    Location.state_id,
                    Location.city_id,
                    Location.remote,
                )
            )
            .order_by(
                desc(
                    ListedJob.posted_time_utc
                )
            )
            .limit(max_jobs_per_page)
            .offset(sql_offset)
            .all()
        )

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        print(f"Process Time: {elapsed_time:.6g} ms", flush=True)

        return result

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        # raise e
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        # raise e
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        # raise e
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        # raise e
        return None


def get_listed_jobs_search_keyword_only_paginate(
        search_keyword: str,
        page_number: int = 1,
        include_expired: bool = False):
    """
    Query database and get Listed Jobs based on a search keyword only.
    Paginates with up to n items per request.
    """

    # Check for valid keyword, then default to normal if invalid.
    # print("Searched Keyword: " + search_keyword, flush=True)
    cleaned_str = clean_search_string(search_keyword)

    if (cleaned_str is None or
            not isinstance(cleaned_str, str) or
            len(cleaned_str) <= 1):
        return None

    # Unauthenticated users are limited to n items per page.
    max_jobs_per_page = (
        max_jobs_unauthenticated
        if not session.get('user_id', False)
        else max_jobs_authenticated
    )

    # paginate from page number
    if (page_number is None or
            page_number == 0):
        page_number = 1

    if (max_jobs_per_page is None or
            max_jobs_per_page < 2):
        # print("Increasing item count to 2.", flush=True)
        max_jobs_per_page = 2

    sql_offset = (max_jobs_per_page * page_number) - max_jobs_per_page

    # Performance check
    start_time = time.time()

    # Database methods are enclosed in a try-except block.
    try:
        search_query = db.func.plainto_tsquery(
            'english',
            cleaned_str
        )
        delimited = delimit_string(input_string=cleaned_str)
        # Access ListedJob Table and get rows
        result = (
            db.session.query(ListedJob)
            .filter(
                and_(
                    ((ListedJob.expiration_time_utc >=
                     datetime.today().date())
                     if not include_expired else True),

                    or_(
                        ListedJob.search_vector_name
                        .op('@@')(search_query),

                        db.func.similarity(
                            ListedJob.name,
                            cleaned_str
                        ) > 0.9,

                        db.func.lower(ListedJob.name).contains(
                            cleaned_str.lower()),

                        or_(*[db.func.lower(ListedJob.name).contains(i.lower())
                            for i in delimited]),
                    )
                )
            )
            .options(
                load_only(
                    ListedJob.id,
                    ListedJob.name,
                    ListedJob.description,
                    ListedJob.salary_currency,
                    ListedJob.min_salary,
                    ListedJob.max_salary,
                    ListedJob.posted_time_utc,
                    ListedJob.api_source_id,
                    ListedJob.company_id
                ),

                selectinload(ListedJob.api_source)
                .load_only(APISource.name),

                selectinload(ListedJob.listed_job_experience_levels)
                .selectinload(ListedJobExperienceLevel.experience_level)
                .load_only(ExperienceLevel.name),

                selectinload(ListedJob.company)
                .load_only(Company.name),

                selectinload(ListedJob.listed_job_location)
                .load_only(ListedJobLocation.location_id)
                .selectinload(ListedJobLocation.listed_job_location)
                .load_only(
                    Location.country_id,
                    Location.state_id,
                    Location.city_id,
                    Location.remote
                )
            )
            .order_by(
                desc(
                    db.func.similarity(
                        ListedJob.name,
                        cleaned_str
                    )
                ),

                desc(
                    db.func.ts_rank_cd(
                        ListedJob.search_vector_name,
                        search_query
                    )
                ),

                desc(
                    ListedJob.posted_time_utc
                )
            )
            .limit(max_jobs_per_page)
            .offset(sql_offset)
            .all()
        )
        # print("Found rows: " + str(len(result)), flush=True)

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        print(
            "Search Keyword: " + search_keyword + " " +
            f"Process Time: {elapsed_time:.6g} ms", flush=True)

        return result

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        # raise e
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        # raise e
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        # raise e
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        # raise e
        return None


def get_listed_jobs_search_location_default_paginate(
        location_keyword: str,
        distance: int = 30,
        page_number: int = 1,
        include_expired: bool = False):
    """
    Query database and get Listed Jobs based on a search keyword only.
    Paginates with up to n items per request.
    """

    # Check for valid keyword, then default to normal if invalid.
    # print("Searched location: " + location_keyword, flush=True)
    cleaned_str = clean_location_string(location_keyword)

    if (cleaned_str is None or
            not isinstance(cleaned_str, str) or
            len(cleaned_str) <= 1):
        return None

    # Unauthenticated users are limited to n items per page.
    max_jobs_per_page = (
        max_jobs_unauthenticated
        if not session.get('user_id', False)
        else max_jobs_authenticated
    )

    # paginate from page number
    if (page_number is None or
            page_number < 0):
        page_number = 1

    if (max_jobs_per_page is None or
            max_jobs_per_page < 2):
        # print("Increasing item count to 2.", flush=True)
        max_jobs_per_page = 2

    if (distance is None or
            not isinstance(distance, int) or
            distance < 0):
        # print("Increasing distance to 0.", flush=True)
        distance = 0

    sql_offset = (max_jobs_per_page * page_number) - max_jobs_per_page

    # Performance check
    start_time = time.time()

    remote_flag = (
        'remote' in cleaned_str.lower()
        if cleaned_str and len(cleaned_str) >= len('remote')
        else False
    )

    # print(cleaned_str, flush=True)

    # Database methods are enclosed in a try-except block.
    try:
        found_location: Location = string_to_location(
            string_to_parse=cleaned_str,
            remote_flag=remote_flag
        )

        # print(str(found_location), flush=True)
        # print("None: " + str(found_location is None), flush=True)
        # print("Instance: " + str(isinstance(found_location, Location)),
        #       flush=True)

        if (found_location is None or
                not isinstance(found_location, Location)):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "location: (" + cleaned_str + ") " +
                  "distance: [" + str(distance) + "] " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        # Only find locations within distance for locations that have a
        # city or a state only, but not a country.
        if (found_location.city_id is not None or
                found_location.state_id is not None):
            location_list = find_locations_within_distance_miles(
                find_latitude=found_location.latitude,
                find_longitude=found_location.longitude,
                distance_miles=distance,
                remote_flag=remote_flag,
            )

        elif remote_flag:
            location_list = find_locations_within_distance_miles_all_remote(
                find_latitude=found_location.latitude,
                find_longitude=found_location.longitude,
                distance_miles=distance,
            )

        else:
            location_list = []

        # print(str(location_list), flush=True)
        # print("Rows: " + str(len(location_list)), flush=True)

        # Retrieve ID only from location_list if there were results.
        # Results are ordered by distance.
        if (location_list is not None and
                isinstance(location_list, list) and
                len(location_list) != 0):
            location_list = [i.id for i in location_list
                             if i is not None and i.id is not None]

        if (found_location is not None and
                found_location.id is not None):
            location_list.append(found_location.id)

        # Debug
        # print("City ID : " + str(found_location.city_id), flush=True)
        # print("State ID : " + str(found_location.state_id), flush=True)
        # print("Country ID : " + str(found_location.country_id), flush=True)
        # print("Subregion ID : " + str(found_location.subregion_id),
        #       flush=True)
        # print("Region ID : " + str(found_location.region_id), flush=True)

        # location_list should at least have the found_location,
        #   or have a found_location.country_id
        #   that can be used to broad-search.
        if ((found_location is None or
             found_location.country_id is None) and
                (location_list is None or
                 not isinstance(location_list, list) or
                 len(location_list) == 0)):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "location: (" + cleaned_str + ") " +
                  "distance: [" + str(distance) + "] " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        # Add broader range search that contain the specified location
        #   regardless of distance.
        if (found_location is not None and
                (found_location.city_id is not None or
                 found_location.state_id is not None or
                 found_location.country_id is not None)):

            # Search for country if state or city is not found.
            if (found_location.state_id is None and
                    found_location.city_id is None and
                    found_location.country_id is not None):
                found_country_locations = find_all_locations_for_country(
                    found_location.country_id)

                # print("Found country locations: " +
                #       str(len(found_city_locations)), flush=True)

                if (found_country_locations is not None and
                        len(found_country_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_country_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_country_locations
                            if (i is not None and
                                i.id is not None)]

            # Search for city if it is specified
            elif found_location.city_id is not None:
                found_city_locations = find_all_locations_for_city(
                    found_location.city_id)

                # print("Found city locations: " +
                #       str(len(found_city_locations)), flush=True)

                if (found_city_locations is not None and
                        len(found_city_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_city_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_city_locations
                            if (i is not None and
                                i.id is not None)]

            # Search for state if it is specified.
            elif found_location.state_id is not None:
                found_state_locations = find_all_locations_for_state(
                    found_location.state_id)

                # print("Found state locations: " +
                #       str(len(found_state_locations)), flush=True)

                if (found_state_locations is not None and 
                        len(found_state_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_state_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_state_locations
                            if (i is not None and
                                i.id is not None)]
        # Debugging
        # print("LOCATION LIST: " + str(location_list), flush=True)

        # If there are no locations, return None
        if (location_list is None or
                not isinstance(location_list, list) or
                len(location_list) == 0):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "Searched location: (" + cleaned_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        # Debugging
        # location_list = convert_raw_locations_id_to_locations(location_list)
        # print(str(location_list), flush=True)

        # Access ListedJob Table and get rows
        result = (
            db.session.query(ListedJobLocation)
            .filter(
                and_(
                    ((ListedJobLocation.listed_job.has(
                        ListedJob.expiration_time_utc >=
                        datetime.today().date()))
                     if not include_expired else True),

                    ListedJobLocation.location_id.in_(
                        location_list if (isinstance(location_list, list) and
                                          len(location_list) != 0) else []
                    )
                )
            )
            .options(
                selectinload(ListedJobLocation.listed_job)
                .selectinload(ListedJob.api_source)
                .load_only(APISource.name),

                selectinload(ListedJobLocation.listed_job)
                .load_only(
                    ListedJob.id,
                    ListedJob.name,
                    ListedJob.description,
                    ListedJob.salary_currency,
                    ListedJob.min_salary,
                    ListedJob.max_salary,
                    ListedJob.posted_time_utc)
                .selectinload(ListedJob.listed_job_experience_levels)
                .selectinload(ListedJobExperienceLevel.experience_level)
                .load_only(ExperienceLevel.name),

                selectinload(ListedJobLocation.listed_job)
                .selectinload(ListedJob.company)
                .load_only(Company.name),

                selectinload(ListedJobLocation.listed_job_location)
                .load_only(
                    Location.country_id,
                    Location.state_id,
                    Location.city_id,
                    Location.remote)
            )
            .limit(max_jobs_per_page)
            .offset(sql_offset)
            .all()
        )
        # re-organize by order in list
        if (result is None or
                len(result) == 0 or
                not isinstance(result, list)):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "location: (" + cleaned_str + ") " +
                  "distance: [" + str(distance) + "] " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        result = order_listed_jobs_location(
            listed_job_locations=result,
            location_list=location_list
        )

        result = [i.listed_job for i in result]

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        print("Searched "
              "location: (" + cleaned_str + ") " +
              "distance: [" +
              (str(distance) if distance is not None else '') +
              "] " +
              f"Process Time: {elapsed_time:.6g} ms", flush=True)

        return result

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        # raise e
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        # raise e
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        # raise e
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        # raise e
        return None


def get_listed_jobs_keyword_location_paginate_old(
        search_keyword: str,
        location_keyword: str,
        distance: int = 30,
        page_number: int = 1,
        include_expired: bool = False):
    """
    Query database and get Listed Jobs based on keyword and location
    Paginates with up to n items per request.
    Slow query, adds 5 seconds due to selectinload options
    rather than lazy loading
    """
    cleaned_search_str = clean_search_string(search_keyword)

    invalid_search = (cleaned_search_str is None or
                      not isinstance(cleaned_search_str, str) or
                      len(cleaned_search_str) <= 1)

    cleaned_location_str = clean_location_string(location_keyword)

    invalid_location = (cleaned_location_str is None or
                        not isinstance(cleaned_location_str, str) or
                        len(cleaned_location_str) <= 1)

    invalid_distance = (distance is None or
                        not isinstance(distance, int) or
                        distance < 0)

    if (invalid_search and
            invalid_location):
        # Return default
        return None

    elif (invalid_search and
          not invalid_location):
        # return get_listed_jobs_search_location_default_paginate(
        #     location_keyword=location_keyword,
        #     page_number=page_number)
        return None

    elif (invalid_location and
          not invalid_search):
        return None

    if invalid_distance:
        distance = 30

    # Unauthenticated users are limited to n items per page.
    max_jobs_per_page = (
        max_jobs_unauthenticated
        if not session.get('user_id', False)
        else max_jobs_authenticated
    )

    # paginate from page number
    if (page_number is None or
            page_number < 0):
        page_number = 1

    if (max_jobs_per_page is None or
            max_jobs_per_page < 2):
        # print("Increasing item count to 2.", flush=True)
        max_jobs_per_page = 2

    sql_offset = (max_jobs_per_page * page_number) - max_jobs_per_page

    # Performance check
    start_time = time.time()

    remote_flag = (
        'remote' in cleaned_location_str.lower()
        if (cleaned_location_str and
            len(cleaned_location_str) >= len('remote'))
        else False
    )

    # Database methods are enclosed in a try-except block.
    try:
        found_location: Location = string_to_location(
            string_to_parse=cleaned_location_str,
            remote_flag=remote_flag,
        )

        print(str(found_location), flush=True)
        # print("None: " + str(found_location is None), flush=True)
        # print("Instance: " + str(isinstance(found_location, Location)),
        #       flush=True)

        if (found_location is None or
                not isinstance(found_location, Location)):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "Searched location: (" + cleaned_location_str + ") " +
                  "Searched keyword: (" + cleaned_search_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        # Only find locations within distance for locations that have a
        # city or a state only, but not a country.
        if (found_location.city_id is not None and
                found_location.country_id is not None):
            location_list = find_locations_within_distance_miles(
                find_latitude=found_location.latitude,
                find_longitude=found_location.longitude,
                distance_miles=distance,
                remote_flag=remote_flag,
            )

        elif remote_flag:
            location_list = find_locations_within_distance_miles_all_remote(
                find_latitude=found_location.latitude,
                find_longitude=found_location.longitude,
                distance_miles=distance,
            )

        else:
            location_list = []

        # print(str(location_list), flush=True)
        # print("Rows: " + str(len(location_list)), flush=True)

        # Retrieve ID only from location_list if there were results.
        # Results are ordered by distance.
        if (location_list is not None and
                isinstance(location_list, list) and
                len(location_list) != 0):
            location_list = [i.id for i in location_list
                             if i is not None and i.id is not None]

        if (found_location is not None and
                found_location.id is not None):
            location_list.append(found_location.id)

        # Debug
        # print("City ID : " + str(found_location.city_id), flush=True)
        # print("State ID : " + str(found_location.state_id), flush=True)
        # print("Country ID : " + str(found_location.country_id), flush=True)
        # print("Subregion ID : " + str(found_location.subregion_id),
        #       flush=True)
        # print("Region ID : " + str(found_location.region_id), flush=True)

        # location_list should at least have the found_location,
        #   or have a found_location.country_id
        #   that can be used to broad-search.
        if ((found_location is None or
             found_location.country_id is None) and
                (location_list is None or
                 not isinstance(location_list, list) or
                 len(location_list) == 0)):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "Searched location: (" + cleaned_location_str + ") " +
                  "Searched keyword: (" + cleaned_search_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        # Add broader range search that contain the specified location
        #   regardless of distance.
        if (found_location is not None and
                (found_location.city_id is not None or
                 found_location.state_id is not None or
                 found_location.country_id is not None)):

            # Search for country if state or city is not found.
            if (found_location.state_id is None and
                    found_location.city_id is None and
                    found_location.country_id is not None):
                found_country_locations = find_all_locations_for_country(
                    found_location.country_id)

                # print("Found country locations: " +
                #       str(len(found_city_locations)), flush=True)

                if (found_country_locations is not None and
                        len(found_country_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_country_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_country_locations
                            if (i is not None and
                                i.id is not None)]

            # Search for city if it is specified
            elif found_location.city_id is not None:
                found_city_locations = find_all_locations_for_city(
                    found_location.city_id)

                # print("Found city locations: " +
                #       str(len(found_city_locations)), flush=True)

                if (found_city_locations is not None and
                        len(found_city_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_city_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_city_locations
                            if (i is not None and
                                i.id is not None)]

            # Search for state if it is specified.
            elif found_location.state_id is not None:
                found_state_locations = find_all_locations_for_state(
                    found_location.state_id
                )

                # print("Found state locations: " +
                #       str(len(found_state_locations)), flush=True)

                if (found_state_locations is not None and
                        len(found_state_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_state_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_state_locations
                            if (i is not None and
                                i.id is not None)]

        # Debugging
        # print("LOCATION LIST: " + str(location_list), flush=True)
        # print("Location Rows: " + str(len(location_list)), flush=True)
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(f"Checkpoint Time: {elapsed_time:.6g} ms", flush=True)

        # If there are no locations, return None
        if (location_list is None or
                not isinstance(location_list, list) or
                len(location_list) == 0):
            # if the distance is invalid,
            # run this function without distance value.
            # Return None instead.
            if not invalid_distance:
                # return get_listed_jobs_keyword_location_paginate_fast(
                #     search_keyword=search_keyword,
                #     location_keyword=location_keyword,
                #     page_number=page_number
                # )

                # db.session.close()
                # return None
                pass

            # return get_listed_jobs_search_keyword_only_paginate(
            #     search_keyword=search_keyword,
            #     page_number=page_number)
            db.session.close()
            return None

        search_query = db.func.plainto_tsquery('english', cleaned_search_str)

        listed_jobs_in_location = (
            db.session.query(ListedJobLocation)
            .filter(
                and_(
                    ListedJobLocation.location_id.in_(location_list),

                    ((ListedJobLocation.listed_job.has(
                        ListedJob.expiration_time_utc >=
                        datetime.today().date()))
                     if not include_expired else True),
                ),
            )
            .options(
                selectinload(ListedJobLocation.listed_job)
                .selectinload(ListedJob.api_source)
                .load_only(APISource.name),

                selectinload(ListedJobLocation.listed_job)
                .load_only(
                    ListedJob.id,
                    ListedJob.name,
                    ListedJob.description,
                    ListedJob.salary_currency,
                    ListedJob.min_salary,
                    ListedJob.max_salary,
                    ListedJob.posted_time_utc)
                .selectinload(ListedJob.listed_job_experience_levels)
                .selectinload(ListedJobExperienceLevel.experience_level)
                .load_only(ExperienceLevel.name),

                selectinload(ListedJobLocation.listed_job)
                .selectinload(ListedJob.company)
                .load_only(Company.name),

                selectinload(ListedJobLocation.listed_job_location)
                .load_only(
                    Location.country_id,
                    Location.state_id,
                    Location.city_id,
                    Location.remote)
            )
            .all()
        )

        print("Listed Job Rows: " + str(len(listed_jobs_in_location)),
              flush=True)
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(f"Checkpoint Time: {elapsed_time:.6g} ms", flush=True)

        # re-organize by order in list
        if (listed_jobs_in_location is None or
                len(listed_jobs_in_location) == 0 or
                not isinstance(listed_jobs_in_location, list)):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "location: (" + cleaned_location_str + ") " +
                  "distance: [" + str(distance) + "] " +
                  "Searched keyword: (" + cleaned_search_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        # Get location ID unsorted
        listed_jobs_in_location = [i.listed_job_id
                                   for i in listed_jobs_in_location]

        # print(str(listed_jobs_in_location), flush=True)
        # Access ListedJob Table and get rows
        # searches based on query and if in location list.
        # then reorders the jobs retrieved based on position in location list.
        result = (
            db.session.query(ListedJob)
            .filter(
                and_(
                    # Search only within location
                    ListedJob.id.in_(listed_jobs_in_location),

                    ((ListedJob.expiration_time_utc >=
                      datetime.today().date())
                     if not include_expired else True),

                    or_(
                        ListedJob.search_vector_name
                        .op('@@')(search_query),

                        db.func.similarity(
                            ListedJob.name,
                            cleaned_search_str
                        ) > 0.9,

                        db.func.lower(ListedJob.name)
                        .contains(cleaned_search_str.lower()),

                        or_(*[db.func.lower(ListedJob.name).contains(i.lower())
                            for i in delimit_string(
                                input_string=cleaned_search_str)]),
                    ),
                )
            )
            .options(
                load_only(
                    ListedJob.id,
                    ListedJob.name,
                    ListedJob.description,
                    ListedJob.salary_currency,
                    ListedJob.min_salary,
                    ListedJob.max_salary,
                    ListedJob.posted_time_utc,
                    ListedJob.api_source_id,
                    ListedJob.company_id
                ),

                selectinload(ListedJob.api_source)
                .load_only(APISource.name),

                selectinload(ListedJob.listed_job_experience_levels)
                .selectinload(ListedJobExperienceLevel.experience_level)
                .load_only(ExperienceLevel.name),

                selectinload(ListedJob.company)
                .load_only(Company.name),

                selectinload(ListedJob.listed_job_location)
                .load_only(ListedJobLocation.location_id)
                .selectinload(ListedJobLocation.listed_job_location)
                .load_only(
                    Location.country_id,
                    Location.state_id,
                    Location.city_id,
                    Location.remote,
                )
            )
            .order_by(
                desc(
                    db.func.similarity(
                        ListedJob.name,
                        cleaned_search_str
                    )
                ),
                desc(
                    db.func.ts_rank_cd(
                        ListedJob.search_vector_name,
                        search_query)
                ),
                desc(
                    ListedJob.posted_time_utc
                ),
            )
            .limit(max_jobs_per_page)
            .offset(sql_offset)
            .all()
        )

        # re-organize by order in list
        result = order_listed_jobs_by_location(
            listed_jobs=result,
            location_list=location_list)

        # result = [i.listed_job for i in result]

        # print("Found rows: " + str(result), flush=True)
        # print("Found rows: " + str(len(result)), flush=True)

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(
            "Searched "
            "location: (" + cleaned_location_str + ") " +
            "distance: [" + str(distance) + "] " +
            f"Process Time: {elapsed_time:.6g} ms", flush=True)

        return result

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        # raise e
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        # raise e
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        # raise e
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        # raise e
        return None


def get_listed_jobs_keyword_location_paginate_fast(
        search_keyword: str,
        location_keyword: str,
        distance: int = 30,
        page_number: int = 1,
        include_expired: bool = False):
    """
    Query database and get Listed Jobs based on keyword and location
    Paginates with up to n items per request.
    """
    cleaned_search_str = clean_search_string(search_keyword)

    invalid_search = (cleaned_search_str is None or
                      not isinstance(cleaned_search_str, str) or
                      len(cleaned_search_str) <= 1)

    cleaned_location_str = clean_location_string(location_keyword)

    invalid_location = (cleaned_location_str is None or
                        not isinstance(cleaned_location_str, str) or
                        len(cleaned_location_str) <= 1)

    invalid_distance = (distance is None or
                        not isinstance(distance, int) or
                        distance < 0)

    if (invalid_search and
            invalid_location):
        return None

    elif (invalid_search and
          not invalid_location):
        # return get_listed_jobs_search_location_default_paginate(
        #     location_keyword=location_keyword,
        #     page_number=page_number)
        return None

    elif (invalid_location and
          not invalid_search):
        # return get_listed_jobs_search_keyword_only_paginate(
        #     search_keyword=search_keyword,
        #     page_number=page_number)
        return None

    if invalid_distance:
        distance = 30

    # Unauthenticated users are limited to n items per page.
    max_jobs_per_page = (
        max_jobs_unauthenticated
        if not session.get('user_id', False)
        else max_jobs_authenticated
    )

    # paginate from page number
    if (page_number is None or
            page_number < 0):
        page_number = 1

    if (max_jobs_per_page is None or
            max_jobs_per_page < 2):
        # print("Increasing item count to 2.", flush=True)
        max_jobs_per_page = 2

    sql_offset = (max_jobs_per_page * page_number) - max_jobs_per_page

    # Performance check
    start_time = time.time()

    remote_flag = (
        'remote' in cleaned_location_str.lower()
        if (cleaned_location_str and
            len(cleaned_location_str) >= len('remote'))
        else False
    )

    # Database methods are enclosed in a try-except block.
    try:
        found_location: Location = string_to_location(
            string_to_parse=cleaned_location_str,
            remote_flag=remote_flag,
        )

        # end_time = time.time()
        # elapsed_time = (end_time - start_time) * 1000
        # print(f"Checkpoint #1 Time: {elapsed_time:.6g} ms", flush=True)

        # print(str(found_location), flush=True)
        # print("None: " + str(found_location is None), flush=True)
        # print("Instance: " + str(isinstance(found_location, Location)),
        #       flush=True)

        if (found_location is None or
                not isinstance(found_location, Location)):
            db.session.close()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "Searched location: (" + cleaned_location_str + ") " +
                  "Searched keyword: (" + cleaned_search_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            return None

        # Only find locations within distance for locations that have a
        # city or a state only, but not a country.
        if (found_location.city_id is not None or
                found_location.state_id is not None):
            if remote_flag:
                location_list = find_locations_within_distance_miles_all_remote(
                    find_latitude=found_location.latitude,
                    find_longitude=found_location.longitude,
                    distance_miles=distance,
                )
            else:
                location_list = find_locations_within_distance_miles(
                    find_latitude=found_location.latitude,
                    find_longitude=found_location.longitude,
                    distance_miles=distance,
                    remote_flag=remote_flag,
                )

        elif remote_flag:
            print("Calling remote function")
            location_list = find_locations_within_distance_miles_all_remote(
                find_latitude=found_location.latitude,
                find_longitude=found_location.longitude,
                distance_miles=distance,
            )

        else:
            location_list = []

        # end_time = time.time()
        # elapsed_time = (end_time - start_time) * 1000
        # print(f"Checkpoint #2 Time: {elapsed_time:.6g} ms", flush=True)

        # print(str(location_list))
        # print("Rows: " + str(len(location_list)), flush=True)

        # Retrieve ID only from location_list if there were results.
        # Results are ordered by distance.
        if (location_list is not None and
                isinstance(location_list, list) and
                len(location_list) != 0):
            location_list = [i.id for i in location_list
                             if i is not None and i.id is not None]

        if (found_location is not None and
                found_location.id is not None):
            location_list.append(found_location.id)

        # Debug
        # print("City ID : " + str(found_location.city_id), flush=True)
        # print("State ID : " + str(found_location.state_id), flush=True)
        # print("Country ID : " + str(found_location.country_id), flush=True)
        # print("Subregion ID : " + str(found_location.subregion_id),
        #       flush=True)
        # print("Region ID : " + str(found_location.region_id), flush=True)

        # location_list should at least have the found_location,
        #   or have a found_location.country_id
        #   that can be used to broad-search.
        if ((found_location is None or
             found_location.country_id is None) and
                (location_list is None or
                 not isinstance(location_list, list) or
                 len(location_list) == 0)):
            db.session.close()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "Searched location: (" + cleaned_location_str + ") " +
                  "Searched keyword: (" + cleaned_search_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            return None

        # Add broader range search that contain the specified location
        #   regardless of distance.
        if (found_location is not None and
                (found_location.city_id is not None or
                 found_location.state_id is not None or
                 found_location.country_id is not None)):

            # Search for country if state or city is not found.
            if (found_location.state_id is None and
                    found_location.city_id is None and
                    found_location.country_id is not None):
                found_country_locations = find_all_locations_for_country(
                    found_location.country_id)

                # print("Found country locations: " +
                #       str(len(found_city_locations)), flush=True)

                if (found_country_locations is not None and
                        len(found_country_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_country_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_country_locations
                            if (i is not None and
                                i.id is not None)]

            # Search for city if it is specified
            elif found_location.city_id is not None:
                found_city_locations = find_all_locations_for_city(
                    found_location.city_id)

                # print("Found city locations: " +
                #       str(len(found_city_locations)), flush=True)

                if (found_city_locations is not None and
                        len(found_city_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_city_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_city_locations
                            if (i is not None and
                                i.id is not None)]

            # Search for state if it is specified.
            elif found_location.state_id is not None:
                found_state_locations = find_all_locations_for_state(
                    found_location.state_id)

                # print("Found state locations: " +
                #       str(len(found_state_locations)), flush=True)

                if (found_state_locations is not None and
                        len(found_state_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_state_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_state_locations
                            if (i is not None and
                                i.id is not None)]

        # Debugging
        # print("LOCATION LIST: " + str(location_list), flush=True)
        # print("Location Rows: " + str(len(location_list)), flush=True)
        # end_time = time.time()
        # elapsed_time = (end_time - start_time) * 1000
        # print(f"Checkpoint #3 Time: {elapsed_time:.6g} ms", flush=True)

        # If there are no locations, return None
        if (location_list is None or
                not isinstance(location_list, list) or
                len(location_list) == 0):
            # if not invalid_distance:
            #     return get_listed_jobs_keyword_location_paginate_fast(
            #         search_keyword=search_keyword,
            #         location_keyword=location_keyword,
            #         page_number=page_number
            #     )

            # return get_listed_jobs_search_keyword_only_paginate(
            #     search_keyword=search_keyword,
            #     page_number=page_number)
            db.session.close()
            return None

        search_query = db.func.plainto_tsquery('english', cleaned_search_str)

        listed_jobs_in_location = (
            db.session.query(ListedJobLocation.listed_job_id)
            .filter(
                and_(
                    ListedJobLocation.location_id.in_(location_list),

                    ((ListedJobLocation.listed_job.has(
                        ListedJob.expiration_time_utc >=
                        datetime.today().date()))
                     if not include_expired else True),
                ),
            )
            .all()
        )

        # print("Listed Job Rows: " + str(len(listed_jobs_in_location)),
        #       flush=True)
        # end_time = time.time()
        # elapsed_time = (end_time - start_time) * 1000
        # print(f"Checkpoint #4 Time: {elapsed_time:.6g} ms", flush=True)

        # re-organize by order in list
        if (listed_jobs_in_location is None or
                len(listed_jobs_in_location) == 0 or
                not isinstance(listed_jobs_in_location, list)):
            db.session.close()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "location: (" + cleaned_location_str + ") " +
                  "distance: [" + str(distance) + "] " +
                  "Searched keyword: (" + cleaned_search_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            return None

        # Get location ID unsorted
        listed_jobs_in_location = [i.listed_job_id
                                   for i in listed_jobs_in_location]

        # end_time = time.time()
        # elapsed_time = (end_time - start_time) * 1000
        # print(f"Checkpoint #5 Time: {elapsed_time:.6g} ms", flush=True)

        # print(str(listed_jobs_in_location), flush=True)
        # Access ListedJob Table and get rows
        # searches based on query and if in location list.
        # then reorders the jobs retrieved based on position in location list.
        result = (
            db.session.query(ListedJob)
            .filter(
                and_(
                    # Search only within location
                    ListedJob.id.in_(listed_jobs_in_location),

                    ((ListedJob.expiration_time_utc >=
                      datetime.today().date())
                     if not include_expired else True),

                    or_(
                        ListedJob.search_vector_name
                        .op('@@')(search_query),

                        db.func.similarity(
                            ListedJob.name,
                            cleaned_search_str
                        ) > 0.9,

                        db.func.lower(ListedJob.name)
                        .contains(cleaned_search_str.lower()),

                        or_(*[db.func.lower(ListedJob.name).contains(i.lower())
                            for i in delimit_string(
                                input_string=cleaned_search_str)]),
                    ),
                )
            )
            .options(
                load_only(
                    ListedJob.id,
                    ListedJob.name,
                    ListedJob.description,
                    ListedJob.salary_currency,
                    ListedJob.min_salary,
                    ListedJob.max_salary,
                    ListedJob.posted_time_utc,
                    ListedJob.api_source_id,
                    ListedJob.company_id
                ),

                selectinload(ListedJob.api_source)
                .load_only(APISource.name),

                selectinload(ListedJob.listed_job_experience_levels)
                .selectinload(ListedJobExperienceLevel.experience_level)
                .load_only(ExperienceLevel.name),

                selectinload(ListedJob.company)
                .load_only(Company.name),

                selectinload(ListedJob.listed_job_location)
                .load_only(ListedJobLocation.location_id)
                .selectinload(ListedJobLocation.listed_job_location)
                .load_only(
                    Location.country_id,
                    Location.state_id,
                    Location.city_id,
                    Location.remote,
                )
            )
            .order_by(
                desc(
                    db.func.similarity(
                        ListedJob.name,
                        cleaned_search_str
                    )
                ),
                desc(
                    db.func.ts_rank_cd(
                        ListedJob.search_vector_name,
                        search_query
                    )
                ),
                desc(
                    ListedJob.posted_time_utc
                ),
            )
            .limit(max_jobs_per_page)
            .offset(sql_offset)
            .all()
        )

        # end_time = time.time()
        # elapsed_time = (end_time - start_time) * 1000
        # print(f"Checkpoint #6 Time: {elapsed_time:.6g} ms", flush=True)

        # re-organize by order in list
        result = order_listed_jobs_by_location(
            listed_jobs=result,
            location_list=location_list
        )

        # end_time = time.time()
        # elapsed_time = (end_time - start_time) * 1000
        # print(f"Checkpoint #7 Time: {elapsed_time:.6g} ms", flush=True)

        # result = [i.listed_job for i in result]

        # print("Found rows: " + str(result), flush=True)
        # print("Found rows: " + str(len(result)), flush=True)

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(
            "Searched "
            "location: (" + cleaned_location_str + ") " +
            "distance: [" + str(distance) + "] " +
            f"Process Time: {elapsed_time:.6g} ms", flush=True)

        return result

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        # raise e
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        # raise e
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        # raise e
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        # raise e
        return None


def get_company_jobs_paginate(
        company_id: int,
        page_number: int = 1,
        include_expired: bool = False):
    """
    Query database and get Listed Jobs
    Paginates with n items per request.
    """
    if (company_id is None or
            company_id < 0):
        return None

    # Unauthenticated users are limited to n items per page.
    max_jobs_per_page = (
        max_jobs_unauthenticated
        if not session.get('user_id', False)
        else max_jobs_authenticated
    )

    # paginate from page number
    if (page_number is None or
            page_number == 0):
        page_number = 1

    if (max_jobs_per_page is None or
            max_jobs_per_page < 2):
        # print("Increasing item count to 2.", flush=True)
        max_jobs_per_page = 2

    sql_offset = (max_jobs_per_page * page_number) - max_jobs_per_page

    # Performance check
    start_time = time.time()

    # Database methods are enclosed in a try-except block.
    try:

        # Access ListedJob Table and get rows
        result = (
            db.session.query(ListedJob)
            .filter(
                and_(
                    ListedJob.company_id == int(company_id),

                    ((ListedJob.expiration_time_utc >=
                      datetime.today().date())
                     if not include_expired else True),
                )
            )
            .options(
                load_only(
                    ListedJob.id,
                    ListedJob.name,
                    ListedJob.description,
                    ListedJob.salary_currency,
                    ListedJob.min_salary,
                    ListedJob.max_salary,
                    ListedJob.posted_time_utc,
                    ListedJob.api_source_id,
                    ListedJob.company_id
                ),

                selectinload(ListedJob.api_source)
                .load_only(APISource.name),

                selectinload(ListedJob.listed_job_experience_levels)
                .selectinload(ListedJobExperienceLevel.experience_level)
                .load_only(ExperienceLevel.name),

                selectinload(ListedJob.company)
                .load_only(Company.name),

                selectinload(ListedJob.listed_job_location)
                .load_only(ListedJobLocation.location_id)
                .selectinload(ListedJobLocation.listed_job_location)
                .load_only(
                    Location.country_id,
                    Location.state_id,
                    Location.city_id,
                    Location.remote,
                )
            )
            .order_by(
                desc(
                    ListedJob.posted_time_utc
                )
            )
            .limit(max_jobs_per_page)
            .offset(sql_offset)
            .all()

        ) if db.session.query(
            exists().where(
                and_(
                    ListedJob.company_id == int(company_id),
                    ((ListedJob.expiration_time_utc >=
                      datetime.today().date())
                     if not include_expired else True),
                ),
            )).scalar() else None

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(
            f"Process Time: {elapsed_time:.6g} ms", flush=True)

        return result if result is not None else None

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        # raise e
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        # raise e
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        # raise e
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        # raise e
        return None


def get_company_jobs_searched_only_paginate(
        company_id: int,
        search_keyword: str,
        page_number: int = 1,
        include_expired: bool = False):
    """
    Query database and get Listed Jobs based on a search keyword only based
    on a specific Company.
    Paginates with up to n items per request.
    """
    if (company_id is None or
            company_id < 0):
        return None

    # Check for valid keyword, then default to normal if invalid.
    # print("Searched Keyword: " + search_keyword, flush=True)
    cleaned_str = clean_search_string(search_keyword)

    # Return None if cleaned string is empty.
    if (cleaned_str is None or
            not isinstance(cleaned_str, str) or
            len(cleaned_str) <= 1):
        # return get_company_jobs_paginate(
        #     company_id=company_id,
        #     page_number=page_number)
        return None

    # print("Searched Term: (" + cleaned_str + ")", flush=True)

    # Unauthenticated users are limited to n items per page.
    max_jobs_per_page = (
        max_jobs_unauthenticated
        if not session.get('user_id', False)
        else max_jobs_authenticated
    )

    # paginate from page number
    if (page_number is None or
            page_number == 0):
        page_number = 1

    if (max_jobs_per_page is None or
            max_jobs_per_page < 2):
        # print("Increasing item count to 2.", flush=True)
        max_jobs_per_page = 2

    sql_offset = (max_jobs_per_page * page_number) - max_jobs_per_page

    # Performance check
    start_time = time.time()

    # Database methods are enclosed in a try-except block.
    try:
        search_query = db.func.plainto_tsquery('english', cleaned_str)

        delimited = delimit_string(input_string=cleaned_str)
        # Access ListedJob Table and get rows
        result = (
            db.session.query(ListedJob)
            .filter(
                and_(
                    ListedJob.company_id == int(company_id),

                    ((ListedJob.expiration_time_utc >=
                      datetime.today().date())
                     if not include_expired else True),

                    or_(
                        ListedJob.search_vector_name
                        .op('@@')(search_query),

                        db.func.similarity(ListedJob.name, cleaned_str) > 0.9,

                        db.func.lower(ListedJob.name).contains(
                            cleaned_str.lower()
                        ),

                        or_(*[db.func.lower(ListedJob.name)
                            .contains(i.lower())
                            for i in delimited]),
                    )
                )
            )
            .options(
                load_only(
                    ListedJob.id,
                    ListedJob.name,
                    ListedJob.description,
                    ListedJob.salary_currency,
                    ListedJob.min_salary,
                    ListedJob.max_salary,
                    ListedJob.posted_time_utc,
                    ListedJob.api_source_id,
                    ListedJob.company_id
                ),

                selectinload(ListedJob.api_source)
                .load_only(APISource.name),

                selectinload(ListedJob.listed_job_experience_levels)
                .selectinload(ListedJobExperienceLevel.experience_level)
                .load_only(ExperienceLevel.name),

                selectinload(ListedJob.company)
                .load_only(Company.name),

                selectinload(ListedJob.listed_job_location)
                .load_only(ListedJobLocation.location_id)
                .selectinload(ListedJobLocation.listed_job_location)
                .load_only(
                    Location.country_id,
                    Location.state_id,
                    Location.city_id,
                    Location.remote,
                )
            )
            .order_by(
                desc(
                    db.func.similarity(
                        ListedJob.name,
                        cleaned_str
                    )
                ),

                desc(
                    db.func.ts_rank_cd(
                        ListedJob.search_vector_name,
                        search_query
                    )
                ),

                desc(
                    ListedJob.posted_time_utc
                )
            )
            .limit(max_jobs_per_page)
            .offset(sql_offset)
            .all()
        )
        # print("Found rows: " + str(len(result)), flush=True)

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(
            "Searched string: (" + cleaned_str + ") " +
            f"Process Time: {elapsed_time:.6g} ms", flush=True)

        return result

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        # raise e
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        # raise e
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        # raise e
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        # raise e
        return None


def get_company_jobs_location_only_paginate(
        company_id: int,
        location_keyword: str,
        distance: int = 30,
        page_number: int = 1,
        include_expired: bool = False):
    """
    Query database and get Listed Jobs based on a location keyword only based
    on a specific Company.
    Paginates with up to n items per request.
    """
    if (company_id is None or
            company_id < 0):
        return None

    # Check for valid location
    cleaned_str = clean_location_string(location_keyword)
    # print("Searched location: " + cleaned_str, flush=True)

    if (cleaned_str is None or
            not isinstance(cleaned_str, str) or
            len(cleaned_str) <= 1):
        return None

    # Unauthenticated users are limited to n items per page.
    max_jobs_per_page = (
        max_jobs_unauthenticated
        if not session.get('user_id', False)
        else max_jobs_authenticated
    )

    # paginate from page number
    if (page_number is None or
            page_number <= 0):
        page_number = 1

    if (max_jobs_per_page is None or
            max_jobs_per_page < 2):
        # print("Increasing item count to 2.", flush=True)
        max_jobs_per_page = 2

    if (distance is None or
            not isinstance(distance, int) or
            distance < 0):
        # print("Increasing distance to 0.", flush=True)
        distance = 0

    sql_offset = (max_jobs_per_page * page_number) - max_jobs_per_page

    # Performance check
    start_time = time.time()

    remote_flag = (
        'remote' in cleaned_str.lower()
        if cleaned_str and len(cleaned_str) >= len('remote')
        else False
    )

    # Database methods are enclosed in a try-except block.
    try:
        found_location: Location = string_to_location(
            string_to_parse=cleaned_str,
            remote_flag=remote_flag
        )

        # print(str(found_location), flush=True)

        if (found_location is None or
                not isinstance(found_location, Location)):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "Searched location: (" + cleaned_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        # found_location = look_for_location(found_location)
        # print("Location found: " + str(found_location), flush=True)

        # Only find locations within distance for locations that have a
        # city or a state only, but not a country.
        if (found_location.city_id is not None or
                found_location.state_id is not None):
            location_list = find_locations_within_distance_miles(
                find_latitude=found_location.latitude,
                find_longitude=found_location.longitude,
                distance_miles=distance,
                remote_flag=remote_flag,
            )

        elif remote_flag:
            location_list = find_locations_within_distance_miles_all_remote(
                find_latitude=found_location.latitude,
                find_longitude=found_location.longitude,
                distance_miles=distance,
            )

        else:
            location_list = []

        # print(str(location_list), flush=True)
        # print("Rows: " + str(len(location_list)), flush=True)

        # Retrieve ID only from location_list if there were results.
        # Results are ordered by distance.
        if (location_list is not None and
                isinstance(location_list, list) and
                len(location_list) != 0):
            location_list = [i.id for i in location_list
                             if i is not None and i.id is not None]

        if (found_location is not None and
                found_location.id is not None):
            location_list.append(found_location.id)

        # Debug
        # print("City ID : " + str(found_location.city_id), flush=True)
        # print("State ID : " + str(found_location.state_id), flush=True)
        # print("Country ID : " + str(found_location.country_id), flush=True)
        # print("Subregion ID : " + str(found_location.subregion_id),
        #       flush=True)
        # print("Region ID : " + str(found_location.region_id), flush=True)

        # location_list should at least have the found_location,
        #   or have a found_location.country_id
        #   that can be used to broad-search.
        if ((found_location is None or
             found_location.country_id is None) and
                (location_list is None or
                 not isinstance(location_list, list) or
                 len(location_list) == 0)):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "Searched location: (" + cleaned_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        # Add broader range search that contain the specified location
        #   regardless of distance.
        if (found_location is not None and
                (found_location.city_id is not None or
                 found_location.state_id is not None or
                 found_location.country_id is not None)):

            # Search for country if state or city is not found.
            if (found_location.state_id is None and
                    found_location.city_id is None and
                    found_location.country_id is not None):
                found_country_locations = find_all_locations_for_country(
                    found_location.country_id)

                # print("Found country locations: " +
                #       str(len(found_city_locations)), flush=True)

                if (found_country_locations is not None and
                        len(found_country_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_country_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_country_locations
                            if (i is not None and
                                i.id is not None)]

            # Search for city if it is specified
            elif found_location.city_id is not None:
                found_city_locations = find_all_locations_for_city(
                    found_location.city_id)

                # print("Found city locations: " +
                #       str(len(found_city_locations)), flush=True)

                if (found_city_locations is not None and
                        len(found_city_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_city_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_city_locations
                            if (i is not None and
                                i.id is not None)]

            # Search for state if it is specified.
            elif found_location.state_id is not None:
                found_state_locations = find_all_locations_for_state(
                    found_location.state_id)

                # print("Found state locations: " +
                #       str(len(found_state_locations)), flush=True)

                if (found_state_locations is not None and
                        len(found_state_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_state_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_state_locations
                            if (i is not None and
                                i.id is not None)]

        # Debugging
        # print("LOCATION LIST: " + str(location_list), flush=True)

        # If there are no locations, run location search only.
        if (location_list is None or
                not isinstance(location_list, list) or
                len(location_list) == 0):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "Searched location: (" + cleaned_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        # Access ListedJob Table and get rows
        listed_jobs_in_location = (
            db.session.query(ListedJobLocation)
            .filter(
                and_(
                    ListedJobLocation.listed_job.has(
                        ListedJob.company_id == int(company_id)),

                    ListedJobLocation.location_id.in_(location_list),

                    ((ListedJobLocation.listed_job.has(
                        ListedJob.expiration_time_utc >=
                        datetime.today().date()))
                     if not include_expired else True),
                )
            )
            .options(
                selectinload(ListedJobLocation.listed_job)
                .load_only(ListedJob.api_source_id)
                .selectinload(ListedJob.api_source)
                .load_only(APISource.name),

                selectinload(ListedJobLocation.listed_job)

                .load_only(ListedJob.id)
                .selectinload(ListedJob.listed_job_experience_levels)

                .load_only(ListedJobExperienceLevel.experience_level_id)
                .selectinload(ListedJobExperienceLevel.experience_level)
                .load_only(ExperienceLevel.name),

                selectinload(ListedJobLocation.listed_job)
                .load_only(
                    ListedJob.id,
                    ListedJob.name,
                    ListedJob.description,
                    ListedJob.salary_currency,
                    ListedJob.min_salary,
                    ListedJob.max_salary,
                    ListedJob.posted_time_utc,
                ),

                selectinload(ListedJobLocation.listed_job)
                .load_only(ListedJob.company_id)
                .selectinload(ListedJob.company)
                .load_only(Company.name),

                selectinload(ListedJobLocation.listed_job_location)
                .load_only(
                    Location.country_id,
                    Location.state_id,
                    Location.city_id,
                    Location.remote,
                )
            )
            .limit(max_jobs_per_page)
            .offset(sql_offset)
            .all()
        )

        # re-organize by order in list
        if (listed_jobs_in_location is None or
                len(listed_jobs_in_location) == 0 or
                not isinstance(listed_jobs_in_location, list)):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "Searched location: (" + cleaned_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        # Get location ID unsorted
        listed_jobs_in_location = [i.listed_job
                                   for i in listed_jobs_in_location]

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        print(
            "Searched location: (" + cleaned_str + ") " +
            f"Process Time: {elapsed_time:.6g} ms", flush=True)

        # print("Found rows: " + str(len(result)), flush=True)

        return listed_jobs_in_location

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        # raise e
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        # raise e
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        # raise e
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        # raise e
        return None


def get_company_jobs_keyword_location_paginate(
        company_id: int,
        search_keyword: str,
        location_keyword: str,
        distance: int = 30,
        page_number: int = 1,
        include_expired: bool = False):
    """
    Query database and get Listed Jobs based on a keyword and location of
    a specific Company.
    Paginates with up to n items per request.
    """
    if (company_id is None or
            company_id < 0):
        return None

    # Check for valid location, then default to normal if invalid.

    cleaned_search_str = clean_search_string(search_keyword)

    invalid_search = (cleaned_search_str is None or
                      not isinstance(cleaned_search_str, str) or
                      len(cleaned_search_str) <= 1)

    cleaned_location_str = clean_location_string(location_keyword)

    invalid_location = (cleaned_location_str is None or
                        not isinstance(cleaned_location_str, str) or
                        len(cleaned_location_str) <= 1)

    invalid_distance = (distance is None or
                        not isinstance(distance, int) or
                        distance < 0)

    if (invalid_search and
            invalid_location):
        # return get_company_jobs_paginate(
        #     company_id=company_id,
        #     page_number=page_number)
        return None

    elif (invalid_search and
          not invalid_location):
        # return get_company_jobs_location_only_paginate(
        #     company_id=company_id,
        #     location_keyword=location_keyword,
        #     page_number=page_number)
        return None

    elif (invalid_location and
          not invalid_search):
        # return get_company_jobs_searched_only_paginate(
        #     company_id=company_id,
        #     search_keyword=search_keyword,
        #     page_number=page_number)
        return None

    if invalid_distance:
        distance = 30

    # Check for valid keyword, then default to normal if invalid.
    # print("Searched keyword: " + cleaned_search_str +
    #       ", Searched location: " + cleaned_location_str, flush=True)

    # Performance check
    start_time = time.time()

    # Unauthenticated users are limited to n items per page.
    max_jobs_per_page = (
        max_jobs_unauthenticated
        if not session.get('user_id', False)
        else max_jobs_authenticated
    )

    # paginate from page number
    if (page_number is None or
            page_number < 0):
        page_number = 1

    if (max_jobs_per_page is None or
            max_jobs_per_page < 2):
        # print("Increasing item count to 2.", flush=True)
        max_jobs_per_page = 2

    sql_offset = (max_jobs_per_page * page_number) - max_jobs_per_page

    remote_flag = (
        'remote' in cleaned_location_str.lower()
        if (cleaned_location_str and
            len(cleaned_location_str) >= len('remote'))
        else False
    )

    # Database methods are enclosed in a try-except block.
    try:
        found_location: Location = string_to_location(
            string_to_parse=cleaned_location_str,
            remote_flag=remote_flag
        )

        # print(str(found_location), flush=True)
        # print("None: " + str(found_location is None), flush=True)
        # print("Instance: " + str(isinstance(found_location, Location)),
        #       flush=True)

        if (found_location is None or
                not isinstance(found_location, Location)):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "location: (" + cleaned_location_str + ") " +
                  "distance: [" + str(distance) + "] " +
                  "keyword: (" + cleaned_search_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        if (found_location.city_id is not None or
                found_location.state_id is not None):
            location_list = find_locations_within_distance_miles(
                find_latitude=found_location.latitude,
                find_longitude=found_location.longitude,
                distance_miles=distance,
                remote_flag=remote_flag,
            )

        elif remote_flag:
            location_list = find_locations_within_distance_miles_all_remote(
                find_latitude=found_location.latitude,
                find_longitude=found_location.longitude,
                distance_miles=distance,
            )

        else:
            location_list = []

        # print(str(location_list), flush=True)
        # print("Rows: " + str(len(location_list)), flush=True)
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(f"Checkpoint Time: {elapsed_time:.6g} ms", flush=True)

        # Retrieve ID only from location_list if there were results.
        # Results are ordered by distance.
        if (location_list is not None and
                isinstance(location_list, list) and
                len(location_list) != 0):
            location_list = [i.id for i in location_list
                             if i is not None and i.id is not None]

        if (found_location is not None and
                found_location.id is not None):
            location_list.append(found_location.id)

        # Debug
        # print("City ID : " + str(found_location.city_id), flush=True)
        # print("State ID : " + str(found_location.state_id), flush=True)
        # print("Country ID : " + str(found_location.country_id), flush=True)
        # print("Subregion ID : " + str(found_location.subregion_id),
        #       flush=True)
        # print("Region ID : " + str(found_location.region_id), flush=True)

        # location_list should at least have the found_location,
        #   or have a found_location.country_id
        #   that can be used to broad-search.
        if ((found_location is None or
             found_location.country_id is None) and
                (location_list is None or
                 not isinstance(location_list, list) or
                 len(location_list) == 0)):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "location: (" + cleaned_location_str + ") " +
                  "distance: [" + str(distance) + "] " +
                  "Searched keyword: (" + cleaned_search_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)

            db.session.close()
            return None

        # Add broader range search that contain the specified location
        #   regardless of distance.
        if (found_location is not None and
                (found_location.city_id is not None or
                 found_location.state_id is not None or
                 found_location.country_id is not None)):

            # Search for country if state or city is not found.
            if (found_location.state_id is None and
                    found_location.city_id is None and
                    found_location.country_id is not None):
                found_country_locations = find_all_locations_for_country(
                    found_location.country_id)

                # print("Found country locations: " +
                #       str(len(found_city_locations)), flush=True)

                if (found_country_locations is not None and
                        len(found_country_locations) != 0):

                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_country_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_country_locations
                            if (i is not None and
                                i.id is not None)]

            # Search for city if it is specified
            elif found_location.city_id is not None:
                found_city_locations = find_all_locations_for_city(
                    found_location.city_id)

                # print("Found city locations: " +
                #       str(len(found_city_locations)), flush=True)

                if (found_city_locations is not None and
                        len(found_city_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_city_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_city_locations
                            if (i is not None and
                                i.id is not None)]

            # Search for state if it is specified.
            elif found_location.state_id is not None:
                found_state_locations = find_all_locations_for_state(
                    found_location.state_id)

                # print("Found state locations: " +
                #       str(len(found_state_locations)), flush=True)

                if (found_state_locations is not None and
                        len(found_state_locations) != 0):
                    if isinstance(location_list, list):
                        location_list.extend([
                            i.id for i in found_state_locations
                            if (i is not None and
                                i.id is not None and
                                i.id not in location_list)])
                    else:
                        location_list = [
                            i.id for i in found_state_locations
                            if (i is not None and
                                i.id is not None)]

        # Debugging
        # print("LOCATION LIST: " + str(location_list), flush=True)

        # Check if locations found
        if (location_list is None or
                not isinstance(location_list, list) or
                len(location_list) == 0):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "Searched location: (" + cleaned_location_str + ") " +
                  "Searched keyword: (" + cleaned_search_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None

        search_query = db.func.plainto_tsquery('english', cleaned_search_str)

        listed_jobs_in_location = (
            db.session.query(ListedJobLocation)
            .filter(
                and_(
                    ListedJobLocation.location_id.in_(location_list),

                    ((ListedJobLocation.listed_job.has(
                        ListedJob.expiration_time_utc >=
                        datetime.today().date()))
                     if not include_expired else True),
                ),
            )
            # .options(
            #     selectinload(ListedJobLocation.listed_job)
            #     .selectinload(ListedJob.api_source)
            #     .load_only(APISource.name),
            #
            #     selectinload(ListedJobLocation.listed_job)
            #     .load_only(ListedJob.id)
            #     .selectinload(ListedJob.listed_job_experience_levels)
            #     .selectinload(ListedJobExperienceLevel.experience_level)
            #     .load_only(ExperienceLevel.name),
            #
            #     selectinload(ListedJobLocation.listed_job)
            #     .load_only(
            #         ListedJob.id,
            #         ListedJob.name,
            #         ListedJob.description,
            #         ListedJob.salary_currency,
            #         ListedJob.min_salary,
            #         ListedJob.max_salary,
            #         ListedJob.posted_time_utc,
            #     ),
            #
            #     selectinload(ListedJobLocation.listed_job)
            #     .load_only(ListedJob.company_id)
            #     .selectinload(ListedJob.company)
            #     .load_only(Company.name),
            #
            #     selectinload(ListedJobLocation.listed_job_location)
            #     .load_only(
            #         Location.country_id,
            #         Location.state_id,
            #         Location.city_id,
            #         Location.remote,
            #     )
            # )
            .all()
        )

        # re-organize by order in list
        if (listed_jobs_in_location is None or
                len(listed_jobs_in_location) == 0 or
                not isinstance(listed_jobs_in_location, list)):
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("No results "
                  "Searched location: (" + cleaned_location_str + ") " +
                  "Searched keyword: (" + cleaned_search_str + ") " +
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)
            db.session.close()
            return None
        else:
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print("Checkpoint "
                  f"Process Time: {elapsed_time:.6g} ms", flush=True)

        # Get location ID unsorted
        listed_jobs_in_location = [i.listed_job_id
                                   for i in listed_jobs_in_location]

        # Access ListedJob Table and get rows
        # searches based on query and if in location list.
        # then reorders the jobs retrieved based on position in location list.
        result = (
            db.session.query(ListedJob)
            .filter(
                and_(
                    # Search only within location
                    ListedJob.id.in_(listed_jobs_in_location),

                    ListedJob.company_id == int(company_id),

                    ((ListedJob.expiration_time_utc >=
                      datetime.today().date())
                     if not include_expired else True),

                    or_(
                        ListedJob.search_vector_name
                        .op('@@')(search_query),

                        db.func.similarity(
                            ListedJob.name,
                            cleaned_search_str
                        ) > 0.9,

                        db.func.lower(ListedJob.name)
                        .contains(cleaned_search_str.lower()),

                        or_(*[db.func.lower(ListedJob.name).contains(i.lower())
                            for i in delimit_string(
                                input_string=cleaned_search_str)]),
                    ),
                )
            )
            .options(
                load_only(
                    ListedJob.id,
                    ListedJob.name,
                    ListedJob.description,
                    ListedJob.salary_currency,
                    ListedJob.min_salary,
                    ListedJob.max_salary,
                    ListedJob.posted_time_utc,
                    # ListedJob.api_source_id,
                    # ListedJob.company_id
                ),

                selectinload(ListedJob.api_source)
                .load_only(APISource.name),

                selectinload(ListedJob.listed_job_experience_levels)
                .selectinload(ListedJobExperienceLevel.experience_level)
                .load_only(ExperienceLevel.name),

                selectinload(ListedJob.company)
                .load_only(Company.name),

                selectinload(ListedJob.listed_job_location)
                .load_only(ListedJobLocation.location_id)
                .selectinload(ListedJobLocation.listed_job_location)
                .load_only(
                    Location.country_id,
                    Location.state_id,
                    Location.city_id,
                    Location.remote
                ),

            )
            .order_by(
                desc(
                    db.func.similarity(
                        ListedJob.name,
                        cleaned_search_str
                    )
                ),
                desc(
                    db.func.ts_rank_cd(
                        ListedJob.search_vector_name,
                        search_query
                    )
                ),
                desc(
                    ListedJob.expiration_time_utc
                ),
            )
            .limit(max_jobs_per_page)
            .offset(sql_offset)
            .all()
        )

        # re-organize by order in list
        result = order_listed_jobs_by_location(
            listed_jobs=result,
            location_list=location_list
        )

        # result = [i.listed_job for i in result]

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        print(
            "location: (" + cleaned_location_str + ") " +
            "distance: [" + str(distance) + "] " +
            "keyword: (" + cleaned_search_str + ") " +
            f"Process Time: {elapsed_time:.6g} ms", flush=True)

        # print("Found rows: " + str(len(result)), flush=True)

        return result

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        # raise e
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        # raise e
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        # raise e
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        # raise e
        return None
