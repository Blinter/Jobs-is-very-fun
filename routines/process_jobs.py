"""
This file can be run
cd <this directory>
PYTHONPATH=<base_dir> python3 <file_name>.py
"""
from datetime import datetime, UTC
import argparse
import pytz
from bson import ObjectId
from pytz import utc
from sqlalchemy import and_, asc, exists, or_
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import load_only

from app import create_app, db
from enums.api_endpoint_types import APIEndpointTypes
from extensions_mongo import fs_mongo
from extensions_proxies import http_pass_codes
from extensions_salaries import convert_salary_currency_to_symbol
from extensions_string import clean_unknown_characters
from models.mariadb.api_endpoints import APIEndpoint
from models.mariadb.api_list_url import APIListURL
from models.mariadb.mongo_storage import MongoStorage
from models.postgres.api_source import APISource
from models.postgres.company import Company
from models.postgres.experience_level import ExperienceLevel
from models.postgres.listed_job import ListedJob
from models.postgres.listed_job_experience_level import (
    ListedJobExperienceLevel
)
from models.postgres.locations.listed_job_location import ListedJobLocation
from models.postgres.locations.location import Location
from routines.parsing.apply_link import get_apply_link
from routines.parsing.company import get_companies
from routines.parsing.conversions import convert_bytes_to_dict_raw
from routines.parsing.description import get_descriptions
from routines.parsing.experience_level import get_experience_levels
from routines.parsing.find_location import cleanup_locations
from routines.parsing.job_title import get_job_titles
from routines.parsing.location import get_locations
from routines.parsing.salary import get_job_salaries
from routines.parsing.times import get_times

scrape_endpoints_type_list = [
    db.cast(APIEndpointTypes.JOBS_SEARCH.value, TINYINT()),
    db.cast(APIEndpointTypes.JOBS_FEED.value, TINYINT()),
    db.cast(APIEndpointTypes.JOB_DETAILS.value, TINYINT()),
]

endpoints_id_broken_list = []

app = create_app()


def populate_broken_endpoint_list(database_app):
    return [broken_endpoint[0] for broken_endpoint in (
        database_app.session.query(APIEndpoint.id)
        .filter(
            or_(
                and_(
                    APIEndpoint.nice_name == "/api/v2/Jobs/Latest",
                    APIEndpoint.http_path ==
                    "https://job-postings1.p.rapidapi.com/",
                ),
                and_(
                    APIEndpoint.nice_name == "httpsJobapiCoUkGet",
                    APIEndpoint.http_path ==
                    "https://zambian-jobs-api1.p.rapidapi.com/getdataNew.php",
                )
            )
        ).all()
    )]


def get_processed_query_list(
        endpoint_types_list: list,
        database_app,
        date_filter: datetime = None):
    """
    Refreshes Processed Query List
     matching allowed scrape endpoints only

     mongo storage columns: endpoint_nice_name, url
     endpoint columns: nice_name, http_path
    """
    result = (
        database_app.session.query(MongoStorage)
        .filter(
            and_(
                MongoStorage.code.in_(http_pass_codes),
                MongoStorage.object_id.is_not(None),
                MongoStorage.query_time.is_not(None),
                MongoStorage.length.is_not(None),
                MongoStorage.data_truncated.is_not(None),
                (MongoStorage.query_time > date_filter
                 if date_filter is not None else True),
            )
        )
        .order_by(asc(MongoStorage.query_time))
        .options(
            load_only(
                MongoStorage.id,
                MongoStorage.object_id,
                MongoStorage.endpoint_nice_name,
                MongoStorage.input_json,
                MongoStorage.url,
            )
        )
        .all()
    )

    final_list = []

    for mongo_stor in result:
        for endpoint_ in endpoint_types_list:
            if (endpoint_.nice_name == mongo_stor.endpoint_nice_name and
                    endpoint_.http_path == mongo_stor.url):
                # print("adding " + endpoint_.nice_name +
                #       "(" + endpoint_.http_path + ")", flush=True)

                final_list.append(mongo_stor)

    return final_list


def get_scrape_endpoint_filtered_types(database_app):
    """
    Retrieve full APIEndpoint List to pull
    URL and Nice_Name details for jobs that can be scraped.
    """
    return (
        database_app.session.query(APIEndpoint)
        .filter(
            and_(
                APIEndpoint.type__.in_(scrape_endpoints_type_list),
                APIEndpoint.id.not_in(endpoints_id_broken_list),
                APIEndpoint.disabled == 0
            )
        )
        .all()
    )


# Parse Arguments
parser = argparse.ArgumentParser(
    description="Accept DateTime String as format "
                "(%a, %d %b %Y %H:%M:%S.%f %Z)")

parser.add_argument(
    '--date',
    type=str,
    help="DateTime of previously processed query"
)

args = parser.parse_args()
# print("Original: " +
#       progress_timestamp)
# print("Date Argument: " +
#       (args.date if args.date is not None else 'None'))

progress_timestamp = "earliest"

