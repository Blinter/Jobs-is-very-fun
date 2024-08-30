/**
 * Retrieves Object of saved_data from server
 * @returns {Promise}
 */
async function getPreviousSettings() {
    try {
        return await axios.get(
            "/admin_query_rest/get_previous_query",
            { headers: { 'Content-Type': 'application/json' } });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;
        console.warn("Get Previous Settings Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves list of API Keys (Key and ID only) from the server
 * @param {?string} apiId - ID of the API List URL to retrieve API keys
 * @returns {Promise}
 */
async function getAPIKeyandIds(apiId) {
    if (apiId == undefined ||
        apiId.length == 0) {
        console.error("getAPIKeyandIds called with no input");
        return undefined;
    }

    try {
        return await axios.get(
            "/admin_query_rest/get_api_key_id_key/" + 
            cleanString(apiId.toString()), {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("Get API Keys for API ID Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves Last Access Value only based on the API Key ID from the server.
 * @param {?string} apiKeyId - ID of the APIKey to retrieve data
 * @returns {Promise}
 */
async function getAPIKeyLastAccessOnly(apiKeyId) {
    if (apiKeyId == undefined ||
        apiKeyId.length == 0) {
        console.error("getAPIKeyLastAccessOnly called with no input");
        return undefined;
    }

    try {
        return await axios.get(
            "/admin_query_rest/get_api_keys_last_access_only/" + 
            cleanString(apiKeyId.toString()), {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("Get API Key Data Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves the Preferred proxy based on the API Key ID from the server.
 * @param {?string} apiKeyId - ID of the APIKey to retrieve data
 * @returns {Promise}
 */
async function getAPIKeyPreferredProxyOnly(apiKeyId) {
    if (apiKeyId == undefined ||
        apiKeyId.length == 0) {
        console.error("getAPIKeyPreferredProxyOnly called with no input");
        return undefined;
    }
    try {
        return await axios.get(
            "/admin_query_rest/get_api_key_preferred_proxy/" + 
            cleanString(apiKeyId), {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("Get API Key Preferred Proxy Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves list of API Endpoints from the server
 * @param {?string} apiId - ID of the API List URL to retrieve API keys
 * @returns {Promise}
 */
async function getAPIEndpointsNameIdOnly(apiId) {
    if (apiId == undefined ||
        apiId.length == 0) {
        console.error("getAPIEndpointsNameIdOnly called with no input");
        return undefined;
    }

    try {
        return await axios.get(
            "/admin_query_rest/get_api_endpoints/" + 
            cleanString(apiId.toString()), {
            headers: { 'Content-Type': 'application/json' }
        });
        
    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("Get API Endpoints for API ID Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves Description of an Endpoint when the selected Endpoint is changed and the description tab element is active.
 * @param {?string} apiEndpointId - ID of the API Endpoint.
 * @returns {Promise}
 */
async function getAPIEndpointNiceDescription(apiEndpointId) {
    if (apiEndpointId == undefined ||
        apiEndpointId.length == 0) {
        console.error("getAPIEndpointNiceDescription called with no input");
        return undefined;
    }
    try {
        return await axios.get(
            "/admin_query_rest/get_api_endpoint_description_only/" + 
            cleanString(apiEndpointId.toString()), {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("Get API Endpoint Description for API Endpoint ID Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves extra counts of an Endpoint when the selected Endpoint is changed.
 * @param {?string} apiEndpointId - ID of the API Endpoint to retrieve API Endpoint count data.
 * @returns {Promise}
 */
async function getAPIEndpointExtrasCount(apiEndpointId) {
    if (apiEndpointId == undefined ||
        apiEndpointId.length == 0) {
        console.error("getAPIEndpointExtrasCount called with no input");
        return undefined;
    }

    try {
        return await axios.get(
            "/admin_query_rest/get_api_endpoint_count_extras_only/" + 
            cleanString(apiEndpointId.toString()), {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("Get API Endpoint Extras Count for API Endpoint ID Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves Endpoint Parameter Data of an Endpoint when the active tab of an Endpoint is set to Params.
 * @param {?string} apiEndpointId - ID of the API Endpoint to retrieve API Endpoint Parameter data.
 * @returns {Promise}
 */
async function getAPIEndpointParams(apiEndpointId) {
    if (apiEndpointId == undefined ||
        apiEndpointId.length == 0) {
        console.error("getAPIEndpointParams called with no input");
        return undefined;
    }

    try {
        return await axios.get(
            "/admin_query_rest/get_api_endpoint_params/" + 
            cleanString(apiEndpointId.toString()), {
            headers: { 'Content-Type': 'application/json' }
        });
        
    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("Get API Endpoint Params Data Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves Endpoint Body Data of an Endpoint when the active tab of an Endpoint is set to Body.
 * @param {String} apiEndpointId - ID of the API Endpoint to retrieve API Endpoint Body data.
 * @returns {Response}
 */
async function getAPIEndpointBodies(apiEndpointId) {
    if (apiEndpointId == undefined ||
        apiEndpointId.length == 0) {
        console.error("getAPIEndpointBodies called with no input");
        return undefined;
    }

    try {
        return await axios.get(
            "/admin_query_rest/get_api_endpoint_bodies/" + 
            cleanString(apiEndpointId.toString()), {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("Get API Endpoint Bodies Data Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves the Extra document ID list when the active tab is set to Docs.
 * @param {String} apiEndpointId - ID of the API Endpoint to retrieve API Endpoint count data.
 * @returns {Response}
 */
async function getAPIEndpointExtraDocs(apiEndpointId) {
    if (apiEndpointId == undefined ||
        apiEndpointId.length == 0) {
        console.error("getAPIEndpointExtraDocs called with no input");
        return undefined;
    }

    try {
        return await axios.get(
            "/admin_query_rest/get_api_endpoint_extra_doc_list/" + 
            cleanString(apiEndpointId.toString()), {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("Get API Endpoint Extras Count for API Endpoint ID Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves Extra Documentation contents when the View Documentation Button has been clicked.
 * @param {String} apiExtraDocumentId - ID of the API Extra Endpoint to retrieve documentation data.
 * @returns {Response}
 */
async function getAPIExtraDocumentData(apiExtraDocumentId) {
    if (apiExtraDocumentId == undefined ||
        apiExtraDocumentId.length == 0) {
        console.error("getAPIExtraDocumentData called with no input");
        return undefined;
    }

    try {
        return await axios.get(
            "/admin_query_rest/get_api_endpoint_extra_doc/" + 
            cleanString(apiExtraDocumentId.toString()), {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;
            
        console.warn("Get API Endpoint Extra Document Data for view_extra Exception");
        console.error(exception);
        throw exception;
    }
}