import urllib.parse

from flask import (
    Blueprint,
    jsonify,
    make_response, session
)
from psycopg2 import (
    IntegrityError,
    OperationalError
)
from sqlalchemy.exc import SQLAlchemyError

from enums.response_codes import ResponseCodesGeneric
from extensions_companies import (
    get_companies_paginate,
    get_companies_searched_only_paginate,
    save_new_search_company
)
from extensions_jobs import (
    get_company_jobs_paginate,
    get_company_jobs_searched_only_paginate,
    get_company_jobs_location_only_paginate,
    get_company_jobs_keyword_location_paginate,
)

from extensions_sql import db

general_rest_companies_bp = Blueprint(
    'general_rest_companies',
    __name__
)


@general_rest_companies_bp.route("/get_companies/<int:page_number>",
                                 methods=["GET"])
def get_companies(page_number: int = 1):
    """
    REST Endpoint
    Used to query all companies and paginates results based on
    the respective limits set by authenticated or unauthenticated users.
    """
    if (page_number is None or
            page_number <= 0 or
            not isinstance(page_number, int)):
        page_number = 1

    try:
        save_new_search_company(
            page_number=page_number
        )

        found_companies: list = get_companies_paginate(page_number=page_number)

        if (found_companies is None or
                len(found_companies) == 0 or
                not isinstance(found_companies, list)):
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Return new ID and successful response upon creation
        return make_response(
            jsonify([i.to_dict_rest() for i in found_companies]),
            int(ResponseCodesGeneric.OK)
        )

    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except OperationalError as e:
        db.session.rollback()
        print(f"OperationalError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"SQLAlchemyError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@general_rest_companies_bp.route(
    "/search_companies/<search_query>/<int:page_number>", methods=["GET"])
def search_companies(
        search_query: str,
        page_number: int = 1):
    """
    REST Endpoint
    Used to search a keyword from all companies and paginates results based on
    the respective limits set by authenticated or unauthenticated users.
    """
    if (page_number is None or
            page_number <= 0 or
            not isinstance(page_number, int)):
        page_number = 1

    if (search_query is None or
            not isinstance(search_query, str) or
            len(search_query) == 0 or
            search_query == ''):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        search_query = urllib.parse.unquote(search_query)

        save_new_search_company(
            page_number=page_number,
            search_keyword=search_query,
        )

        found_companies: list = get_companies_searched_only_paginate(
            search_keyword=search_query,
            page_number=page_number
        )

        if (found_companies is None or
                len(found_companies) == 0 or
                not isinstance(found_companies, list)):
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Return new ID and successful response upon creation
        return make_response(
            jsonify([i.to_dict_rest() for i in found_companies]),
            int(ResponseCodesGeneric.OK)
        )

    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except OperationalError as e:
        db.session.rollback()
        print(f"OperationalError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"SQLAlchemyError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@general_rest_companies_bp.route(
    "/get_company_jobs/<int:company_id>/<int:page_number>",
    methods=["GET"])
def get_company_jobs(
        company_id: int,
        page_number: int = 1):
    """
    REST Endpoint
    Used to get a list of all jobs from a specific company and paginates
    results based on the respective limits set by authenticated or
    unauthenticated users.
    """
    if (not isinstance(page_number, int) or
            page_number <= 0):
        page_number = 1

    if (not isinstance(company_id, int) or
            company_id < 0):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        save_new_search_company(
            company_id=company_id,
            page_number=page_number
        )

        found_jobs: list = get_company_jobs_paginate(
            company_id=company_id,
            page_number=page_number
        )

        if (not isinstance(found_jobs, list) or
                len(found_jobs) == 0):
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Return new ID and successful response upon creation
        return make_response(
            jsonify([i.to_dict_rest() for i in found_jobs]),
            int(ResponseCodesGeneric.OK)
        )

    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except OperationalError as e:
        db.session.rollback()
        print(f"OperationalError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"SQLAlchemyError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@general_rest_companies_bp.route(
    "/search_company_jobs_k/<int:company_id>/<search_query>/<int:page_number>",
    methods=["GET"])
def search_company_jobs_keyword(
        company_id: int,
        search_query: str,
        page_number: int = 1):
    """
    REST Endpoint
    Used to search a keyword from of all jobs from a specific company and
    paginates results based on the respective limits set by authenticated or
    unauthenticated users.
    """
    if (company_id is None or
            not isinstance(company_id, int) or
            company_id < 0):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    if (page_number is None or
            page_number <= 0 or
            not isinstance(page_number, int)):
        page_number = 1

    if (search_query is None or
            not isinstance(search_query, str) or
            len(search_query) == 0 or
            search_query == ''):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        search_query = urllib.parse.unquote(search_query)

        save_new_search_company(
            company_id=company_id,
            page_number=page_number,
            search_keyword=search_query,
            distance=30,
        )

        found_jobs: list = get_company_jobs_searched_only_paginate(
            company_id=company_id,
            search_keyword=search_query,
            page_number=page_number
        )

        if (found_jobs is None or
                len(found_jobs) == 0 or
                not isinstance(found_jobs, list)):
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Return new ID and successful response upon creation
        return make_response(
            jsonify([i.to_dict_rest() for i in found_jobs]),
            int(ResponseCodesGeneric.OK)
        )

    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except OperationalError as e:
        db.session.rollback()
        print(f"OperationalError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"SQLAlchemyError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@general_rest_companies_bp.route(
    "/search_company_jobs_l/<int:company_id>/<location_query>/"
    "<int:page_number>", methods=["GET"])
def search_company_jobs_location(
        company_id: int,
        location_query: str,
        page_number: int = 1):
    """
    REST Endpoint
    Used to search a keyword and location from of all jobs from a specific
    company and paginates results based on the respective limits set by
    authenticated or unauthenticated users.
    """
    if (company_id is None or
            not isinstance(company_id, int) or
            company_id < 0):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    if (page_number is None or
            page_number <= 0 or
            not isinstance(page_number, int)):
        page_number = 1

    if (location_query is None or
            not isinstance(location_query, str) or
            len(location_query) == 0 or
            location_query == ''):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        location_query = urllib.parse.unquote(location_query)

        save_new_search_company(
            company_id=company_id,
            page_number=page_number,
            location_keyword=location_query,
            distance=30,
        )

        found_jobs: list = get_company_jobs_location_only_paginate(
            company_id=company_id,
            location_keyword=location_query,
            page_number=page_number
        )

        if (found_jobs is None or
                len(found_jobs) == 0 or
                not isinstance(found_jobs, list)):
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Return new ID and successful response upon creation
        return make_response(
            jsonify([i.to_dict_rest() for i in found_jobs]),
            int(ResponseCodesGeneric.OK)
        )

    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except OperationalError as e:
        db.session.rollback()
        print(f"OperationalError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"SQLAlchemyError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@general_rest_companies_bp.route(
    "/search_company_jobs_ld/<int:company_id>/<location_query>/<int:distance>/"
    "<int:page_number>", methods=["GET"])
def search_company_jobs_location_distance(
        company_id: int,
        location_query: str,
        distance: int,
        page_number: int = 1):
    """
    REST Endpoint
    Used to search a location and a specific distance of all jobs from
    a specific company and paginates results based on the respective limits
    set by authenticated or unauthenticated users.
    """
    if (company_id is None or
            not isinstance(company_id, int) or
            company_id < 0):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    if (page_number is None or
            page_number <= 0 or
            not isinstance(page_number, int)):
        page_number = 1

    if (location_query is None or
            not isinstance(location_query, str) or
            len(location_query) == 0 or
            location_query == ''):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    if (distance is None or
            not isinstance(distance, int) or
            distance < 0):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        location_query = urllib.parse.unquote(location_query)

        save_new_search_company(
            company_id=company_id,
            page_number=page_number,
            location_keyword=location_query,
            distance=distance,
        )

        found_jobs: list = get_company_jobs_location_only_paginate(
            company_id=company_id,
            location_keyword=location_query,
            page_number=page_number
        )

        if (found_jobs is None or
                len(found_jobs) == 0 or
                not isinstance(found_jobs, list)):
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Return new ID and successful response upon creation
        return make_response(
            jsonify([i.to_dict_rest() for i in found_jobs]),
            int(ResponseCodesGeneric.OK)
        )

    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except OperationalError as e:
        db.session.rollback()
        print(f"OperationalError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"SQLAlchemyError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@general_rest_companies_bp.route(
    "/search_company_jobs_kl/<int:company_id>/<search_query>/<location_query>/"
    "<int:page_number>", methods=["GET"])
def search_company_jobs_keyword_and_location(
        company_id: int,
        search_query: str,
        location_query: str,
        page_number: int = 1):
    """
    REST Endpoint
    Used to search a keyword, location of all jobs from
    a specific company and paginates results based on the respective limits
    set by authenticated or unauthenticated users.
    """
    if (company_id is None or
            not isinstance(company_id, int) or
            company_id < 0):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    if (page_number is None or
            page_number <= 0 or
            not isinstance(page_number, int)):
        page_number = 1

    if ((search_query is None or
         not isinstance(search_query, str) or
         len(search_query) == 0 or
         search_query == '') and
            (location_query is None or
             not isinstance(location_query, str) or
             len(location_query) == 0 or
             location_query == '')):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    elif (search_query is None or
          not isinstance(search_query, str) or
          len(search_query) == 0 or
          search_query == ''):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    elif (location_query is None or
          not isinstance(location_query, str) or
          len(location_query) == 0 or
          location_query == ''):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        location_query = urllib.parse.unquote(location_query)
        search_query = urllib.parse.unquote(search_query)

        save_new_search_company(
            company_id=company_id,
            search_keyword=search_query,
            location_keyword=location_query,
            page_number=page_number,
            distance=30,
        )

        found_jobs: list = get_company_jobs_keyword_location_paginate(
            company_id=company_id,
            search_keyword=search_query,
            location_keyword=location_query,
            page_number=page_number
        )

        if (found_jobs is None or
                len(found_jobs) == 0 or
                not isinstance(found_jobs, list)):
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Return new ID and successful response upon creation
        return make_response(
            jsonify([i.to_dict_rest() for i in found_jobs]),
            int(ResponseCodesGeneric.OK)
        )

    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except OperationalError as e:
        db.session.rollback()
        print(f"OperationalError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"SQLAlchemyError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@general_rest_companies_bp.route(
    "/search_company_jobs_kld/<int:company_id>/<search_query>/<location_query>/"
    "<int:distance>/<int:page_number>", methods=["GET"])
def search_company_jobs_keyword_and_location_distance(
        company_id: int,
        search_query: str,
        location_query: str,
        distance: int = 30,
        page_number: int = 1):
    """
    REST Endpoint
    Used to search a keyword, location, and distance of all jobs from
    a specific company and paginates results based on the respective limits
    set by authenticated or unauthenticated users.
    """
    if (company_id is None or
            not isinstance(company_id, int) or
            company_id < 0):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    if (page_number is None or
            page_number <= 0 or
            not isinstance(page_number, int)):
        page_number = 1

    if ((search_query is None or
         not isinstance(search_query, str) or
         len(search_query) == 0 or
         search_query == '') and
            (location_query is None or
             not isinstance(location_query, str) or
             len(location_query) == 0 or
             location_query == '') and
            (distance is None or
             not isinstance(distance, int) or
             distance < 0)):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    elif (search_query is None or
          not isinstance(search_query, str) or
          len(search_query) == 0 or
          search_query == ''):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    elif (location_query is None or
          not isinstance(location_query, str) or
          len(location_query) == 0 or
          location_query == ''):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    elif (distance is None or
          not isinstance(distance, int) or
          distance < 0):
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        location_query = urllib.parse.unquote(location_query)
        search_query = urllib.parse.unquote(search_query)

        save_new_search_company(
            company_id=company_id,
            page_number=page_number,
            search_keyword=search_query,
            location_keyword=location_query,
            distance=distance,
        )

        found_jobs: list = get_company_jobs_keyword_location_paginate(
            company_id=company_id,
            search_keyword=search_query,
            location_keyword=location_query,
            page_number=page_number
        )

        if (found_jobs is None or
                len(found_jobs) == 0 or
                not isinstance(found_jobs, list)):
            return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

        # Return new ID and successful response upon creation
        return make_response(
            jsonify([i.to_dict_rest() for i in found_jobs]),
            int(ResponseCodesGeneric.OK)
        )

    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except OperationalError as e:
        db.session.rollback()
        print(f"OperationalError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"SQLAlchemyError: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))

    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")
        # raise e
        return make_response('', int(
            ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@general_rest_companies_bp.route(
    "/retrieve_last_search_company", methods=["GET"])
def retrieve_last_search_company():
    """
    REST Endpoint
    Used to retrieve the previous search parameters in order to maintain
    the correct state by the client.
    """
    return make_response(
        {
            # 'company_id': session.get('company_view_id'),
            'page_number': session.get('company_page_number'),
            'search': session.get('company_search_query'),
            'location': session.get('company_location_query'),
            'distance': session.get('company_location_distance'),
        }, int(ResponseCodesGeneric.OK)
    )
