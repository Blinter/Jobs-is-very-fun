import datetime

from flask import session
from sqlalchemy import and_, or_, select, asc
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import load_only

from extensions_user import get_authenticated_user_name
from extensions_sql import db
from models.mariadb.api_list_url import APIListURL
from models.mariadb.api_keys import APIKey
from datetime import datetime, UTC, timedelta
from secrets_jobs.credentials import admin_list


def calculate_next(
        api: APIListURL,
        current_date_time_utc=datetime.now(UTC)):
    """
    Calculate next query time after an API key is used.
    """
    try:
        max_date_time_utc = current_date_time_utc

        if api.month_limit is not None:
            # Calculate amount of queries per month
            # 31 days max
            max_date_time_utc = (
                max(
                    max_date_time_utc,
                    (current_date_time_utc +
                     timedelta(days=(
                             31/api.month_limit
                     )))
                )
            )

        if api.daily_limit is not None:
            # Calculate amount of queries per day
            max_date_time_utc = (
                max(max_date_time_utc,
                    (current_date_time_utc +
                     timedelta(hours=(24/api.daily_limit)))))

        if api.hour_limit is not None:
            # Calculate amount of queries per hour
            max_date_time_utc = (
                max(
                    max_date_time_utc,
                    (current_date_time_utc +
                     timedelta(minutes=(
                             60/api.hour_limit
                     )))
                )
            )

        if api.minute_limit is not None:
            # Calculate amount of queries per minute
            max_date_time_utc = (
                max(
                    max_date_time_utc,
                    (current_date_time_utc +
                     timedelta(seconds=(
                             60/api.minute_limit)))
                )
            )

        if api.second_limit_per is not None:
            # Calculate amount of queries per second from milliseconds
            max_date_time_utc = (
                max(
                    max_date_time_utc,
                    (current_date_time_utc +
                     timedelta(milliseconds=(
                             1000/api.second_limit_per)))
                )
            )

        return max_date_time_utc

    # Catch any errors related to timedate or timedelta functions.
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)
        # Default to one extra day.
        return datetime.now(UTC) + timedelta(days=1)


def calculate_next_special(
        api: APIListURL,
        api_key: APIKey,
        current_date_time_utc=datetime.now(UTC)):
    """
    Calculate next query time after an API key is used.
    """
    try:
        max_date_time_utc = current_date_time_utc

        # Revert back to normal limits if APIKey does not have special limits
        # set.
        if not api_key.special_limits:

            if api.month_limit is not None:
                # Calculate amount of queries per month
                # 31 days max
                max_date_time_utc = (
                    max(
                        max_date_time_utc,
                        (current_date_time_utc +
                         timedelta(days=(
                                 31/api.month_limit)))
                    )
                )

            if api.daily_limit is not None:
                # Calculate amount of queries per day
                max_date_time_utc = (
                    max(
                        max_date_time_utc,
                        (current_date_time_utc +
                         timedelta(hours=(
                                 24/api.daily_limit)))
                    )
                )

            if api.hour_limit is not None:
                # Calculate amount of queries per hour
                max_date_time_utc = (
                    max(
                        max_date_time_utc,
                        (current_date_time_utc +
                         timedelta(minutes=(
                                 60/api.hour_limit)))
                        )
                )

            if api.minute_limit is not None:
                # Calculate amount of queries per minute
                max_date_time_utc = (
                    max(
                        max_date_time_utc,
                        (current_date_time_utc +
                         timedelta(seconds=(
                                 60/api.minute_limit)))
                        )
                )

            if api.second_limit_per is not None:
                # Calculate amount of queries per second from milliseconds
                max_date_time_utc = (
                    max(max_date_time_utc,
                        (current_date_time_utc +
                         timedelta(milliseconds=(
                                 1000/api.second_limit_per)))
                        )
                )

            return max_date_time_utc

        else:

            if api_key.custom_month_limit is not None:
                # Calculate amount of queries per month
                # 31 days max
                max_date_time_utc = (
                    max(
                        max_date_time_utc,
                        (current_date_time_utc +
                         timedelta(days=(
                                 31/api_key.custom_month_limit)))
                        )
                )

            if api_key.custom_daily_limit is not None:
                # Calculate amount of queries per day
                max_date_time_utc = (
                    max(
                        max_date_time_utc,
                        (current_date_time_utc +
                         timedelta(hours=(
                                 24/api_key.custom_daily_limit)))
                    )
                )

            if api_key.custom_hour_limit is not None:
                # Calculate amount of queries per hour
                max_date_time_utc = (
                    max(max_date_time_utc,
                        (current_date_time_utc +
                         timedelta(minutes=(
                                 60/api_key.custom_hour_limit)))
                        )
                )

            if api_key.custom_minute_limit is not None:
                # Calculate amount of queries per minute
                max_date_time_utc = (
                    max(
                        max_date_time_utc,
                        (current_date_time_utc +
                         timedelta(seconds=(
                                 60/api_key.custom_minute_limit)))
                        )
                )

            if api_key.custom_second_limit_per is not None:
                # Calculate amount of queries per second from milliseconds
                max_date_time_utc = (
                    max(
                        max_date_time_utc,
                        (current_date_time_utc +
                         timedelta(milliseconds=(
                                 1000/api_key.custom_second_limit_per)))
                        )
                )

            return max_date_time_utc

    # Catch any errors related to timedate or timedelta functions.
    except Exception as e:
        db.session.close()
        print(f"Error: {e}", flush=True)

        # Default to one extra day.
        return datetime.now(UTC) + timedelta(days=1)


def get_api_key_id_key(api_id: int):
    """
    Query database and use selective load to grab ID's and Keys.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access the API keys that can be queried in the next access only
        # order the API Key list by lowest next_access
        return (
            db.session.scalars(
                select(APIKey, APIListURL)
                .filter(
                    and_(APIKey.url == APIListURL.url,
                         APIListURL.id == api_id,
                         APIListURL.disabled.is_(False),
                         APIKey.disabled.is_(False),
                         or_(
                             APIKey.next_access.is_(None),
                             APIKey.next_access <= datetime.now(UTC))
                         )
                )
                .order_by(asc(APIKey.next_access))
                .options(
                    load_only(
                        APIKey.id,
                        APIKey.key)
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


def get_api_keys_last_access_only(api_key_id: int):
    """
    Query database and retrieve last_access data only.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access API keys based on query.
        return (
            db.session.scalars(
                select(APIKey)
                .filter(APIKey.id == api_key_id)
                .options(load_only(APIKey.last_access))
            ).first()
        )

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}")
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}")
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}")
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}")
        return None


def get_api_key_preferred_proxy(api_key_id: int):
    """
    Query database and retrieve last_access data only.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access API key preferred proxy based on query.
        return (
            db.session.scalars(
                select(APIKey.preferred_proxy)
                .filter(APIKey.id == api_key_id)
            ).first()
        )

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}")
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}")
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}")
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}")
        return None


def get_api_key_only(api_key_id: int):
    """
    Query database and retrieve API Key based on ID.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return None

    # Database methods are enclosed in a try-except block.
    try:
        # Access API keys based on query.
        return (
            db.session.scalars(
                select(APIKey)
                .filter(APIKey.id == api_key_id)
                .options(load_only(APIKey.key))
            ).first()
        )

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.close()
        print(f"IntegrityError: {e}")
        return None

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.close()
        print(f"OperationalError: {e}")
        return None

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.close()
        print(f"SQLAlchemyError: {e}")
        return None

    # Other Errors
    except Exception as e:
        db.session.close()
        print(f"Error: {e}")
        return None
