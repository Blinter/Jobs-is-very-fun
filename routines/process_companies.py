"""
This file can be run
cd <this directory>
PYTHONPATH=<base_dir> python3 <file_name>.py
"""
import argparse
from datetime import datetime, UTC

import pytz
from bson import ObjectId
from sqlalchemy import and_, asc, exists, or_
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import load_only

from app import create_app, db
from enums.api_endpoint_types import APIEndpointTypes
from extensions_mongo import fs_mongo
from extensions_proxies import http_pass_codes
from extensions_string import clean_unknown_characters
from models.mariadb.api_endpoints import APIEndpoint
from models.mariadb.api_list_url import APIListURL
from models.mariadb.mongo_storage import MongoStorage
from models.postgres.api_source import APISource
from models.postgres.company import Company
from routines.parsing.company import get_companies
from routines.parsing.apply_link import get_apply_link
from routines.parsing.job_title import get_job_titles
from routines.parsing.conversions import convert_bytes_to_dict_raw
from routines.parsing.description import get_descriptions

company_endpoints_type_list: list = [
    db.cast(APIEndpointTypes.JOBS_SEARCH.value, TINYINT()),
    db.cast(APIEndpointTypes.JOBS_FEED.value, TINYINT()),
    db.cast(APIEndpointTypes.JOB_DETAILS.value, TINYINT()),
    db.cast(APIEndpointTypes.COMPANY_DETAILS.value, TINYINT()),
    db.cast(APIEndpointTypes.COMPANY_SEARCH.value, TINYINT()),
]

company_extra_endpoints_type_list: list = [
    db.cast(APIEndpointTypes.COMPANY_DETAILS.value, TINYINT()),
    db.cast(APIEndpointTypes.COMPANY_SEARCH.value, TINYINT()),
]


endpoints_id_broken_list = []

