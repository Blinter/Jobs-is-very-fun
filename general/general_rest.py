import urllib.parse

import pytz
from flask import (
    Blueprint,
    jsonify,
    make_response
)
from psycopg2 import (
    IntegrityError,
    OperationalError
)
from sqlalchemy.exc import SQLAlchemyError

from enums.response_codes import ResponseCodesGeneric
from extensions_companies import (
    get_companies_paginate,
    get_companies_searched_only_paginate
)
from extensions_jobs import (
    get_listed_jobs_paginate,
    get_company_jobs_paginate,
    get_company_jobs_searched_only_paginate,
    get_listed_jobs_search_keyword_only_paginate,
    get_listed_jobs_search_location_default_paginate,
    get_company_jobs_location_only_paginate,
    get_company_jobs_keyword_location_paginate
)
from extensions_locations import (
    string_to_location,
    look_for_location
)
from extensions_sql import db
from extensions_string import clean_location_string
from extensions_timegraph import get_current_timegraph_data
from models.postgres.locations.location import Location

general_rest_bp = Blueprint(
    'general_rest',
    __name__
)


@general_rest_bp.route(
    "/get_active_jobs_home/",
    methods=["GET"]
)
def get_timegraph():
    """
    REST endpoint that returns a list of dictionaries containing values
    relating to the statistics of the Job Database.
    """
    upload_today = True
    import datetime
    return (
        make_response(
            jsonify([
                i.to_dict_rest()
                for i in reversed(result)
                if (
                        i.time.replace(tzinfo=pytz.UTC).date() <
                        datetime.datetime.today()
                        .replace(tzinfo=pytz.UTC).date()
                        if not upload_today else
                        i.time.replace(tzinfo=pytz.UTC).date()
                        <= datetime.datetime.today()
                        .replace(tzinfo=pytz.UTC).date()
                )
            ]),
            int(ResponseCodesGeneric.OK))
        if ((result := get_current_timegraph_data()) is not None and
            len(result) != 0)
        else make_response('', int(ResponseCodesGeneric.NO_CONTENT))
    )


@general_rest_bp.route(
    "/parse_location/"
    "<location_string>/",
    methods=["GET"]
)
def parse_location_str(
        location_string: str):
    """
    Attempts to parse a single location string encoded by the user by matching
    a string to a Location Table.
    This REST endpoint is a test endpoint and used primarily for debugging.
    """
    if (location_string is None or
            len(location_string) < 2):
        return make_response('', int(
            ResponseCodesGeneric.NO_CONTENT))

    try:
        location_string = urllib.parse.unquote(location_string)

        found_location: Location = string_to_location(
            string_to_parse=clean_location_string(location_string)
        )

        if (found_location is None or
                not isinstance(found_location, Location)):
            return make_response('', int(
                ResponseCodesGeneric.NO_CONTENT))

        found_location = look_for_location(found_location)

        if (found_location is None or
                not isinstance(found_location, Location)):
            return make_response('', int(
                ResponseCodesGeneric.NO_CONTENT))

        # print(found_location)

        # Return new ID and successful response upon creation
        return make_response(
            jsonify(found_location.id),
            int(ResponseCodesGeneric.OK)
        )

    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except OperationalError as e:
        db.session.rollback()
        print(f"OperationalError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"SQLAlchemyError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@general_rest_bp.route(
    "/parse_locations/"
    "<location_string>/",
    methods=["GET"]
)
def parse_locations_str(location_string: str = None):
    """
    Attempts to parse a location string and return specific jobs matching that
    string.
    This REST endpoint is a test endpoint and used primarily for debugging.
    """
    if (location_string is None or
            len(location_string) < 2):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        location_string = urllib.parse.unquote(location_string)
        location_string = clean_location_string(location_string)
        found_jobs: list = get_listed_jobs_search_location_default_paginate(
            location_keyword=location_string)

        if (found_jobs is None or
                not isinstance(found_jobs, list) or
                len(found_jobs) == 0):
            print("Could not find jobs based on search: " + location_string)
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Return new ID and successful response upon creation
        return make_response(
            jsonify([i.to_dict_rest() for i in found_jobs]),
            int(ResponseCodesGeneric.OK)
        )

    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except OperationalError as e:
        db.session.rollback()
        print(f"OperationalError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"SQLAlchemyError: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))
