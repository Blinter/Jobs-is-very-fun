from flask import session
from sqlalchemy import and_, select, func, asc
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import load_only, selectinload

from enums.api_endpoint_types import api_endpoint_type_to_description
from extensions_user import get_authenticated_user_name
from extensions_sql import db
from models.mariadb.api_list_url import APIListURL
from models.mariadb.api_headers import APIHeader
from models.mariadb.api_endpoints import APIEndpoint
from models.mariadb.api_endpoint_headers import APIEndpointHeader
from models.mariadb.api_endpoint_bodies import APIEndpointBody
from models.mariadb.api_endpoint_params import APIEndpointParam
from models.mariadb.api_endpoint_extras import APIEndpointExtra
from secrets_jobs.credentials import admin_list


def get_api_endpoint_name_id(api_id):
    """
    Query database and get API Endpoints.
    Load only id, api_id, nice_name, and disabled.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpoint Table
        return (
            db.session.scalars(
                select(APIEndpoint)
                .filter(
                    and_(
                        APIEndpoint.api_id == api_id,
                        APIEndpoint.disabled.is_(False)
                    )
                )
                .options(
                    load_only(
                        APIEndpoint.nice_name,
                        APIEndpoint.id,
                        APIEndpoint.api_id,
                        APIEndpoint.disabled
                    )
                )
            ).all()
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


def get_api_endpoint_description_only(api_endpoint_id: int):
    """
    Query database and get API Endpoint Description only
    Loads nice_description only.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access API APIEndpoint Table
        return (
            db.session.scalars(
                select(APIEndpoint)
                .filter(APIEndpoint.id == api_endpoint_id)
                .options(
                    load_only(APIEndpoint.nice_description)
                )
            ).first()
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


def get_api_endpoint_count_extras_only(api_endpoint_id: int):
    """
    Query database and get API Endpoint
    Loads only counts for Params/Bodies/Extra
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpointParam, APIEndpointBody, and APIEndpointExtra Tables
        return ([
            db.session.scalar(
                select(func.count(APIEndpointParam.api_endpoint_id))
                .filter(APIEndpointParam.api_endpoint_id == api_endpoint_id)
            ),
            db.session.scalar(
                select(func.count(APIEndpointBody.api_endpoint_id))
                .filter(APIEndpointBody.api_endpoint_id == api_endpoint_id)
            ),
            db.session.scalar(
                select(func.count(APIEndpointExtra.api_endpoint_id))
                .filter(APIEndpointExtra.api_endpoint_id == api_endpoint_id)
            )
        ])

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


def get_api_endpoint_extra_doc_list(api_endpoint_id: int):
    """
    Query database and get API Endpoint Extra ID's only.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpointExtra Table
        return (
            db.session.scalars(
                select(APIEndpointExtra)
                .filter(APIEndpointExtra.api_endpoint_id == api_endpoint_id)
                .options(load_only(APIEndpointExtra.id))
            ).all()
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


def get_api_endpoint_params(api_endpoint_id: int):
    """
    Query database and get API Endpoint Params.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpointParam Table
        return (
            db.session.scalars(
                select(APIEndpointParam)
                .filter(
                    and_(
                        APIEndpointParam.api_endpoint_id == api_endpoint_id,
                        APIEndpointParam.disabled.is_(False)
                    )
                )
                # .options(load_only())
            ).all()
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


def get_api_endpoint_bodies(api_endpoint_id: int):
    """
    Query database and get API Endpoint Bodies.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpointBody Table
        return (
            db.session.scalars(
                select(APIEndpointBody)
                .filter(
                    and_(
                        APIEndpointBody.api_endpoint_id == api_endpoint_id,
                        APIEndpointBody.disabled.is_(False)
                    )
                )
                # .options(load_only())
            ).all()
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


def get_api_endpoint_extra_doc(api_endpoint_extra_id: int):
    """
    Query database and get API Endpoint Extra Documentation content only.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpointExtra Table
        return (
            db.session.scalars(
                select(APIEndpointExtra)
                .filter(APIEndpointExtra.id == api_endpoint_extra_id)
                .options(load_only(APIEndpointExtra.extra_documentation))
            ).first()
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


def get_api_endpoint_http_path_and_nice_name_only(api_endpoint_id: int):
    """
    Query database and get API Endpoint HTTP Path and Nice_Name only.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpoint Table
        return (
            db.session.scalars(
                select(APIEndpoint)
                .filter(APIEndpoint.id == api_endpoint_id)
                .options(
                    load_only(
                        APIEndpoint.http_path,
                        APIEndpoint.nice_name
                    )
                )
            ).first()
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


def get_api_endpoint_full(api_endpoint_id: int):
    """
    Query database and get API Endpoint data.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpoint Table
        return (
            db.session.scalars(
                select(APIEndpoint)
                .filter(APIEndpoint.id == api_endpoint_id)
            ).first()
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


def get_api_endpoints_dashboard_display():
    """
    Query database and get API Endpoint data for display only.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpoint Table
        return (
            db.session.query(APIEndpoint)
            .options(
                load_only(
                    APIEndpoint.id,
                    APIEndpoint.api_id,
                    APIEndpoint.nice_name,
                    APIEndpoint.nice_description,
                    APIEndpoint.disabled,
                    APIEndpoint.type__
                ),
                selectinload(APIEndpoint.api)
                .load_only(
                    APIListURL.nice_name,
                    APIListURL.host
                )
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


def get_api_endpoints_type_list_existing():
    """
    Query database and get an API Types tuple list containing converted strings
     of distinct API Endpoint Types
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpoint Table
        type_list = []
        type_description_list = []
        found_types = (
            db.session.query(APIEndpoint.type__)
            .distinct()
            .order_by(asc(APIEndpoint.type__))
            .all()
        )

        if (found_types is None or
                len(found_types) == 0):
            db.session.close()
            return None

        for i in found_types:
            # print(
            #     str(i[0]) + " " + str(api_endpoint_type_to_description(i[0])),
            #     flush=True)
            type_list.append(i[0])
            type_description_list.append(api_endpoint_type_to_description(i[0]))

        return zip(type_list, type_description_list)

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


def get_api_endpoints_filtered_dashboard_display(filtered_types: list):
    """
    Query database and get API Endpoint data for display based on filters
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # print(str(filtered_types), flush=True)

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpoint Table
        return (
            db.session.query(APIEndpoint)
            .filter(APIEndpoint.type__.in_(filtered_types))
            .options(
                load_only(
                    APIEndpoint.id,
                    APIEndpoint.nice_name,
                    APIEndpoint.nice_description,
                    APIEndpoint.disabled,
                    APIEndpoint.type__
                ),
                selectinload(APIEndpoint.api)
                .load_only(
                    APIListURL.nice_name,
                    APIListURL.host
                )
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


def get_api_endpoints_filtered_mongo_storage_display(
        filtered_types: list,
        filtered_api_list_urls: list):
    """
    Query database and get API Endpoint data for display based on filters
    Retrieves only nice_name, and http_path for identification
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # print(str(filtered_types), flush=True)

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpoint Table
        return (
            db.session.query(APIEndpoint)
            .filter(
                and_(
                    APIEndpoint.type__.in_(
                        filtered_types
                    ) if (filtered_types is not None and
                          isinstance(filtered_types, list) and
                          '-1' not in filtered_types) else True,
                    APIEndpoint.api_id.in_(
                        filtered_api_list_urls
                    ) if (filtered_api_list_urls is not None and
                          isinstance(filtered_api_list_urls, list) and
                          '-1' not in filtered_api_list_urls) else True,
                )
            )
            .options(
                load_only(
                    APIEndpoint.nice_name,
                    APIEndpoint.http_path,
                    APIEndpoint.type__
                ),
            )
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


def toggle_endpoint(
        endpoint_id: int,
        enable: bool = True):
    """
    Update API endpoint to disable or enable based on user action
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return False

    if (enable is None or
            not isinstance(enable, bool) or
            endpoint_id is None or
            not isinstance(endpoint_id, int) or
            endpoint_id < 0):
        return False

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIListURL Table
        (db.session.query(APIEndpoint)
         .filter(APIEndpoint.id == endpoint_id)
         .update({APIEndpoint.disabled: b'\x00' if enable else b'\x01'},
                 synchronize_session='fetch'))
        db.session.commit()
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


def toggle_endpoint_header(
        endpoint_header_id: int,
        enable: bool = True):
    """
    Update API endpoint to disable or enable based on user action

    Note: There are no optional headers in the current API Endpoint list
    so this cannot be fully tested.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return False

    if (enable is None or
            not isinstance(enable, bool) or
            endpoint_header_id is None or
            not isinstance(endpoint_header_id, int) or
            endpoint_header_id < 0):
        return False

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpointHeader Table
        (db.session.query(APIEndpointHeader)
         .filter(APIEndpointHeader.id == endpoint_header_id)
         .update({APIEndpointHeader.disabled: b'\x00' if enable else b'\x01'},
                 synchronize_session='fetch'))
        db.session.commit()
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


def toggle_endpoint_param(
        endpoint_param_id: int,
        enable: bool = True):
    """
    Update an optional API Endpoint Param to
    disable or enable based on user action
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return False

    if (enable is None or
            not isinstance(enable, bool) or
            endpoint_param_id is None or
            not isinstance(endpoint_param_id, int) or
            endpoint_param_id < 0):
        return False

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpointHeader Table
        (db.session.query(APIEndpointParam)
         .filter(
            and_(
                APIEndpointParam.id == endpoint_param_id,
                APIEndpointParam.required == 0,
            )
        )
         .update({APIEndpointParam.disabled: b'\x00' if enable else b'\x01'},
                 synchronize_session='fetch'))
        db.session.commit()
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


def toggle_endpoint_body(
        endpoint_body_id: int,
        enable: bool = True):
    """
    Update an optional API Endpoint Body to
    disable or enable based on user action
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return False

    if (enable is None or
            not isinstance(enable, bool) or
            endpoint_body_id is None or
            not isinstance(endpoint_body_id, int) or
            endpoint_body_id < 0):
        return False

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIEndpointBody Table
        (db.session.query(APIEndpointBody)
         .filter(
            and_(
                APIEndpointBody.id == endpoint_body_id,
                APIEndpointBody.required == 0,
            )
        )
         .update({APIEndpointBody.disabled: b'\x00' if enable else b'\x01'},
                 synchronize_session='fetch'))
        db.session.commit()
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
