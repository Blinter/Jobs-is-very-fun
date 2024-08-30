import requests
from flask import session
from requests.auth import HTTPBasicAuth
from sqlalchemy import asc, select
from sqlalchemy.dialects.mysql import TINYINT, SMALLINT
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError
from sqlalchemy.orm import load_only

from enums.proxies import ProxyType
from enums.response_codes import ResponseCodesGeneric
from extensions_user import get_authenticated_user_name
from extensions_sql import db
from models.mariadb.proxies import Proxy
from secrets_jobs.credentials import admin_list, proxy_public_website_check

preferred_residential_proxy_type_list = [
    db.cast(ProxyType.PREMIUM_STATIC_RES_HTTPS.value, TINYINT()),
    # db.cast(ProxyType.DEDICATED_RES_HTTPS.value, TINYINT()),
    # db.cast(ProxyType.ROTATING_RES_HTTPS.value, TINYINT()),
    # db.cast(ProxyType.PRIVATE_RES_HTTPS.value, TINYINT()),
    # db.cast(ProxyType.FREE_RES_HTTPS.value, TINYINT()),
    # db.cast(ProxyType.OWN_RES_HTTPS.value, TINYINT()),
    # db.cast(ProxyType.RES_HTTPS.value, TINYINT()),

    db.cast(ProxyType.PREMIUM_STATIC_RES_HTTP.value, TINYINT()),
    # db.cast(ProxyType.ROTATING_RES_HTTP.value, TINYINT()),
    # db.cast(ProxyType.DEDICATED_RES_HTTP.value, TINYINT()),
    # db.cast(ProxyType.PRIVATE_RES_HTTP.value, TINYINT()),
    # db.cast(ProxyType.FREE_RES_HTTP.value, TINYINT()),
    # db.cast(ProxyType.OWN_RES_HTTP.value, TINYINT()),
    # db.cast(ProxyType.RES_HTTP.value, TINYINT()),

    db.cast(ProxyType.PREMIUM_STATIC_RES_SOCKS4.value, TINYINT()),
    # db.cast(ProxyType.DEDICATED_RES_SOCKS4.value, TINYINT()),
    # db.cast(ProxyType.ROTATING_RES_SOCKS4.value, TINYINT()),
    # db.cast(ProxyType.PRIVATE_RES_SOCKS4.value, TINYINT()),
    # db.cast(ProxyType.FREE_RES_SOCKS4.value, TINYINT()),
    # db.cast(ProxyType.OWN_RES_SOCKS4.value, TINYINT()),
    # db.cast(ProxyType.RES_SOCKS4.value, TINYINT()),

    db.cast(ProxyType.PREMIUM_STATIC_RES_SOCKS5.value, TINYINT()),
    # db.cast(ProxyType.DEDICATED_RES_SOCKS5.value, TINYINT()),
    # db.cast(ProxyType.ROTATING_RES_SOCKS5.value, TINYINT()),
    # db.cast(ProxyType.PRIVATE_RES_SOCKS5.value, TINYINT()),
    # db.cast(ProxyType.FREE_RES_SOCKS5.value, TINYINT()),
    # db.cast(ProxyType.OWN_RES_SOCKS5.value, TINYINT()),
    # db.cast(ProxyType.RES_SOCKS5.value, TINYINT())
]