if (args.date is not None and
        isinstance(args.date, str) and
        len(args.date) > 0):
    if args.date == "earliest":
        progress_timestamp = ""
        latest_date_time = datetime.min

    else:
        progress_timestamp = args.date
        latest_date_time = datetime.strptime(
            args.date,
            "%a, %d %b %Y %H:%M:%S.%f %Z"
        )

else:
    latest_date_time = datetime.strptime(
        progress_timestamp,
        "%a, %d %b %Y %H:%M:%S.%f %Z"
    )
# raise ValueError(progress_timestamp)


with app.app_context():
    try:
        # populate ID's for broken endpoints
        endpoints_id_broken_list: list = populate_broken_endpoint_list(db)

        # Grab all queries
        processed_queries: list = get_processed_query_list(
            endpoint_types_list=(
                get_scrape_endpoint_filtered_types(database_app=db)),
            date_filter=latest_date_time.replace(tzinfo=pytz.UTC),
            database_app=db
        )
        for query in processed_queries:

            if (latest_date_time.replace(tzinfo=pytz.UTC) <
                    query.query_time.replace(tzinfo=pytz.UTC)):
                test_string = (
                    query.query_time
                    .replace(tzinfo=pytz.UTC)
                    .strftime("%a, %d %b %Y %H:%M:%S.%f %Z"))
                if not test_string.endswith("UTC"):
                    test_string += "UTC"
                print("Reset current timestamp to " +
                      test_string,
                      flush=True)
                latest_date_time = query.query_time.replace(tzinfo=pytz.UTC)

            selected_api_name = (
                db.session.query(APIListURL.nice_name).filter(
                    APIListURL.url == query.api).first()[0]
            )
            # print('selected api name: ' + str(selected_api_name), flush=True)

            # Check if API is in API_Sources Table
            if not (db.session.query(
                    exists().where(APISource.name.ilike(str(selected_api_name)))
            ).scalar()):

                selected_api_source: APISource = APISource(
                    name=str(selected_api_name),
                    last_updated=datetime.now(UTC)
                )
                db.session.add(selected_api_source)
                db.session.commit()
                # print("Added APISource - " + str(selected_api_source),
                #       flush=True)
            else:
                selected_api_source: APISource = (
                    db.session.query(APISource).filter(
                        APISource.name.ilike(str(selected_api_name))
                    ).first()
                )
                # print("Selected APISource - " + selected_api_source.name,
                #       flush=True)

            new_dict: dict = convert_bytes_to_dict_raw(
                fs_mongo.get(file_id=ObjectId(query.object_id))
                .read().decode()
            )

            # Fix for special error code
            if ('code' in new_dict.keys() and
                    'message' in new_dict.keys() and
                    new_dict.get('code') == "57014"):
                continue

            # Fix for key
            if (query.url == "https://glassdoor.p.rapidapi.com"
                             "/job/" and
                    query.endpoint_nice_name == "Job details"):
                new_dict = {
                    query.input_json.get('job_id'): new_dict
                }

            # Default debug
            print("ID: " + str(query.id) + " " +
                  "URL: " + query.url +
                  " (" + query.endpoint_nice_name + ")", flush=True)

            new_jobs = {}

            # Key Debug Error
            # not_found = False

            # Check for other non-error code

            for i in new_dict.keys():
                if "error" in i.lower():
                    break

                new_jobs[i] = {'api_source': selected_api_source}
                # if i == "3966852888":
                #     print("Key: " + i, flush=True)
                #     print("Trace: " + str(names[i]), flush=True)
                #     not_found = True
                #     raise ValueError("FIX")
                # else:
                #     new_jobs[i] = {}
                #     continue

            # if not not_found:
            #     continue

            names: dict = get_job_titles(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
            )

            # print("ID: " + str(query.id) + " " +
            #       "URL: " + query.url + " (" +
            #       query.endpoint_nice_name +
            #       ")", flush=True)

            # Add names to dictionary
            for i in names.keys():
                if "error" in i.lower():
                    # print("No names for ID: " + str(query.id) + " " +
                    #       query.endpoint_nice_name, flush=True)
                    for j in new_dict.keys():
                        if "error" in str(j).lower():
                            break
                        # new_jobs[str(j)]['name'] = None
                    break

                new_jobs[i]['name'] = clean_unknown_characters(names[i])

            descriptions: dict = get_descriptions(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
            )

            # print("ID: " + str(query.id) + " " +
            #       "URL: " + query.url + " (" +
            #       query.endpoint_nice_name +
            #       ")", flush=True)

            # Add descriptions to the dictionary
            for i in descriptions.keys():
                if "error" in i.lower():
                    # print("No descriptions for ID: " + str(query.id) + " " +
                    #       query.endpoint_nice_name, flush=True)
                    for j in new_dict.keys():
                        if "error" in str(j).lower():
                            break
                        # new_jobs[str(j)]['description'] = None
                    break

                new_jobs[i]['description'] = clean_unknown_characters(
                    descriptions[i]
                )

            salaries: dict = get_job_salaries(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
            )

            # print("ID: " + str(query.id) + " " +
            #       "URL: " + query.url + " (" +
            #       query.endpoint_nice_name +
            #       ")", flush=True)

            # Add salaries to the dictionary
            for i in salaries.keys():
                if "error" in i.lower():
                    # print("No salaries for ID: " + str(query.id) + " " +
                    #       query.endpoint_nice_name, flush=True)
                    for j in new_dict.keys():
                        if "error" in str(j).lower():
                            break
                        # new_jobs[str(j)]['salaries'] = None
                    break

                if not isinstance(salaries[i], dict):
                    print("salaries[i] = " + str(salaries[i]) +
                          " key: " + i, flush=True)
                    raise ValueError("Fix this")

                new_jobs[i]['salaries'] = salaries[i]

            # for i in new_jobs.keys():
            #     print(i + ": " + str(new_jobs[i]), flush=True)

            apply_links: dict = get_apply_link(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
            )

            for i in apply_links.keys():
                if "error" in i.lower():
                    # print("No apply links for ID: " + str(query.id) + " " +
                    #       str(query.endpoint_nice_name), flush=True)
                    for j in new_dict.keys():
                        if "error" in str(j).lower():
                            break
                        # new_jobs[str(j)]['apply_links'] = None
                    break

                if isinstance(apply_links[i], str):
                    apply_links[i] = [apply_links[i]]

                elif not isinstance(apply_links[i], list):
                    print("apply_links[i] = " + str(apply_links[i]) +
                          " key: " + i, flush=True)
                    raise ValueError("Fix this")

                new_jobs[i]['apply_links'] = clean_unknown_characters(
                    apply_links[i][0])

            times: dict = get_times(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
                query_time=query.query_time
            )

            # print("ID: " + str(query.id) + " " +
            #       "URL: " + query.url + " (" +
            #       query.endpoint_nice_name +
            #       ")", flush=True)

            for i in times.keys():
                if "error" in i.lower():
                    # print("No times for ID: " + str(query.id) + " " +
                    #       str(query.endpoint_nice_name), flush=True)
                    for j in new_dict.keys():
                        if "error" in str(j).lower():
                            break
                        # new_jobs[str(j)]['times'] = None
                    break

                if not isinstance(times[i], dict):
                    print("times[i] = " + str(times[i]) +
                          " key: " + i, flush=True)
                    raise ValueError("Fix this")

                new_jobs[i]['times'] = times[i]

            # for i in new_jobs.keys():
            #     print(i + ": " + str(new_jobs[i]), flush=True)

            companies: dict = get_companies(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
            )

            # print("ID: " + str(query.id) + " " +
            #       "URL: " + query.url + " (" +
            #       query.endpoint_nice_name +
            #       ")", flush=True)

            for i in companies.keys():
                if "error" in i.lower():
                    # print("No Companies for ID: " + str(query.id) + " " +
                    #       str(query.endpoint_nice_name), flush=True)
                    for j in new_dict.keys():
                        if "error" in str(j).lower():
                            break
                        # new_jobs[str(j)]['company_id'] = None
                    break

                if companies[i] is None:
                    # new_jobs[i]['company_id'] = None
                    continue

                if not isinstance(companies[i], str):
                    print("companies[i] = " + str(companies[i]) +
                          " key: " + i, flush=True)
                    raise ValueError("Fix this")

                # Add to companies
                company_str = clean_unknown_characters(companies[i])

                if companies[i] is None:
                    continue

                if (company_str is None or
                        len(company_str) == 0 or
                        company_str == ' '):
                    company_str = None

                if company_str is not None:

                    # print("Company (" + str(company_str) + ")", flush=True)

                    # Check if company is in Companies Table
                    if not (db.session.query(
                            exists().where(Company.name.ilike(str(company_str)))
                    ).scalar()):

                        selected_company: Company = Company(
                            name=str(company_str),
                            last_updated=datetime.now(UTC)
                        )

                        db.session.add(selected_company)

                        db.session.commit()
                        print("Added Company " + str(selected_company.name) +
                              " ID: " + str(selected_company.id), flush=True)

                    else:
                        with db.session.no_autoflush:
                            selected_company: Company = (
                                db.session.query(Company).filter(
                                    Company.name.ilike(str(company_str))
                                ).first()
                            )
                            # print("Found Company " +
                            #       str(selected_company.name) +
                            #       " ID: " + str(selected_company.id))

                    new_jobs[i]['company']: Company = selected_company
                    # print("Selected Company" + str(new_jobs[i]['company']),
                    #       flush=True)

            # Enough data to populate.
            for i in new_jobs:

                if (new_jobs[i] is None or
                        len(new_jobs[i]) == 0):
                    continue

                try:
                    # Apply Links check
                    if (new_jobs.get(i) is None or
                            'apply_links' not in new_jobs[i] or
                            new_jobs[i].get('apply_links') is None):
                        new_jobs[i] = {}
                        continue
                except Exception as e:
                    print(str(e), flush=True)

                new_name = new_jobs[i].get('name', None)

                if new_name is None:
                    continue

                api_source: APISource = new_jobs[i].get('api_source', None)

                if api_source is None:
                    continue

                currency = None
                min_salary = None
                max_salary = None

                if new_jobs[i].get('salaries') is not None:
                    salaries_dict: dict = new_jobs[i].get('salaries')

                    if isinstance(salaries_dict, dict):
                        currency = salaries_dict.get('currency')
                        if currency is not None and isinstance(currency, str):
                            currency = convert_salary_currency_to_symbol(
                                currency
                            )
                        min_salary = salaries_dict.get('min_salary', None)
                        max_salary = salaries_dict.get('max_salary', None)

                        if ((isinstance(min_salary, str) and
                             min_salary == "0" and
                             len(min_salary) == 0) or
                                (isinstance(min_salary, int) and
                                 min_salary <= 0)):
                            min_salary = None

                        if ((isinstance(max_salary, str) and
                             max_salary == "0" and
                             len(max_salary) == 0) or
                                (isinstance(max_salary, int) and
                                 max_salary <= 0)):
                            max_salary = None

                posted_time_utc: None = None
                expiration_time_utc: None = None

                if new_jobs[i].get('times') is not None:
                    times_dict: dict = new_jobs[i].get('times')

                    if isinstance(times_dict, dict):
                        posted_time_utc: datetime = (
                            times_dict.get('posted_time_utc')
                        )

                        expiration_time_utc: datetime = (
                            times_dict.get('expiration_time_utc')
                        )

                selected_company: None = None

                if new_jobs[i].get('company') is not None:
                    selected_company = new_jobs[i].get('company')

                # Check name, API Source ID, and reference name.
                with db.session.no_autoflush:
                    if (db.session.query(
                            exists().where(
                                and_(
                                    ListedJob.name == new_name,
                                    ListedJob.api_source_id == (
                                            int(new_jobs[i]
                                                .get('api_source').id)),
                                    ListedJob.api_reference_name.ilike(i)
                                )
                            )).scalar()):

                        current_job: ListedJob = (
                            db.session.query(ListedJob).filter(
                                and_(
                                    ListedJob.name == new_name,
                                    ListedJob.api_source_id == (
                                        int(new_jobs[i].get('api_source').id)
                                    ),
                                    ListedJob.api_reference_name.ilike(i)
                                )
                            ).first()
                        )
                        # Debugging
                        # print(str(current_job), flush=True)

                        if current_job is None:
                            raise ValueError("Could not find job.")

                        updated_job = False

                        # Apply current parsed settings
                        if new_jobs[i].get('description') is not None:
                            cleaned_previous_job_description = (
                                clean_unknown_characters(
                                    current_job.description
                                )
                                if current_job.description is not None
                                else None
                            )

                            cleaned_new_job_description = (
                                clean_unknown_characters(
                                    new_jobs[i].get('description')
                                ) if new_jobs[i].get('description') is not None
                                else None
                            )

                            if (cleaned_previous_job_description is None and
                                    cleaned_new_job_description is not None or

                                (isinstance(
                                    cleaned_previous_job_description, str) and
                                 isinstance(
                                     cleaned_new_job_description, str) and
                                 len(cleaned_previous_job_description)
                                 < len(cleaned_new_job_description))):
                                current_job.description = (
                                    cleaned_new_job_description
                                )

                                updated_job = True

                        if (currency is not None and
                                (current_job.salary_currency is None or
                                 str(current_job.salary_currency) !=
                                 str(currency))):
                            current_job.salary_currency = currency
                            updated_job = True

                            print("Updated currency for " +
                                  str(current_job.id), flush=True)

                        # Keep min_salary which is smallest
                        # noinspection PyTypeChecker
                        if (min_salary is not None and
                                (current_job.min_salary is None or
                                 int(current_job.min_salary) >
                                 int(min_salary))):

                            current_job.min_salary = min_salary

                            if (not isinstance(current_job.min_salary, int) or
                                    (isinstance(current_job.min_salary, int) and
                                     current_job.min_salary <= 0) or
                                    isinstance(current_job.min_salary, str)):
                                current_job.min_salary = None

                            else:
                                updated_job = True
                                print("Updated minimum salary for " +
                                      str(current_job.id), flush=True)

                        # Keep max_salary which is largest
                        # noinspection PyTypeChecker
                        if (max_salary is not None and
                                (current_job.max_salary is None or
                                 int(current_job.max_salary) <
                                 int(max_salary))):
                            current_job.max_salary = max_salary

                            if (not isinstance(current_job.max_salary, int) or
                                    (isinstance(current_job.max_salary, int) and
                                     current_job.max_salary <= 0) or
                                    isinstance(current_job.max_salary, str)):
                                current_job.max_salary = None

                            else:
                                updated_job = True
                                print("Updated maximum salary for " +
                                      str(current_job.id), flush=True)

                        # Keep apply link with the longest length
                        if (new_jobs[i].get('apply_links') is not None and
                                (current_job.apply_link is None or
                                 len(clean_unknown_characters(
                                     current_job.apply_link)) <
                                 len(clean_unknown_characters(
                                     new_jobs[i].get('apply_links'))))):
                            current_job.apply_link = clean_unknown_characters(
                                new_jobs[i].get('apply_links')
                            )
                            print("UPDATED apply_links FOR " +
                                  str(current_job.id), flush=True)
                            updated_job = True

                        # Not implemented yet (Fix parsing between apply links)
                        current_job.original_source_link = None

                        # Keep earliest posted time
                        # noinspection PyUnresolvedReferences
                        if (posted_time_utc is not None and
                                (current_job.posted_time_utc is None or
                                 current_job.posted_time_utc
                                 .replace(tzinfo=utc) >
                                 posted_time_utc.replace(tzinfo=utc))):
                            current_job.posted_time_utc = posted_time_utc
                            updated_job = True
                            print("Updated Posted Time for " +
                                  str(current_job.id), flush=True)

                        # Keep latest expiration time
                        # noinspection PyUnresolvedReferences
                        if (expiration_time_utc is not None and
                                (current_job.expiration_time_utc is None or
                                 (current_job.expiration_time_utc
                                  .replace(tzinfo=utc)) <
                                 expiration_time_utc.replace(tzinfo=utc))):
                            current_job.expiration_time_utc = (
                                expiration_time_utc
                            )
                            updated_job = True
                            print("Updated Expiration Time for " +
                                  str(current_job.id), flush=True)

                        if (selected_company is not None and
                                (current_job.company_id is None or
                                 int(current_job.company_id) !=
                                 int(selected_company.id))):
                            current_job.company_id = int(selected_company.id)
                            updated_job = True
                            print("Updated Company for " +
                                  str(current_job.id), flush=True)

                        if updated_job:
                            print("Updated ListedJob with ID: " +
                                  str(current_job.id), flush=True)
                            current_job.verified = True
                            db.session.commit()

                        else:
                            # No change
                            # print("No change in ListedJob with ID: " +
                            #       str(current_job.id), flush=True)
                            pass

                        new_jobs[i]['ListedJob']: ListedJob = current_job

                        # Debugging
                        # print("Printing key: " + i, flush=True)
                        # print("Key: " + i, flush=True)
                        #
                        # if current_job is None:
                        #     raise ValueError("CURRENT JOB IS NONE")
                        # for j in new_jobs[i].keys():
                        #     if j is None:
                        #         print("Jkey is NONE", flush=True)
                        #         continue
                        #     print("JKey: " + str(j), flush=True)
                        #     if new_jobs[i][j] is None:
                        #         print("JValue: None", flush=True)
                        #         continue
                        #     else:
                        #         print('value: ' + str(new_jobs[i][j]),
                        #               flush=True)
                        # print("Value: " + str(new_jobs[i]), flush=True)
                        #
                        # print(str(new_jobs[i]['ListedJob']), flush=True)

                    else:
                        new_job: ListedJob = ListedJob(
                            name=new_name,
                            description=clean_unknown_characters(
                                new_jobs[i].get('description', None)),

                            salary_currency=None
                            if (min_salary == 0 and
                                max_salary == 0)
                            else currency,

                            min_salary=None
                            if (min_salary == 0 or
                                isinstance(min_salary, str))
                            else min_salary,

                            max_salary=None
                            if (max_salary == 0 or
                                isinstance(max_salary, str))
                            else max_salary,

                            apply_link=clean_unknown_characters(
                                new_jobs[i].get('apply_links', None)),
                            # Not implemented yet
                            # (Fix parsing between apply links)
                            original_source_link=None,
                            posted_time_utc=posted_time_utc,
                            expiration_time_utc=expiration_time_utc,
                            company_id=(
                                int(selected_company.id)
                                if selected_company is not None else None
                            ),
                            api_source_id=int(new_jobs[i].get('api_source').id),
                            api_reference_name=i
                        )

                        db.session.add(new_job)
                        db.session.commit()
                        # print("New ListedJob added with ID: " +
                        #       str(new_job.id),
                        #       flush=True)

                        new_jobs[i]['ListedJob']: ListedJob = new_job

            # print(str(new_dict), flush=True)

            # Experience Levels
            experience_levels: dict = get_experience_levels(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
            )

            # print("ID: " + str(query.id) + " " +
            #       "URL: " + query.url +
            #       " (" + query.endpoint_nice_name + ")", flush=True)

            # Add experience levels to the dictionary
            for i in experience_levels.keys():
                if "error" in str(i).lower():
                    # print("No experience for ID: " + str(query.id) + " " +
                    #       query.endpoint_nice_name, flush=True)
                    for j in new_dict.keys():
                        if "error" in str(j).lower():
                            break
                        # new_jobs[str(j)]['experience_level'] = None
                    break
                # print("Key: " + i, flush=True)
                # print("Trace: " + str(experience_level[i]), flush=True)

                if (experience_levels[str(i)] is None or
                        not isinstance(experience_levels[str(i)], str) or
                        len(experience_levels[str(i)]) == 0):
                    # new_jobs[i]['experience_level'] = None
                    continue

                new_jobs[str(i)]['experience_levels'] = (
                    clean_unknown_characters(experience_levels[str(i)])
                )

                if (experience_levels[str(i)] is None or
                        not isinstance(experience_levels[str(i)], str) or
                        len(experience_levels[str(i)]) == 0):
                    # new_jobs[i]['experience_level'] = None
                    continue

                if not isinstance(experience_levels[str(i)], str):
                    print("experience_levels[i] = " +
                          str(experience_levels[str(i)]) + " key: " + str(i),
                          flush=True)
                    raise ValueError("Fix this")

                # Add to experience_levels
                new_jobs[str(i)]['experience_levels'] = (
                    clean_unknown_characters(experience_levels[str(i)])
                )

                # Implemented for str only, not list
                sel_exp_level: ExperienceLevel = (
                    new_jobs[str(i)]['experience_levels']
                )

                # Check if location is in locations table
                if not (db.session.query(
                        exists().where(
                            ExperienceLevel.name.ilike(str(sel_exp_level)))
                ).scalar()):
                    sel_exp_level: ExperienceLevel = (
                        ExperienceLevel(name=sel_exp_level)
                    )
                    db.session.add(sel_exp_level)
                    db.session.commit()
                    print("Added new unique experience level with ID: " +
                          str(sel_exp_level.id), flush=True)

                else:
                    sel_exp_level: ExperienceLevel = (
                        db.session.query(ExperienceLevel).filter(
                            ExperienceLevel.name.ilike(str(
                                sel_exp_level))
                        ).first()
                    )

                # retrieve ID then set ExperienceLevel of the job by adding
                # to M2M table: ListedJobExperienceLevel
                if sel_exp_level is not None:
                    # print("Selected Experience Level is: ID: " +
                    #       str(sel_exp_level.id), flush=True)
                    # Add to new_jobs
                    if sel_exp_level.id is None:
                        raise ValueError(
                            "Error getting sel_exp_level.id")

                    new_jobs[i]['sel_exp_level']: ExperienceLevel = (
                        sel_exp_level
                    )

            # Populate M2M table
            for i in new_jobs.keys():

                if (new_jobs[i] is None or
                        len(new_jobs[i]) == 0):
                    continue

                try:
                    # Apply Links check
                    if (new_jobs.get(i) is None or
                            'apply_links' not in new_jobs[i] or
                            new_jobs[i].get('apply_links') is None):
                        print("Skipping key " + i +
                              " due to unknown of apply link.")
                        new_jobs[i] = {}
                        continue
                except Exception as e:
                    print(str(e), flush=True)

                if (i is None or
                        new_jobs[i] is None or
                        new_jobs[i].get(
                            'sel_exp_level', None) is None or
                        new_jobs[i].get('ListedJob', None) is None):
                    continue

                sel_exp_level: ExperienceLevel = (
                    new_jobs[i]['sel_exp_level'])

                if sel_exp_level is None:
                    raise ValueError("ExperienceLevel is None.. continuing")

                selected_job: ListedJob = new_jobs[i]['ListedJob']

                if selected_job is None:
                    raise ValueError("Job is None.. continuing")

                # Look for Experience Level already existing for ListedJob
                if (db.session.query(
                        exists().where(
                            ListedJobExperienceLevel.listed_job_id ==
                            int(selected_job.id))).scalar()):

                    sel_listed_job_exp_levels: list = (
                        db.session.query(ListedJobExperienceLevel)
                        .filter(
                            ListedJobExperienceLevel.listed_job_id ==
                            int(selected_job.id)
                        ).all()
                    )

                    if len(sel_listed_job_exp_levels) > 1:
                        raise ValueError("Multiple Job Experience Levels. "
                                         "Error: not yet implemented.")

                    sel_listed_job_exp_levels: ListedJobExperienceLevel = (
                        sel_listed_job_exp_levels[0]
                    )

                    if (int(sel_listed_job_exp_levels.experience_level_id)
                            != int(sel_exp_level.id)):

                        print("Incorrect Experience Level found. Changing from"
                              " " + str(sel_listed_job_exp_levels
                                        .experience_level_id) +
                              " to " + str(sel_exp_level.id), flush=True)

                        # print("Debug: " + str(
                        #     sel_listed_job_exp_levels
                        #     .experience_level_id), flush=True)

                        # print(str(sel_exp_level), flush=True)

                        sel_listed_job_exp_levels.experience_level_id = (
                            sel_exp_level.id
                        )

                        sel_listed_job_exp_levels.verified = True
                        db.session.commit()

                    else:
                        # Debug here
                        # print("ListedJobExperienceLevel check completed for "
                        #       "ListedJob ID: " +
                        #       str(selected_job.id) +
                        #       " Selected Experience Level ID: " +
                        #       str(sel_exp_level.id), flush=True)
                        pass

                else:

                    sel_listed_job_exp_levels: ListedJobExperienceLevel = (
                        ListedJobExperienceLevel(
                            listed_job_id=int(selected_job.id),
                            experience_level_id=int(
                                sel_exp_level.id)
                        )
                    )
                    db.session.add(sel_listed_job_exp_levels)
                    db.session.commit()

                    # print("ListedJobExperienceLevels added for "
                    #       "ListedJob ID: " +
                    #       str(selected_job.id) + " Experience Level ID: " +
                    #       str(sel_listed_job_exp_levels.experience_level_id),
                    #       flush=True)

            # Locations
            locations: dict = get_locations(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
            )

            # print("ID: " + str(query.id) + " " +
            #       "URL: " + query.url +
            #       " (" + query.endpoint_nice_name + ")", flush=True)
            # print(str(locations), flush=True)

            for i in locations.keys():
                if (i is None or
                        "error" in i.lower()):
                    # print("No Locations for ID: " + str(query.id) + " " +
                    #       str(query.endpoint_nice_name), flush=True)
                    for j in new_dict.keys():
                        if "error" in str(j).lower():
                            break
                        # new_jobs[str(j)]['location'] = None
                    break

                if locations[i] is None:
                    # new_jobs[i]['location'] = None
                    continue

                if not isinstance(locations[i], dict):
                    print("locations[i] = " + str(locations[i]) +
                          " key: " + i, flush=True)
                    raise ValueError("Fix this")

                # Add to location
                new_jobs[i]['locations']: dict = (
                    cleanup_locations(locations[i])
                )

                # print("Debug Locations", flush=True)
                # print(str(new_jobs[i]['locations']), flush=True)

                selected_locations: dict = new_jobs[i]['locations']

                if (selected_locations.get('region_id', None) is None and
                        selected_locations.get('subregion_id', None)
                        is None and
                        selected_locations.get('country_id', None) is None and
                        selected_locations.get('state_id', None) is None and
                        selected_locations.get('city_id', None) is None and
                        selected_locations.get('latitude', None) is None and
                        selected_locations.get('longitude', None) is None and
                        selected_locations.get('remote', None) is None):
                    selected_location: None = None

                else:
                    # Check if location is in locations table
                    if not (db.session.query(
                            exists().where(
                                and_(
                                    ((Location.region_id == int(
                                        selected_locations.get('region_id')))
                                     if selected_locations.get(
                                         'region_id', None)
                                        is not None else True),

                                    ((Location.subregion_id == int(
                                        selected_locations.get('subregion_id')))
                                     if selected_locations.get(
                                         'subregion_id', None)
                                        is not None else True),

                                    ((Location.country_id == int(
                                        selected_locations.get('country_id')))
                                     if selected_locations.get(
                                        'country_id', None)
                                        is not None else True),

                                    ((Location.state_id == int(
                                        selected_locations.get('state_id')))
                                     if selected_locations.get('state_id', None)
                                        is not None else True),

                                    ((Location.city_id == int(
                                        selected_locations.get('city_id')))
                                     if selected_locations.get('city_id', None)
                                        is not None else True),

                                    ((Location.latitude == float(
                                        selected_locations.get('latitude')))
                                     if selected_locations.get('latitude', None)
                                        is not None else True),

                                    ((Location.longitude == float(
                                        selected_locations.get('longitude')))
                                     if selected_locations.get(
                                        'longitude', None)
                                        is not None else True),

                                    ((Location.remote == (
                                            selected_locations.get('remote')))
                                     if selected_locations.get('remote', None)
                                        is not None else True),
                                )
                            )
                    ).scalar()):
                        selected_location: Location = Location(
                            region_id=(
                                int(selected_locations.get('region_id'))
                                if selected_locations.get('region_id', None)
                                is not None else None),

                            subregion_id=(
                                int(selected_locations.get('subregion_id'))
                                if selected_locations.get('subregion_id', None)
                                is not None else None),

                            country_id=(
                                int(selected_locations.get('country_id'))
                                if selected_locations.get('country_id', None)
                                is not None else None),

                            state_id=(
                                int(selected_locations.get('state_id'))
                                if selected_locations.get('state_id', None)
                                is not None else None),

                            city_id=(
                                int(selected_locations.get('city_id'))
                                if selected_locations.get('city_id', None)
                                is not None else None),

                            latitude=(float(
                                selected_locations.get('latitude'))
                                      if selected_locations.get(
                                         'latitude', None)
                                      is not None else None),

                            longitude=(float(
                                selected_locations.get('longitude'))
                                       if selected_locations.get(
                                        'longitude', None)
                                       is not None else None),

                            remote=selected_locations.get('remote', False),
                        )
                        db.session.add(selected_location)
                        db.session.commit()
                        # print("Added new unique location with ID: " +
                        #       str(selected_location.id), flush=True)

                    else:
                        selected_location: Location = (
                            db.session.query(Location).filter(
                                and_(
                                    ((Location.region_id == int(
                                        selected_locations.get('region_id')))
                                     if selected_locations.get(
                                        'region_id', None)
                                        is not None else True),

                                    ((Location.subregion_id == int(
                                        selected_locations.get(
                                            'subregion_id')))
                                     if selected_locations.get(
                                        'subregion_id', None)
                                        is not None else True),

                                    ((Location.country_id == int(
                                        selected_locations.get('country_id')))
                                     if selected_locations.get(
                                        'country_id', None)
                                        is not None else True),

                                    ((Location.state_id == int(
                                        selected_locations.get('state_id')))
                                     if selected_locations.get(
                                        'state_id', None)
                                        is not None else True),

                                    ((Location.city_id == int(
                                        selected_locations.get('city_id')))
                                     if selected_locations.get(
                                        'city_id', None)
                                        is not None else True),

                                    ((Location.latitude == float(
                                        selected_locations.get('latitude')))
                                     if selected_locations.get(
                                        'latitude', None)
                                        is not None else True),

                                    ((Location.longitude == float(
                                        selected_locations.get('longitude')))
                                     if selected_locations.get(
                                        'longitude', None)
                                        is not None else True),

                                    ((Location.remote == (
                                        selected_locations.get('remote')))
                                     if selected_locations.get(
                                        'remote', None)
                                        is not None else True),
                                )
                            ).first()
                        )

                # retrieve ID then set location_id of the job by adding
                # to M2M table: listedJoblocation
                if selected_location is not None:
                    # print("Selected Location is: ID: " +
                    #       str(selected_location.id), flush=True)
                    # Add to new_jobs
                    if selected_location.id is None:
                        raise ValueError("Error getting selected_location.id")

                    new_jobs[i]['selected_location']: Location = (
                        selected_location
                    )

            # Populate M2M table
            for i in new_jobs.keys():

                if (new_jobs[i] is None or
                        len(new_jobs[i]) == 0):
                    continue

                if (i is None or
                        new_jobs[i] is None or
                        new_jobs[i].get('selected_location', None) is None or
                        new_jobs[i].get('ListedJob', None) is None):
                    continue

                selected_location: Location = new_jobs[i]['selected_location']

                if selected_location is None:
                    raise ValueError("Location is None.. continuing")

                selected_job: ListedJob = new_jobs[i]['ListedJob']

                if selected_job is None:
                    raise ValueError("Job is None.. continue")

                # Look for locations already existing for ListedJob
                if (db.session.query(exists().where(
                        ListedJobLocation.listed_job_id ==
                        int(selected_job.id))).scalar()):

                    selected_listed_job_location: list = (
                        db.session.query(ListedJobLocation)
                        .filter(
                            ListedJobLocation.listed_job_id ==
                            int(selected_job.id)
                        ).all()
                    )

                    if len(selected_listed_job_location) > 1:
                        raise ValueError("Multiple Job locations. "
                                         "Error: not yet implemented.")

                    selected_listed_job_location: ListedJobLocation = (
                        selected_listed_job_location[0]
                    )

                    if (int(selected_listed_job_location.location_id) !=
                            int(selected_location.id)):

                        print("Incorrect location found. Changing from " +
                              str(selected_listed_job_location.location_id) +
                              " to " + str(selected_location.id),
                              flush=True)

                        print("Debug\n Previous: " + str(
                            selected_listed_job_location.listed_job_location),
                              flush=True)
                        print("Updated: " + str(selected_location), flush=True)

                        selected_listed_job_location.location_id = (
                            selected_location.id
                        )

                        selected_listed_job_location.verified = True
                        db.session.commit()

                    else:
                        # Debug here
                        # print("ListedJobLocation check completed for "
                        #       "ListedJob ID: " +
                        #       str(selected_job.id) + " Location ID: " +
                        #       str(selected_location.id), flush=True)
                        pass

                else:

                    selected_listed_job_location: ListedJobLocation = (
                        ListedJobLocation(
                            listed_job_id=int(selected_job.id),
                            location_id=int(selected_location.id)
                        )
                    )
                    db.session.add(selected_listed_job_location)
                    db.session.commit()

                    # print("ListedJobLocation added for ListedJob ID: " +
                    #       str(selected_job.id) + " Location ID: " +
                    #       str(selected_location.id), flush=True)

                # More debug
                # if new_jobs[i] is None:
                #     continue

                # Debugging
                # print("Key: " + i, flush=True)
                # for j in new_jobs[i].keys():
                #     if j is None:
                #         print("Jkey is NONE", flush=True)
                #         continue
                #     print("JKey: " + str(j), flush=True)
                #     if new_jobs[i][j] is None:
                #         print("JValue: None", flush=True)
                #         continue
                #     else:
                #         print('value: ' + str(new_jobs[i][j]), flush=True)
                # print("Value: " + str(new_jobs[i]), flush=True)
                # print(i + ": " + str(new_jobs[i]), flush=True)

            # raise ValueError("Only running first query")

        if (latest_date_time
                .replace(tzinfo=pytz.UTC)
                .strftime("%a, %d %b %Y %H:%M:%S.%f %Z") !=
                progress_timestamp):

            print("Reset current timestamp to " +
                  latest_date_time
                  .replace(tzinfo=pytz.UTC)
                  .strftime("%a, %d %b %Y %H:%M:%S.%f %Z"),
                  flush=True)

            # print(progress_timestamp + " vs. " +
            #       latest_date_time
            #       .replace(tzinfo=pytz.UTC)
            #       .strftime("%a, %d %b %Y %H:%M:%S.%f %Z"),
            #       flush=True)
            raise ChildProcessError(
                "Completed. Latest DateTime: [[" +
                latest_date_time
                .replace(tzinfo=pytz.UTC)
                .strftime("%a, %d %b %Y %H:%M:%S.%f %Z") + "]]"
            )

        raise ChildProcessError("Parsing Completed")

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        raise e

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        raise e

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        raise e

    # Handler Process error for jobs processed successfully.
    except ChildProcessError as e:
        if ('Completed. Latest DateTime: [[' not in str(e) or
                "Parsing Completed" not in str(e)):
            db.session.rollback()
        db.session.close()
        raise e

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}", flush=True)
        raise e

    finally:
        db.session.close()
