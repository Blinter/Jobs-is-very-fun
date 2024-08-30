/**
 * Sends a request to the server to toggle a proxy on or off.
 * @param {?number} proxyId - Proxy ID
 * @param {?boolean} toggle - Enable or Disable
 * @returns {Promise}
 */
async function toggleProxyEndpoint(proxyId, toggle) {
    if (proxyId == undefined ||
        toggle == undefined) {
        console.error("toggleProxyEndpoint called with undefined input");
        return undefined;
    }

    if (proxyId < 0 &&
        (toggle ||
            !toggle)) {
        return undefined;
    }

    const enable = toggle ? 1 : 0;
    try {
        return await axios.get(
            "/admin_rest/toggle_proxy/" +
            cleanString(proxyId.toString()) +
            "/" +
            cleanString(enable.toString()), {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 400)
            return undefined;

        console.warn("toggleProxyEndpoint Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Sends a request to the server to test a proxy.
 * @param {?number} proxyId - Proxy ID
 * @returns {Promise}
 */
async function testProxyEndpoint(proxyId) {
    if (proxyId == undefined) {
        console.error("testProxyEndpoint called with undefined input");
        return undefined;
    }

    if (proxyId < 0) {
        return undefined;
    }
    
    try {
        return await axios.get(
            "/admin_rest/test_proxy/" +
            cleanString(proxyId.toString()), {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("testProxyEndpoint Exception");
        console.error(exception);
        throw exception;
    }
}
