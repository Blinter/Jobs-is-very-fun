/**
 * Sends a request to the server to toggle the selected API when the enable/disable button is clicked.
 * Updates the DOM by changing the class and text elements of the button that was clicked.
 * Modifies the DOM.
 * @param {object} e - Event for Button Click
 * @param {?number|?string} apiId - API ID
 * @returns {void}
 */
async function toggleAPI(e, apiId) {
    const toggle = cleanHTMLString($(e.target).text()) == "Enable" ? true : false;
    await toggleAPIEndpoint(apiId, toggle)
        .then(r => {
            // console.debug(r);
            if (r) {
                if (!toggle) {
                    $(e.target).text("Enable");
                    $(e.target).attr({'class': 'btn-linkAdmin rounded bg-success'});
                } else {
                    $(e.target).text("Disable");
                    $(e.target).attr({'class': 'btn-linkAdmin rounded bg-danger'});
                }
            } else {
                console.error("Server did not complete successfully from toggleAPI.");
            }
        });
}
