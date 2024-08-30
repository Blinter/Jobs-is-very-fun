const adminPath = '/admin';

let apiEndpointFilterArray = ['-1'];
let apiEndpointsRefreshing = false;

/**
 * Continue loading data from REST when the page is loaded.
 * Adds Event Handlers to form change events.
 * Modifies the DOM
 */
$(document).ready(() => {
    const foundActiveItems = $('.btn-EndpointMenuFilterItemActive');
    if (foundActiveItems == undefined)
        return

    if (foundActiveItems.length > 0) {
        apiEndpointFilterArray = []
        for (item of foundActiveItems)
            apiEndpointFilterArray.push($(item).attr('data-type-id'))
        $(item).on('click', event => setFilterToInactive(event));
    }

    const foundInactiveItems = $('.btn-EndpointMenuFilterItem');

    if (foundInactiveItems == undefined)
        return;

    if (foundInactiveItems.length > 0)
        for (item of foundInactiveItems)
            $(item).on('click', event => setFilterToActive(event));

    // console.debug(apiEndpointFilterArray);
});

/**
 * Opens a pop-up window that allows the admin to view additional endpoint details.
 * Modifies the DOM (by opening a pop-up)
 * @param {string} apiEndpointId - ID of API Endpoint to view details for
 * @returns {void}
 */
function viewEndpoint(apiEndpointId) {
    window.open(
        adminPath +
        "/view_endpoint/" +
        apiEndpointId.toString(),

        "",

        "width=1024," +
        "height=768," +

        "left=" +
        ((screen.width - 1024) / 2) +
        "," +

        "top=" +
        ((screen.height - 768) / 2) +
        "," +

        "scrollbars=yes," +
        "resizable=yes," +
        "status=no," +
        "location=no," +
        "channelmode=yes," +
        "fullscreen=no," +
        "directories=no," +
        "toolbar=no," +
        "menubar=no"
    );
}

/**
 * Opens a pop-up window that allows the admin to view additional endpoint extra details.
 * Modifies the DOM (by opening a po-up)
 * @param {object} event - Click Event Target
 * @param {string} apiExtraDocId - ID of API Endpoint to view details for
 * @returns {void}
 */
function viewEndpointExtraDoc(apiExtraDocId) {
    window.open(
        "/admin_query/view_extra/" +
        apiExtraDocId.toString(),

        "",

        "width=1024," +
        "height=768," +

        "left=" +
        ((screen.width - 1024) / 2) +
        "," +

        "top=" +
        ((screen.height - 768) / 2) +
        "," +

        "scrollbars=yes," +
        "resizable=yes," +
        "status=no," +
        "location=no," +
        "channelmode=yes," +
        "fullscreen=no," +
        "directories=no," +
        "toolbar=no," +
        "menubar=no"
    );
}

/**
 * Sets an active filter to inactive
 * Modifies the DOM
 * @param {object} event - Click Event Target
 * @returns {void}
 */
function setFilterToInactive(event) {
    // console.debug("set filter to inactive");
    if ($(event.target) == undefined)
        return;

    $(event.target).attr({
        class: 'btn-EndpointMenuFilterItem'
    });

    apiEndpointFilterArray = apiEndpointFilterArray.filter(v =>
        v != $(event.target).attr('data-type-id')
    );

    $(event.target).off('click');
    $(event.target).on('click', newEvent => setFilterToActive(newEvent));

    checkEmptyFilters();
    // console.debug(apiEndpointFilterArray);    
    refreshAPIEndpoints();
}

/**
 * Sets an inactive filter to active
 * Modifies the DOM
 * @param {object} event - Click Event Target
 * @returns {void}
 */
function setFilterToActive(event) {
    // console.debug("set filter to active");
    if ($(event.target) == undefined)
        return;

    $(event.target).attr({
        class: 'btn-EndpointMenuFilterItemActive'
    });

    $(event.target).off('click');
    $(event.target).on('click', newEvent => setFilterToInactive(newEvent));
    apiEndpointFilterArray.push($(event.target).attr('data-type-id'))
    // console.debug(apiEndpointFilterArray);
    refreshAPIEndpoints();
}

/**
 * Checks for empty filter Array
 * Modifies the DOM
 * @returns {void}
 */
function checkEmptyFilters() {
    if (apiEndpointFilterArray.length != 0)
        return;

    const defaultFilterButton = $('#defaultFilterItem');
    if ($(defaultFilterButton) == undefined)
        return;

    apiEndpointFilterArray.push($(defaultFilterButton).attr('data-type-id'));
    $(defaultFilterButton).attr({
        class: 'btn-EndpointMenuFilterItemActive'
    });

    $(defaultFilterButton).off('click');
    $(defaultFilterButton).on('click', newEvent => setFilterToInactive(newEvent));
}

