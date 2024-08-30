const adminPath = '/admin';
const adminMongoScrapeStorage = '/admin_mongo_scrape_storage';
const adminMongoScrapeViewExtra = adminPath + '/view_scrape/';
const adminMongoScrapeConfirmDelete = adminPath + '/confirm_scrape_deletion/';

let apiRefreshing = false;
let currentPageNumber = 1;

/**
 * Continue loading data from REST when the page is loaded.
 * Adds Event Handlers to form change events.
 */
$(document).ready(() => {
    if (window.location.pathname.includes(adminMongoScrapeStorage)) {
        displayMongoScrapeStorage();
        //Pagination
        //Hook onto click
        const currentPageElements = $("li.page-item");

        $(currentPageElements).on("click", e => {
            if ($(e.target).closest("ul").attr("id") == "pagination-bottom") {
                if ($(e.target).closest('li').attr('data-page-number') != '1') {
                    hookPaginationControls(e, bottom = true);
                }

            } else {
                if ($(e.target).closest('li').attr('data-page-number') != '1') {
                    hookPaginationControls(e)
                }
            }
        });

        const foundInactiveItems = $('.btn-EndpointMenuFilterItem');
        if (foundInactiveItems == undefined)
            return;

        if (foundInactiveItems.length > 0)
            for (item of foundInactiveItems)
                $(item).on('click', event => setFilterToActive(event));

    } else if (window.location.pathname.includes(adminMongoScrapeViewExtra)) {
        displayMongoScrapeDocument();

    } else if (window.location.pathname.includes(adminMongoScrapeConfirmDelete)) {
        displayMongoScrapeDelete();
    }
});

/**
 * Sets an inactive Filter to active
 * Modifies the DOM
 * @param {?object} event - Click Event Target
 * @returns {void}
 */
function setFilterToActive(event) {
    // console.debug("set filter to active");
    if (event == undefined || 
        $(event.target) == undefined)
        return;

    const currentActiveItem = $(".btn-EndpointMenuFilterItemActive");
    if (currentActiveItem != undefined) {
        $(currentActiveItem).attr({ class: 'btn-EndpointMenuFilterItem bg-muted text-light' });
        $(currentActiveItem).on('click', newEvent => setFilterToActive(newEvent));
    }

    $(event.target).attr({
        class: 'btn-EndpointMenuFilterItemActive bg-muted text-light'
    });

    $(event.target).off('click');

    refreshMongoScrapeStorage();
}

/**
 * Function that is called when a page control item is clicked.
 * @param {object} e - Event
 * @param {?boolean} bottom - Scroll to bottom after load
 * @returns {void}
 */
function hookPaginationControls(
    e, 
    bottom = false) {
    const currentlyClickedPage = $(e.target).closest("li");
    const clickedPageNumber = $(currentlyClickedPage).attr('data-page-number');

    if (currentPageNumber == 1 &&
        clickedPageNumber == "-1") {
        return;
    }
    // console.debug("Clicked: " + 
    //     clickedPageNumber.toString());

    //Update page number, then update the DOM if page number is only over 3.
    switch (clickedPageNumber) {
        case "-1":
            if (currentPageNumber != 1)
                currentPageNumber--;
            break;

        case "+1":
            currentPageNumber++;
            break;

        default:
            if (clickedPageNumber == undefined) {
                console.error("Data attribute not found in pagination controls.")
                return;
            }
            currentPageNumber = +clickedPageNumber;
            break;
    }

    renumberPaginationControls();
    displayMongoScrapeStorage(bottom);
}


/**
 * Renumbers the pages and disables page controls based on currentPageNumber or pageMax.
 * Modifies the DOM
 * @param {?number} pageMax - If the maximum page number is reached, this will be filled.
 * @returns {void}
 */
