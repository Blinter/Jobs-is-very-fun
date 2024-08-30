const adminPath = '/admin';
const adminMongoStorage = '/admin_mongo_storage';
const adminMongoViewExtra = adminPath + '/view_mongo/';
const adminMongoConfirmDelete = adminPath + '/confirm_mongo_deletion/';

let apiEndpointFilterArray = ['-1'];
let apiListFilterArray = ['-1'];
let apiRefreshing = false;

/**
 * Continue loading data from REST when the page is loaded.
 * Adds Event Handlers to form change events.
 */
$(document).ready(() => {
    if (window.location.pathname.includes(adminMongoStorage)) {
        displayMongoStorage();

        const foundActiveEndpointItems = $('.btn-EndpointMenuFilterItemActive');

        if (foundActiveEndpointItems == undefined)
            return;

        if (foundActiveEndpointItems.length > 0) {
            apiEndpointFilterArray = [];
            for (item of foundActiveEndpointItems)
                apiEndpointFilterArray.push($(item).attr('data-type-id'));

            $(item).on('click', event => setEndpointFilterToInactive(event));
        }

        const foundInactiveEndpointItems = $('.btn-EndpointMenuFilterItem');
        if (foundInactiveEndpointItems == undefined)
            return;

        if (foundInactiveEndpointItems.length > 0)
            for (item of foundInactiveEndpointItems)
                $(item).on('click', event => setEndpointFilterToActive(event));

        const foundActiveAPIItems = $('.btn-APIMenuFilterItemActive');
        if (foundActiveAPIItems == undefined)
            return;

        if (foundActiveAPIItems.length > 0) {
            apiListFilterArray = [];
            for (item of foundActiveAPIItems)
                apiListFilterArray.push($(item).attr('data-type-id'));

            $(item).on('click', event => setAPIFilterToInactive(event));
        }

        const foundInactiveAPIItems = $('.btn-APIMenuFilterItem');
        if (foundInactiveAPIItems == undefined)
            return;
        if (foundInactiveAPIItems.length > 0)
            for (item of foundInactiveAPIItems)
                $(item).on('click', event => setAPIFilterToActive(event));

        // console.debug(apiEndpointFilterArray);

    } else if (window.location.pathname.includes(adminMongoViewExtra)) {
        displayMongoDocument();

    } else if (window.location.pathname.includes(adminMongoConfirmDelete)) {
        displayMongoDelete();
    }
});

/**
 * Refreshes Mongo Storage List when the filter is changed.
 * Modifies the DOM
 * @returns {void}
 */
async function refreshMongoStorage() {
    if (apiEndpointFilterArray == undefined ||
        apiEndpointFilterArray.length == 0 ||
        apiRefreshing)
        return;

    // console.debug("refreshing endpoints for");
    // console.debug(apiEndpointFilterArray);
    apiRefreshing = true;

    const documentHolder = $("#mongoStorageBody");
    if ($(documentHolder) == undefined) {
        console.error("Could not find element holder to load in document data.");
        return;
    }

    $(documentHolder).empty();

    await getMongoStorageFiltered(apiEndpointFilterArray, apiListFilterArray)
        .then(response => {
            $(documentHolder).empty();

            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                console.error("refreshMongoStorage Response did not return anything.");
                apiRefreshing = false;
                return;
            }

            response.data.forEach(v => {
                $(documentHolder)
                    .append(
                        generateMongoStorageRowTemplate(v)
                    );
            });

            apiRefreshing = false;
        });
}

/**
 * Sets an inactive Endpoint filter to active
 * Modifies the DOM
 * @param {?object} event - Click Event Target
 * @returns {void}
 */
function setEndpointFilterToActive(event) {
    // console.debug("set filter to active");
    if (event == undefined ||
        $(event.target) == undefined)
        return;

    $(event.target).attr({
        class: 'btn-EndpointMenuFilterItemActive'
    });

    $(event.target).off('click');
    $(event.target).on('click', newEvent => setEndpointFilterToInactive(newEvent));
    apiEndpointFilterArray.push($(event.target).attr('data-type-id'));
    // console.debug(apiEndpointFilterArray);
    refreshMongoStorage();
}

/**
 * Sets an active API filter to inactive
 * Modifies the DOM
 * @param {?object} event - Click Event Target
 * @returns {void}
 */
