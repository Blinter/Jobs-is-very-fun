
from extensions_sql import db, get_session
from bson import ObjectId
from flask import session
from sqlalchemy import select, desc, exists, asc
from sqlalchemy.orm import load_only

from extensions_api_endpoints import (
    get_api_endpoints_filtered_mongo_storage_display
)

from extensions_user import get_authenticated_user_name
from models.mariadb.mongo_scrape_storage import MongoScrapeStorage
from models.mariadb.mongo_storage import MongoStorage
from secrets_jobs.credentials import (
    mongodb_information_login_details,
    mongodb_database_name,
    admin_list
)

from pymongo import MongoClient
import gridfs
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

pymongo_client = MongoClient(mongodb_information_login_details)
db_mongo = pymongo_client[mongodb_database_name]
fs_mongo = gridfs.GridFS(db_mongo)

# API provides only HTML output when requesting JSON data.
mongo_html_output = {
    'https://job-postings1.p.rapidapi.com/': '/api/v2/Jobs/Latest'
}


def fs_upload(input_to_upload: bytes):
    return fs_mongo.put(
        data=input_to_upload
    ) if input else 0


def fs_delete(object_id: ObjectId):
    if not object_id:
        print("Invalid ObjectId provided.", flush=True)
        return False

    try:
        fs_mongo.delete(object_id)
        print(f"Successfully deleted file with id {object_id}", flush=True)
        return True

    except gridfs.errors.NoFile:
        print(f"No file found with id {object_id}", flush=True)
        return False

    except Exception as e:
        print(f"An error occurred: {e}", flush=True)
        return False


def check_db():
    return mongodb_database_name in pymongo_client.list_database_names()


def check_exists(file_hash):
    return fs_mongo.exists(file_hash)


def check_for_html_output(mongo_storage_id: int):
    found_mongo = get_mongo_db_url_nice_name_and_input(mongo_storage_id)

    return (found_mongo and
            found_mongo.url in mongo_html_output.keys() and
            mongo_html_output[found_mongo.url] ==
            found_mongo.endpoint_nice_name)


def mongo_storage_add(new_mongo_storage: MongoStorage):
    """
    Query database and get API Endpoint data.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        db.session.add(new_mongo_storage)
        db.session.commit()
        result = str(new_mongo_storage.id)
        db.session.close()
        return result

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        return None

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}", flush=True)
        return None


def get_mongo_doc(mongo_id: int):
    """
    Query database and pull MongoDB query response data as string
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access MongoStorage Table and load only object ID
        # Return decoded data as string from MongoDB accessing the object_id
        mongo_object_id = (
            db.session.scalars(
                select(MongoStorage)
                .filter(MongoStorage.id == mongo_id)
                .options(load_only(MongoStorage.object_id))
            ).first().object_id
        )
        db.session.close()

        return (
            fs_mongo.get(
                file_id=ObjectId(mongo_object_id)
            ).read().decode()
        )

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


def get_mongo_doc_raw(mongo_id: int):
    """
    Query database and pull MongoDB raw query response data
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            mongo_id < 0 or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access MongoStorage Table and load only object_id
        # (MongoStorage Data Object)
        # Return bytes read from MongoDB accessing the object_id
        mongo_object_id = (
            db.session.scalars(
                select(MongoStorage)
                .filter(MongoStorage.id == mongo_id)
                .options(load_only(MongoStorage.object_id))
            ).first().object_id
        )
        db.session.close()

        return (
            fs_mongo.get(
                file_id=ObjectId(mongo_object_id)
            ).read()
        )

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


def get_mongo_scrape_from_url(job_url: str):
    """
    Query database and pull MongoDB raw scrape response data based from
    apply link

    Compatibility in the same session between two different databases,
    add a new session with mariadb.
    """

    # Database methods are enclosed in a try-except block.
    try:
        database_app_session = get_session('mariadb')

        # Check if job_url exists in the MongoScrapeStorage
        if (job_url is None or
                len(job_url) == 0 or
                not database_app_session.query(
                    exists().where(MongoScrapeStorage.url.ilike(job_url))
                ).scalar()):
            database_app_session.close()
            return None
        else:
            database_app_session.close()

        # print("URL: " + str(job_url), flush=True)

        mongo_scrape_object_id: ObjectId = (
            db.session.scalars(
                select(MongoScrapeStorage)
                .filter(MongoScrapeStorage.url.ilike(job_url))
                .options(load_only(MongoScrapeStorage.object_id))
            )
            .first()
            .object_id
        )
        db.session.close()
        # print("Object ID: " + str(mongo_scrape_object_id), flush=True)

        scraped_data = fs_mongo.get(
                file_id=ObjectId(mongo_scrape_object_id)
            ).read().decode()

        # print(scraped_data, flush=True)

        return scraped_data

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


def get_mongo_scrape_doc(mongo_scrape_id: int):
    """
    Query database and pull MongoDB raw scrape response data
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            mongo_scrape_id < 0 or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access MongoScrapeStorage Table and load only object_id
        # (MongoScrapeStorage Data Object)
        # Return bytes read from MongoDB accessing the object_id
        mongo_scrape_object_id: ObjectId = (
            db.session.scalars(
                select(MongoScrapeStorage)
                .filter(MongoScrapeStorage.id == mongo_scrape_id)
                .options(load_only(MongoScrapeStorage.object_id))
            ).first().object_id
        )
        db.session.close()
        return (
            fs_mongo.get(
                file_id=ObjectId(mongo_scrape_object_id)
            ).read().decode()
        )

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


