from flask import (
    session,
    make_response,
    jsonify,
    Blueprint
)

from enums.response_codes import ResponseCodesGeneric
from extensions_api_endpoints import (
    get_api_endpoint_name_id,
    get_api_endpoint_description_only,
    get_api_endpoint_count_extras_only,
    get_api_endpoint_extra_doc_list,
    get_api_endpoint_extra_doc,
    get_api_endpoint_bodies,
    get_api_endpoint_params
)

from extensions_api_keys import (
    get_api_key_id_key,
    get_api_keys_last_access_only,
    get_api_key_preferred_proxy
)

from extensions_user import get_authenticated_user_name
from secrets_jobs.credentials import admin_list

admin_query_rest_bp = Blueprint(
    'admin_query_rest',
    __name__
)


@admin_query_rest_bp.route(
    "/admin_query_rest/get_api_key_id_key/<int:api_key_id>",
    methods=["GET"]
)
def admin_query_get_api_key_id_key(api_key_id: int):
    """
    REST endpoint
    Send the last_access column value to an admin whenever the API key is
    changed on the client.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    api_key_data = get_api_key_id_key(api_key_id)

    if api_key_data is not None:
        return (jsonify([i.to_dict_get_api_key_id_key()
                         for i in api_key_data]),
                int(ResponseCodesGeneric.OK))

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_query_rest_bp.route(
    "/admin_query_rest/get_previous_query",
    methods=["GET"]
)
def admin_query_get_previous_query():
    """
    REST endpoint
    Send the saved data to the client from a previously successful query.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    if session.get('saved_settings', False):
        if isinstance(session.get('saved_settings'), dict):
            return (jsonify(session.get('saved_settings', None)),
                    int(ResponseCodesGeneric.OK))

    return make_response('', int(ResponseCodesGeneric.NO_CONTENT))


@admin_query_rest_bp.route(
    "/admin_query_rest/get_api_key_preferred_proxy/<int:api_key_id>",
    methods=["GET"]
)
def admin_query_get_api_key_preferred_proxy(api_key_id: int):
    """
    REST endpoint
    Send the possible value of a preferred proxy whenever the API key is
    changed on the client.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    preferred_proxy = get_api_key_preferred_proxy(api_key_id)

    if preferred_proxy is not None:
        return (jsonify(
            {'preferred_proxy': preferred_proxy}),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_query_rest_bp.route(
    "/admin_query_rest/get_api_keys_last_access_only/<int:api_id>",
    methods=["GET"]
)
def admin_query_get_api_key_last_access(api_id: int):
    """
    REST endpoint
    Send the id, key, and last_access column value to an admin whenever the
    client changes the selected API.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    api_keys = get_api_keys_last_access_only(api_id)

    if api_keys is not None:
        return (
            jsonify(api_keys.to_dict_get_api_keys_last_access_only()),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_query_rest_bp.route(
    "/admin_query_rest/get_api_endpoints/<int:api_id>",
    methods=["GET"]
)
def admin_query_get_api_endpoint_name_id(api_id: int):
    """
    REST endpoint
    Send the nice_name, nice_description, and other data associated with the
    endpoint to the client whenever the selected endpoint is changed.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    api_endpoints = get_api_endpoint_name_id(api_id)

    if api_endpoints is not None:
        return (
            jsonify([i.to_dict_get_api_endpoint_name_id()
                     for i in api_endpoints]),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_query_rest_bp.route(
    "/admin_query_rest/get_api_endpoint_description_only/<int:api_endpoint_id>",
    methods=["GET"]
)
def admin_query_get_api_endpoint_description_only(api_endpoint_id: int):
    """
    REST endpoint
    Send the nice_description and other data associated with the
    endpoint to the client whenever the selected endpoint is changed.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    api_endpoint_description = (
        get_api_endpoint_description_only(api_endpoint_id)
    )

    if api_endpoint_description is not None:
        return (
            jsonify(api_endpoint_description
                    .to_dict_get_api_endpoint_description_only()),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_query_rest_bp.route(
    "/admin_query_rest/get_api_endpoint_count_extras_only/"
    "<int:api_endpoint_id>",
    methods=["GET"]
)
def admin_query_get_api_endpoint_count_extras_only(api_endpoint_id: int):
    """
    REST endpoint
    Send count of extras to admin user whenever the selected endpoint is
    changed.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    api_endpoint_extras_count = (
        get_api_endpoint_count_extras_only(api_endpoint_id))

    if api_endpoint_extras_count is not None:
        return (
            jsonify(api_endpoint_extras_count),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_query_rest_bp.route(
    "/admin_query_rest/get_api_endpoint_extra_doc_list/"
    "<int:api_endpoint_id>",
    methods=["GET"]
)
def admin_query_get_api_endpoint_extra_doc_list(api_endpoint_id: int):
    """
    REST endpoint
    Send the ids of the extra docs so that the admin can access them.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    api_endpoint_extra_doc_list = (
        get_api_endpoint_extra_doc_list(api_endpoint_id))

    if api_endpoint_extra_doc_list is not None:
        return (
            jsonify([i.to_dict_id_only()
                     for i in api_endpoint_extra_doc_list]),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_query_rest_bp.route(
    "/admin_query_rest/get_api_endpoint_extra_doc/"
    "<int:api_endpoint_extra_id>",
    methods=["GET"]
)
def admin_query_get_api_endpoint_extra_doc(api_endpoint_extra_id: int):
    """
    REST endpoint
    Send the contents of the extra documentation so that the admin can read
    them.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    api_endpoint_extra_doc = get_api_endpoint_extra_doc(api_endpoint_extra_id)

    if api_endpoint_extra_doc is not None:
        return (
            jsonify(api_endpoint_extra_doc.to_dict_extra_doc_only()),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_query_rest_bp.route(
    "/admin_query_rest/get_api_endpoint_params/"
    "<int:api_endpoint_id>",
    methods=["GET"]
)
def admin_query_get_api_endpoint_params(api_endpoint_id: int):
    """
    REST endpoint
    Retrieve the data from endpoint params so that the admin can access them.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    api_endpoint_params = get_api_endpoint_params(api_endpoint_id)

    if api_endpoint_params is not None:
        return (
            jsonify([i.to_dict()
                     for i in api_endpoint_params]),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))


@admin_query_rest_bp.route(
    "/admin_query_rest/get_api_endpoint_bodies/"
    "<int:api_endpoint_id>",
    methods=["GET"]
)
def admin_query_get_api_endpoint_bodies(api_endpoint_id: int):
    """
    REST endpoint
    Retrieve the data from endpoint bodies so that the admin can access them.
    """

    if (not session.get('user_id', False) or
            get_authenticated_user_name() not in admin_list):
        return make_response('', int(ResponseCodesGeneric.FORBIDDEN))

    api_endpoint_bodies = get_api_endpoint_bodies(api_endpoint_id)

    if api_endpoint_bodies is not None:
        return (
            jsonify([i.to_dict()
                     for i in api_endpoint_bodies]),
            int(ResponseCodesGeneric.OK)
        )

    return make_response('', int(ResponseCodesGeneric.INTERNAL_SERVER_ERROR))