function renumberPaginationControls(pageMax = -1) {
    const currentPageElementsTop = $("#pagination-top");
    const currentPageElementsBottom = $("#pagination-bottom");

    if (currentPageElementsTop == undefined ||
        currentPageElementsBottom == undefined)
        return;

    $(currentPageElementsTop).children().off('click');
    $(currentPageElementsBottom).children().off('click');

    $(currentPageElementsTop).empty();
    $(currentPageElementsBottom).empty();

    const newPreviousLITop = $("<li>")
        .attr({
            'class': 'page-item',
            'id': 'page-previous-top',
            'data-page-number': "-1"
        });

    const newPreviousLIBottom = $("<li>")
        .attr({
            'class': 'page-item',
            'id': 'page-previous-bottom',
            'data-page-number': "-1"
        });

    const newPreviousLinkTop = $("<a>");
    const newPreviousLinkBottom = $("<a>");
    if (currentPageNumber == 1) {
        $(newPreviousLinkTop).attr({
            'class': 'page-link',
            'disabled': 'disabled'
        })
            .css({
                'cursor': 'not-allowed'
            });

        $(newPreviousLinkBottom).attr({
            'class': 'page-link',
            'disabled': 'disabled'
        })
            .css({
                'cursor': 'not-allowed'
            });

    } else {
        $(newPreviousLinkTop).attr({
            'class': 'page-link'
        });

        $(newPreviousLinkBottom).attr({
            'class': 'page-link'
        });
    }
    $(newPreviousLinkTop).text('Previous');
    $(newPreviousLinkBottom).text('Previous');

    $(newPreviousLITop).append($(newPreviousLinkTop));
    $(newPreviousLIBottom).append($(newPreviousLinkBottom));
    $(currentPageElementsTop).append($(newPreviousLITop));
    $(currentPageElementsBottom).append($(newPreviousLIBottom));

    if (currentPageNumber != 1) {
        $(newPreviousLITop).on("click", e => hookPaginationControls(e));
        $(newPreviousLIBottom).on("click", e => hookPaginationControls(e, bottom = true));
    }

    for (let i = Math.max(1, (currentPageNumber - 2)); i < Math.max(6, (currentPageNumber + 3)); i++) {
        const newLITop = $("<li>");

        if (currentPageNumber != i) {
            $(newLITop).attr({
                'class': 'page-item',
                'data-page-number': i.toString()
            });

        } else {
            $(newLITop).attr({
                'class': 'page-item active',
                'data-page-number': i.toString()
            });
        }

        const newLinkTop = $("<a>");
        if (currentPageNumber == i ||
            (pageMax != -1 &&
                i > pageMax)) {
            $(newLinkTop).attr({
                'class': 'page-link',
                'disabled': 'disabled'
            })
                .css({
                    'cursor': 'not-allowed'
                });

        } else {
            $(newLinkTop).attr({
                'class': 'page-link'
            });
        }

        $(newLinkTop).text(i.toString());

        const newLIBottom = $(newLITop).clone(true);
        const newLinkBottom = $(newLinkTop).clone(true);

        $(newLITop).append($(newLinkTop));
        $(newLIBottom).append($(newLinkBottom));

        $(currentPageElementsTop).append($(newLITop));
        $(currentPageElementsBottom).append($(newLIBottom));

        if ((currentPageNumber != i) &&
            pageMax == -1 ||
            i < pageMax) {
            $(newLITop).on("click", e => hookPaginationControls(e));
            $(newLIBottom).on("click", e => hookPaginationControls(e, bottom = true));
        }
    }

    const newNextLITop = $("<li>")
        .attr({
            'class': 'page-item',
            'id': 'page-previous-top',
            'data-page-number': "+1"
        });

    const newNextLIBottom = $("<li>")
        .attr({
            'class': 'page-item',
            'id': 'page-previous-bottom',
            'data-page-number': "+1"
        });

    const newNextLinkTop = $("<a>");
    if (pageMax != -1 &&
        currentPageNumber == pageMax) {
        $(newNextLinkTop).attr({
            'class': 'page-link',
            'disabled': 'disabled'
        })
            .css({
                'cursor': 'not-allowed'
            });

    } else {
        $(newNextLinkTop).attr({
            'class': 'page-link'
        });
    }

    $(newNextLinkTop).text('Next');

    const newNextLinkBottom = $(newNextLinkTop).clone(true);

    $(newNextLITop).append($(newNextLinkTop));
    $(newNextLIBottom).append($(newNextLinkBottom));

    $(currentPageElementsTop).append($(newNextLITop));
    $(currentPageElementsBottom).append($(newNextLIBottom));

    if (pageMax == -1 ||
        currentPageNumber != pageMax) {
        $(newNextLinkTop).on("click", e => hookPaginationControls(e));
        $(newNextLinkBottom).on("click", e => hookPaginationControls(e, bottom = true));
    }
}

/**
 * Refreshes Mongo Scrape Storage List when the filter is changed.
 * Modifies the DOM
 * @returns {void}
 */
async function refreshMongoScrapeStorage() {
    if (apiRefreshing)
        return;

    apiRefreshing = true;

    const documentHolder = $("#mongoScrapeStorageBody");
    if ($(documentHolder) == undefined) {
        console.error("Could not find element holder to load in document data.");
        return;
    }

    $(documentHolder).empty();
    const currentActiveItem = $(".btn-EndpointMenuFilterItemActive");
    if (currentActiveItem == undefined) {
        console.error("Could not find active sort method to query scrape rows.");
        return;
    }
    // console.debug($(currentActiveItem).attr('data-type-id'));
    await getAPIMongoScrapeDocumentStorageList(
        cleanString($(currentActiveItem).attr('data-type-id')),
        currentPageNumber)
        .then(response => {
            $(documentHolder).empty();
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                console.warn("refreshMongoScrapeStorage Response did not return anything.");
                apiRefreshing = false;
                return;
            }

            response.data.forEach(v => {
                $(documentHolder)
                    .append(
                        generateMongoScrapeStorageRowTemplate(v)
                    );
            });

            apiRefreshing = false;
        });
}