/**
 * Refreshes API Endpoints when the filter is changed.
 * Modifies the DOM
 * @returns {void}
 */
async function refreshAPIEndpoints() {
    if (apiEndpointFilterArray == undefined ||
        apiEndpointFilterArray.length == 0 ||
        apiEndpointsRefreshing)
        return;

    // console.debug("refreshing endpoints for");
    // console.debug(apiEndpointFilterArray);
    apiEndpointsRefreshing = true;
    await getAPIEndpointsFiltered(apiEndpointFilterArray)
        .then(response => {
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                console.error("refreshAPIEndpoints Response did not return anything.");
                apiEndpointsRefreshing = false;
                return;
            }
            const endpointsDashboard = $('.adminAPIEndpointList');

            $(endpointsDashboard).empty();
            const endpointsDashboardBody = $('<div>')
                .attr({
                    'class': 'row justify-content-center row-cols-auto gx-1 gx-lg-2 gx-xl-3 gx-xxl-4 gy-1 gy-xl-2 gy-xxl-3'
                });

            $(endpointsDashboard).append($(endpointsDashboardBody));
            for (item of response.data) {
                $(endpointsDashboardBody).append(generateAPIEndpointTemplate(item));
            }

            apiEndpointsRefreshing = false;
        });
}

/**
 * Creates an element with data retrieved from the API Endpoints Filtered REST endpoint.
 * @param {Promise} apiEndpointRowData - Row data returned from server
 * @returns {object} API Endpoint data and form controls produced by the server
 */
function generateAPIEndpointTemplate(apiEndpointRowData) {
    if (apiEndpointRowData == undefined)
        return undefined;

    const element1 = $("<div>")
        .attr({
            'class': 'col-auto'
        });

    const element2 = $("<div>")
        .attr({
            'class': 'adminAPIEndpointListLink figure rounded bg-dark px-lg-1 px-xl-2 px-xxl-3 py-1 py-lg-2'
        });

    $(element1).append($(element2));

    const element3 = $("<span>")
        .attr({
            'class': 'text-info'
        })
        .css({
            'font-size': '16px'
        })
        .text(apiEndpointRowData.api_nice_name);
    $(element2).append($(element3));

    const element4 = $("<br>");
    $(element2).append($(element4));

    const element5 = $("<span>")
        .attr({
            'class': 'fluidLongTextFlex'
        })
        .css({
            'font-size': '14px',
            'font-weight': 'bolder'
        })
        .text(apiEndpointRowData.nice_name);
    $(element2).append($(element5));

    const element6 = $("<br>");
    $(element2).append($(element6));

    const element7 = $("<span>")
        .attr({
            'class': 'fluidLongTextFlex text-info'
        })
        .css({
            'font-size': '14px',
        })
        .text(apiEndpointRowData.type);
    $(element2).append($(element7));

    const element8 = $("<br>");
    $(element2).append($(element8));

    const element9 = $("<hr>")
        .attr({
            'class': 'mx-5'
        })
        .css({
            'color': 'white'
        })
    $(element2).append($(element9));

    if (apiEndpointRowData.nice_description != undefined &&
        apiEndpointRowData.nice_description.length > 0) {
        const element10 = $("<span>")
            .attr({
                'class': 'fluidLongTextFlex',
            })
            .css({
                'font-size': '12px'
            })
            .text(apiEndpointRowData.nice_description);
        $(element2).append($(element10));

        const element11 = $("<br>")
            .attr({
                'class': 'mx-5'
            })
            .css({
                'color': 'white'
            });
        $(element2).append($(element11));

        const element12 = $("<hr>")
            .attr({
                'class': 'mx-5'
            })
            .css({
                'color': 'white'
            });
        $(element2).append($(element12));
    }

    const element13 = $("<button>")
        .attr({
            'class': 'btn-linkAdminMini rounded bg-primary'
        })
        .on('click', () => viewEndpoint(apiEndpointRowData.id))
        .text('View');
    $(element2).append($(element13));

    $(element2).append(' ');

    if (apiEndpointRowData.disabled == 0) {
        const element14 = $("<button>")
            .attr({
                'class': 'btn-linkAdminMini rounded bg-danger'
            })
            .on('click', e => toggleEndpoint(e, apiEndpointRowData.id))
            .text('Disable');
        $(element2).append($(element14));

    } else {
        const element15 = $("<button>")
            .attr({
                'class': 'btn-linkAdminMini rounded bg-success'
            })
            .on('click', e => toggleEndpoint(e, apiEndpointRowData.id))
            .text('Enable');
        $(element2).append($(element15));
    }

    const element16 = $("<br>");
    $(element2).append($(element16));

    const element17 = $('<span>')
        .attr({
            'class': 'fluidLongTextFlex text-info'
        })
        .text(apiEndpointRowData.api_host)
    $(element2).append($(element17));

    return $(element1);
}

