from flask import Blueprint

from general.general_rest_companies import (
    get_companies,
    get_company_jobs,
    search_company_jobs_keyword,
    search_company_jobs_location,
    search_company_jobs_keyword_and_location_distance,
    search_companies,
    search_company_jobs_keyword_and_location
)
from general.general_rest_jobs import (
    get_jobs,
    search_jobs_keyword,
    search_jobs_location,
    search_jobs_keyword_and_location,
    search_jobs_keyword_and_location_distance,
    search_jobs_location_distance
)

general_rest_stub_bp = Blueprint(
    'general_rest_stub',
    __name__
)
"""
Provides routes and proper behavior for developers or users attempting to query 
data using the API.
"""


@general_rest_stub_bp.route("/get_jobs", methods=["GET"])
def get_jobs_no_page():
    return get_jobs()


@general_rest_stub_bp.route("/get_jobs/", methods=["GET"])
def get_jobs_slash_no_page():
    return get_jobs()


@general_rest_stub_bp.route("/get_jobs/<int:page_number>/", methods=["GET"])
def get_jobs_page_number_slash_default(page_number: int = 1):
    return get_jobs(page_number=page_number)


@general_rest_stub_bp.route("/get_companies", methods=["GET"])
def get_companies_no_page():
    return get_companies()


@general_rest_stub_bp.route("/get_companies/", methods=["GET"])
def get_companies_slash_no_page():
    return get_companies()


@general_rest_stub_bp.route(
    "/get_companies/<int:page_number>/", methods=["GET"])
def get_companies_page_number_slash_default(page_number: int = 1):
    return get_companies(page_number=page_number)


@general_rest_stub_bp.route("/search_companies", methods=["GET"])
def search_companies_no_keyword_no_page():
    return get_companies()


@general_rest_stub_bp.route("/search_companies/", methods=["GET"])
def search_companies_no_keyword_slash_no_page():
    return get_companies()


@general_rest_stub_bp.route(
    "/search_companies/<search_query>", methods=["GET"])
def search_companies_keyword_no_page(search_query: str):
    return search_companies(search_query=search_query)


@general_rest_stub_bp.route(
    "/search_companies/<search_query>/", methods=["GET"])
def search_companies_keyword_slash_no_page(search_query: str):
    return search_companies(search_query=search_query)


@general_rest_stub_bp.route(
    "/search_companies/<search_query>/<int:page_number>/", methods=["GET"])
def search_companies_keyword_page_slash(
        search_query: str,
        page_number: int = 1):
    return search_companies(
        search_query=search_query,
        page_number=page_number
    )


@general_rest_stub_bp.route("/search_jobs_k", methods=["GET"])
def search_jobs_keyword_no_options():
    return get_jobs()


@general_rest_stub_bp.route("/search_jobs_k/", methods=["GET"])
def search_jobs_keyword_slash_no_options():
    return get_jobs()


@general_rest_stub_bp.route("/search_jobs_k/<search_query>", methods=["GET"])
def search_jobs_keyword_no_page(search_query: str):
    return search_jobs_keyword(search_query=search_query)


@general_rest_stub_bp.route("/search_jobs_k/<search_query>/", methods=["GET"])
def search_jobs_keyword_no_page_slash(search_query: str):
    return search_jobs_keyword(search_query=search_query)


@general_rest_stub_bp.route(
    "/search_jobs_k/<search_query>/<int:page_number>/", methods=["GET"])
def search_jobs_keyword_page_slash(
        search_query: str,
        page_number: int = 1):
    return search_jobs_keyword(
        search_query=search_query,
        page_number=page_number
    )


@general_rest_stub_bp.route("/search_jobs_l", methods=["GET"])
def search_jobs_no_location():
    return get_jobs()


@general_rest_stub_bp.route("/search_jobs_l/", methods=["GET"])
def search_jobs_no_location_slash():
    return get_jobs()


@general_rest_stub_bp.route("/search_jobs_l/<location_query>", methods=["GET"])
def search_jobs_location_no_page(location_query: str):
    return search_jobs_location(location_query=location_query)


@general_rest_stub_bp.route("/search_jobs_l/<location_query>/", methods=["GET"])
def search_jobs_location_no_page_slash(location_query: str):
    return search_jobs_location(location_query=location_query)


@general_rest_stub_bp.route(
    "/search_jobs_l/<location_query>/<int:page_number>/", methods=["GET"])
def search_jobs_location_slash(
        location_query: str,
        page_number: int = 1):
    return search_jobs_location(
        location_query=location_query,
        page_number=page_number
    )