/**
 * Continue loading contents of the Mongo Storage data from REST after the page is loaded.
 * Modifies the DOM.
 * @param {?boolean} bottom - true or false to scroll the window to the bottom after loading items.
 * @returns {void}
 */
async function displayMongoScrapeStorage(bottom = false) {
    const documentHolder = $("#mongoScrapeStorageBody");
    if ($(documentHolder) == undefined) {
        console.error("Could not find element holder to load in document data.");
        return;
    }

    $(documentHolder).empty();
    if (currentPageNumber == undefined) {
        retrieveAllMongoScrapeStorage();
        return;
    }

    const currentActiveItem = $(".btn-EndpointMenuFilterItemActive");
    if (currentActiveItem == undefined) {
        console.error("Could not find active sort method to query scrape rows.");
        return;
    }
    // console.debug($(currentActiveItem).attr('data-type-id'));
    await getAPIMongoScrapeDocumentStorageList(
        cleanString($(currentActiveItem).attr('data-type-id')),
        currentPageNumber)
        .then(response => {
            $(documentHolder).empty();

            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                //Page back-track here.
                if (currentPageNumber <= 1) {
                    console.error("getAPIMongoScrapeDocumentStorageList response did not return anything.");
                } else {
                    currentPageNumber--;
                    renumberPaginationControls(currentPageNumber);
                    displayMongoScrapeStorage(bottom = bottom);
                }
                return;
            }

            response.data.forEach(v => {
                $(documentHolder)
                    .append(
                        generateMongoScrapeStorageRowTemplate(v)
                    );

            });
        });

    if (bottom) {
        window.scrollTo(0, document.body.scrollHeight);
    }
}


/**
 * Failsafe load for retrieving all items from the MongoScrape storage, if page control elements cannot be found.
 * Modifies the DOM.
 * @returns {void}
 */
async function retrieveAllMongoScrapeStorage() {
    await getAPIMongoScrapeDocumentStorageAll()
        .then(response => {
            $(documentHolder).empty();
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                console.error("getAPIMongoScrapeDocumentStorageList response did not return anything.");
                return;
            }

            response.data.forEach(v => {
                $(documentHolder)
                    .append(
                        generateMongoScrapeStorageRowTemplate(v)
                    );

            });

        });
}

/**
 * Continue loading contents of the documentation data from REST after the page is loaded.
 * Modifies the DOM.
 * @returns {void}
 */
async function displayMongoScrapeDocument() {
    const documentHolder = $(".extraDocumentationBody");
    if ($(documentHolder) == undefined) {
        console.error("Could not find element holder to load in document data.");
        return;
    }

    const documentId = window.location.pathname.replace(adminMongoScrapeViewExtra, "");
    // console.debug(documentId);

    await getAPIMongoScrapeDocumentData(documentId)
        .then(response => {
            $(documentHolder).empty();
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                console.error("getAPIMongoScrapeDocumentData response did not return anything.");
                return;
            }

            $(documentHolder).text(response.data);
        });
}

/**
 * Continue loading contents of Mongo Scrape ID from REST in a text box that allows selection, after the page is loaded.
 * Allows the user to delete the row and Mongo DB Object ID
 * Modifies the DOM.
 * @returns {void}
 */
async function displayMongoScrapeDelete() {
    const documentHolder = $("#mongoDataRaw");
    if ($(documentHolder) == undefined) {
        console.error("Could not find element holder to load in document data.");
        return;
    }

    const documentId = window.location.pathname.replace(adminMongoScrapeConfirmDelete, "");
    await getAPIMongoScrapeDocumentData(documentId)
        .then(response => {
            $(documentHolder).empty();
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                console.error("getAPIMongoScrapeDocumentData response did not return anything.");
                return;
            }

            $(documentHolder).text(response.data);
        });
}

/**
 * Loads a mongo scrape window viewing the text response of a GET.
 * Modifies the DOM (by opening a pop-up window)
 * @param {number} mongo_scrape_id - ID of MongoScrapeStorage Row
 * @returns {void}
 */