function setAPIFilterToActive(event) {
    // console.debug("set filter to active");
    if (event == undefined ||
        $(event.target) == undefined)
        return;
    $(event.target).attr({
        class: 'btn-APIMenuFilterItemActive'
    });

    $(event.target).off('click');
    $(event.target).on('click', newEvent => setAPIFilterToInactive(newEvent));
    apiListFilterArray.push($(event.target).attr('data-type-id'));
    // console.debug(apiListFilterArray);
    refreshMongoStorage();
}

/**
 * Sets an active filter Endpoint to inactive
 * Modifies the DOM
 * @param {?object} event - Click Event Target
 * @returns {void}
 */
function setEndpointFilterToInactive(event) {
    // console.debug("set filter to inactive");
    if (event == undefined ||
        $(event.target) == undefined)
        return;

    $(event.target).attr({
        class: 'btn-EndpointMenuFilterItem'
    });

    apiEndpointFilterArray = apiEndpointFilterArray.filter(v =>
        v != $(event.target).attr('data-type-id')
    );

    $(event.target).off('click');
    $(event.target).on('click', newEvent => setEndpointFilterToActive(newEvent));

    checkEmptyEndpointFilters();
    // console.debug(apiEndpointFilterArray);    
    refreshMongoStorage();
}

/**
 * Sets an active API filter to inactive
 * Modifies the DOM
 * @param {?object} event - Click Event Target
 * @returns {void}
 */
function setAPIFilterToInactive(event) {
    // console.debug("set API filter to inactive");
    if (event == undefined ||
        $(event.target) == undefined)
        return;

    $(event.target).attr({
        class: 'btn-APIMenuFilterItem'
    });

    apiListFilterArray = apiListFilterArray.filter(v =>
        v != $(event.target).attr('data-type-id')
    );
    $(event.target).off('click');
    $(event.target).on('click', newEvent => setAPIFilterToActive(newEvent));
    checkEmptyAPIFilters();
    // console.debug(apiFilterArray);    
    refreshMongoStorage();
}

/**
 * Checks for empty Endpoint filter Array
 * Modifies the DOM
 * @returns {void}
 */
function checkEmptyEndpointFilters() {
    if (apiEndpointFilterArray.length != 0)
        return;

    const defaultEndpointFilterButton = $('#defaultEndpointFilterItem');
    if ($(defaultEndpointFilterButton) == undefined)
        return;

    apiEndpointFilterArray.push($(defaultEndpointFilterButton).attr('data-type-id'));
    $(defaultEndpointFilterButton).attr({
        class: 'btn-EndpointMenuFilterItemActive'
    });

    $(defaultEndpointFilterButton).off('click');
    $(defaultEndpointFilterButton).on('click', newEvent => setEndpointFilterToInactive(newEvent));
}

/**
 * Checks for empty API filter Array
 * Modifies the DOM
 * @returns {void}
 */
function checkEmptyAPIFilters() {
    if (apiListFilterArray.length != 0)
        return;
    const defaultAPIFilterButton = $('#defaultAPIFilterItem');
    if ($(defaultAPIFilterButton) == undefined)
        return;

    apiListFilterArray.push($(defaultAPIFilterButton).attr('data-type-id'));
    $(defaultAPIFilterButton).attr({
        class: 'btn-APIMenuFilterItemActive'
    });

    $(defaultAPIFilterButton).off('click');
    $(defaultAPIFilterButton).on('click', newEvent => setAPIFilterToInactive(newEvent));
}

/**
 * Continue loading contents of the Mongo Storage data from REST after the page is loaded.
 * Modifies the DOM.
 * @returns {void}
 */
async function displayMongoStorage() {
    const documentHolder = $("#mongoStorageBody");
    if ($(documentHolder) == undefined) {
        console.error("Could not find element holder to load in document data.");
        return;
    }

    $(documentHolder).empty();
    await getAPIMongoDocumentStorageList()
        .then(response => {
            $(documentHolder).empty();
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                console.error("getAPIMongoDocumentStorageList response did not return anything.");
                return;
            }

            response.data.forEach(v => {
                $(documentHolder)
                    .append(
                        generateMongoStorageRowTemplate(v)
                    );
            });
        });
}

/**
 * Continue loading contents of a Mongo object from REST after the page is loaded.
 * Modifies the DOM.
 * @return {void}
 */
