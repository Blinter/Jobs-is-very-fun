/**
 * Sends a request to the server to enable or disable an API Endpoint.
 * @param {?number} apiId - API List URL ID
 * @param {?boolean} toggle - Toggle on or off
 * @returns {Promise}
 */
async function toggleAPIEndpoint(apiId, toggle) {
    if (apiId == undefined ||
        toggle == undefined) {
        console.error("toggleAPIEndpoint called with undefined input");
        return undefined;
    }

    if (apiId < 0 &&
        (toggle ||
            !toggle)) {
        return undefined;
    }

    const enable = toggle ? 1 : 0;
    try {
        return await axios.get(
            "/admin_rest/toggle_api/" +
            cleanString(apiId.toString()) +
            "/" +
            cleanString(enable.toString()), {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 400)
            return undefined;

        console.warn("toggleAPIEndpoint Exception");
        console.error(exception);
        throw exception;
    }
}
