/**
 * Sends a request to the server to toggle the selected Proxy when the enable/disable button is clicked.
 * Updates the DOM by changing the class and text elements of the button that was clicked.
 * Modifies the DOM.
 * @param {object} e - Event for Button Click
 * @param {string} proxyId - Proxy ID
 * @returns {void}
 */
async function toggleProxy(e, proxyId) {
    const toggle = cleanHTMLString($(e.target).text()) == "Enable" ? true : false;
    await toggleProxyEndpoint(proxyId, toggle)
        .then(r => {
            // console.debug(r);
            if (r) {
                if (!toggle) {
                    $(e.target).text("Enable");
                    $(e.target).attr({ 'class': 'btn-linkAdmin rounded placeholder-wave bg-primary' });
                } else {
                    $(e.target).text("Disable");
                    $(e.target).attr({ 'class': 'btn-linkAdmin rounded bg-danger' });
                }
            } else {
                console.error("Server did not complete successfully from toggleProxy.");
            }
        });
}


/**
 * Sends a request to the server to test the selected Proxy when the test button is clicked.
 * Updates the DOM by changing the last access text on the bottom.
 * Increases the requests count and failed requests count for the proxy on client DOM as reflected by the server.
 * Modifies the DOM.
 * @param {object} e - Event for Button Click
 * @param {string} proxyId - Proxy ID
 * @returns {void}
 */
async function testProxy(e, proxyId) {

    const lastAccessElement = $(e.target)
        .parent()
        .children(".fluidTextBottom");

    const requestsCountElement = $(e.target)
        .parent()
        .children("#requests" + proxyId.toString());

    const failedRequestsCountElement = $(e.target)
        .parent()
        .children("#failed_count" + proxyId.toString());

    if (requestsCountElement == undefined || 
        failedRequestsCountElement == undefined) {
        console.error("Could not find Requests or Failed Requests count element to modify.");
        return;
    }

    await testProxyEndpoint(proxyId)
        .then(r => {
            const requestsCount = $(requestsCountElement).text()
                .replace("Requests:", "")
                .replace("None", "0")
                .trim();

            const failedRequestsCount = $(failedRequestsCountElement).text()
                .replace("Failed Requests:", "")
                .replace("None", "0")
                .trim();

            // console.debug(+cleanHTMLString(requestsCount).toString());
            // console.debug(+cleanHTMLString(failedRequestsCount).toString());

            const newRequestCount = (+cleanHTMLString(requestsCount) + 1).toString().trim();

            if (r != false &&
                r != true &&
                r != undefined &&
                r.length != 0 &&
                r.data.length != 0) {
                $(lastAccessElement).attr({ 'class': 'fluidLongTextFlex text-primary' });
                $(lastAccessElement).text(r.data.toString().trim());

            } else {
                $(lastAccessElement).text("Test failed. Check Proxy.");
                $(failedRequestsCountElement).text("Failed Requests: " +
                    (+failedRequestsCount.toString().trim() + 1).toString());
            }

            $(requestsCountElement).text("Requests: " + newRequestCount.toString());
        });
}