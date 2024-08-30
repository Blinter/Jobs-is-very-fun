"""
This file can be run
cd <this directory>
PYTHONPATH=<base_dir> python3 <file_name>.py
"""
import json
from datetime import datetime, UTC
from decimal import Decimal

import requests
from requests.auth import HTTPBasicAuth
from sqlalchemy import and_, or_, asc
from sqlalchemy.orm import load_only
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

from app import create_app, db
from extensions_api_keys import calculate_next
from extensions_mongo import fs_upload
from extensions_proxies import proxy_type_prefix_dict
from models.mariadb.api_headers import APIHeader
from models.mariadb.api_endpoints import APIEndpoint
from models.mariadb.api_endpoint_headers import APIEndpointHeader
from models.mariadb.api_endpoint_bodies import APIEndpointBody
from models.mariadb.api_endpoint_params import APIEndpointParam
from models.mariadb.api_endpoint_extras import APIEndpointExtra
from models.mariadb.api_keys import APIKey
from models.mariadb.api_list_url import APIListURL
from models.mariadb.mongo_storage import MongoStorage
from models.mariadb.proxies import Proxy

app = create_app()

quick_skip_id_list = []

with app.app_context():
    try:
        def refresh_proxy_list():
            """
            Refreshes Proxy List
            """
            return (
                db.session.query(Proxy)
                .filter(
                    and_(
                        Proxy.disabled.is_(False),
                        Proxy.testing.is_(False)
                    )
                ).all()
            )

        def refresh_apikey_list():
            """
            Refreshes API Key List
            """
            return (
                db.session.query(APIKey)
                .filter(
                    and_(
                        APIKey.disabled.is_(False),
                        or_(
                            APIKey.next_access.is_(None),
                            APIKey.next_access <= datetime.now(UTC)
                        )
                    )
                )
                .order_by(asc(APIKey.next_access))
                .all()
            )

        def refresh_api_list():
            """
            Refreshes API List
            """
            return (
                db.session.query(APIListURL)
                .filter(APIListURL.disabled.is_(False))
                .all()
            )

        def refresh_query_list():
            """
            Refreshes Query List
            """
            return (
                db.session.query(MongoStorage)
                .filter(
                    and_(
                        MongoStorage.object_id.is_(None),
                        MongoStorage.query_time.is_(None),
                        MongoStorage.length.is_(None),
                        MongoStorage.data_truncated.is_(None),
                        MongoStorage.code.is_(None)
                    )
                )
                .order_by(asc(MongoStorage.time))
                .options(
                    load_only(
                        MongoStorage.time,
                        MongoStorage.proxy,
                        MongoStorage.api,
                        MongoStorage.api_key,
                        MongoStorage.api_key_auto,
                        MongoStorage.url,
                        MongoStorage.endpoint_nice_name,
                        MongoStorage.input_json
                    )
                )
                .all()
            )

        def api_quick_skip(api_to_check):
            """
            Loads ID of MongoStorage if no API Keys are available
            Speeding up the processing time.
            """
            return (
                db.session.query(MongoStorage)
                .filter(
                    and_(
                        MongoStorage.api == api_to_check,
                        MongoStorage.object_id.is_(None),
                        MongoStorage.query_time.is_(None),
                        MongoStorage.length.is_(None),
                        MongoStorage.data_truncated.is_(None),
                        MongoStorage.code.is_(None)
                    )
                )
                .order_by(asc(MongoStorage.time))
                .options(
                    load_only(
                        MongoStorage.id
                    )
                )
                .all()
            )

        # Load Proxy Rows
        proxy_list = refresh_proxy_list()
        # Load APIListURL Rows
        api_list = refresh_api_list()
        # Load MongoStorage Rows
        query_list = refresh_query_list()
        final_query_status = ""
        count_query_list = len(query_list)
        current_count_query_list = 0

        # Filter only APIs that have an available API Key.
        # Access URL from MongoStorage to access Endpoint data.
        # Access API from MongoStorage as API ID, to access Keys.
        for query in query_list:
            if query.id in quick_skip_id_list:
                # print("Skip (" + str(query.id) + ")", end=' ', flush=True)
                continue

            # Refresh API Key data from list
            # Automatic processing keeps most recent updates.

            # Load APIKey Rows
            apikey_list = refresh_apikey_list()

            # Check for automatic API Key selection
            if query.api_key_auto:
                # Get available API Keys.
                api_key = [api_key for api_key in apikey_list
                           if api_key.url == query.api]

            else:
                # Load the Proxy as Selected Proxy
                proxy = [proxy for proxy in proxy_list
                         if proxy.proxy_address == query.proxy]

                # Make sure Proxy is only matched once
                if len(proxy) == 0:
                    print(str("Proxy not found"), flush=True)
                    final_query_status += ("Query ID " + str(query.id) +
                                           " has NOT been processed\n")
                    continue

                elif len(proxy) > 1:
                    raise ValueError("More than one Proxy matches on query_"
                                     "list ID " + str(query.id) + ".")

                # Load the API Key as selected API Key
                api_key = [api_key for api_key in apikey_list
                           if api_key.key == query.api_key and
                           api_key.url == query.api]

            # Make sure API key is matched and is found
            # query is skipped if an available API key is on cooldown.
            if (api_key is None or
                    len(api_key) == 0):
                # Skip Debug
                # print("An available API Key not found for " +
                #       str(query.api), flush=True)
                pass
                # final_query_status += ("Query ID " + str(query.id) +
                #                        " has NOT been processed.\n")

                prev_quick_skip_count = (
                    len(quick_skip_id_list)
                    if (isinstance(quick_skip_id_list, list) and
                        quick_skip_id_list is not None)
                    else 0
                )

                # find other ID's
                quick_skip_id_list = (
                        quick_skip_id_list +
                        [to_skip.id for to_skip in api_quick_skip(query.api)
                         if to_skip.id not in quick_skip_id_list]
                )

                new_quick_skip_count = (
                    len(quick_skip_id_list) if (
                            isinstance(quick_skip_id_list, list) and
                            quick_skip_id_list is not None)
                    else 0)

                if prev_quick_skip_count != new_quick_skip_count:
                    # print(
                    #     str(new_quick_skip_count - prev_quick_skip_count) +
                    #     " other queries were skipped due to "
                    #     "specified rate limit settings."
                    # )
                    pass

                continue

            # If filtered APIKey list is found and the query isn't an
            # automatic select, raise an exception.
            elif (len(api_key) > 1 and
                  not query.api_key_auto):

                raise ValueError("More than one API key matches on query_list "
                                 "ID " + str(query.id) + ".")

            # Skip update if there is only one query processed.
            if (current_count_query_list > 1 and
                    current_count_query_list + 1 != count_query_list):
                print("Current Query: (" +
                      str(current_count_query_list) +
                      "/" +
                      str(count_query_list) +
                      ") " +
                      "Processing ID: " + str(query.id), flush=True)

            # Load the API as selected API
            api = [api for api in api_list if api.url == query.api]

            # Make sure API is only matched once
            if len(api) == 0:
                print("API not found", flush=True)
                final_query_status += ("Query ID " + str(query.id) +
                                       " has NOT been processed.\n")
                continue

            elif len(api) > 1:
                raise ValueError("More than one API matches on query_list "
                                 "ID " + str(query.id) + ".")
            # print(str(query.id))
            # print(str(query.url))
            # print(str(query.endpoint_nice_name))
            endpoint = (
                db.session.query(APIEndpoint)
                .filter(and_(
                    APIEndpoint.http_path == query.url,
                    APIEndpoint.nice_name == query.endpoint_nice_name,
                    APIEndpoint.disabled.is_(False))
                )).all()

            # Make sure Endpoint is only matched once
            if len(api) == 0:
                print("Endpoint not found", flush=True)
                final_query_status += ("Query ID " + str(query.id) +
                                       " has NOT been processed.\n")
                continue

            elif len(api) > 1:
                raise ValueError("More than one Endpoint matches on query_"
                                 "list ID " + str(query.id) + ".")

            # Select the first API Key in the list of filtered API Keys.
            api_key = api_key[0]

            # Check for automatic API Key selection
            if query.api_key_auto:
                # Grab the preferred proxy
                # Set the proxy
                # Load the preferred proxy for the first API Key
                # First index of api_key list is selected for the API_Key
                proxy = [proxy for proxy in proxy_list
                         if api_key.preferred_proxy == proxy.proxy_address][0]

            else:
                # Default - Manual selection of Proxy which should be a
                # single row if the query isn't an automatically selected API
                # Key.
                proxy = proxy[0]

            api = api[0]

            if len(endpoint) == 0:
                raise ValueError("Endpoint identification error: " +
                                 str(query.id) + ", " +
                                 str(query.endpoint_nice_name) + ", " +
                                 str(query.api) + ", " +
                                 str(query.url))

            endpoint = endpoint[0]
            endpoint_headers = endpoint.endpoint_headers
            endpoint_params = endpoint.endpoint_params
            endpoint_bodies = endpoint.endpoint_bodies
            # check if all params and bodies are loaded properly.
            # combined parameters and bodies
            # use .copy() since we are validating the dictionary by using .pop
            data_dict = query.input_json.copy()

            data_dict_keys = (data_dict.keys()
                              if len(data_dict) > 0 else None)
            # print("Input_JSON: " + str(data_dict), flush=True)
            # Path Params adds the path param to the end of the URL
            # Load path parameters
            required_path_params = [i for i in endpoint_params
                                    if i.path_param != 0 and
                                    i.required != 0]
            # Param Suffixes adds the path param to the end of the URL
            # Load path parameters
            loaded_path_param_suffix = (
                endpoint.http_path_suffix
                if endpoint.http_path_suffix is not None else "")

            throw_on_non_required = False
            required_params = [i for i in endpoint_params if i.required != 0]
            required_bodies = [i for i in endpoint_bodies if i.required != 0]
            try:

                # Check if there is more than one Path Parameter
                # This can either be 0, or 1.
                if (required_path_params is not None and
                        len(required_path_params) > 1):
                    raise KeyError("Path Params in Endpoint"
                                   "data not properly set.")

                # Check if current data does not have all keys required
                for param in required_params:
                    if param.param not in data_dict_keys:
                        raise KeyError("Param Input requires " +
                                       str(param.param) + " to be loaded.")

                for body in required_bodies:
                    if body.key not in data_dict_keys:
                        raise KeyError("Body Input requires " +
                                       str(body.key) + " to be loaded.")

                # Check if current data has extra keys
                if data_dict_keys is not None:
                    if len(data_dict_keys) != 0:
                        for i in [i for i in data_dict_keys]:
                            if len(endpoint_params) != 0:
                                for j in [j for j in endpoint_params
                                          if i == j.param]:
                                    data_dict.pop(i, None)

                            if len(endpoint_bodies) != 0:
                                for j in [j for j in endpoint_bodies
                                          if i == j.key]:
                                    data_dict.pop(i, None)

                    # optional keys may be included
                    if (len(data_dict) != 0 and
                            throw_on_non_required):
                        # print("Debug", flush=True)
                        print(str(data_dict), flush=True)
                        raise KeyError("Query JSON has more input keys "
                                       "than expected.")

                # Reset the data_dict dictionary after checks
                data_dict = query.input_json
                data_dict_keys = data_dict.keys()
                # Data verified
                # Load base API headers
                api_headers = api.headers
                headers = {}

                # Add API key and other headers to headers
                for i in api_headers:
                    if i.api_key_header != 0:
                        headers[i.header] = api_key.key
                        continue

                    if i.value is not None:
                        headers[i.header] = i.value

                # Add headers from API (Endpoint headers)
                for i in endpoint_headers:
                    # print("Checking " + str(i.header) +
                    #       ": " + str(i.value), flush=True)
                    if (i.header is not None and
                       i.value is not None):
                        # print("adding endpoint header: " + str(i.header) +
                        #      ": " + str(i.value), flush=True)
                        headers[i.header] = i.value

                # Set URL for query
                url = query.url

                print("Original URL: " + url, flush=True)

                # Add the path param to the end of the URL
                for i in [j for j in endpoint_params
                          if j.path_param != 0]:
                    if (i.param in data_dict_keys and
                       data_dict[i.param] is not None):

                        url += data_dict[i.param]

                # Add the suffix to the end of the URL
                if str(loaded_path_param_suffix) != "":
                    url += loaded_path_param_suffix

                params_payload = {}
                # input test:
                print("======", flush=True)

                if proxy:
                    pass
                    # print("Using Proxy: " + str(proxy.proxy_address),
                    #       flush=True)

                # print(str(url), flush=True)
                # print(str(headers), flush=True)

                # Add params to params_payload if not a
                # path parameter
                # for ii in [ii for ii in temp_params
                #     if not ii.path_param]:
                #     params_payload[ii.key] = data_dict.get(ii.key)
                # Add body parameters
                # for ii in temp_bodies:
                #     params_payload[ii.key] = data_dict.get(ii.key)
                # print(str(params_payload), flush=True)

                # disable rest of code block here to debug
                # url/headers/params_payload only

                response = None

                selected_proxy_prefix = ''
                for i in proxy_type_prefix_dict.keys():
                    for j in proxy_type_prefix_dict[i]:
                        if j == proxy.proxy_type:
                            selected_proxy_prefix = i

                proxy_proxy = {
                    'http': selected_proxy_prefix + proxy.proxy_address,
                    'https': selected_proxy_prefix + proxy.proxy_address
                }

                if endpoint.http_method == "GET":

                    # Add params to params_payload if not a
                    # path parameter
                    for i in [i for i in endpoint_params
                              if i.path_param != 1 and
                              i.param in data_dict_keys and
                              (i.required != 0 or
                               (data_dict.get(i.param) is not None and
                                data_dict.get(i.param) != ""))]:

                        # Convert values to appropriate types.
                        if i.hint_type == 'Number':
                            if data_dict.get(i.param) is not None:
                                params_payload[i.param] = int(
                                    data_dict.get(i.param)
                                )

                        elif i.hint_type == 'Decimal':
                            if data_dict.get(i.param) is not None:
                                params_payload[i.param] = (
                                    Decimal(str(data_dict.get(i.param)))
                                )

                        elif i.hint_type == 'Object':
                            temp_string = data_dict.get(i.param)

                            if not temp_string:
                                continue

                            if temp_string[0] != "{":
                                temp_string = "{" + temp_string

                            if temp_string[-1] != "}":
                                temp_string = temp_string + "}"

                            try:
                                if temp_string:
                                    params_payload[i.key] = (
                                        json.loads(temp_string)
                                    )

                                # print(str(params_payload[i.param]),
                                #       flush=True)
                                break

                            except ValueError as e:
                                print(str(data_dict.get(i.param)), flush=True)
                                print(f"Error decoding JSON: {e}", flush=True)

                        elif i.hint_type == 'Array Object':
                            try:
                                params_payload[i.param] = (
                                    json.loads(data_dict.get(i.param))
                                )
                                # print(str(params_payload[i.param]),
                                #       flush=True)
                                break

                            except ValueError as e:
                                print(str(data_dict.get(i.param)), flush=True)
                                print("Error decoding Array Object from JSON:"
                                      f" {e}", flush=True)

                        elif (i.hint_type == 'Array' or
                              i.hint_type == 'Array String'):
                            if data_dict.get(i.param) is not None:
                                # print(str(data_dict.get(i.param)), flush=True)
                                params_payload[i.param] = (
                                    json.loads(data_dict.get(i.param))
                                )

                        elif i.hint_type == 'Array Number':
                            if data_dict.get(i.param) is not None:
                                params_payload[i.param] = (
                                    json.loads(data_dict.get(i.param))
                                )

                            for j in [j for j
                                      in params_payload[i.param].keys()]:
                                if params_payload[i.param][j] is not None:
                                    load = params_payload[i.param].pop(j)
                                    if load:
                                        params_payload[i.param][j] = (
                                            int(params_payload[i.param].pop(j))
                                        )

                        elif i.hint_type == 'Boolean String':
                            params_payload[i.param] = (
                                "true"
                                if (str(data_dict.get(i.param)).lower()
                                    == "true")
                                else "false"
                            )

                        elif i.hint_type == 'Boolean':
                            if data_dict.get(i.param) is not None:
                                params_payload[i.param] = (
                                        str(data_dict.get(i.param))
                                        == "True" or
                                        (str(data_dict.get(i.param)).lower()
                                         != 'false')
                                )
                        else:
                            params_payload[i.param] = data_dict.get(i.param)

                    print("= Params = ", flush=True)
                    print(str(params_payload), flush=True)
                    print("= Params End = ", flush=True)
                    print(" = Headers =", flush=True)
                    # print(str(headers), flush=True)
                    # print(" = Headers End = ", flush=True)
                    print("URL: " + str(url), flush=True)

                    # finally, send the query.
                    # use requests to retrieve the GET response

                    response = requests.get(
                        url=url.replace('\\', ''),
                        headers=headers if headers else None,
                        params=params_payload
                        if params_payload and len(params_payload) > 0 else None,
                        proxies=proxy_proxy,
                        auth=(HTTPBasicAuth(
                            proxy.proxy_username,
                            proxy.proxy_password)
                              if proxy.auth_required != 0 else None)
                    )

                elif endpoint.http_method == "POST":

                    # Add body parameters
                    for i in [i for i in endpoint_bodies
                              if i.key in data_dict_keys and
                              (i.required != 0 or
                               (data_dict.get(i.key) is not None and
                                data_dict.get(i.key) != ""))]:

                        # Convert values to appropriate types.
                        if i.value_hint_type == 'Number':
                            params_payload[i.key] = int(data_dict.get(i.key))

                        elif i.value_hint_type == 'Decimal':
                            params_payload[i.key] = (
                                Decimal(str(data_dict.get(i.key)))
                            )

                        elif i.value_hint_type == 'Object':
                            temp_string = data_dict.get(i.key)

                            if len(temp_string) == 0:
                                continue

                            if temp_string[0] != "{":
                                temp_string = "{" + temp_string

                            if temp_string[-1] != "}":
                                temp_string = temp_string + "}"

                            try:
                                params_payload[i.key] = (
                                    json.loads(temp_string)
                                )
                                # print(str(params_payload[i.key]), flush=True)
                                break

                            except ValueError as e:
                                print(str(data_dict.get(i.key)), flush=True)
                                print(f"Error decoding JSON: {e}", flush=True)

                        elif i.value_hint_type == 'Array Object':

                            try:
                                params_payload[i.key] = (
                                    json.loads(data_dict.get(i.key))
                                )
                                # print(str(params_payload[i.key]), flush=True)
                                break

                            except ValueError as e:
                                print(str(data_dict.get(i.key)), flush=True)
                                print("Error decoding Array Object from JSON:"
                                      f" {e}", flush=True)

                        elif (i.value_hint_type == 'Array' or
                              i.value_hint_type == 'Array String'):
                            try:
                                params_payload[i.key] = (
                                    json.loads(data_dict.get(i.key))
                                )
                                if isinstance(params_payload[i.key], dict):
                                    for j in [(j for j in
                                               params_payload[i.key].keys())]:
                                        popped_value = (
                                            params_payload[i.key].pop(j))
                                        if (len(popped_value) != 0 and
                                                popped_value is not None):
                                            try:
                                                params_payload[i.key][j] = (
                                                    popped_value
                                                )
                                            except ValueError as e:
                                                print(f"Error in Array/"
                                                      f"Array String",
                                                      flush=True)
                            except Exception as e:
                                print(str(data_dict.get(i.key)), flush=True)
                                print("Error decoding Array/Array String "
                                      "Object from JSON: "
                                      f"{e}", flush=True)

                        elif i.value_hint_type == 'Array Number':
                            try:
                                params_payload[i.key] = (
                                    json.loads(data_dict.get(i.key))
                                )

                                if isinstance(params_payload[i.key], dict):
                                    for j in [(j for j in
                                               params_payload[i.key].keys())]:
                                        popped_value = (
                                            params_payload[i.key].pop(j))
                                        if (len(popped_value) != 0 and
                                                popped_value is not None):
                                            try:
                                                params_payload[i.key][j] = (
                                                    int(popped_value)
                                                )
                                            except ValueError as e:
                                                print(f"Error converting "
                                                      f"string to int: "
                                                      f"{e}", flush=True)
                            except Exception as e:
                                print(str(data_dict.get(i.key)), flush=True)
                                print("Error decoding Array Number from JSON:"
                                      f" {e}", flush=True)

                        elif i.value_hint_type == 'Boolean String':
                            params_payload[i.key] = (
                                "true"
                                if str(data_dict.get(i.key)).lower() == "true"
                                else "false"
                            )

                        elif i.value_hint_type == 'Boolean':
                            params_payload[i.key] = (
                                    str(data_dict.get(i.key))
                                    == "True" or
                                    str(data_dict.get(i.key)).lower()
                                    != 'false'
                            )

                        else:
                            params_payload[i.key] = data_dict.get(i.key)

                    print("= Body =", flush=True)
                    print(str(params_payload), flush=True)
                    print("= Body End =", flush=True)
                    # finally, send the query.
                    # use requests to retrieve the POST response
                    response = requests.post(
                        url=url.replace('\\', ''),
                        headers=headers
                        if headers else None,
                        json=params_payload
                        if params_payload and len(params_payload) > 0
                        else None,
                        proxies=proxy_proxy,
                        auth=(HTTPBasicAuth(
                            proxy.proxy_username,
                            proxy.proxy_password)
                              if proxy.auth_required != 0 else None)
                    )

                else:

                    raise ValueError("Unknown HTTP Method" +
                                     str(endpoint.http_method))

                current_time = datetime.now(UTC)
                # print("======", flush=True)

                if response is None:
                    raise ValueError("Response did not go through.")

                # print(str(response.headers), flush=True)
                try:
                    response_json = json.dumps(response.json())

                except ValueError as e:
                    print(f"Status Code: {str(response.status_code)} Error "
                          f"decoding JSON: {e}", flush=True)
                    print(str(response), flush=True)
                    # malformed json response. Save the response itself
                    # without json.dumps.
                    print("API returned data that is not a JSON object. "
                          "Saving the text instead", flush=True)
                    response_json = response.text

                # Fill the Mongo_Storage with response
                # Insert response json into mongo_fs
                query.object_id = fs_upload(response_json.encode()).binary
                # Check for automatic API Key selection
                if query.api_key_auto:
                    # Fill in the proxy address and api key
                    # if the automatic API key was selected.
                    query.proxy = proxy.proxy_address
                    query.api_key = api_key.key

                # Add query time
                query.query_time = current_time
                query.length = len(response_json)
                query.data_truncated = response.text[:255]
                query.code = response.status_code
                query.verified = True

                # Now update the API key and set next
                # time based on the rate limit settings.
                if (response.status_code != 500 and
                   response.status_code != 400 and
                        response.status_code != 401):
                    api_key.next_access = calculate_next(
                        api=api,
                        current_date_time_utc=current_time
                    )

                    if api.requests_count is None:
                        api.requests_count = 0

                    api.requests_count += 1
                    api.verified = True
                    api_key.verified = True
                # Check for system blocked API Key message
                if (response.status_code == 401 and
                        response.text == """\
{"message":"Blocked User. Please contact your API provider."}"""):
                    print("QUERY FAILED, Disable API KEY SINCE API PROVIDER "
                          "HAS BLOCKED USER", flush=True)

                    if api.failed_count is None:
                        api.failed_count = 0

                    api.failed_count += 1
                    api.verified = True
                    # This API key likely got blocked due to batch processing
                    # Disable the API Key for respective API.
                    api_key.disabled = True
                    api_key.verified = True

                db.session.commit()
                # Add counter to process status messages and process
                # changes to automatic API Key selection.
                current_count_query_list += 1

                if (response.status_code != 500 and
                        response.status_code != 400 and
                        response.status_code != 401):
                    final_query_status += ("Query ID " + str(query.id) +
                                           " has been processed.\n")

                else:
                    pass
                    # Skip Debug
                    # final_query_status += ("Query ID " + str(query.id) +
                    #                        " has NOT been processed.\n")

            except KeyError as e:
                final_query_status += (str(e) + " - Could not process "
                                       "query ID " + str(query.id) + ".\n")
                raise e

        if (final_query_status is None or
                len(final_query_status) == 0):
            db.session.close()
            raise ChildProcessError("No queries completed")
        else:
            print(final_query_status, flush=True)

        raise ChildProcessError("Parsing Completed")

    # Database exception errors
    # Catch integrity constraints, such as unique violations or foreign key
    # constraints.
    except IntegrityError as e:
        db.session.rollback()
        db.session.close()
        print(f"IntegrityError: {e}", flush=True)
        raise e

    # Catch errors related to DB operations (connection issues or
    # unavailability)
    except OperationalError as e:
        db.session.rollback()
        db.session.close()
        print(f"OperationalError: {e}", flush=True)
        raise e

    # SQLAlchemy-specific errors
    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        print(f"SQLAlchemyError: {e}", flush=True)
        raise e

    # Handler Process error for no queries processed. (No database changes)
    except ChildProcessError as e:
        if ('No queries completed' not in str(e) or
                'Parsing Completed' not in str(e)):
            db.session.rollback()
        db.session.close()
        raise e

    # Other Errors
    except Exception as e:
        db.session.rollback()
        db.session.close()
        print(f"Error: {e}", flush=True)
        raise e
