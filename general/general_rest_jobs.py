import urllib.parse

from flask import (
    Blueprint,
    jsonify,
    make_response,
    session
)
from psycopg2 import (
    IntegrityError,
    OperationalError
)
from sqlalchemy.exc import SQLAlchemyError

from enums.response_codes import ResponseCodesGeneric

from extensions_jobs import (
    get_listed_jobs_paginate,
    get_listed_jobs_search_keyword_only_paginate,
    get_listed_jobs_search_location_default_paginate,
    save_new_search_job,
    get_listed_jobs_keyword_location_paginate_fast,
)

from extensions_sql import db

general_rest_jobs_bp = Blueprint(
    'general_rest_jobs',
    __name__
)


@general_rest_jobs_bp.route("/get_jobs/<int:page_number>", methods=["GET"])
def get_jobs(page_number: int = 1):
    """
    REST Endpoint
    Used to get a list of all jobs and paginates results based on the respective
    limits set by authenticated or unauthenticated users.
    """
    if (page_number is None or
            page_number <= 0 or
            not isinstance(page_number, int)):
        page_number = 1

    try:
        found_jobs: list = get_listed_jobs_paginate(page_number=page_number)

        save_new_search_job(page_number=page_number)

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


@general_rest_jobs_bp.route(
    "/search_jobs_k/<search_query>/<int:page_number>", methods=["GET"])