@general_rest_stub_bp.route("/search_jobs_ld", methods=["GET"])
def search_jobs_no_location_distance():
    return get_jobs()


@general_rest_stub_bp.route("/search_jobs_ld/", methods=["GET"])
def search_jobs_no_location_distance_slash():
    return get_jobs()


@general_rest_stub_bp.route("/search_jobs_ld/<location_query>", methods=["GET"])
def search_jobs_location_distance_no_distance_no_page(location_query: str):
    return search_jobs_location(location_query=location_query)


@general_rest_stub_bp.route(
    "/search_jobs_ld/<location_query>/", methods=["GET"])
def search_jobs_location_distance_no_distance_no_page_slash(
        location_query: str):
    return search_jobs_location(location_query=location_query)


@general_rest_stub_bp.route(
    "/search_jobs_ld/<location_query>/<int:distance>", methods=["GET"])
def search_jobs_location_distance_no_page(
        location_query: str,
        distance: int = 30):
    return search_jobs_location_distance(
        location_query=location_query,
        distance=distance)


@general_rest_stub_bp.route(
    "/search_jobs_ld/<location_query>/<int:distance>/", methods=["GET"])
def search_jobs_location_distance_no_page_slash(
        location_query: str,
        distance: int = 30):
    return search_jobs_location_distance(
        location_query=location_query,
        distance=distance)


@general_rest_stub_bp.route(
    "/search_jobs_ld/<location_query>/<int:distance>/<int:page_number>/",
    methods=["GET"])
def search_jobs_location_distance_slash(
        location_query: str,
        distance: int = 30,
        page_number: int = 1):
    return search_jobs_location_distance(
        location_query=location_query,
        distance=distance,
        page_number=page_number)


@general_rest_stub_bp.route("/search_jobs_kl", methods=["GET"])
def search_jobs_keyword_and_location_no_extra():
    return get_jobs()


@general_rest_stub_bp.route("/search_jobs_kl/", methods=["GET"])
def search_jobs_keyword_and_location_no_extra_slash():
    return get_jobs()


@general_rest_stub_bp.route("/search_jobs_kl/<search_query>", methods=["GET"])
def search_jobs_keyword_and_location_no_location_no_page(search_query: str):
    return search_jobs_keyword(search_query=search_query)


@general_rest_stub_bp.route("/search_jobs_kl/<search_query>/", methods=["GET"])
def search_jobs_keyword_and_location_keyword_only_slash(search_query: str):
    return search_jobs_keyword(search_query=search_query)


@general_rest_stub_bp.route(
    "/search_jobs_kl/<search_query>/<location_query>", methods=["GET"])
def search_jobs_keyword_and_location_no_page(search_query: str):
    return search_jobs_keyword(search_query=search_query)


@general_rest_stub_bp.route(
    "/search_jobs_kl/<search_query>/<location_query>/", methods=["GET"])
def search_jobs_keyword_and_location_no_page_slash(
        search_query: str,
        location_query: str):
    return search_jobs_keyword_and_location(
        search_query=search_query,
        location_query=location_query
    )


@general_rest_stub_bp.route(
    "/search_jobs_kl/<search_query>/<location_query>/<int:page_number>/",
    methods=["GET"])
def search_jobs_keyword_and_location_slash(
        search_query: str,
        location_query: str,
        page_number: int = 1):
    return search_jobs_keyword_and_location(
        search_query=search_query,
        location_query=location_query,
        page_number=page_number,
    )


@general_rest_stub_bp.route("/search_jobs_kld", methods=["GET"])
def search_jobs_keyword_and_loc_dist_no_extra():
    return get_jobs()


@general_rest_stub_bp.route("/search_jobs_kld/", methods=["GET"])
def search_jobs_keyword_and_loc_dist_slash_no_extra():
    return get_jobs()


@general_rest_stub_bp.route("/search_jobs_kld/<search_query>", methods=["GET"])
def search_jobs_keyword_and_loc_dist_no_location(search_query: str):
    return search_jobs_keyword(search_query=search_query)


@general_rest_stub_bp.route("/search_jobs_kld/<search_query>/", methods=["GET"])
def search_jobs_keyword_and_loc_dist_no_location_slash(search_query: str):
    return search_jobs_keyword(search_query=search_query)


@general_rest_stub_bp.route(
    "/search_jobs_kld/<search_query>/<location_query>", methods=["GET"])
def search_jobs_keyword_and_loc_dist_no_dist_no_page(
        search_query: str,
        location_query: str):
    return search_jobs_keyword_and_location_distance(
        search_query=search_query,
        location_query=location_query)