def get_mongo_storage():
    """
    Query database and get all Mongo Storage Rows
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access MongoStorage Table and get all rows
        return (
            db.session.query(MongoStorage)
            .order_by(desc(MongoStorage.id))
            .limit(300) # Hard limit fix, add pagination later
            .all()
        )

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


def get_mongo_scrape_storage():
    """
    Query database and get all Mongo Scrape Storage Rows
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access MongoStorage Table and get all rows
        return (
            db.session.query(MongoScrapeStorage)
            .order_by(
                desc(MongoScrapeStorage.code),
                desc(MongoScrapeStorage.query_time)
            )
            .all()
        )

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


def get_mongo_scrape_storage_paginate(
        sort_method: str,
        page_number: int,
        items=1000):
    """
    Query database and get all Mongo Scrape Storage Rows
    Paginates with 1000 rows per page.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    if (sort_method is None or
            not isinstance(sort_method, str) or
            len(sort_method) == 0):
        return None

    # paginate from page number
    if (page_number is None or
            page_number == 0):
        page_number = 1

    if (items is None or
            items < 2):
        print("Increasing item count to 2.", flush=True)
        items = 2

    if items > 8000:
        print("Decreasing item count to 8000.", flush=True)
        items = 8000

    sql_offset = (items * page_number) - items

    # Database methods are enclosed in a try-except block.
    try:
        # Access MongoStorage Table
        match sort_method:
            case "query_time_desc":
                return (
                    db.session.query(MongoScrapeStorage)
                    .order_by(
                        desc(MongoScrapeStorage.query_time)
                    )
                    .limit(items)
                    .offset(sql_offset)
                    .all()
                )

            case "query_time_asc":
                return (
                    db.session.query(MongoScrapeStorage)
                    .order_by(
                        asc(MongoScrapeStorage.query_time)
                    )
                    .limit(items)
                    .offset(sql_offset)
                    .all()
                )

            case "id_desc":
                return (
                    db.session.query(MongoScrapeStorage)
                    .order_by(
                        desc(MongoScrapeStorage.id)
                    )
                    .limit(items)
                    .offset(sql_offset)
                    .all()
                )

            case "id_asc":
                return (
                    db.session.query(MongoScrapeStorage)
                    .order_by(
                        asc(MongoScrapeStorage.id)
                    )
                    .limit(items)
                    .offset(sql_offset)
                    .all()
                )

            case "time_desc":
                return (
                    db.session.query(MongoScrapeStorage)
                    .order_by(
                        desc(MongoScrapeStorage.time)
                    )
                    .limit(items)
                    .offset(sql_offset)
                    .all()
                )

            case "time_asc":
                return (
                    db.session.query(MongoScrapeStorage)
                    .order_by(
                        asc(MongoScrapeStorage.time)
                    )
                    .limit(items)
                    .offset(sql_offset)
                    .all()
                )

            case "code_desc":
                return (
                    db.session.query(MongoScrapeStorage)
                    .order_by(
                        desc(MongoScrapeStorage.code)
                    )
                    .limit(items)
                    .offset(sql_offset)
                    .all()
                )

            case "code_asc":
                return (
                    db.session.query(MongoScrapeStorage)
                    .order_by(
                        asc(MongoScrapeStorage.code)
                    )
                    .limit(items)
                    .offset(sql_offset)
                    .all()
                )

            case "length_desc":
                return (
                    db.session.query(MongoScrapeStorage)
                    .order_by(
                        desc(MongoScrapeStorage.length)
                    )
                    .limit(items)
                    .offset(sql_offset)
                    .all()
                )

            case "length_asc":
                return (
                    db.session.query(MongoScrapeStorage)
                    .order_by(
                        asc(MongoScrapeStorage.length)
                    )
                    .limit(items)
                    .offset(sql_offset)
                    .all()
                )

            case _:
                return (
                    db.session.query(MongoScrapeStorage)
                    .order_by(
                        desc(MongoScrapeStorage.code),
                        desc(MongoScrapeStorage.query_time)
                    )
                    .limit(items)
                    .offset(sql_offset)
                    .all()
                )

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


def get_mongo_db_url_nice_name_and_input(mongo_storage_id: int):
    """
    Query database and retrieve mongo_storage URL/nice_name/InputJSON data
    from mariadb row
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access MongoStorage Table and retrieve URL data based on ID
        return (
            db.session.query(MongoStorage)
            .filter(MongoStorage.id == mongo_storage_id)
            .options(
                load_only(
                    MongoStorage.url,
                    MongoStorage.endpoint_nice_name,
                    MongoStorage.input_json
                )
            )
            .first()
        )

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


