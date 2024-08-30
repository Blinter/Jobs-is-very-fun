"""
This file can be run
cd <this directory>
PYTHONPATH=<base_dir> python3 <file_name>.py
"""
from datetime import datetime, UTC

from bson import ObjectId
from sqlalchemy import and_, asc, exists, or_
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import load_only

from app import create_app, db
from enums.api_endpoint_types import APIEndpointTypes
from extensions_mongo import fs_mongo
from extensions_proxies import http_pass_codes
from models.mariadb.api_endpoints import APIEndpoint
from models.mariadb.api_list_url import APIListURL
from models.mariadb.mongo_storage import MongoStorage
from models.postgres.api_source import APISource
from models.postgres.company import Company
from models.postgres.listed_job import ListedJob
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


def get_processed_query_list(endpoint_types_list: list, database_app):
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
            )
        )
        .order_by(asc(MongoStorage.time))
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
                #       "(" + endpoint_.http_path + ")")

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


with app.app_context():
    try:
        # populate ID's for broken endpoints
        endpoints_id_broken_list = populate_broken_endpoint_list(db)

        # Grab all queries
        processed_queries = get_processed_query_list(
            get_scrape_endpoint_filtered_types(database_app=db),
            database_app=db
        )
        for query in processed_queries:
            # Skip 2 minute+ parse
            # if (query.url == "https://jsearch.p.rapidapi.com"
            #                  "/search" and
            #         query.endpoint_nice_name == "Search"):
            #     continue
            # elif (query.url != "https://active-jobs-db.p.rapidapi.com"
            #                    "/rest/v1/active_ats_textdescription_v1" and
            #       query.endpoint_nice_name !=
            #       "Get Jobs - (Text Description)"):
            #     continue

            selected_api_name = (
                db.session.query(APIListURL.nice_name).filter(
                    APIListURL.url == query.api).first()[0]
            )
            # print('selected api name: ' + str(selected_api_name))

            # Check if API is in API_Sources Table
            if not (db.session.query(
                    exists().where(
                        APISource.name == str(selected_api_name))).scalar()):

                selected_api_source = APISource(
                    name=str(selected_api_name),
                    last_updated=datetime.now(UTC)
                )
                db.session.add(selected_api_source)
                db.session.commit()
                # print("Added APISource - " + str(selected_api_source))
            else:
                selected_api_source = (
                    db.session.query(APISource).filter(
                        APISource.name == str(selected_api_name)
                    ).first()
                )
                # print("Selected APISource - " + selected_api_source.name)

            new_dict = convert_bytes_to_dict_raw(
                fs_mongo.get(file_id=ObjectId(query.object_id))
                .read().decode()
            )

            # Fix for key
            if (query.url == "https://glassdoor.p.rapidapi.com"
                             "/job/" and
                    query.endpoint_nice_name == "Job details"):
                new_dict = {query.input_json.get('job_id'): new_dict}

            # Default debug
            print("ID: " + str(query.id) + " " +
                  "URL: " + query.url + " (" + query.endpoint_nice_name + ")")

            new_jobs = {}

            for i in new_dict.keys():
                if "error" in str(i).lower():
                    break

                new_jobs[str(i)] = {'api_source': selected_api_source}

            experience_levels = get_experience_levels(
                api_url=query.url,
                nice_name=query.endpoint_nice_name,
                dict_new=new_dict,
            )

            print("ID: " + str(query.id) + " " +
                  "URL: " + query.url + " (" + query.endpoint_nice_name + ")")

            # Add experience levels to the dictionary
            for i in experience_levels.keys():
                if "error" in str(i).lower():
                    # print("No experience for ID: " + str(query.id) + " " +
                    #       query.endpoint_nice_name)
                    for j in new_dict.keys():
                        if "error" in str(j).lower():
                            break
                        # new_jobs[str(j)]['name'] = None
                    break
                # print("Key: " + str(i))
                # print("Trace: " + str(names[str(i)]))

                new_jobs[str(i)]['experience_levels'] = (
                    experience_levels[str(i)])

                # Debugging
                print("Key: " + str(i))
                for j in new_jobs[str(i)].keys():
                    if j is None:
                        print("Jkey is NONE")
                        continue
                    print("JKey: " + str(j))
                    if new_jobs[i][j] is None:
                        print("JValue: None")
                        continue
                    else:
                        print('value: ' + str(new_jobs[i][j]))

                print("Value: " + str(new_jobs[str(i)]))
                print(str(i) + ": " + str(new_jobs[str(i)]))

        db.session.close()
        print("Parsing Completed.")

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {e}.")
        raise e

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        print(f"OperationalError: {e}.")
        raise e

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"SQLAlchemyError: {e}.")
        raise e

    # Other Errors
    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}.")
        raise e