# Endpoints containing extraneous company data
# mgujjargamingm | Linkedin BULK data scraper - Search Jobs
"""
company_data': {
        'name': '', 
        'logo': 'https://', 
        'backgroundCoverImage': 'https://', 
        'description': "Text", 
        'staffCount': 000, 
        'staffCountRange': {
            'staffCountRangeStart': 000, 
            'staffCountRangeEnd': 000
        }, 
        'universalName': '', 
        'url': 'https://www.linkedin.com/', 
        'industries': ['xxx'], 
        'specialities': [
            'xxx', 
        ]
    },
    'companyUniversalName': 'xxx', 
    'companyName': 'xxx', 
    'comapnyURL1': 'https://linkedin.com/ID',  <--- Typo
    'comapnyURL2': 'https://linkedin.com/NAME',  <--- Typo
    'companyId': '', 
    'companyApplyUrl': 'https://direct-company-link', '''
"""

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
     matching allowed endpoints only

     mongo storage columns: endpoint_nice_name, url
     endpoint columns: nice_name, http_path
    """
    result: list = (
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


def get_endpoint_filtered_types(database_app):
    """
    Retrieve full APIEndpoint List based on filtered types
    """
    return (
        database_app.session.query(APIEndpoint)
        .filter(
            and_(
                APIEndpoint.type__.in_(company_endpoints_type_list),
                APIEndpoint.id.not_in(endpoints_id_broken_list),
                APIEndpoint.disabled == 0
            )
        )
        .all()
    )


def get_company_details_filtered_types(database_app):
    """
    Retrieve full APIEndpoint List based on filtered types
    """
    return (
        database_app.session.query(APIEndpoint)
        .filter(
            and_(
                APIEndpoint.type__.in_(company_extra_endpoints_type_list),
                APIEndpoint.id.not_in(endpoints_id_broken_list),
                APIEndpoint.disabled == 0
            )
        )
        .all()
    )


# Parse Arguments
parser = argparse.ArgumentParser(
    description="Accept Datetime String as format "
                "(%a, %d %b %Y %H:%M:%S.%f %Z)")

parser.add_argument(
    '--date',
    type=str,
    help="Datetime of previously processed query"
)

args = parser.parse_args()
# print("Original: " +
#       progress_timestamp)
# print("Date Argument: " +
#       (args.date if args.date is not None else 'None'))

progress_timestamp = "Tue, 27 Aug 2024 11:15:07.831000 UTC"

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
            get_endpoint_filtered_types(database_app=db),
            date_filter=latest_date_time.replace(tzinfo=pytz.UTC),
            database_app=db
        )

        # Add fresh company names only
        for query in processed_queries:

            if (latest_date_time.replace(tzinfo=pytz.UTC) <
                    query.query_time.replace(tzinfo=pytz.UTC)):
                test_string = (
                    query.query_time
                    .replace(tzinfo=pytz.UTC)
                    .strftime("%a, %d %b %Y %H:%M:%S.%f %Z"))
                if not test_string.endswith("UTC"):
                    test_string += "UTC"
                # print("Reset current timestamp to " +
                #       test_string,
                #       flush=True)
                latest_date_time = query.query_time.replace(tzinfo=pytz.UTC)

            new_dict: dict = convert_bytes_to_dict_raw(
                fs_mongo.get(file_id=ObjectId(query.object_id))
                .read().decode()
            )

            # Fix for key
            if (query.url == "https://glassdoor.p.rapidapi.com"
                             "/job/" and
                    query.endpoint_nice_name == "Job details"):
                new_dict = {query.input_json.get('job_id'): new_dict}

            print("ID: " + str(query.id) + " " +
                  "URL: " + query.url + " (" + query.endpoint_nice_name + ")",
                  flush=True)

            new_companies = {}

            companies: dict = get_companies(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
            )

            company_added_count: int = 0

            for i in companies.keys():
                # print(str(i), flush=True)
                if i.startswith('error') or "error" in i.lower():
                    print("No Companies for ID: " + str(query.id) + " " +
                          str(query.endpoint_nice_name), flush=True)
                    for j in new_dict.keys():
                        if j.startswith('error') or "error" in j.lower():
                            break
                        new_companies[str(j)] = {'company': None}
                    break

                if companies[i] is None:
                    new_companies[i] = {
                        'company': None
                    }
                    continue

                if not isinstance(companies[i], str):
                    print("companies[i] = " + str(companies[i]) + " "
                          "key: " + i, flush=True)
                    raise ValueError("Fix this")

                # Clean Strings
                companies[i] = clean_unknown_characters(companies[i])

                # Add to companies
                company_str = companies[i]

                if (company_str is None or
                        len(company_str) == 0 or
                        company_str == ' '):
                    continue

                # Check if company is in Companies Table
                if not (db.session.query(
                        exists().where(Company.name.ilike(str(company_str))))
                        .scalar()):

                    selected_company: Company = Company(
                        name=str(company_str),
                        last_updated=datetime.now(UTC)
                    )
                    db.session.add(selected_company)
                    db.session.commit()
                    print("Added Company " + str(selected_company.name) + " " +
                          "ID: " + str(selected_company.id), flush=True)

                    company_added_count += 1
        db.session.commit()
        # Grab all queries
        # to process descriptions/apply links
        processed_queries: list = get_processed_query_list(
            get_company_details_filtered_types(database_app=db),
            date_filter=latest_date_time.replace(tzinfo=pytz.UTC),
            database_app=db,
        )

        for query in processed_queries:

            print("ID: " + str(query.id) + " " +
                  "URL: " + query.url + " (" + query.endpoint_nice_name + ")",
                  flush=True)

            new_dict: dict = convert_bytes_to_dict_raw(
                fs_mongo.get(file_id=ObjectId(query.object_id))
                .read().decode()
            )

            companies: dict = get_companies(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
            )

            # for i in companies.keys():
            #     print(i + ": " + str(companies[i]), flush=True)

            descriptions: dict = get_descriptions(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
            )

            apply_links: dict = get_apply_link(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
                input_json=query.input_json,
            )

            for i in descriptions.keys():
                if ("error" in i or
                        descriptions[i] is None or
                        "error" in descriptions[i] or
                        len(descriptions[i]) == 0):
                    continue

                if i in companies.keys():
                    if (companies[i] is None or
                            'error' in companies[i] or
                            len(companies[i]) == 0):
                        continue

                    # Check if company is in Companies Table
                    if not (db.session.query(
                            exists().where(
                                Company.name.ilike(
                                    clean_unknown_characters(companies[i]))
                            )).scalar()):
                        selected_company: Company = Company(
                            name=clean_unknown_characters(
                                companies[i]
                            ),
                            last_updated=datetime.now(UTC),
                            description=clean_unknown_characters(
                                descriptions[i]
                            )
                        )

                        db.session.add(selected_company)

                        db.session.commit()
                        print("Added Company " + str(
                            selected_company.name) + " " +
                              "ID: " + str(selected_company.id), flush=True)
                    else:
                        selected_company: Company = (
                            db.session.query(Company).filter(
                                Company.name.ilike(
                                    clean_unknown_characters(companies[i])
                                )
                            ).first()
                        )
                        if (selected_company.description is not None and
                                len(clean_unknown_characters(
                                    selected_company.description)) != 0):
                            # Comparing desc and keeping largest desc.
                            if (len(clean_unknown_characters(
                                    selected_company.description))
                                    < len(clean_unknown_characters(
                                        descriptions[i]))):
                                selected_company.description = (
                                    clean_unknown_characters(descriptions[i])
                                )
                                selected_company.last_updated = (
                                    datetime.now(UTC))
                                selected_company.verified = True
                                db.session.commit()

                                print("Updated description for " +
                                      selected_company.name + " ID: " +
                                      str(selected_company.id), flush=True)
                        else:
                            selected_company.description = (
                                clean_unknown_characters(descriptions[i])
                            )
                            selected_company.last_updated = datetime.now(UTC)
                            selected_company.verified = True
                            db.session.commit()

                            print("Updated description for " +
                                  selected_company.name + " ID: " +
                                  str(selected_company.id), flush=True)

            for i in apply_links.keys():
                if ("error" in i or
                        apply_links[i] is None or
                        "error" in apply_links[i] or
                        len(apply_links[i]) == 0):
                    continue

                if i in companies.keys():
                    if (companies[i] is None or
                            'error' in companies[i] or
                            len(companies[i]) == 0):
                        continue

                    if isinstance(apply_links[i], list):
                        print(str(apply_links[i]), flush=True)
                        raise ValueError("LIST FOUND")

                    # Check if company is in Companies Table
                    if not (db.session.query(
                            exists().where(
                                Company.name.ilike(
                                    clean_unknown_characters(companies[i]))
                            )).scalar()):
                        selected_company: Company = Company(
                            name=clean_unknown_characters(companies[i]),
                            last_updated=datetime.now(UTC),
                            websites=clean_unknown_characters(apply_links[i])
                        )

                        db.session.add(selected_company)
                        db.session.commit()
                        print("Added Company " + str(
                            selected_company.name) + " " +
                              "ID: " + str(selected_company.id), flush=True)

                    else:
                        selected_company: Company = (
                            db.session.query(Company).filter(
                                Company.name.ilike(
                                    clean_unknown_characters(companies[i])
                                )
                            ).first()
                        )
                        if (selected_company.websites is not None and
                                len(selected_company.websites) != 0):
                            # Comparing link and keeping largest link.
                            if (len(selected_company.websites) <
                                    len(apply_links[i])):

                                selected_company.websites = (
                                    clean_unknown_characters(apply_links[i])
                                )

                                selected_company.last_updated = (
                                    datetime.now(UTC)
                                )

                                selected_company.verified = True

                                db.session.commit()

                                print("Updated websites for " +
                                      selected_company.name + " ID: " +
                                      str(selected_company.id), flush=True)
                        else:
                            selected_company.websites = (
                                clean_unknown_characters(apply_links[i])
                            )

                            selected_company.last_updated = datetime.now(UTC)
                            selected_company.verified = True

                            db.session.commit()

                            print("Updated websites for " +
                                  selected_company.name + " ID: " +
                                  str(selected_company.id), flush=True)

        # print("=====", flush=True)
        # print(str(company_added_count) + " new companies added.", flush=True)
        # print("Company Process complete!", flush=True)

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
                'Parsing Completed' not in str(e)):
            db.session.rollback()
        db.session.close()
        raise e

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}", flush=True)
        raise e
