from flask import session
from sqlalchemy import asc, select, and_
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import load_only

from extensions_user import get_authenticated_user_name
from extensions_sql import db
from models.mariadb.api_list_url import APIListURL
from secrets_jobs.credentials import admin_list


def api_get_list():
    """
    Query database and get a dictionary of API List URL's.
    Include disabled as well.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return {}

    # Database methods are enclosed in a try-except block.
    try:
        # Retrieve the API List
        api_list = (
            db.session.query(APIListURL)
            .options(
                load_only(
                    APIListURL.nice_name,
                    APIListURL.last_access,
                    APIListURL.url,
                    APIListURL.disabled,
                    APIListURL.requests_count,
                    APIListURL.failed_count,
                )
            )
            .order_by(asc(APIListURL.id))
            .all()
        )
        # Convert to dictionary
        # Return successful upon creation
        return [i.to_dict_jinja_api_list() for i in api_list]

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        return {}

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        return {}

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        return {}

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        return {}


def api_get_list_base():
    """
    Query database and get a full list of APIListURL's
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return {}

    # Database methods are enclosed in a try-except block.
    try:
        # Retrieve the proxies
        api_list = (
            db.session.query(APIListURL)
            .filter(APIListURL.disabled.is_(False))
            .order_by(asc(APIListURL.id))
            .all()
        )
        # Convert to dictionary
        # Return successful upon creation
        return api_list

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        return {}

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        return {}

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        return {}

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        return {}


def get_api_list_url_only(api_id: int):
    """
    Query database and get API List URL (URL) only
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIListURL Table
        return (
            db.session.scalars(
                select(APIListURL)
                .filter(
                    and_(
                        APIListURL.id == api_id,
                        APIListURL.disabled.is_(False),
                    )
                )
                .options(load_only(APIListURL.url))
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


def get_api_list_url_full(api_id: int):
    """
    Query database and get API List URL data.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIListURL Table
        return (
            db.session.scalars(
                select(APIListURL)
                .filter(
                    and_(
                        APIListURL.id == api_id,
                        APIListURL.disabled.is_(False)
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


def get_api_list_url_filters_dashboard_display():
    """
    Query database and get API List URL data for dashboard display
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # print(str(filtered_types), flush=True)

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIListURL Table
        return (
            db.session.query(APIListURL)
            .filter(
                APIListURL.disabled.is_(False)
            )
            .options(
                load_only(
                    APIListURL.id,
                    APIListURL.nice_name,
                ),
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


def toggle_api(
        api_list_url_id: int,
        enable: bool = True):
    """
    Update API List URL to disable or enable based on user action
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return False

    if (enable is None or
            not isinstance(enable, bool) or
            api_list_url_id is None or
            not isinstance(api_list_url_id, int) or
            api_list_url_id < 0):
        return False

    # Database methods are enclosed in a try-except block.
    try:
        # Access APIListURL Table
        (db.session.query(APIListURL)
         .filter(APIListURL.id == api_list_url_id)
         .update({APIListURL.disabled: b'\x00' if enable else b'\x01'},
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