def get_mongo_db_url_query_time(mongo_storage_id: int):
    """
    Query database and retrieve mongo_storage query_time data
    from mariadb row
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access MongoStorage Table and retrieve URL data based on ID
        return (
            db.session.query(MongoStorage)
            .filter(MongoStorage.id == mongo_storage_id)
            .options(load_only(MongoStorage.query_time))
            .first()
        )

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


def get_mongo_storage_filtered_dashboard_display(
        filtered_types: list,
        filtered_api_list_urls: list):
    """
    Query database and get API Endpoint data for display based on filters
    Unique Columns:
        api
        endpoint_nice_name
        url
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # print(str(filtered_types), flush=True)

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpoint Table
        # API_Endpoints_List
        found_endpoints = (
            get_api_endpoints_filtered_mongo_storage_display(
                filtered_types=filtered_types,
                filtered_api_list_urls=filtered_api_list_urls
            )
        )

        if found_endpoints is None:
            db.session.close()
            return None

        # for i in found_endpoints:
        #     print(str(i.nice_name), flush=True)
        found_endpoints_alias = db.aliased(found_endpoints.subquery())

        # match endpoint nice_name column
        # match endpoint http_path (Path parameters + suffix not included)
        return (
            db.session.query(MongoStorage)
            .join(
                found_endpoints_alias,
                (MongoStorage.endpoint_nice_name ==
                 found_endpoints_alias.c.nice_name) &
                (MongoStorage.url == found_endpoints_alias.c.http_path),
                isouter=False
            )
            .order_by(desc(MongoStorage.id))
            .limit(300) # Hard limit fix, add pagination later
            .all()
        )

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


def delete_mongo_storage(mongo_storage_id: int):
    """
    Delete Mongo Storage Row from MongoStorage Table and from MongoDB
    """

    # Check if User is logged in and is an admin.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return False

    # Session context will switch from Postgres to MariaDB
    # Database methods are enclosed in a try-except block.
    try:
        database_app_session = get_session('mariadb')

        if (mongo_storage_id is None or
                not isinstance(mongo_storage_id, int) or
                mongo_storage_id < 0 or
                not database_app_session.query(
                    exists().where(MongoStorage.id == mongo_storage_id)
                ).scalar()):
            print("Does not exist", flush=True)
            database_app_session.close()
            return False
        else:
            database_app_session.close()

        current_mongo_storage = (
            db.session.query(MongoStorage)
            .filter(MongoStorage.id == int(mongo_storage_id))
            .options(load_only(MongoStorage.object_id))
            .first()
        )

        if (current_mongo_storage.object_id is None or
                not check_exists(current_mongo_storage.object_id)):
            # Delete from MongoStorage
            db.session.delete(current_mongo_storage)
            db.session.commit()
            db.session.close()
            return True

        if fs_delete(current_mongo_storage.object_id):
            # Delete from MongoStorage
            db.session.delete(current_mongo_storage)
            db.session.commit()

        else:
            print("Could not delete Object from MongoDB. Clean this up later.",
                  flush=True)

        db.session.close()
        return True

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        return False

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        return False

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        return False

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}", flush=True)
        return False


def delete_mongo_scrape_storage(mongo_scrape_storage_id: int):
    """
    Delete Mongo Storage Row from MongoStorage Table and from MongoDB
    """

    # Check if User is logged in and is an admin.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return False

    # Session context will switch from Postgres to MariaDB
    # Database methods are enclosed in a try-except block.
    try:
        database_app_session = get_session('mariadb')

        if (mongo_scrape_storage_id is None or
                not isinstance(mongo_scrape_storage_id, int) or
                mongo_scrape_storage_id < 0 or
                not database_app_session.query(
                    exists().where(
                        MongoScrapeStorage.id == int(mongo_scrape_storage_id))
                ).scalar()):
            print("Does not exist", flush=True)
            database_app_session.close()
            return False
        else:
            database_app_session.close()

        current_mongo_scrape_storage = (
            db.session.query(MongoScrapeStorage)
            .filter(MongoScrapeStorage.id == int(mongo_scrape_storage_id))
            .options(load_only(MongoScrapeStorage.object_id))
            .first()
        )

        if (current_mongo_scrape_storage.object_id is None or
                not check_exists(current_mongo_scrape_storage.object_id)):
            # Delete from MongoScrapeStorage
            db.session.delete(current_mongo_scrape_storage)
            db.session.commit()
            db.session.close()
            return True

        if fs_delete(current_mongo_scrape_storage.object_id):
            # Delete from MongoScrapeStorage
            db.session.delete(current_mongo_scrape_storage)
            db.session.commit()

        else:
            print("Could not delete Object from MongoDB. Clean this up later.",
                  flush=True)

        db.session.close()
        return True

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        return False

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        return False

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        return False

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}", flush=True)
        return False