function openScrapeMongo(mongo_scrape_id) {
    window.open(
        adminPath +
        "/view_scrape/" +
        mongo_scrape_id.toString(),

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
 * Loads a window confirming the deletion of a mongo scrape storage row.
 * Opens a pop-up window confirming the deletion of the MongoScrape storage row and MongoDB object.
 * Modifies the DOM (by opening a pop-up window)
 * @param {number} mongo_scrape_id - ID of MongoStorage Row
 * @returns {void}
 */
function openMongoScrapeDeletion(mongo_scrape_id) {
    window.open(
        adminPath +
        "/confirm_scrape_deletion/" +
        mongo_scrape_id.toString(),

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
 * Creates an element with data retrieved from the API Mongo Scrape Storage Filtered REST endpoint.
 * @param {Promise} v - Row data returned from server
 * @returns {void}
 */
function generateMongoScrapeStorageRowTemplate(v) {
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

    if (v.code != undefined) {
        const viewScrapeMongo = $('<a>')
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

        $(viewScrapeMongo).on('click', () => openScrapeMongo(v.id));
        $(viewButton).append($(viewScrapeMongo));
    }


    const confirmDeleteMongoScrapeMenuLink = $('<a>')
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
    $(confirmDeleteMongoScrapeMenuLink).on('click', () => openMongoScrapeDeletion(v.id));

    if (v.code != undefined) {
        $(viewButton).append('<div class="dropdown-divider">');
    }

    $(viewButton).append($(confirmDeleteMongoScrapeMenuLink));

    $(actionMenuControl).append($(actionMenuButton));
    $(actionMenuControl).append($(viewButton));

    $(newColumn).append($(actionMenuControl));
    $(newRow).append($(newColumn));

    if (v.query_time == undefined) {
        newColumn = $("<td class='col border-top'>").append("Unprocessed");
        $(newRow).append($(newColumn));

    } else {
        newColumn = $("<td class='col border-top'>").text(v.query_time);
        $(newRow).append($(newColumn));
    }

    if (v.length == undefined) {
        newColumn = $("<td class='col border-top'>").append("Unprocessed");
        $(newRow).append($(newColumn));

    } else {
        newColumn = $("<td class='col border-top'>").text(v.length);
        $(newRow).append($(newColumn));
    }

    if (v.data_truncated == undefined) {
        newColumn = $("<td class='col border-top'>").append("Unprocessed");
        $(newRow).append($(newColumn));

    } else {
        let newButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show")
        newColumn = $("<td class='col border-top'>").append($(newButton));

        ((tempElement, newText) =>
            $(tempElement).on('click', () => {
                const elementParent = $(tempElement).parent();
                const tempHideButton = $("<button class='btn-TableButtonItem align-middle'>").text("Hide")
                const tempShowButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show")

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
        $(newRow).append($(newColumn));
    }

    if (v.code == undefined) {
        newColumn = $("<td class='col border-top'>").append("Unprocessed");
        $(newRow).append($(newColumn));

    } else {
        newColumn = $("<td class='col border-top'>").text(v.code);
        $(newRow).append($(newColumn));
    }

    newColumn = $("<td class='col border-top'>").text(v.time);
    $(newRow).append($(newColumn));

    if (v.proxy == undefined) {
        newColumn = $("<td class='col border-top'>").append("Unprocessed");
        $(newRow).append($(newColumn));

    } else {
        let newButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show");
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

        $(newRow).append($(newColumn));
        // newColumn = $("<td class='col border-top'>").text(v.proxy);
        // $(newRow).append($(newColumn));
    }

    newColumn = $("<td class='col border-top'>").text(v.url);
    $(newRow).append($(newColumn));

    if (v.headers == undefined) {
        newColumn = $("<td class='col border-top'>").append("Unprocessed");
        $(newRow).append($(newColumn));

    } else {
        let newButton = $("<button class='btn-TableButtonItem align-middle'>").text("Show")
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
        )($(newButton), v.headers);
        $(newRow).append($(newColumn));
        // newColumn = $("<td class='col border-top'>").text(JSON.stringify(v.headers));
        // $(newRow).append($(newColumn));
    }

    return $(newRow);
}

/**
 * Deletes a Mongo Scrape Storage row and MongoDB Object ID from the server and then closes the window.
 * Modifies the DOM
 * @param {?string} mongoScrapeStorageId - Mongo Scrape Storage Row ID
 * @returns {void}
 */
async function confirmedMongoScrapeDelete(mongoScrapeStorageId) {
    // console.debug(mongoScrapeStorageId);
    if (mongoScrapeStorageId == undefined ||
        mongoScrapeStorageId < 0) {
        console.error("mongoScrapeStorageId invalid input for confirmedMongoScrapeDelete");
        return;
    }

    await sendMongoScrapeStorageDelete(mongoScrapeStorageId)
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