def search_jobs_keyword(
        search_query: str,
        page_number: int = 1):
    """
    REST Endpoint
    Used to search a keyword from of all jobs and paginates results based on
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
        # return get_jobs(page_number)
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        search_query = urllib.parse.unquote(search_query)

        save_new_search_job(
            search_keyword=search_query,
            page_number=page_number,
            distance=30,
        )

        found_jobs: list = get_listed_jobs_search_keyword_only_paginate(
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


@general_rest_jobs_bp.route(
    "/search_jobs_l/<location_query>/<int:page_number>", methods=["GET"])
def search_jobs_location(
        location_query: str,
        page_number: int = 1):
    """
    REST Endpoint
    Used to search a keyword and location from of all jobs and paginates
    results based on the respective limits set by authenticated or
    unauthenticated users.
    """
    if (page_number is None or
            page_number <= 0 or
            not isinstance(page_number, int)):
        page_number = 1

    if (location_query is None or
            not isinstance(location_query, str) or
            len(location_query) == 0 or
            location_query == ''):
        # return get_jobs(page_number=page_number)
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        location_query = urllib.parse.unquote(location_query)

        save_new_search_job(
            location_keyword=location_query,
            page_number=page_number,
            distance=30,
        )

        found_jobs: list = get_listed_jobs_search_location_default_paginate(
            location_keyword=location_query,
            page_number=page_number
        )

        if (found_jobs is None or
                len(found_jobs) == 0 or
                not isinstance(found_jobs, list)):
            # print("No Found Jobs")
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


@general_rest_jobs_bp.route(
    "/search_jobs_ld/<location_query>/<int:distance>/<int:page_number>",
    methods=["GET"])
def search_jobs_location_distance(
        location_query: str,
        distance: int,
        page_number: int = 1):
    """
    REST Endpoint
    Used to search a location and a specific distance of all jobs and paginates
    results based on the respective limits set by authenticated or
    unauthenticated users.
    """
    if (page_number is None or
            page_number <= 0 or
            not isinstance(page_number, int)):
        page_number = 1

    if (location_query is None or
            not isinstance(location_query, str) or
            len(location_query) == 0 or
            location_query == ''):
        # return get_jobs(page_number=page_number)
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    if (distance is None or
            not isinstance(distance, int) or
            distance < 0):
        # return search_jobs_location(
        #     location_query=location_query,
        #     page_number=page_number
        # )
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        location_query = urllib.parse.unquote(location_query)

        save_new_search_job(
            location_keyword=location_query,
            page_number=page_number,
            distance=distance,
        )

        found_jobs: list = get_listed_jobs_search_location_default_paginate(
            location_keyword=location_query,
            page_number=page_number,
            distance=distance
        )

        if (found_jobs is None or
                len(found_jobs) == 0 or
                not isinstance(found_jobs, list)):
            # print("No Found Jobs")
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


@general_rest_jobs_bp.route(
    "/search_jobs_kl/<search_query>/<location_query>/<int:page_number>",
    methods=["GET"])
def search_jobs_keyword_and_location(
        search_query: str,
        location_query: str,
        page_number: int = 1):
    """
    REST Endpoint
    Used to search a keyword, location of all jobs and paginates results based
    on the respective limits set by authenticated or unauthenticated users.
    """
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
        # return get_jobs(page_number=page_number)
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    elif (search_query is None or
          not isinstance(search_query, str) or
          len(search_query) == 0 or
          search_query == ''):
        # return search_jobs_location(
        #     location_query=location_query,
        #     page_number=page_number
        # )
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    elif (location_query is None or
          not isinstance(location_query, str) or
          len(location_query) == 0 or
          location_query == ''):
        # return search_jobs_keyword(
        #     search_query=search_query,
        #     page_number=page_number
        # )
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        location_query = urllib.parse.unquote(location_query)
        search_query = urllib.parse.unquote(search_query)

        save_new_search_job(
            search_keyword=search_query,
            location_keyword=location_query,
            page_number=page_number,
            distance=30,
        )

        found_jobs: list = get_listed_jobs_keyword_location_paginate_fast(
            search_keyword=search_query,
            location_keyword=location_query,
            page_number=page_number
        )

        if (found_jobs is None or
                len(found_jobs) == 0 or
                not isinstance(found_jobs, list)):
            # print("No Found Jobs")
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


@general_rest_jobs_bp.route(
    "/search_jobs_kld/<search_query>/<location_query>/<int:distance>/"
    "<int:page_number>",
    methods=["GET"])
def search_jobs_keyword_and_location_distance(
        search_query: str,
        location_query: str,
        distance: int = 30,
        page_number: int = 1):
    """
    REST Endpoint
    Used to search a keyword, location, and distance of all jobs
    and paginates results based on the respective limits
    set by authenticated or unauthenticated users.
    """
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
        # return get_jobs(page_number=page_number)
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    elif (search_query is None or
          not isinstance(search_query, str) or
          len(search_query) == 0 or
          search_query == ''):
        # return search_jobs_location(
        #     location_query=location_query,
        #     page_number=page_number
        # )
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    elif (location_query is None or
          not isinstance(location_query, str) or
          len(location_query) == 0 or
          location_query == ''):
        # return search_jobs_keyword(
        #     search_query=search_query,
        #     page_number=page_number
        # )
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    elif (distance is None or
          not isinstance(distance, int) or
          distance < 0):
        # return search_jobs_keyword_and_location(
        #     location_query=location_query,
        #     search_query=search_query,
        #     page_number=page_number,
        # )
        return make_response('', int(ResponseCodesGeneric.NO_CONTENT))

    try:
        location_query = urllib.parse.unquote(location_query)
        search_query = urllib.parse.unquote(search_query)

        save_new_search_job(
            search_keyword=search_query,
            location_keyword=location_query,
            page_number=page_number,
            distance=distance,
        )

        found_jobs: list = get_listed_jobs_keyword_location_paginate_fast(
            search_keyword=search_query,
            location_keyword=location_query,
            distance=distance,
            page_number=page_number
        )

        if (found_jobs is None or
                len(found_jobs) == 0 or
                not isinstance(found_jobs, list)):
            # print("No Found Jobs")
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


@general_rest_jobs_bp.route("/retrieve_last_search_job", methods=["GET"])
def retrieve_last_search_job():
    """
    REST Endpoint
    Used to retrieve the previous search parameters in order to maintain
    the correct state by the client.
    """
    return make_response(
        {
            # 'job_view': session.get('job_view_id'),
            # 'company_id': session.get('job_company_id'),
            'page_number': session.get('job_page_number', None),
            'search': session.get('job_search_query', None),
            'location': session.get('job_location_query', None),
            'distance': session.get('job_location_distance', None),
        }, int(ResponseCodesGeneric.OK)
    )