async function displayMongoDocument() {
    const documentHolder = $(".extraDocumentationBody");
    if ($(documentHolder) == undefined) {
        console.error("Could not find element holder to load in document data.");
        return;
    }

    const documentId = window.location.pathname.replace(adminMongoViewExtra, "");
    await getAPIMongoDocumentData(documentId)
        .then(response => {
            $(documentHolder).empty();
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                console.error("getAPIMongoDocumentData response did not return anything.");
                return;
            }

            $(documentHolder).text(response.data);
        });
}

/**
 * Continue loading contents of Mongo ID from REST in a text box that allows selection, after the page is loaded.
 * Allows the user to delete the row and Mongo DB Object ID
 * Modifies the DOM.
 * @returns {void}
 */
async function displayMongoDelete() {
    const documentHolder = $("#mongoDataRaw");
    if ($(documentHolder) == undefined) {
        console.error("Could not find element holder to load in document data.");
        return;
    }

    const documentId = window.location.pathname.replace(adminMongoConfirmDelete, "");
    await getAPIMongoDocumentData(documentId)
        .then(response => {
            $(documentHolder).empty();
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                console.error("getAPIMongoDocumentData response did not return anything.");
                return;
            }

            $(documentHolder).text(response.data);
        });
}

/**
 * Loads a mongo window viewing the text response of a query.
 * Modifies the DOM.
 * Opens a pop-up window
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openMongo(mongo_id) {
    window.open(
        adminPath +
        "/view_mongo/" +
        mongo_id.toString(),

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
 * Loads a window viewing the raw JSON response of a query.
 * Modifies the DOM.
 * Opens a pop-up window
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openRaw(mongo_id) {
    window.open(
        adminPath +
        "/view_raw/" +
        mongo_id.toString(),

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
 * Loads a window viewing the raw parsed location of a query.
 * Modifies the DOM.
 * Opens a pop-up window
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openRawLocations(mongo_id) {
    window.open(
        adminPath +
        "/view_raw_locations/" +
        mongo_id.toString(),

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
 * Loads a window viewing the raw parsed company of a query.
 * Modifies the DOM.
 * Opens a pop-up window
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openRawCompanies(mongo_id) {
    window.open(
        adminPath +
        "/view_raw_companies/" +
        mongo_id.toString(),

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
 * Loads a window viewing the raw parsed description of a query.
 * Modifies the DOM.
 * Opens a pop-up window
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openRawDescriptions(mongo_id) {
    window.open(
        adminPath +
        "/view_raw_descriptions/" +
        mongo_id.toString(),

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
 * Loads a window viewing the raw parsed apply link of a query.
 * Modifies the DOM.
 * Opens a pop-up window
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openRawApplyLinks(mongo_id) {
    window.open(
        adminPath +
        "/view_raw_apply_links/" +
        mongo_id.toString(),

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
 * Loads a window viewing the raw parsed experience levels of a query.
 * Modifies the DOM.
 * Opens a pop-up window
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openRawExperienceLevels(mongo_id) {
    window.open(
        adminPath +
        "/view_raw_experience_levels/" +
        mongo_id.toString(),

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
 * Loads a window viewing the raw parsed job titles of a query.
 * Modifies the DOM.
 * Opens a pop-up window
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openRawJobTitles(mongo_id) {
    window.open(
        adminPath +
        "/view_raw_job_titles/" +
        mongo_id.toString(),

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
 * Loads a window viewing the raw parsed job types of a query.
 * Modifies the DOM.
 * Opens a pop-up window
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openRawJobTypes(mongo_id) {
    window.open(
        adminPath +
        "/view_raw_job_types/" +
        mongo_id.toString(),

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
 * Loads a window viewing the raw parsed salaries of a query.
 * Modifies the DOM.
 * Opens a pop-up window
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openRawSalaries(mongo_id) {
    window.open(
        adminPath +
        "/view_raw_salaries/" +
        mongo_id.toString(),

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
 * Loads a window viewing the raw parsed times of a query.
 * Modifies the DOM.
 * Opens a pop-up window
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openRawTimes(mongo_id) {
    window.open(
        adminPath +
        "/view_raw_times/" +
        mongo_id.toString(),

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
 * Loads a window viewing the raw parsed data of a query.
 * Modifies the DOM.
 * Opens a pop-up window
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openRawAll(mongo_id) {
    openRawTimes(mongo_id);
    openRawSalaries(mongo_id);
    openRawJobTypes(mongo_id);
    openRawJobTitles(mongo_id);
    openRawExperienceLevels(mongo_id);
    openRawApplyLinks(mongo_id);
    openRawDescriptions(mongo_id);
    openRawCompanies(mongo_id);
    openRawLocations(mongo_id);
    openRaw(mongo_id);
}

/**
 * Loads a window confirming the deletion of a mongo storage row.
 * Opens a pop-up window confirming the deletion of the row and MongoDB object.
 * @param {number} mongo_id - ID of MongoStorage Row
 * @returns {void}
 */