/**
 * Sends a request to the server to toggle the selected Endpoint when the enable/disable button is clicked.
 * Updates the DOM by changing the class and text elements of the button that was clicked.
 * Modifies the DOM.
 * @param {object} e - Event for Button Click
 * @param {string} apiEndpointId - API Endpoint ID
 * @returns {void}
 */
async function toggleEndpoint(e, apiEndpointId) {
    const toggle = cleanHTMLString($(e.target).text()) == "Enable" ? true : false;
    await toggleEndpointEndpoint(apiEndpointId, toggle)
        .then(r => {
            // console.debug(r);
            if (r) {
                if (!toggle) {
                    $(e.target).text("Enable");
                    $(e.target).attr({ 'class': 'btn-linkAdminMini rounded bg-success' });
                } else {
                    $(e.target).text("Disable");
                    $(e.target).attr({ 'class': 'btn-linkAdminMini rounded bg-danger' });
                }
            } else {
                console.error("Server did not complete the request successfully from toggleEndpoint.");
            }
        });
}

/**
 * Sends a request to the server to toggle the selected Endpoint Header when the enable/disable button is clicked.
 * Updates the DOM by changing the class and text elements of the button that was clicked.
 * Note: There are no optional headers in the current API Endpoint list so this cannot be fully tested.
 * Modifies the DOM.
 * @param {object} e - Event for Button Click
 * @param {string} apiEndpointHeaderId - API Endpoint Header ID
 * @returns {void}
 */
async function toggleEndpointHeader(e, apiEndpointHeaderId) {
    const toggle = cleanHTMLString($(e.target).text()) == "Enable" ? true : false;
    await toggleEndpointHeaderEndpoint(apiEndpointHeaderId, toggle)
        .then(r => {
            // console.debug(r);
            if (r) {
                if (!toggle) {
                    $(e.target).text("Enable");
                    $(e.target).attr({ 'class': 'btn-linkAdminMini rounded bg-success' });
                } else {
                    $(e.target).text("Disable");
                    $(e.target).attr({ 'class': 'btn-linkAdminMini rounded bg-danger' });
                }
            } else {
                console.error("Server did not complete the request successfully from toggleEndpointHeader.");
            }
        });
}

/**
 * Sends a request to the server to toggle the selected Endpoint Parameter (Optional only) when the enable/disable button is clicked.
 * Updates the DOM by changing the class and text elements of the button that was clicked.
 * Modifies the DOM.
 * @param {object} e - Event for Button Click
 * @param {string} apiEndpointParamId - API Endpoint Param ID
 * @returns {void}
 */
async function toggleEndpointParam(e, apiEndpointParamId) {
    const toggle = cleanHTMLString($(e.target).text()) == "Enable" ? true : false;
    await toggleEndpointParamEndpoint(apiEndpointParamId, toggle)
        .then(r => {
            // console.debug(r);
            if (r) {
                if (!toggle) {
                    $(e.target).text("Enable");
                    $(e.target).attr({ 'class': 'btn-linkAdminMini rounded bg-success' });
                } else {
                    $(e.target).text("Disable");
                    $(e.target).attr({ 'class': 'btn-linkAdminMini rounded bg-danger' });
                }
            } else {
                console.error("Server did not complete the request successfully from toggleEndpointParam.");
            }
        });
}

/**
 * Sends a request to the server to toggle the selected Endpoint Body (Optional only) when the enable/disable button is clicked.
 * Updates the DOM by changing the class and text elements of the button that was clicked.
 * Modifies the DOM.
 * @param {object} e - Event for Button Click
 * @param {string} apiEndpointBodyId - API Endpoint Param ID
 * @returns {void}
 */
async function toggleEndpointBody(e, apiEndpointBodyId) {
    const toggle = cleanHTMLString($(e.target).text()) == "Enable" ? true : false;
    await toggleEndpointBodyEndpoint(apiEndpointBodyId, toggle)
        .then(r => {
            // console.debug(r);
            if (r) {
                if (!toggle) {
                    $(e.target).text("Enable");
                    $(e.target).attr({ 'class': 'btn-linkAdminMini rounded bg-success' });
                } else {
                    $(e.target).text("Disable");
                    $(e.target).attr({ 'class': 'btn-linkAdminMini rounded bg-danger' });
                }
            } else {
                console.error("Server did not complete the request successfully from toggleEndpointBody.");
            }
        });
}
