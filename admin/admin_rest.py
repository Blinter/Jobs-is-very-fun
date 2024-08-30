import json

from flask import (
    session,
    make_response,
    jsonify,
    Blueprint,
    request
)

from enums.response_codes import ResponseCodesGeneric
from extensions_api_endpoints import (
    get_api_endpoints_dashboard_display,
    get_api_endpoints_filtered_dashboard_display, toggle_endpoint,
    toggle_endpoint_header, toggle_endpoint_param, toggle_endpoint_body
)
from extensions_api_list import toggle_api

from extensions_mongo import (
    get_mongo_storage,
    get_mongo_doc,
    get_mongo_storage_filtered_dashboard_display,
    get_mongo_scrape_storage,
    get_mongo_scrape_doc, get_mongo_scrape_storage_paginate,
    delete_mongo_storage, delete_mongo_scrape_storage
)
from extensions_proxies import toggle_proxy, test_proxy

from extensions_user import get_authenticated_user_name
from extensions_html_parsing import (
    parse_webpage_html2text,
    parse_webpage_bs4,
    parse_webpage_bs4_html5lib
)
from secrets_jobs.credentials import admin_list

admin_rest_bp = Blueprint(
    'admin_rest',
    __name__
)


@admin_rest_bp.route(
    "/admin_rest/get_mongo_storage_filtered",
    methods=["GET"]
)
def admin_query_get_mongo_storage_filtered():
    """
    REST endpoint
    Send back the Mongo Storage list based on filter settings.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    filtered_endpoints = request.args.get('f1')
    filtered_api_list_urls = request.args.get('f2')
    # print("filtered array")
    # print(str(filtered_array))

    if (filtered_endpoints is not None and
            filtered_api_list_urls is not None):

        try:
            filtered_endpoints = json.loads(filtered_endpoints)
            filtered_api_list_urls = json.loads(filtered_api_list_urls)

            if filtered_endpoints is not None:
                if ('-1' in filtered_endpoints and
                        '-1' in filtered_api_list_urls):

                    mongo_storage_list = get_mongo_storage()

                    if mongo_storage_list is not None:
                        return (
                            jsonify([
                                i.to_dict_rest()
                                for i in mongo_storage_list]
                            ),
                            int(ResponseCodesGeneric.OK)
                        )
                else:
                    return make_response(jsonify([
                        i.to_dict_rest()
                        for i in get_mongo_storage_filtered_dashboard_display(
                            filtered_types=filtered_endpoints,
                            filtered_api_list_urls=filtered_api_list_urls
                        ) if i is not None]),
                        int(ResponseCodesGeneric.OK)
                    )

        except Exception as e:
            print(str(e))
            raise e

    return make_response('', int(ResponseCodesGeneric.NO_CONTENT))


@admin_rest_bp.route(
    "/admin_rest/get_mongo_storage",
    methods=["GET"]
)
def admin_get_mongo_storage():
    """
    REST endpoint
    Retrieve the data from endpoint bodies so that the admin can access them.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    mongo_storage_list = get_mongo_storage()

    if mongo_storage_list is not None:
        return (
            jsonify([i.to_dict_rest() for i in mongo_storage_list]),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_rest_bp.route(
    "/admin_rest/get_mongo_scrape_storage/<sort_method>/<int:current_page>",
    methods=["GET"]
)
def admin_get_mongo_scrape_storage(
        sort_method: str,
        current_page: int):
    """
    REST endpoint
    Retrieve the data from endpoint bodies so that the admin can access them.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    if (sort_method is None or
            not isinstance(sort_method, str) or
            len(sort_method) == 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    mongo_scrape_storage_list = get_mongo_scrape_storage_paginate(
        sort_method=sort_method,
        items=50,
        page_number=current_page
    )

    if mongo_scrape_storage_list is not None:
        return (
            jsonify([i.to_dict_rest() for i in mongo_scrape_storage_list]),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_rest_bp.route(
    "/admin_rest/get_mongo_scrape_storage_all",
    methods=["GET"]
)
def admin_get_mongo_scrape_storage_all():
    """
    REST endpoint
    Retrieve the data from endpoint bodies so that the admin can access them.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    mongo_scrape_storage_list = get_mongo_scrape_storage()

    if mongo_scrape_storage_list is not None:
        return (
            jsonify([i.to_dict_rest() for i in mongo_scrape_storage_list]),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_rest_bp.route(
    "/admin_rest/get_mongo_doc/"
    "<int:mongo_id>",
    methods=["GET"]
)
def admin_get_mongo_doc(mongo_id: int):
    """
    REST endpoint
    Send the contents of the extra documentation so that the admin can read.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    mongo_doc = get_mongo_doc(mongo_id)

    if mongo_doc is not None:
        return (
            jsonify(mongo_doc),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_rest_bp.route(
    "/admin_rest/get_mongo_scrape_doc/"
    "<int:mongo_scrape_id>",
    methods=["GET"]
)
def admin_get_mongo_scrape_doc(mongo_scrape_id: int):
    """
    REST endpoint
    Send the contents of the extra documentation so that the admin can read.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    mongo_scrape_doc = get_mongo_scrape_doc(mongo_scrape_id)

    if mongo_scrape_doc is not None:
        # Scrape document using a preferred html parser to convert the document
        # to text.
        # For now, give raw document as text.
        return (

            jsonify(
                # parse_webpage_bs4(mongo_scrape_doc)
                # parse_webpage_bs4_html5lib(mongo_scrape_doc)
                # parse_webpage_html2text(mongo_scrape_doc)
                mongo_scrape_doc
            ),

            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_rest_bp.route(
    "/admin_rest/get_api_endpoint_filtered",
    methods=["GET"]
)
def admin_query_get_api_endpoint_filtered():
    """
    REST endpoint
    Send back the APIEndpoint list based on filter settings.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    filtered_array = request.args.get('filter')

    if filtered_array is not None:
        try:

            filtered_array = json.loads(filtered_array)

            if filtered_array is not None:

                if '-1' in filtered_array:
                    return make_response(jsonify([
                        i.to_dict_dashboard_template()
                        for i in get_api_endpoints_dashboard_display()
                        if i is not None]),
                        int(ResponseCodesGeneric.OK))

                else:
                    return make_response(jsonify([
                        i.to_dict_dashboard_template()
                        for i in get_api_endpoints_filtered_dashboard_display(
                            filtered_array) if i is not None]),
                        int(ResponseCodesGeneric.OK))

        except Exception as e:
            print(str(e))
            raise e

    return make_response('', int(ResponseCodesGeneric.NO_CONTENT))


@admin_rest_bp.route(
    "/admin_rest/toggle_api/<int:api_list_url_id>/<int:enable>",
    methods=["GET"]
)
def admin_toggle_api(
        api_list_url_id: int,
        enable: int):
    """
    REST endpoint
    Allows an Admin to disable or enable an API List URL while accessing the
    admin_api_list page.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    if (not isinstance(enable, int) or
            (enable != 0 and
             enable != 1) or
            not isinstance(api_list_url_id, int) or
            api_list_url_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    return (
        jsonify(
            toggle_api(
                api_list_url_id=api_list_url_id,
                enable=True if enable == 1 else False
            ),
        ),
        int(ResponseCodesGeneric.OK)
    )


@admin_rest_bp.route(
    "/admin_rest/toggle_proxy/<int:proxy_id>/<int:enable>",
    methods=["GET"]
)
def admin_toggle_proxy(
        proxy_id: int,
        enable: int):
    """
    REST endpoint
    Allows an Admin to disable or enable an Proxy while accessing the
    admin_proxy_list page.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    if (not isinstance(enable, int) or
            (enable != 0 and
             enable != 1) or
            not isinstance(proxy_id, int) or
            proxy_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    return (
        jsonify(
            toggle_proxy(
                proxy_id=proxy_id,
                enable=True if enable == 1 else False)),
        int(ResponseCodesGeneric.OK)
    )


@admin_rest_bp.route(
    "/admin_rest/test_proxy/<int:proxy_id>",
    methods=["GET"]
)
def admin_test_proxy(proxy_id: int):
    """
    REST endpoint
    Allows an admin to test a Proxy and returns the IP of the proxy.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    if (not isinstance(proxy_id, int) or
            proxy_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    result = test_proxy(proxy_id=proxy_id)

    return (
        make_response(
            '' if not result else result,
            int(ResponseCodesGeneric.OK)
        )
    )


@admin_rest_bp.route(
    "/admin_rest/toggle_endpoint/<int:endpoint_id>/<int:enable>",
    methods=["GET"]
)
def admin_toggle_endpoint(
        endpoint_id: int,
        enable: int):
    """
    REST endpoint
    Allows an Admin to disable or enable an Endpoint Param while accessing the
    admin_api_endpoints page.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    if (not isinstance(enable, int) or
            (enable != 0 and
             enable != 1) or
            not isinstance(endpoint_id, int) or
            endpoint_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    return (
        jsonify(
            toggle_endpoint(
                endpoint_id=endpoint_id,
                enable=True if enable == 1 else False)),
        int(ResponseCodesGeneric.OK)
    )


@admin_rest_bp.route(
    "/admin_rest/toggle_endpoint_header/<int:endpoint_header_id>/<int:enable>",
    methods=["GET"]
)
def admin_toggle_endpoint_header(
        endpoint_header_id: int,
        enable: int):
    """
    REST endpoint
    Allows an Admin to disable or enable an Endpoint Param while accessing the
    admin_api_endpoints page.

    Note: There are no optional headers in the current API Endpoint list
    so this cannot be fully tested.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    if (not isinstance(enable, int) or
            (enable != 0 and
             enable != 1) or
            not isinstance(endpoint_header_id, int) or
            endpoint_header_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    return (
        jsonify(
            toggle_endpoint_header(
                endpoint_header_id=endpoint_header_id,
                enable=True if enable == 1 else False)),
        int(ResponseCodesGeneric.OK)
    )


@admin_rest_bp.route(
    "/admin_rest/toggle_endpoint_param/<int:endpoint_param_id>/<int:enable>",
    methods=["GET"]
)
def admin_toggle_endpoint_param(
        endpoint_param_id: int,
        enable: int):
    """
    REST endpoint
    Allows an Admin to disable or enable an optional Endpoint Param while
    accessing the detailed view for a selected API Endpoint.

    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    if (not isinstance(enable, int) or
            (enable != 0 and
             enable != 1) or
            not isinstance(endpoint_param_id, int) or
            endpoint_param_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    return (
        jsonify(
            toggle_endpoint_param(
                endpoint_param_id=endpoint_param_id,
                enable=True if enable == 1 else False)),
        int(ResponseCodesGeneric.OK)
    )


@admin_rest_bp.route(
    "/admin_rest/toggle_endpoint_body/<int:endpoint_body_id>/<int:enable>",
    methods=["GET"]
)
def admin_toggle_endpoint_body(
        endpoint_body_id: int,
        enable: int):
    """
    REST endpoint
    Allows an Admin to disable or enable an optional Endpoint Body while
    accessing the detailed view for a selected API Endpoint.

    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    if (not isinstance(enable, int) or
            (enable != 0 and
             enable != 1) or
            not isinstance(endpoint_body_id, int) or
            endpoint_body_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    return (
        jsonify(
            toggle_endpoint_body(
                endpoint_body_id=endpoint_body_id,
                enable=True if enable == 1 else False)),
        int(ResponseCodesGeneric.OK)
    )


@admin_rest_bp.route(
    "/admin_rest/delete_mongo_storage/<int:mongo_storage_id>",
    methods=["DELETE"]
)
def admin_delete_mongo_storage(mongo_storage_id: int):
    """
    REST endpoint
    Allows an Admin to delete a Mongo Storage Row and returns
    200 on success - 500 on error.

    """
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    if (not isinstance(mongo_storage_id, int) or
            mongo_storage_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    result = delete_mongo_storage(mongo_storage_id=mongo_storage_id)

    # print(str(result))

    return (
        make_response(
            '',
            int(ResponseCodesGeneric.OK)
            if result is not False
            else int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR)
        )
    )


@admin_rest_bp.route(
    "/admin_rest/delete_mongo_scrape_storage/<int:mongo_scrape_storage_id>",
    methods=["DELETE"]
)
def admin_delete_mongo_scrape_storage(mongo_scrape_storage_id: int):
    """
    REST endpoint
    Allows an Admin to delete a Mongo Scrape Storage Row and returns
    200 on success - 500 on error.

    """
    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    if (not isinstance(mongo_scrape_storage_id, int) or
            mongo_scrape_storage_id < 0):
        return make_response('', int(ResponseCodesGeneric.BAD_REQUEST))

    result = delete_mongo_scrape_storage(
        mongo_scrape_storage_id=mongo_scrape_storage_id)

    # print(str(result))

    return (
        make_response(
            '',
            int(ResponseCodesGeneric.OK)
            if result is not False
            else int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR)
        )
    )