@general_rest_stub_bp.route(
    "/search_jobs_kld/<search_query>/<location_query>/", methods=["GET"])
def search_jobs_keyword_and_loc_dist_no_dist_no_page_slash(
        search_query: str,
        location_query: str):
    return search_jobs_keyword_and_location_distance(
        search_query=search_query,
        location_query=location_query)


@general_rest_stub_bp.route(
    "/search_jobs_kld/<search_query>/<location_query>/<int:distance>",
    methods=["GET"])
def search_jobs_keyword_and_loc_dist_no_page(
        search_query: str,
        location_query: str,
        distance: int = 30):
    return search_jobs_keyword_and_location_distance(
        search_query=search_query,
        location_query=location_query,
        distance=distance)


@general_rest_stub_bp.route(
    "/search_jobs_kld/<search_query>/<location_query>/<int:distance>/",
    methods=["GET"])
def search_jobs_keyword_and_loc_dist_no_page_slash(
        search_query: str,
        location_query: str,
        distance: int = 30):
    return search_jobs_keyword_and_location_distance(
        search_query=search_query,
        location_query=location_query,
        distance=distance)


@general_rest_stub_bp.route(
    "/search_jobs_kld/<search_query>/<location_query>/<int:distance>/"
    "<int:page_number>/",
    methods=["GET"])
def search_jobs_keyword_and_loc_dist_slash(
        search_query: str,
        location_query: str,
        distance: int = 30,
        page_number: int = 1):
    return search_jobs_keyword_and_location_distance(
        search_query=search_query,
        location_query=location_query,
        distance=distance,
        page_number=page_number)


@general_rest_stub_bp.route("/get_company_jobs", methods=["GET"])
def get_company_jobs_default_no_company_no_page():
    return None


@general_rest_stub_bp.route("/get_company_jobs/", methods=["GET"])
def get_company_jobs_slash_default_no_company_no_page():
    return None


@general_rest_stub_bp.route("/get_company_jobs/<int:company_id>",
                            methods=["GET"])
def get_company_jobs_no_page(company_id: int):
    return get_company_jobs(company_id=company_id)


@general_rest_stub_bp.route("/get_company_jobs/<int:company_id>/",
                            methods=["GET"])
def get_company_jobs_slash_no_page(company_id: int):
    return get_company_jobs(company_id=company_id)


@general_rest_stub_bp.route(
    "/get_company_jobs/<int:company_id>/<int:page_number>/",
    methods=["GET"])
def get_company_jobs_slash(
        company_id: int,
        page_number: int = 1):
    return get_company_jobs(
        company_id=company_id,
        page_number=page_number)


@general_rest_stub_bp.route("/search_company_jobs_k", methods=["GET"])
def search_company_jobs_keyword_default_no_company():
    return None


@general_rest_stub_bp.route("/search_company_jobs_k/", methods=["GET"])
def search_company_jobs_keyword_slash_default_no_company():
    return None


@general_rest_stub_bp.route("/search_company_jobs_k/<int:company_id>",
                            methods=["GET"])
def search_company_jobs_keyword_default_no_search(company_id: int):
    return get_company_jobs(company_id=int(company_id))


@general_rest_stub_bp.route("/search_company_jobs_k/<int:company_id>/",
                            methods=["GET"])
def search_company_jobs_keyword_slash_default_no_search(company_id: int):
    return get_company_jobs(company_id=int(company_id))


@general_rest_stub_bp.route(
    "/search_company_jobs_k/<int:company_id>/<search_query>",
    methods=["GET"])
def search_company_jobs_keyword_default_no_page(
        company_id: int,
        search_query: str):
    return search_company_jobs_keyword(
        company_id=company_id,
        search_query=search_query,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_k/<int:company_id>/<search_query>/",
    methods=["GET"])
def search_company_jobs_keyword_slash_default_no_page(
        company_id: int,
        search_query: str):
    return search_company_jobs_keyword(
        company_id=company_id,
        search_query=search_query,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_k/<int:company_id>/<search_query>/<int:page_number>/",
    methods=["GET"])
def search_company_jobs_keyword_slash(
        company_id: int,
        search_query: str,
        page_number: int = 1):
    return search_company_jobs_keyword(
        company_id=company_id,
        search_query=search_query,
        page_number=page_number,
    )


@general_rest_stub_bp.route("/search_company_jobs_l", methods=["GET"])
def search_company_jobs_location_default_no_company():
    return None


@general_rest_stub_bp.route("/search_company_jobs_l/", methods=["GET"])
def search_company_jobs_location_slash_default_no_company():
    return None