proxy_type_prefix_dict = {
    "http://": [
        ProxyType.PREMIUM_STATIC_RES_HTTP,
        ProxyType.ROTATING_RES_HTTP,
        ProxyType.DEDICATED_RES_HTTP,
        ProxyType.PRIVATE_RES_HTTP,
        ProxyType.FREE_RES_HTTP,
        ProxyType.OWN_RES_HTTP,
        ProxyType.RES_HTTP,
        ProxyType.DC_HTTP,
        ProxyType.FREE_DC_HTTP,
        ProxyType.OWN_DC_HTTP,
        ProxyType.PREMIUM_DC_HTTP,
        ProxyType.PRIVATE_DC_HTTP,
        ProxyType.ROTATING_DC_HTTP,
        ProxyType.DEDICATED_DC_HTTP,
        ProxyType.SCRAPED_UNTRUSTED_HTTP,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_1_HTTP,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_2_HTTP,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_3_HTTP,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_4_HTTP,
    ],
    "https://": [
        ProxyType.PREMIUM_STATIC_RES_HTTPS.value,
        ProxyType.DEDICATED_RES_HTTPS.value,
        ProxyType.ROTATING_RES_HTTPS.value,
        ProxyType.PRIVATE_RES_HTTPS.value,
        ProxyType.FREE_RES_HTTPS.value,
        ProxyType.OWN_RES_HTTPS.value,
        ProxyType.RES_HTTPS.value,
        ProxyType.DC_HTTPS.value,
        ProxyType.FREE_DC_HTTPS.value,
        ProxyType.OWN_DC_HTTPS.value,
        ProxyType.PREMIUM_DC_HTTPS.value,
        ProxyType.PRIVATE_DC_HTTPS.value,
        ProxyType.ROTATING_DC_HTTPS.value,
        ProxyType.DEDICATED_DC_HTTPS.value,
        ProxyType.SCRAPED_UNTRUSTED_HTTPS.value,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_1_HTTPS.value,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_2_HTTPS.value,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_3_HTTPS.value,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_4_HTTPS.value,
    ],
    "socks4://": [
        ProxyType.PREMIUM_STATIC_RES_SOCKS4.value,
        ProxyType.DEDICATED_RES_SOCKS4.value,
        ProxyType.ROTATING_RES_SOCKS4.value,
        ProxyType.PRIVATE_RES_SOCKS4.value,
        ProxyType.FREE_RES_SOCKS4.value,
        ProxyType.OWN_RES_SOCKS4.value,
        ProxyType.RES_SOCKS4.value,
        ProxyType.DC_SOCKS4.value,
        ProxyType.FREE_DC_SOCKS4.value,
        ProxyType.OWN_DC_SOCKS4.value,
        ProxyType.PREMIUM_DC_SOCKS4.value,
        ProxyType.PRIVATE_DC_SOCKS4.value,
        ProxyType.ROTATING_DC_SOCKS4.value,
        ProxyType.DEDICATED_DC_SOCKS4.value,
        ProxyType.SCRAPED_UNTRUSTED_SOCKS4.value,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_1_SOCKS4.value,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_2_SOCKS4.value,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_3_SOCKS4.value,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_4_SOCKS4.value,
    ],
    "socks5://": [
        ProxyType.PREMIUM_STATIC_RES_SOCKS5.value,
        ProxyType.DEDICATED_RES_SOCKS5.value,
        ProxyType.ROTATING_RES_SOCKS5.value,
        ProxyType.PRIVATE_RES_SOCKS5.value,
        ProxyType.FREE_RES_SOCKS5.value,
        ProxyType.OWN_RES_SOCKS5.value,
        ProxyType.RES_SOCKS5.value,
        ProxyType.DC_SOCKS5.value,
        ProxyType.FREE_DC_SOCKS5.value,
        ProxyType.OWN_DC_SOCKS5.value,
        ProxyType.PREMIUM_DC_SOCKS5.value,
        ProxyType.PRIVATE_DC_SOCKS5.value,
        ProxyType.ROTATING_DC_SOCKS5.value,
        ProxyType.DEDICATED_DC_SOCKS5.value,
        ProxyType.SCRAPED_UNTRUSTED_SOCKS5.value,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_1_SOCKS5.value,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_2_SOCKS5.value,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_3_SOCKS5.value,
        ProxyType.SCRAPED_UNTRUSTED_TYPE_4_SOCKS5.value,
    ]
}

http_pass_codes = [
    db.cast(ResponseCodesGeneric.OK.value, SMALLINT()),
    db.cast(ResponseCodesGeneric.CREATED.value, SMALLINT()),
]


