/**
 * Retrieves Endpoint data based on an array of types to filter
 * @param {?Array.<number>} apiFilterArray - Array of Types of API Endpoints
 * @returns {Promise}
 */
async function getAPIEndpointsFiltered(apiFilterArray) {
    if (apiFilterArray == undefined) {
        console.error("getAPIEndpointsFiltered called with undefined input");
        return undefined;
    }

    if (apiFilterArray.length == 0) {
        apiFilterArray = [-1]
    }
    try {
        return await axios.get(
            "/admin_rest/get_api_endpoint_filtered", {
            headers: { 'Content-Type': 'application/json' },
            params: { filter: JSON.stringify(apiFilterArray) }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;
            
        console.warn("Get API Endpoints Filtered for API Endpoint filter array Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Sends a request to the server to enable or disable an API Endpoint.
 * @param {?string} endpointId - API Endpoint ID
 * @param {?boolean} toggle - Toggle on or off
 * @returns {Promise}
 */
async function toggleEndpointEndpoint(
    endpointId, 
    toggle) {
    if (endpointId == undefined ||
        toggle == undefined) {
        console.error("toggleEndpointEndpoint called with undefined input");
        return undefined;
    }

    if (endpointId < 0 &&
        (toggle ||
            !toggle)) {
        return undefined;
    }

    const enable = toggle ? 1 : 0;

    try {
        return await axios.get(
            "/admin_rest/toggle_endpoint/" +
            cleanString(endpointId.toString()) +
            "/" +
            enable.toString(), {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 400)
            return undefined;

        console.warn("toggleEndpointEndpoint Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Sends a request to the server to enable or disable an API Header Endpoint.
 * Note: There are no optional headers in the current API Endpoint list so this cannot be fully tested.
 * @param {?string} endpointHeaderId - API Endpoint Header ID
 * @param {?boolean} toggle - Toggle on or off
 * @returns {Promise}
 */
async function toggleEndpointHeaderEndpoint(
    endpointHeaderId, 
    toggle) {
    if (endpointHeaderId == undefined ||
        toggle == undefined) {
        console.error("toggleEndpointHeaderEndpoint called with undefined input");
        return undefined;
    }

    if (endpointId < 0 &&
        (toggle ||
            !toggle)) {
        return undefined;
    }

    const enable = toggle ? 1 : 0;
    
    try {
        return await axios.get(
            "/admin_rest/toggle_endpoint/" +
            cleanString(endpointHeaderId.toString()) +
            "/" +
            enable.toString(), {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 400)
            return undefined;

        console.warn("toggleEndpointHeaderEndpoint Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Sends a request to the server to enable or disable an API Endpoint Param (Optional Parameter only).
 * @param {?string} endpointParamId - API Endpoint Parameter ID
 * @param {?boolean} toggle - Toggle on or off
 * @returns {Promise}
 */
async function toggleEndpointParamEndpoint(endpointParamId, toggle) {
    if (endpointParamId == undefined ||
        toggle == undefined) {
        console.error("toggleEndpointParamEndpoint called with undefined input");
        return undefined;
    }

    if (endpointParamId < 0 &&
        (toggle ||
            !toggle)) {
        return undefined;
    }

    const enable = toggle ? 1 : 0;
    
    try {
        return await axios.get(
            "/admin_rest/toggle_endpoint_param/" +
            cleanString(endpointParamId.toString()) +
            "/" +
            enable.toString(), {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 400)
            return undefined;

        console.warn("toggleEndpointParamEndpoint Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Sends a request to the server to enable or disable an API Endpoint Body (Optional Parameter only).
 * @param {?string} endpointBodyId - API Endpoint Body ID
 * @param {?boolean} toggle - Toggle on or off
 * @returns {Promise}
 */
async function toggleEndpointBodyEndpoint(endpointBodyId, toggle) {
    if (endpointBodyId == undefined ||
        toggle == undefined) {
        console.error("toggleEndpointBodyEndpoint called with undefined input");
        return undefined;
    }

    if (endpointBodyId < 0 &&
        (toggle ||
            !toggle)) {
        return undefined;
    }

    const enable = toggle ? 1 : 0;
    
    try {
        return await axios.get(
            "/admin_rest/toggle_endpoint_body/" +
            cleanString(endpointBodyId.toString()) +
            "/" +
            cleanString(enable.toString()), {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 400)
            return undefined;

        console.warn("toggleEndpointBodyEndpoint Exception");
        console.error(exception);
        throw exception;
    }
}
