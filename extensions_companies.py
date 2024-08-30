import time

from flask import session
from sqlalchemy import desc, exists, or_

from extensions_string import clean_search_string
from models.postgres.company import Company

from extensions_sql import db
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from routines.parsing.find_location import delimit_string
from user_jobs.user_limits import (
    max_companies_unauthenticated,
    max_companies_authenticated
)


def clear_previous_company_search():
    if session.get('company_view_id'):
        session.pop('company_view_id', None)

    if session.get('company_page_number'):
        session.pop('company_page_number', None)

    if session.get('company_search_query'):
        session.pop('company_search_query', None)

    if session.get('company_location_query'):
        session.pop('company_location_query', None)

    if session.get('company_location_distance'):
        session.pop('company_location_distance', None)


def save_new_search_company(
        company_id: int = None,
        page_number: int = None,
        search_keyword: str = None,
        location_keyword: str = None,
        distance: int = None):
    clear_previous_company_search()

    if company_id is not None:
        session['company_view_id'] = company_id

    if page_number is not None:
        session['company_page_number'] = page_number

    if search_keyword is not None:
        session['company_search_query'] = search_keyword

    if location_keyword is not None:
        session['company_location_query'] = location_keyword

    if distance is not None:
        session['company_location_distance'] = distance


def get_company_by_id(company_id: int):
    """
    Query database and get a specific company based on ID.
    """
    if (company_id is None or
            not isinstance(company_id, int) or
            company_id < 0):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access ListedJob Table and get row
        return (
            db.session.query(Company)
            .filter(Company.id == int(company_id))
            .first()
        ) if db.session.query(
            exists().where(Company.id == int(company_id))).scalar() else None

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        return None


def get_companies_paginate(page_number: int, items=25):
    """
    Query database and get Companies
    Paginates with up to 10 items per request.
    """

    # Unauthenticated users are limited to 25 items per page.
    max_companies_per_page = (
        max_companies_unauthenticated
        if not session.get('user_id', False)
        else max_companies_authenticated
    )

    # paginate from page number
    if page_number is None or page_number == 0:
        page_number = 1

    if items is None or items < 2:
        # print("Increasing item count to 2.", flush=True)
        items = 2

    if items > max_companies_per_page:
        # print("Decreasing item count to 25.", flush=True)
        items = max_companies_per_page

    sql_offset = (items * page_number) - items

    # Performance check
    start_time = time.time()

    # Database methods are enclosed in a try-except block.
    try:

        # Access Company Table and get rows
        result = (
            db.session.query(Company)
            .order_by(
                desc(
                    Company.current_job_count
                )
            )
            .limit(items)
            .offset(sql_offset)
            .all()
        )

        # print("found rows: " + str(len(result)), flush=True)

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        print(
            f"Process Time: {elapsed_time:.6g} ms", flush=True)

        return result

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        return None


def get_companies_searched_only_paginate(
        search_keyword: str,
        page_number: int,
        items: int = 20):
    """
    Query database and get Companies based on a search keyword only.
    Paginates with up to 20 items per request.
    """

    # Check for valid keyword, then default to normal if invalid.
    # print("Searched Keyword: " + search_keyword, flush=True)
    cleaned_str = clean_search_string(search_keyword)
    if (cleaned_str is None or
            not isinstance(cleaned_str, str) or
            len(cleaned_str) <= 1):
        # Return default
        # print("Returning no search get jobs", flush=True)
        # return get_companies_paginate(page_number, items)
        return None

    # Unauthenticated users are limited to 9 items per page.
    max_companies_per_page = (
        max_companies_unauthenticated
        if not session.get('user_id', False)
        else max_companies_authenticated
    )

    # paginate from page number
    if page_number is None or page_number == 0:
        page_number = 1

    if items is None or items < 2:
        # print("Increasing item count to 2.", flush=True)
        items = 2

    if items > max_companies_per_page:
        # print("Decreasing item count to 20.", flush=True)
        items = max_companies_per_page

    sql_offset = (items * page_number) - items

    # Performance check
    start_time = time.time()

    # Database methods are enclosed in a try-except block.
    try:
        search_query = db.func.plainto_tsquery(
            'english',
            cleaned_str
        )

        delimited = delimit_string(input_string=cleaned_str)

        # Access Company Table and get rows
        result: list = (
            db.session.query(Company)
            .filter(
                or_(
                    Company.search_vector.op('@@')(search_query),
                    db.func.similarity(Company.name, cleaned_str) > 0.5,
                    db.func.lower(Company.name).contains(cleaned_str.lower()),
                    or_(*[db.func.lower(Company.name).contains(i.lower())
                        for i in delimited]),
                )
            )
            .order_by(
                desc(
                  db.func.similarity(
                      Company.name,
                      cleaned_str
                  )
                ),
                desc(
                    db.func.ts_rank_cd(
                        Company.search_vector,
                        search_query)
                ),
                desc(
                    Company.last_updated
                ),
            )
            .limit(items)
            .offset(sql_offset)
            .all()
        )

        # print("Found rows: " + str(len(result)), flush=True)

        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000

        print(
            f"Process Time: {elapsed_time:.6g} ms", flush=True)

        return result

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        return None