def proxy_get_proxies():
    """
    Query database and get a dictionary of proxies.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return {}

    # Database methods are enclosed in a try-except block.
    try:
        # Retrieve the proxies
        proxies = (
            db.session.query(Proxy)
            .order_by(asc(Proxy.id))
            .all()
        )

        # Convert to dictionary
        # Return successful upon creation
        return [i.to_dict_jinja() for i in proxies]

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
        print(f"Error: {e}")
        return {}


def proxy_get_proxies_base():
    """
    Query database and get proxy list.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return {}

    # Database methods are enclosed in a try-except block.
    try:
        # Retrieve the proxies
        return (
            db.session.query(Proxy)
            .order_by(asc(Proxy.id))
            .all()
        )

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


def proxy_get_proxies_base_last_used():
    """
    Query database and get proxy list. Orders by last access.
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return {}

    # Database methods are enclosed in a try-except block.
    try:
        # Retrieve the proxies
        return (
            db.session.query(Proxy)
            .order_by(asc(Proxy.last_access))
            .all()
        )

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


def proxy_get_proxy_name(proxy_id: int):
    """
    Query database and get proxy name associated with the proxy_id
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return {}

    # Database methods are enclosed in a try-except block.
    try:
        # Retrieve the proxies
        return (
            db.session.scalars(
                select(Proxy)
                .filter(Proxy.id == proxy_id)
                .options(load_only(Proxy.proxy_address))
            ).first()
        )

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


def toggle_proxy(
        proxy_id: int,
        enable: bool = True):
    """
    Update Proxy to disable or enable based on user action
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return False

    if (enable is None or
            not isinstance(enable, bool) or
            proxy_id is None or
            not isinstance(proxy_id, int) or
            proxy_id < 0):
        return False

    # Database methods are enclosed in a try-except block.
    try:
        # Access Proxy Table
        (db.session.query(Proxy)
         .filter(Proxy.id == proxy_id)
         .update({Proxy.disabled: b'\x00' if enable else b'\x01'},
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


def test_proxy(proxy_id: int):
    """
    Test a proxy and return the response
    """

    # Check if User is logged in.
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return False

    if (proxy_id is None or
            not isinstance(proxy_id, int) or
            proxy_id < 0):
        return False

    # Database methods are enclosed in a try-except block.
    try:
        # Access Proxy Table
        proxy = (
            db.session.query(Proxy)
            .filter(Proxy.id == proxy_id)
            .first()
        )

        if proxy is None:
            db.session.close()
            return False

        selected_proxy_prefix = ''
        for i in proxy_type_prefix_dict.keys():
            for j in proxy_type_prefix_dict[i]:
                if j == proxy.proxy_type:
                    selected_proxy_prefix = i

        if selected_proxy_prefix == '':
            db.session.close()
            return False

        proxy_proxy = {
            'http': selected_proxy_prefix + proxy.proxy_address,
            'https': selected_proxy_prefix + proxy.proxy_address
        }

        response = requests.get(
            url=proxy_public_website_check,
            proxies=proxy_proxy,
            auth=(
                HTTPBasicAuth(
                    proxy.proxy_username,
                    proxy.proxy_password)
                if proxy.auth_required != 0
                else None)
        )

        # Update proxy counters
        if proxy.requests is None:
            proxy.requests = 0

        proxy.requests += 1

        if response.status_code != 200:
            if proxy.failed_requests is None:
                proxy.failed_requests = 0
            proxy.failed_requests += 1

        proxy.verified = True

        db.session.commit()
        db.session.close()

        return (
            response.text
            if response.status_code == 200
            else False
        )

    # SQLAlchemy-specific errors
    # except SQLAlchemyError as e:
    #     db.session.rollback()
    #     print(f"SQLAlchemyError: {e}", flush=True)
    #     return False

    # Other Errors
    except Exception as e:
        db.session.rollback()

        proxy = (
            db.session.query(Proxy)
            .filter(Proxy.id == proxy_id)
            .first()
        )

        if proxy is None:
            db.session.close()
            return False

        if proxy.requests is None:
            proxy.requests = 0

        proxy.requests = proxy.requests + 1

        if proxy.failed_requests is None:
            proxy.failed_requests = 0

        proxy.failed_requests = proxy.failed_requests + 1

        proxy.verified = True
        db.session.commit()
        db.session.close()

        print(f"Soft Fail: {e}", flush=True)
        return False

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