@general_rest_stub_bp.route("/search_company_jobs_l/<int:company_id>",
                            methods=["GET"])
def search_company_jobs_location_default_no_location(company_id: int):
    return get_company_jobs(company_id=int(company_id))


@general_rest_stub_bp.route("/search_company_jobs_l/<int:company_id>/",
                            methods=["GET"])
def search_company_jobs_location_slash_default_no_location(company_id: int):
    return get_company_jobs(company_id=int(company_id))


@general_rest_stub_bp.route(
    "/search_company_jobs_l/<int:company_id>/<location_query>",
    methods=["GET"])
def search_company_jobs_location_default_no_page(
        company_id: int,
        location_query: str):
    return search_company_jobs_location(
        company_id=company_id,
        location_query=location_query,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_l/<int:company_id>/<location_query>/",
    methods=["GET"])
def search_company_jobs_location_slash_default_no_page(
        company_id: int,
        location_query: str):
    return search_company_jobs_location(
        company_id=company_id,
        location_query=location_query,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_l/<int:company_id>/<location_query>/"
    "<int:page_number>/",
    methods=["GET"])
def search_company_jobs_location_slash(
        company_id: int,
        location_query: str,
        page_number: int = 1):
    return search_company_jobs_location(
        company_id=company_id,
        location_query=location_query,
        page_number=page_number,
    )


@general_rest_stub_bp.route("/search_company_jobs_ld", methods=["GET"])
def search_company_jobs_location_distance_default_no_company():
    return None


@general_rest_stub_bp.route("/search_company_jobs_ld/", methods=["GET"])
def search_company_jobs_location_distance_slash_default_no_company():
    return None


@general_rest_stub_bp.route("/search_company_jobs_ld/<int:company_id>",
                            methods=["GET"])
def search_company_jobs_location_distance_default_no_location(company_id: int):
    return get_company_jobs(company_id=company_id)


@general_rest_stub_bp.route("/search_company_jobs_ld/<int:company_id>/",
                            methods=["GET"])
def search_company_jobs_location_distance_slash_default_no_location(
        company_id: int):
    return get_company_jobs(company_id=company_id)


@general_rest_stub_bp.route(
    "/search_company_jobs_ld/<int:company_id>/<location_query>",
    methods=["GET"])
def search_company_jobs_location_distance_default_no_distance(
        company_id: int,
        location_query: str):
    return search_company_jobs_location(
        company_id=company_id,
        location_query=location_query,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_ld/<int:company_id>/<location_query>/",
    methods=["GET"])
def search_company_jobs_location_distance_slash_default_no_distance(
        company_id: int,
        location_query: str):
    return search_company_jobs_location(
        company_id=company_id,
        location_query=location_query,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_ld/<int:company_id>/<location_query>/<int:distance>/",
    methods=["GET"])
def search_company_jobs_location_distance_slash_no_page(
        company_id: int,
        location_query: str,
        distance: int = 30):
    return search_company_jobs_location(
        company_id=company_id,
        location_query=location_query,
        distance=distance,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_ld/<int:company_id>/<location_query>/<int:distance>/"
    "<int:page_number>/",
    methods=["GET"])
def search_company_jobs_location_distance_slash(
        company_id: int,
        location_query: str,
        distance: int = 30,
        page_number: int = 1):
    return search_company_jobs_location(
        company_id=company_id,
        location_query=location_query,
        distance=distance,
        page_number=page_number
    )


@general_rest_stub_bp.route("/search_company_jobs_kl", methods=["GET"])
def search_company_jobs_keyword_location_default_no_company():
    return None


@general_rest_stub_bp.route("/search_company_jobs_kl/", methods=["GET"])
def search_company_jobs_keyword_location_slash_default_no_company():
    return None


@general_rest_stub_bp.route("/search_company_jobs_kl/<int:company_id>",
                            methods=["GET"])
def search_company_jobs_keyboard_location_default_no_search(company_id: int):
    return get_company_jobs(company_id=int(company_id))


@general_rest_stub_bp.route("/search_company_jobs_kl/<int:company_id>/",
                            methods=["GET"])
def search_company_jobs_keyboard_location_slash_default_no_search(
        company_id: int):
    return get_company_jobs(company_id=int(company_id))


@general_rest_stub_bp.route(
    "/search_company_jobs_kl/<int:company_id>/<search_query>",
    methods=["GET"])
def search_company_jobs_keyword_location_default_no_location(
        company_id: int,
        search_query: str):
    return search_company_jobs_keyword(
        company_id=company_id,
        search_query=search_query,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_kl/<int:company_id>/<search_query>/",
    methods=["GET"])