function openMongoDeletion(mongo_id) {
    window.open(
        adminPath +
        "/confirm_mongo_deletion/" +
        mongo_id.toString(),

        "",

        "width=1024," +
        "height=1024," +

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
 * Creates an element with data retrieved from the API Mongo Storage Filtered REST endpoint.
 * @param {Promise} v - Row data returned from server
 * @returns {object}
 */
function generateMongoStorageRowTemplate(v) {
    const newRow = $("<tr>")
        .attr({ 'class': 'row mx-auto adminLargeTableTextItem' });

    let newColumn = $("<td>")
        .attr({ 'class': 'col border-top' })
        .text(v.id)
        .append("<br>");

    const actionMenuControl = $("<div>")
        .attr({ 'class': 'dropup' });

    const actionMenuButton = $("<button>")
        .attr({
            'class': 'btn btn-success btn-sm dropdown-toggle',
            'type': 'button',
            'id': 'buttonControlMenu' + v.id,
            'data-bs-toggle': 'dropdown',
            'aria-haspopup': 'true',
            'aria-expanded': 'false',
            'data-bs-popper-config': '{"strategy": "fixed"}'
        })
        .text("Controls");

    const viewButton = $("<div>")
        .attr({
            'class': 'dropdown-menu',
            'aria-labelledby': 'buttonControlMenu' + v.id
        });

    const viewMongo = $('<a>')
        .text("View")
        .attr({ 'class': 'dropdown-item' })
        .css({ 'cursor': 'pointer' })
        .hover(
            function (event) {
                $(event.target).css({
                    'background-color': 'teal',
                    'color': 'white'
                });
            },
            function (event) {
                $(event.target).css({
                    'background-color': '',
                    'color': 'black'
                });
            }
        );

    $(viewMongo).on('click', () => openMongo(v.id));
    $(viewButton).append($(viewMongo));

    if (v.code != undefined) {
        const viewRaw = $('<a>')
            .text("View Raw")
            .attr({ 'class': 'dropdown-item' })
            .css({ 'cursor': 'pointer' })
            .hover(
                function (event) {
                    $(event.target).css({
                        'background-color': 'teal',
                        'color': 'white'
                    });
                },
                function (event) {
                    $(event.target).css({
                        'background-color': '',
                        'color': 'black'
                    });
                }
            );

        $(viewRaw).on('click', () => openRaw(v.id));
        $(viewButton).append($(viewRaw));

        const viewRawLocations = $('<a>')
            .text("View Raw Locations")
            .attr({ 'class': 'dropdown-item' })
            .css({ 'cursor': 'pointer' })
            .hover(
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': 'teal',
                            'color': 'white'
                        });
                },
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': '',
                            'color': 'black'
                        });
                }
            );

        $(viewRawLocations).on('click', () => openRawLocations(v.id));
        $(viewButton).append($(viewRawLocations));

        const viewRawCompanies = $('<a>')
            .text("View Raw Companies")
            .attr({ 'class': 'dropdown-item' })
            .css({ 'cursor': 'pointer' })
            .hover(
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': 'teal',
                            'color': 'white'
                        });
                },
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': '',
                            'color': 'black'
                        });
                }
            );

        $(viewRawCompanies).on('click', () => openRawCompanies(v.id));
        $(viewButton).append($(viewRawCompanies));

        const viewRawDescriptions = $('<a>')
            .text("View Raw Descriptions")
            .attr({ 'class': 'dropdown-item' })
            .css({ 'cursor': 'pointer' })
            .hover(
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': 'teal',
                            'color': 'white'
                        });
                },
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': '',
                            'color': 'black'
                        });
                }
            );

        $(viewRawDescriptions).on('click', () => openRawDescriptions(v.id));
        $(viewButton).append($(viewRawDescriptions));

        const viewRawApplyLinks = $('<a>')
            .text("View Raw Apply Links")
            .attr({ 'class': 'dropdown-item' })
            .css({ 'cursor': 'pointer' })
            .hover(
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': 'teal',
                            'color': 'white'
                        });
                },
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': '',
                            'color': 'black'
                        });
                }
            );

        $(viewRawApplyLinks).on('click', () => openRawApplyLinks(v.id));
        $(viewButton).append($(viewRawApplyLinks));

        const viewRawExperienceLevels = $('<a>')
            .text("View Raw Experience Levels")
            .attr({ 'class': 'dropdown-item' })
            .css({ 'cursor': 'pointer' })
            .hover(
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': 'teal',
                            'color': 'white'
                        });
                },
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': '',
                            'color': 'black'
                        });
                }
            );

        $(viewRawExperienceLevels).on('click', () => openRawExperienceLevels(v.id));
        $(viewButton).append($(viewRawExperienceLevels));

        const viewJobTitles = $('<a>')
            .text("View Raw Job Titles")
            .attr({ 'class': 'dropdown-item' })
            .css({ 'cursor': 'pointer' })
            .hover(
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': 'teal',
                            'color': 'white'
                        });
                },
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': '',
                            'color': 'black'
                        });
                }
            );

        $(viewJobTitles).on('click', () => openRawJobTitles(v.id));
        $(viewButton).append($(viewJobTitles));

        const viewRawJobTypes = $('<a>')
            .text("View Raw Job Types")
            .attr({ 'class': 'dropdown-item' })
            .css({ 'cursor': 'pointer' })
            .hover(
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': 'teal',
                            'color': 'white'
                        });
                },
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': '',
                            'color': 'black'
                        });
                }
            );

        $(viewRawJobTypes).on('click', () => openRawJobTypes(v.id));
        $(viewButton).append($(viewRawJobTypes));

        const viewRawSalaries = $('<a>')
            .text("View Raw Salaries")
            .attr({ 'class': 'dropdown-item' })
            .css({ 'cursor': 'pointer' })
            .hover(
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': 'teal',
                            'color': 'white'
                        });
                },
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': '',
                            'color': 'black'
                        });
                }
            );

        $(viewRawSalaries).on('click', () => openRawSalaries(v.id));
        $(viewButton).append($(viewRawSalaries));

        const viewRawTimes = $('<a>')
            .text("View Raw Times")
            .attr({ 'class': 'dropdown-item' })
            .css({ 'cursor': 'pointer' })
            .hover(
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': 'teal',
                            'color': 'white'
                        });
                },
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': '',
                            'color': 'black'
                        });
                }
            );

        $(viewRawTimes).on('click', () => openRawTimes(v.id));
        $(viewButton).append($(viewRawTimes));

        const viewRawAll = $('<a>')
            .text("View Raw All")
            .attr({ 'class': 'dropdown-item' })
            .css({ 'cursor': 'pointer' })
            .hover(
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': 'teal',
                            'color': 'white'
                        });
                },
                function (event) {
                    $(event.target)
                        .css({
                            'background-color': '',
                            'color': 'black'
                        });
                }
            );

        $(viewRawAll).on('click', () => openRawAll(v.id));
        $(viewButton).append($(viewRawAll));
    }

    const confirmDeleteMongoMenuLink = $('<a>')
        .text("Delete")
        .attr({ 'class': 'dropdown-item' })
        .css({ 'cursor': 'pointer' })
        .hover(
            function (event) {
                $(event.target)
                    .css({
                        'background-color': 'teal',
                        'font-weight': '900',
                        'color': 'red'
                    });
            },
            function (event) {
                $(event.target)
                    .css({
                        'background-color': '',
                        'font-weight': '',
                        'color': 'black'
                    });
            }
        );

    $(confirmDeleteMongoMenuLink).on('click', () => openMongoDeletion(v.id));

    if (v.code != undefined) {
        $(viewButton).append('<div class="dropdown-divider">');
        $(viewButton).append($(confirmDeleteMongoMenuLink));
    }

    $(actionMenuControl).append($(actionMenuButton));
    $(actionMenuControl).append($(viewButton));

    $(newColumn).append($(actionMenuControl));

    // let newButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show")
    // newColumn = $("<td class='col border-top'>").append($(newButton));
    // ((tempElement, newText) =>
    //     $(newButton).on('click', () =>
    //         $(tempElement).text(newText))
    // )($(newColumn), v.object_id)
    //newColumn = $("<td class='col border-top'>").text();
    $(newRow).append($(newColumn));

    if (v.query_time == undefined ||
        v.query_time.length == 0) {
        newColumn = $("<td class='col border-top'>").append("Unprocessed");

    } else {
        newColumn = $("<td class='col border-top'>").text(v.query_time);
    }
    $(newRow).append($(newColumn));


    if (v.length == undefined ||
        v.length.length == 0) {
        newColumn = $("<td class='col border-top'>").append("Unprocessed");

    } else {
        newColumn = $("<td class='col border-top'>").text(v.length);
    }
    $(newRow).append($(newColumn));

    let newButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show")
    newColumn = $("<td class='col border-top'>").append($(newButton));

    if (v.data_truncated == undefined ||
        v.data_truncated.length == 0 ||
        v.data_truncated == '' ||
        v.data_truncated == ' ') {
        newColumn = $("<td class='col border-top'>").append("Unprocessed");
    } else {
        ((tempElement, newText) =>
            $(tempElement).on('click', () => {
                const elementParent = $(tempElement).parent();
                const tempHideButton = $("<button class='btn-TableButtonItem align-middle'>").text("Hide");
                const tempShowButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show");

                function elementShowText() {
                    $(tempHideButton).off('click');
                    $(elementParent).empty();
                    $(elementParent).text(newText);
                    $(elementParent).append("<br/>");
                    $(elementParent).append($(tempHideButton));
                    $(tempHideButton).on('click', () => elementHiddenShowButton());
                }

                function elementHiddenShowButton() {
                    $(tempShowButton).off('click');
                    $(elementParent).empty();
                    $(elementParent).append($(tempShowButton));
                    $(tempShowButton).on('click', () => elementShowText());
                }

                elementShowText();
            })
        )($(newButton), v.data_truncated);
    }
    $(newRow).append($(newColumn));

    if (v.code == undefined ||
        v.code.length == 0 ||
        v.code == '' ||
        v.code == ' ') {
        newColumn = $("<td class='col border-top'>").append("Unprocessed");
    } else {
        newColumn = $("<td class='col border-top'>").text(v.code);
    }
    $(newRow).append($(newColumn));

    newColumn = $("<td class='col border-top'>").text(v.time);
    $(newRow).append($(newColumn));

    if (v.proxy == undefined ||
        v.proxy.length == 0 ||
        v.proxy == '' ||
        v.proxy == ' ') {
        newColumn = $("<td class='col border-top'>").append("Auto");
    } else {
        newButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show")
        newColumn = $("<td class='col border-top'>").append($(newButton));
        ((tempElement, newText) =>
            $(tempElement).on('click', () => {
                const elementParent = $(tempElement).parent();
                const tempHideButton = $("<button class='btn-TableButtonItem align-middle'>").text("Hide");
                const tempShowButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show");

                function elementShowText() {
                    $(tempHideButton).off('click');
                    $(elementParent).empty();
                    $(elementParent).text(newText);
                    $(elementParent).append("<br/>");
                    $(elementParent).append($(tempHideButton));
                    $(tempHideButton).on('click', () => elementHiddenShowButton());
                }

                function elementHiddenShowButton() {
                    $(tempShowButton).off('click');
                    $(elementParent).empty();
                    $(elementParent).append($(tempShowButton));
                    $(tempShowButton).on('click', () => elementShowText());
                }

                elementShowText();
            })
        )($(newButton), v.proxy);
    }
    $(newRow).append($(newColumn));

    // newColumn = $("<td class='col border-top'>").text(v.proxy);
    // $(newRow).append($(newColumn));


    newButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show");
    newColumn = $("<td class='col border-top'>").append($(newButton));

    ((tempElement, newText) =>
        $(tempElement).on('click', () => {
            const elementParent = $(tempElement).parent();
            const tempHideButton = $("<button class='btn-TableButtonItem align-middle'>").text("Hide");
            const tempShowButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show");

            function elementShowText() {
                $(tempHideButton).off('click');
                $(elementParent).empty();
                $(elementParent).text(newText);
                $(elementParent).append("<br/>");
                $(elementParent).append($(tempHideButton));
                $(tempHideButton).on('click', () => elementHiddenShowButton());
            }

            function elementHiddenShowButton() {
                $(tempShowButton).off('click');
                $(elementParent).empty();
                $(elementParent).append($(tempShowButton));
                $(tempShowButton).on('click', () => elementShowText());
            }

            elementShowText();
        })
    )($(newButton), v.api);

    $(newRow).append($(newColumn));
    //newColumn = $("<td class='col border-top'>").text(v.api);
    //$(newRow).append($(newColumn));

    if (v.api_key == undefined ||
        v.api_key.length == 0 ||
        v.api_key == '' ||
        v.api_key == ' ') {
        newColumn = $("<td class='col border-top'>").append("Auto");
    } else {
        newButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show");
        newColumn = $("<td class='col border-top'>").append($(newButton));
        ((tempElement, newText) =>
            $(tempElement).on('click', () => {
                const elementParent = $(tempElement).parent();
                const tempHideButton = $("<button class='btn-TableButtonItem align-middle'>").text("Hide");
                const tempShowButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show");

                function elementShowText() {
                    $(tempHideButton).off('click');
                    $(elementParent).empty();
                    $(elementParent).text(newText);
                    $(elementParent).append("<br/>");
                    $(elementParent).append($(tempHideButton));
                    $(tempHideButton).on('click', () => elementHiddenShowButton());
                }

                function elementHiddenShowButton() {
                    $(tempShowButton).off('click');
                    $(elementParent).empty();
                    $(elementParent).append($(tempShowButton));
                    $(tempShowButton).on('click', () => elementShowText());
                }

                elementShowText();
            })
        )($(newButton), v.api_key);
    }
    $(newRow).append($(newColumn));

    //newColumn = $("<td class='col border-top'>").text(v.api_key);
    //$(newRow).append($(newColumn));

    newColumn = $("<td class='col border-top'>").text(v.url);
    $(newRow).append($(newColumn));

    newColumn = $("<td class='col border-top'>").text(v.endpoint_nice_name);
    $(newRow).append($(newColumn));

    if (v.input_json == undefined ||
        JSON.stringify(v.input_json).length == 0 ||
        JSON.stringify(v.input_json) == "{}") {
        newColumn = $("<td class='col border-top'>").append("None");
        $(newRow).append($(newColumn));

    } else {
        newButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show");
        newColumn = $("<td class='col border-top'>").append($(newButton));

        ((tempElement, newText) =>
            $(tempElement).on('click', () => {
                const elementParent = $(tempElement).parent();
                const tempHideButton = $("<button class='btn-TableButtonItem align-middle'>").text("Hide");
                const tempShowButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show");

                function elementShowText() {
                    $(tempHideButton).off('click');
                    $(elementParent).empty();
                    $(elementParent).text(JSON.stringify(newText));
                    $(elementParent).append("<br/>");
                    $(elementParent).append($(tempHideButton));
                    $(tempHideButton).on('click', () => elementHiddenShowButton());
                }

                function elementHiddenShowButton() {
                    $(tempShowButton).off('click');
                    $(elementParent).empty();
                    $(elementParent).append($(tempShowButton));
                    $(tempShowButton).on('click', () => elementShowText());
                }

                elementShowText();
            })
        )($(newButton), v.input_json);

        $(newRow).append($(newColumn));
    }

    // newColumn = $("<td class='col border-top'>").text(JSON.stringify(v.input_json));
    // $(newRow).append($(newColumn));

    return $(newRow);
}

/**
 * Deletes a Mongo Storage row and MongoDB Object ID from the server and then closes the window.
 * Modifies the DOM
 * @param {?number} mongoStorageId - Mongo Storage Row ID
 * @returns {void}
 */
async function confirmedMongoDelete(mongoStorageId) {
    if (mongoStorageId == undefined ||
        mongoStorageId < 0) {
        console.error("mongoStorageId invalid input for confirmedMongoDelete");
        return;
    }
    await sendMongoStorageDelete(mongoStorageId)
        .then(r => {
            if (r != undefined &&
                r.status == 200) {
                $("#adminResponseDataText").text("Delete Successful! You may close this page.");
                $("#bottomControlDash").empty();
                $("#bottomControlDash").append(`
                <button class="btn-linkAdmin btn-primary bg-primary
                text-light text-center justify-content-center mx-auto mb-5 placeholder-wave" type="button"
                onclick="window.close();">Close</button>`);
            } else {
                $("#adminResponseDataText").text("Request Failed. Try again or check logs.");
            }
        }).catch(e => {
            console.error(e);
            $("#adminResponseDataText").text("Request Failed. Might already be deleted. Try again or check logs.");
        })
}