def search_company_jobs_keyword_location_default_no_location_slash(
        company_id: int,
        search_query: str):
    return search_company_jobs_keyword(
        company_id=company_id,
        search_query=search_query,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_kl/<int:company_id>/<search_query>/<location_query>",
    methods=["GET"])
def search_company_jobs_keyword_location_no_page(
        company_id: int,
        search_query: str,
        location_query: str):
    return search_company_jobs_keyword_and_location(
        company_id=company_id,
        search_query=search_query,
        location_query=location_query
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_kl/<int:company_id>/<search_query>/<location_query>/",
    methods=["GET"])
def search_company_jobs_keyword_location_no_page_slash(
        company_id: int,
        search_query: str,
        location_query: str):
    return search_company_jobs_keyword_and_location(
        company_id=company_id,
        search_query=search_query,
        location_query=location_query
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_kl/<int:company_id>/<search_query>/<location_query>/"
    "<int:page_number>/",
    methods=["GET"])
def search_company_jobs_keyword_location_slash(
        company_id: int,
        search_query: str,
        location_query: str,
        page_number: int = 1):
    return search_company_jobs_keyword_and_location(
        company_id=company_id,
        search_query=search_query,
        location_query=location_query,
        page_number=page_number
    )


@general_rest_stub_bp.route("/search_company_jobs_kld", methods=["GET"])
def search_company_jobs_keyword_location_distance_default_no_company():
    return None


@general_rest_stub_bp.route("/search_company_jobs_kld/", methods=["GET"])
def search_company_jobs_keyword_location_distance_slash_default_no_company():
    return None


@general_rest_stub_bp.route("/search_company_jobs_kld/<int:company_id>",
                            methods=["GET"])
def search_company_jobs_keyboard_location_dist_default_no_params(
        company_id: int):
    return get_company_jobs(company_id=int(company_id))


@general_rest_stub_bp.route("/search_company_jobs_kld/<int:company_id>/",
                            methods=["GET"])
def search_company_jobs_keyboard_loc_dist_slash_default_no_params(
        company_id: int):
    return get_company_jobs(company_id=int(company_id))


@general_rest_stub_bp.route(
    "/search_company_jobs_kld/<int:company_id>/<search_query>",
    methods=["GET"])
def search_company_jobs_keyword_location_distance_default_no_location(
        company_id: int,
        search_query: str):
    return search_company_jobs_keyword(
        company_id=company_id,
        search_query=search_query,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_kld/<int:company_id>/<search_query>/",
    methods=["GET"])
def search_company_jobs_key_and_loc_dist_no_loc_no_dist_no_page(
        company_id: int,
        search_query: str):
    return search_company_jobs_keyword(
        company_id=company_id,
        search_query=search_query,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_kld/<int:company_id>/<search_query>/<location_query>",
    methods=["GET"])
def search_company_jobs_key_and_loc_dist_no_dist_no_page(
        company_id: int,
        search_query: str,
        location_query: str,
        page_number: int = 1):
    return search_company_jobs_keyword_and_location(
        company_id=company_id,
        search_query=search_query,
        location_query=location_query,
        page_number=page_number,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_kld/<int:company_id>/<search_query>/<location_query>/"
    "<int:distance>", methods=["GET"])
def search_company_jobs_key_and_loc_dist_no_dist_no_page_slash(
        company_id: int,
        search_query: str,
        location_query: str,
        page_number: int = 1):
    return search_company_jobs_keyword_and_location(
        company_id=company_id,
        search_query=search_query,
        location_query=location_query,
        page_number=page_number,
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_kld/<int:company_id>/<search_query>/<location_query>/"
    "<int:distance>/", methods=["GET"])
def search_company_jobs_key_and_loc_dist_no_page_slash(
        company_id: int,
        search_query: str,
        location_query: str,
        distance: int = 30):
    return search_company_jobs_keyword_and_location_distance(
        company_id=company_id,
        search_query=search_query,
        location_query=location_query,
        distance=distance
    )


@general_rest_stub_bp.route(
    "/search_company_jobs_kld/<int:company_id>/<search_query>/<location_query>/"
    "<int:distance>/<int:page_number>/", methods=["GET"])
def search_company_jobs_key_and_loc_dist_slash(
        company_id: int,
        search_query: str,
        location_query: str,
        distance: int = 30,
        page_number: int = 1):
    return search_company_jobs_keyword_and_location_distance(
        company_id=company_id,
        search_query=search_query,
        location_query=location_query,
        distance=distance,
        page_number=page_number,
    )
