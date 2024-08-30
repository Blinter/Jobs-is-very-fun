const jobDashboardPath = '/jobs';
const jobViewExtra = '/view_job/';

let previousPageNumber = 0;
let currentPageNumber = 1;

let currentSearchTerm = "";
let previousSearchTerm = "";

let currentSearchLocation = "";
let previousSearchLocation = "";

let currentSearchDistance = 30;
let previousSearchDistance = 30;

let maxJobSearchPages = -1;

const scrapedDataElement = $('#rawScrapedData');
const scrapedDataLabelText = $('#scrapedDataLabelText');
const scrapedDataShowButton = $('#scrapedDataButton');

const jobsDashboard = $("#jobsDashboard");
const searchKeyword = $("#jobSearchKeyword");
const searchLocation = $("#jobSearchLocation");

const searchLocationDistance = $('#distanceMiles');
const searchLocationDistanceLabel = $('#distanceMilesLabel');

const loadingSpinnerElement = $("#loadingSpinner");

let searchTimer = null;
let refreshTimer = null;

let savedJobs = [];
let savedCompanies = [];

/**
 * Load jobs onto dashboard when page is fully loaded.
 * Add pagination controls and hook onto clicks
 * Hook onto search keyword text box
 * Start event timer to maintain dashboard responsiveness
 */
$(document).ready(() => {
    if (window.location.pathname.includes(jobDashboardPath)) {
        if (activeProfile) {
            (async () => await retrieveSavedJobs()
                .then(r => savedJobs = r.data)
            )();
        }

        // $(searchLocationDistance).show();
        // $(searchLocationDistanceLabel).show();
        displayJobs();

        //Pagination
        //Hook onto click
        const currentPageElements = $("li.page-item");

        if (currentPageElements != null) {
            $(currentPageElements).on("click", e => {
                if (loadingSpinnerElement) {
                    $(loadingSpinnerElement).show();
                }

                if ($(e.target).closest("ul").attr("id") === "pagination-bottom") {
                    if ($(e.target).closest('li').attr('data-page-number') !== '1') {
                        hookPaginationControls(e, true);
                    }

                } else {
                    if ($(e.target).closest('li').attr('data-page-number') !== '1') {
                        hookPaginationControls(e);
                    }
                }
            });
        }

        //Convert event hooks to a timer check instead
        // Update timer to only callback once at a time, 
        // waiting for previous execution to complete fully.

        if (searchTimer != null) {
            clearTimeout(searchTimer);
        }
        searchTimer = setTimeout(checkSearchChanged, 1000);

        //Filter Searches
        if (searchKeyword != null) {
            $(searchKeyword).on("keyup change", e => {
                currentSearchTerm = cleanString($(e.target).val());
                // console.debug(currentSearchTerm);
                if (previousSearchTerm == currentSearchTerm) {
                    if (loadingSpinnerElement != null) {
                        $(loadingSpinnerElement).hide();
                    }
                    return;
                }

                if (loadingSpinnerElement != null) {
                    $(loadingSpinnerElement).show();
                }
            });
        }

        //Filter Locations
        if (searchLocation != null) {
            $(searchLocation).on("keyup change", e => {
                currentSearchLocation = cleanString($(e.target).val());

                if (searchLocationDistance != null &&
                    searchLocationDistanceLabel != null) {
                    if (currentSearchLocation === "" ||
                        currentSearchLocation.length <= 1) {
                        $(searchLocationDistance).tooltip('dispose');
                        $(searchLocationDistance).hide();
                        $(searchLocationDistanceLabel).hide();

                    } else {
                        $(searchLocationDistance).show();
                        $(searchLocationDistanceLabel).show();
                    }
                }

                if (previousSearchLocation == currentSearchLocation) {
                    if (loadingSpinnerElement != null) {
                        $(loadingSpinnerElement).hide();
                    }
                    return;
                }

                if (loadingSpinnerElement != null) {
                    $(loadingSpinnerElement).show();
                }
            });
        }

        //Filter Distance
        if (searchLocationDistance != null) {
            $(searchLocationDistance).on("input click", e => {
                if (searchLocationDistance != null &&
                    $(searchLocationDistance).is(":hidden")) {
                    return;
                }

                if (loadingSpinnerElement != null) {
                    $(loadingSpinnerElement).show();
                }
                const currentDistanceString = $(searchLocationDistance).val();

                currentSearchDistance = +currentDistanceString;
                if (searchLocationDistance != null) {
                    $(searchLocationDistance)
                        .attr({ 'data-bs-title': 'Miles: ' + currentDistanceString })
                        .tooltip('dispose')
                        .tooltip('show');
                    if ($(searchLocationDistance).is(":visible")) {
                        $(searchLocationDistance).tooltip();
                    }
                }

                if (previousSearchDistance == currentSearchDistance) {
                    if (loadingSpinnerElement != null) {
                        $(loadingSpinnerElement).hide();
                    }
                    return;
                }
            });
        }

        if (searchLocationDistance != null &&
            $(searchLocationDistance).is(":visible")) {
            $(searchLocationDistance).tooltip();
        }

        // Check if page loaded with text already loaded in the form (User soft-refreshed page)
        if (searchKeyword != null &&
            $(searchKeyword).val().length != 0 &&
            searchLocation != null &&
            $(searchLocation).val().length != 0) {

            currentSearchTerm = cleanString($(searchKeyword).val());
            currentSearchLocation = cleanString($(searchLocation).val());

            if (currentSearchLocation === "" ||
                currentSearchLocation.length <= 1) {
                $(searchLocationDistance).tooltip('dispose');
                $(searchLocationDistance).hide();
                $(searchLocationDistanceLabel).hide();

            } else {
                if (searchLocationDistance != null &&
                    searchLocationDistanceLabel != null) {
                    $(searchLocationDistance).show();
                    $(searchLocationDistanceLabel).show();
                }

                //Now that location distance is displayed, set the value that had been set on the element.
                //Display the previously set values
                if (searchLocationDistance != null &&
                    $(searchLocationDistance).is(":visible")) {

                    if (currentSearchDistance != null &&
                        currentSearchDistance.toString().length != 0) {
                        $(searchLocationDistance).val(currentSearchDistance.toString());
                        resetDistanceTooltip();

                    } else if (previousSearchDistance != null &&
                        previousSearchDistance.toString().length != 0) {
                        $(searchLocationDistance).val(previousSearchDistance.toString());
                        resetDistanceTooltip();
                    }
                }
            }

            if (previousSearchTerm == currentSearchTerm &&
                previousSearchLocation == currentSearchLocation &&
                previousSearchDistance == currentSearchDistance) {
                if (loadingSpinnerElement != null) {
                    $(loadingSpinnerElement).hide();
                }
                return;
            }

            if (loadingSpinnerElement != null) {
                $(loadingSpinnerElement).show();
            }

        } else if ((searchKeyword == undefined ||
            $(searchKeyword).val().length == 0) &&
            searchLocation != null &&
            $(searchLocation).val().length != 0) {
            // Search keyword is not filled out but location keyword is.

            currentSearchLocation = cleanString($(searchLocation).val());
            if (searchLocationDistance != null &&
                searchLocationDistanceLabel != null) {
                $(searchLocationDistance).show();
                $(searchLocationDistanceLabel).show();
            }

            if (loadingSpinnerElement != null) {
                $(loadingSpinnerElement).show();
            }

        } else if ((searchLocation == undefined ||
            $(searchLocation).val().length == 0) &&
            searchKeyword != null &&
            $(searchKeyword).val().length != 0) {
            // Location keyword is not filled out but search keyword is.

            currentSearchDistance = +$(searchLocationDistance).val();

            if (searchLocationDistance != null &&
                $(searchLocationDistance).is(":visible")) {
                $(searchLocationDistance)
                    .attr({ 'data-bs-title': 'Miles: ' + $(searchLocationDistance).val() })
                    .tooltip('dispose')
                    .tooltip('show');
            }

            if (previousSearchDistance == currentSearchDistance) {
                if (loadingSpinnerElement != null) {
                    $(loadingSpinnerElement).hide();
                }
                return;
            }

            if (loadingSpinnerElement != null) {
                $(loadingSpinnerElement).show();
            }

        }

    } else if (window.location.pathname.includes(jobViewExtra)) {
        adjustInputWidth();

        if (scrapedDataElement != null) {
            $(scrapedDataElement).empty();
        }

        if ($('#jobApplyLink') != null) {
            $('#jobApplyLink').on('input', () => adjustInputWidth());
        }

        if ($('#jobApplyLink') != null) {
            $('#jobApplyLink').tooltip();
        }

        if ($('#scrapedDataLabelText') != null) {
            $('#scrapedDataLabelText').tooltip();
        }

        if ($('#scrapedDataButton') != null) {
            $('#scrapedDataButton').tooltip();
        }
    }
});

/**
 * Checks if a value in any of the search controls are changed
 * Hides the spinner if there was no change.
 * Modifies the DOM.
 * @returns {boolean}
 */
async function checkSearchChanged() {
    if (checkKeywordChange() |
        checkLocationChange() |
        checkDistanceChange()) {
        //Reset job search pages number for new change.
        maxJobSearchPages = -1;
        await displayJobs()
            .then(() => {
                if (searchTimer != null) {
                    clearTimeout(searchTimer);
                }
                searchTimer = setTimeout(checkSearchChanged, 1000);
            });

    } else {
        if (loadingSpinnerElement != null) {
            $(loadingSpinnerElement).hide();
        }
        if (searchTimer != null) {
            clearTimeout(searchTimer);
        }
        searchTimer = setTimeout(checkSearchChanged, 1000);
    }
}

/**
 * Reset the distance tooltip to show the correct value.
 * Modifies the DOM.
 * @returns {void}
 */
function resetDistanceTooltip() {
    if (searchLocationDistance == undefined ||
        $(searchLocationDistance).is(":hidden")) {
        return;
    }

    testSearchDistance = $(searchLocationDistance).val();
    if (testSearchDistance == undefined ||
        testSearchDistance.length == 0) {
        return;
    }

    currentSearchDistance = +$(searchLocationDistance).val();

    $(searchLocationDistance)
        .attr({ 'data-bs-title': 'Miles: ' + $(searchLocationDistance).val() })
        .tooltip('dispose')
        .tooltip('show');
}

/**
 * Checks currently loaded search keyword against the previously searched keyword
 * @returns {boolean}
 */
function checkKeywordChange() {
    if (previousSearchTerm == currentSearchTerm) {
        return false;
    }
    // console.debug("checkKeywordChange Change");
    return true;
}

/**
 * Checks currently loaded location keyword against the previously searched location keyword
 * If the location string is empty, hide the distance label and range.
 * Modifies the DOM.
 * @returns {boolean}
 */
function checkLocationChange() {
    if (currentSearchLocation === "") {
        currentSearchDistance = 30;
        if (searchLocationDistance != null) {
            $(searchLocationDistance).val(currentSearchDistance.toString());
            $(searchLocationDistance).tooltip('dispose');
            $(searchLocationDistance).hide();
        }
        if (searchLocationDistanceLabel != null) {
            $(searchLocationDistanceLabel).hide();
        }
    }

    if (previousSearchLocation == currentSearchLocation) {
        return false;
    }

    // console.debug("Location Change");
    return true;
}

/**
 * Checks currently loaded distance against the previously searched distance
 * @returns {boolean}
 */
function checkDistanceChange() {
    if (currentSearchDistance == previousSearchDistance)
        return false;

    // console.debug("Distance Change");
    return true;
}

/**
 * Updates the width of a job link using a hidden element.
 * Modifies the DOM.
 * @returns {void}
 */
function adjustInputWidth() {
    const input = document.getElementById('jobApplyLink');
    if (input == undefined)
        return;

    const hiddenText = document.getElementById('hiddenText');
    if (hiddenText == undefined)
        return;

    // Set the text of the hidden element to the input's value
    hiddenText.textContent = input.value;

    // Copy font properties from the input to the hidden element
    const inputStyle = window.getComputedStyle(input);
    hiddenText.style.fontFamily = inputStyle.fontFamily;
    hiddenText.style.fontSize = inputStyle.fontSize;
    hiddenText.style.fontWeight = inputStyle.fontWeight;
    hiddenText.style.fontStyle = inputStyle.fontStyle;
    hiddenText.style.letterSpacing = inputStyle.letterSpacing;

    // Measure the width of the text inside the hidden element
    const textWidth = hiddenText.offsetWidth;

    // Set the width of the input to the measured text width plus some padding
    //Adjust for extremely long links
    input.style.width = Math.min(768, (textWidth + 10)) + 'px';
}

/**
 * Shows a tooltip for the user when hovering a job link
 * Allows user to copy the text to the clipboard.
 * Modifies the user's clipboard.
 * @returns {void}
 */
function copyToClipboard() {
    const applyLinkElement = document.getElementById('jobApplyLink');
    if (applyLinkElement == undefined) {
        console.error('Element with id "jobApplyLink" not found.');
        return;
    }

    const jApplyLinkElement = $('#jobApplyLink');
    if (jApplyLinkElement == undefined) {
        console.error('Element with id "jobApplyLink" not found.');
        return;
    }

    // Ensure the element is an input or textarea
    if (applyLinkElement.tagName !== 'INPUT' &&
        applyLinkElement.tagName !== 'TEXTAREA') {
        console.error('Element with id "jobApplyLink" is not an input or textarea.');
        return;
    }

    applyLinkElement.select();
    applyLinkElement.setSelectionRange(0, 99999);

    navigator.clipboard.writeText(applyLinkElement.value)
        .catch(err => {
            console.error('Async: Could not copy text: ', err);
        });

    $(jApplyLinkElement)
        .attr({ 'data-bs-title': 'Copied to clipboard!' })
        .tooltip('dispose')
        .tooltip('show');

    setTimeout(() => {
        $(jApplyLinkElement)
            .attr('data-bs-title', 'Click to copy to clipboard')
            .tooltip('dispose')
            .tooltip();
    }, 3000);

}

/**
 * Toggles the raw scraped data that was scraped for the specified job,
 * when viewing the job details.
 * Modifies the DOM.
 * @param {object} event - Event passed when the 'Show' button for scraped data is clicked.
 * @returns {void}
 */
function toggleRawScrapedData(event) {
    if (scrapedDataElement == undefined)
        return;

    if ($(scrapedDataElement).text().length == 0 ||
        $(scrapedDataElement).text() == '' ||
        $(scrapedDataElement).text() == undefined) {
        $(event.target).text('Hide');
        $(scrapedDataElement).text(rawScrapedDataText);

    } else {
        $(scrapedDataElement).text('');
        $(event.target).text('Show');
    }
}

/**
 * Updates pagination controls when a page control item is clicked.
 * Modifies the DOM.
 * @param {object} e - Event passed when a page is clicked.
 * @param {?boolean} bottom - Scroll to bottom after load
 * @returns {void}
 */
function hookPaginationControls(e, bottom = false) {
    const currentlyClickedPage = $(e.target).closest("li");
    if (currentlyClickedPage == undefined) {
        return;
    }

    const clickedPageNumber = $(currentlyClickedPage).attr('data-page-number');

    // console.debug("Clicked: " +
    //     clickedPageNumber.toString());
    if (currentPageNumber == 1 &&
        clickedPageNumber == "-1") {
        return;
    }

    //Update page number, then update the DOM if page number is only over 3.
    //Also update DOM if the search term has changed.
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
    displayJobs(bottom);
}

/**
 * Re-numbers the pages and disables page controls based on currentPageNumber or pageMax.
 * Modifies the DOM
 * @param {?number} pageMax - If the maximum page number is reached, this will be filled. Otherwise defaults to -1.
 * @returns {void}
 */
function renumberPaginationControls(pageMax = -1) {
    // console.debug("Renumber called (Page Max: " + 
    //     pageMax.toString());
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
        //Disable the previous button if the first page is loaded.
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

        //The previous page is not loaded so don't disable.
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

    //Hook on click event for previous button if the first page is not selected.
    if (currentPageNumber != 1) {
        $(newPreviousLITop).on("click", e => {
            $(loadingSpinnerElement).show();
            hookPaginationControls(e);
        });

        $(newPreviousLIBottom).on("click", e => {
            $(loadingSpinnerElement).show();
            hookPaginationControls(e, true);
        });
    }

    // fix for searched terms max-pages
    if (maxJobSearchPages != -1 &&
        pageMax == -1 &&
        currentSearchTerm == '') {
        pageMax = maxJobSearchPages;

    } else if (maxJobSearchPages != -1) {
        pageMax = maxJobSearchPages;
    }

    //Set default in loop condition to ignore -1 value.
    let loopMaxPages = Math.max(6, currentPageNumber + 3);

    //Loop max Page Min Fix
    if (currentSearchTerm != '' &&
        maxJobSearchPages != -1) {
        loopMaxPages = Math.min(maxJobSearchPages + 1, loopMaxPages);
    }

    let loopMinPages = Math.max(1, (currentPageNumber - 2));
    //console.debug(loopMinPages.toString());

    if (maxJobSearchPages != -1 &&
        maxJobSearchPages < 5 &&
        currentSearchTerm == '') {
        loopMinPages = 1;
    }

    //Iterate and always display 5 page numbers, centering the currently selected page unless
    //  page 2 or below are selected.
    for (let i = loopMinPages; i < loopMaxPages; i++) {
        const newLITop = $("<li>");

        if (currentPageNumber != i) {
            $(newLITop).attr({
                'class': 'page-item',
                'data-page-number': i.toString()
            });

        } else {
            //Set active attribute if the current page number is the currently generated page-item.
            $(newLITop).attr({
                'class': 'page-item active',
                'data-page-number': i.toString()
            });
        }

        //Continue populating the page numbers with an <a> element.

        const newLinkTop = $("<a>");
        //Disable the element if the current page is the currently generated page,
        //  or if the pageMax is defined and the generated page is above the max page.
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

        //Hook and allow click if the generated page number is not the current page,
        //  or if the pageMax is defined and the generated page is below the page number.
        if (currentPageNumber != i &&
            pageMax == -1 ||
            i <= pageMax) {
            $(newLITop).on("click", e => {
                if ($(loadingSpinnerElement) != null) {
                    $(loadingSpinnerElement).show();
                }
                hookPaginationControls(e);
            });

            $(newLIBottom).on("click", e => {
                if ($(loadingSpinnerElement) != null) {
                    $(loadingSpinnerElement).show();
                }
                hookPaginationControls(e, true)
            });
        }
        if (currentPageNumber == i) {
            $(newLITop).off("click");
            $(newLIBottom).off("click");
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

    //Hook and allow click for the next button if current page number is not the page max
    //  and the page max is not defined.
    if (pageMax == -1 ||
        currentPageNumber != pageMax) {
        $(newNextLinkTop).on("click", e => {
            if (loadingSpinnerElement != null) {
                $(loadingSpinnerElement).show();
            }
            hookPaginationControls(e);
        });

        $(newNextLinkBottom).on("click", e => {
            if (loadingSpinnerElement != null) {
                $(loadingSpinnerElement).show();
            }
            hookPaginationControls(e, true);
        });
    }
}


/**
 * Load jobs data from REST
 * Modifies the DOM.
 * @param {?boolean} bottom - true or false to scroll the window to the bottom after loading items.
 * @returns {void}
 */
async function displayJobs(bottom = false) {
    if (jobsDashboard == undefined) {
        console.error("Could not find element to load in jobs data.");
        return;
    }

    //Do not query again if the search term is the same and the page number is the same as the last queried.
    if (
        //Search Terms
        previousSearchTerm != null &&
        previousSearchTerm == currentSearchTerm &&

        //Search Locations
        previousSearchLocation != null &&
        previousSearchLocation == currentSearchLocation &&

        //Search Location Distance
        previousSearchDistance != null &&
        previousSearchDistance == currentSearchDistance &&

        previousPageNumber == currentPageNumber) {
        // console.debug("Returning from previous " +
        //     "searchTerm=current " +
        //     "searchLocation=current " +
        //     "searchDistance=current " +
        //     "and previouspagenumber==current");

        return;
    }

    //Reset the page numbering when a new term or location is searched, defaulting to page 1.
    if (previousSearchTerm != currentSearchTerm ||
        previousSearchLocation != currentSearchLocation) {
        // console.debug("Search Term Check: " + previousSearchTerm + " != " + currentSearchTerm + "\n" +
        //     "Search Location Check: " + previousSearchLocation + " != " + previousSearchLocation);
        currentPageNumber = 1;
        previousSearchDistance = 30;
        // console.debug(previousSearchDistance + " = 30 - a");

        if (searchLocationDistance != null &&
            $(searchLocationDistance).is(":visible")) {
            $(searchLocationDistance).val('30');
            resetDistanceTooltip();
        }

        renumberPaginationControls();

    } else if (previousSearchDistance != currentSearchDistance) {
        currentPageNumber = 1;
        renumberPaginationControls();
    }

    //Check if Search terms are specified and default to a general query instead.
    if ((currentSearchTerm == undefined ||
        typeof currentSearchTerm != "string" ||
        currentSearchTerm.length < 1) &&
        (currentSearchLocation == undefined ||
            typeof currentSearchLocation != "string" ||
            currentSearchLocation.length < 1)) {

        await getJobs(currentPageNumber)
            .then(r => {
                populateJobs(r, bottom);
                if (loadingSpinnerElement != null) {
                    $(loadingSpinnerElement).hide();
                }
                if (r == undefined ||
                    r.data == undefined) {
                    return;
                }

                previousSearchTerm = "";
                previousSearchLocation = "";
                previousSearchDistance = 30;
                previousPageNumber = currentPageNumber;
            }).then(() => {
                if ($("#pagination-top") != null &&
                    $("#pagination-top").is(":hidden")) {
                    $("#pagination-top").show();
                }
                if ($("#pagination-bottom") != null &&
                    $("#pagination-bottom").is(":hidden")) {
                    $("#pagination-bottom").show();
                }
                //Fail-safe event to make sure current search has been successfully processed.
                if (refreshTimer != null) {
                    clearTimeout(refreshTimer);
                }

                refreshTimer = setTimeout(checkSearchQueryBase, 1000);
            });

    } else {
        if (currentSearchTerm != '') {
            // console.debug("Send Term: " + currentSearchTerm);
        }
        if (currentSearchLocation != '') {
            // console.debug("Send Location: " + currentSearchLocation);
        }
        await searchJobs(
            currentSearchTerm,
            currentSearchLocation,
            currentSearchDistance,
            currentPageNumber)
            .then(r => {
                populateJobs(r, bottom);
                // console.debug(previousSearchDistance + " = " + currentSearchDistance + "c");

                if (loadingSpinnerElement != null) {
                    $(loadingSpinnerElement).hide();
                }
                if (r == undefined ||
                    r.data == undefined) {
                    return;
                }

                previousSearchTerm = currentSearchTerm;
                previousSearchLocation = currentSearchLocation;
                previousSearchDistance = currentSearchDistance;

                previousPageNumber = currentPageNumber;

            }).then(() => {
                //Fail-safe event to make sure current search has been successfully processed.
                if (refreshTimer != null) {
                    clearTimeout(refreshTimer);
                }

                refreshTimer = setTimeout(checkSearchQueryFull, 1000);
            });
    }

    if (bottom) {
        window.scrollTo(0, document.body.scrollHeight);
    }
}


/**
 * Checks previously sent query against server's latest response, after it has been completed.
 * Modifies the DOM.
 * @returns {void}
 */
async function checkSearchQueryBase() {
    await retrievePreviousSearchJob()
        .then(r => {
            if (r == undefined ||
                r.data == undefined) {
                return;
            }

            if (r.data.page_number != null &&
                previousPageNumber != cleanString(r.data.page_number)) {
                // console.debug("Incorrect Page: [" +
                //     previousPageNumber.toString() + "]!=[" +
                //     cleanString(r.data.page_number).toString() + "]");
                previousPageNumber = cleanString(r.data.page_number);
            }
        });
}

/**
 * Checks previously sent query against server's latest response, after it has been completed.
 * Modifies the DOM.
 * @returns {void}
 */
async function checkSearchQueryFull() {
    await retrievePreviousSearchJob()
        .then(r => {
            if (r == undefined ||
                r.data == undefined) {
                return;
            }

            if (r.data.page_number != null &&
                previousPageNumber != cleanString(r.data.page_number)) {
                if (loadingSpinnerElement != null) {
                    $(loadingSpinnerElement).show();
                }
                // console.debug("Incorrect Page: [" +
                //     previousPageNumber.toString() + "]!=[" +
                //     cleanString(r.data.page_number).toString() + "]");
                previousPageNumber = cleanString(r.data.page_number);
            }

            if (r.data.search != null &&
                previousSearchTerm != cleanString(r.data.search)) {
                if (loadingSpinnerElement != null) {
                    $(loadingSpinnerElement).show();
                }
                // console.debug("Incorrect Term: [" +
                //     previousSearchTerm.toString() + "]!=[" +
                //     cleanString(r.data.search).toString() + "]");
                previousSearchTerm = cleanString(r.data.search);
            }

            if (r.data.location != null &&
                previousSearchLocation != cleanString(r.data.location)) {
                if (loadingSpinnerElement != null) {
                    $(loadingSpinnerElement).show();
                }
                // console.debug("Incorrect Location: [" +
                //     previousSearchLocation.toString() + "]!=[" +
                //     cleanString(r.data.location).toString() + "]");
                previousSearchLocation = cleanString(r.data.location);
            }

            if (r.data.distance != null &&
                cleanString(r.data.distance) != null &&
                previousSearchDistance != cleanString(r.data.distance)) {
                if (loadingSpinnerElement != null) {
                    $(loadingSpinnerElement).show();
                }

                // console.debug("Incorrect Distance: [" +
                //     previousSearchDistance.toString() + "]!=[" +
                //     cleanString(r.data.distance).toString() + "]");

                previousSearchDistance = cleanString(r.data.distance);
            }
        });
}


/**
 * Populate data received from REST endpoints.
 * Modifies the DOM.
 * @param {Promise} response - Response received from server
 * @param {?boolean} bottom - true or false to scroll to bottom after load
 * @returns {void}
 */
function populateJobs(
    response,
    bottom = false) {
    if ($(jobsDashboard) == undefined) {
        console.error("Could not find element to load in jobs data.");
        return;
    }

    $(jobsDashboard).empty();
    if (response == undefined ||
        response.data == undefined ||
        response.data.length == 0) {
        //Page back-track here.
        //If there's no results from the server, subtract the page number by 1 and redisplay for that page.
        if (currentPageNumber <= 1) {
            // console.log("No result found!");
            if (jobsDashboard != null) {
                $(jobsDashboard).append("No results!");
            }
            // console.warn("displayJobsDefault response did not return anything.");

        } else {
            if (loadingSpinnerElement != null) {
                $(loadingSpinnerElement).show();
            }
            previousPageNumber = currentPageNumber;
            currentPageNumber--;
            //track max pages (usually for a search term)
            maxJobSearchPages = currentPageNumber;

            displayJobs(bottom);
            renumberPaginationControls(currentPageNumber);
        }

        return;
    }
    response.data.forEach(v => {
        $(jobsDashboard).append(generateJobRowTemplate2(v));
    });

    if ($("#pagination-top") != null &&
        $("#pagination-top").is(":hidden")) {
        $("#pagination-top").show();
    }
    if ($("#pagination-bottom") != null &&
        $("#pagination-bottom").is(":hidden")) {
        $("#pagination-bottom").show();
    }
}

/**
 * Opens a popup from a click event and retrieves the 'data-id' of the element as the path parameter
 * when user clicks view for a job.
 * Modifies the DOM (by opening a pop-up.)
 * @param {object} event - Event when user clicks on the 'view' button.
 * @returns {void}
 */
function viewJob(event) {
    event.preventDefault();
    window.open(
        "/view_job/" +
        cleanHTMLString($(event.target).attr('data-id')).toString(),

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
 * Opens a popup from a click event and retrieves the 'data-id' of the element as the path parameter
 * when viewing a company.
 * Modifies the DOM (by opening a pop-up.)
 * @param {object} event - Event when user clicks on the 'view' button.
 * @returns {void}
 */
function viewCompany(event) {
    event.preventDefault();
    window.open(
        "/view_company/" +
        cleanHTMLString($(event.target).attr("data-id")).toString(),

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
 * Creates an element with row data retrieved from the Get Jobs REST endpoint.
 * Maintains proper gutter.
 * @returns {Promise} v - Response data returned from a job query
 * @returns {string}
 */
function generateJobRowTemplate2(v) {
    let returnHTML = `
    <div class="userJobListLink figure rounded bg-dark mb-2 px-lg-1 px-xl-2 px-xxl-3 py-1 py-lg-2">
        <span
            style="font-size:17px;">${v.name}</span>
        <br />`;

    if (v.company != null &&
        v.company != '') {
        returnHTML += `<span class="fluidLongTextFlex text-primary"
            style="font-size:15px;">${v.company}</span>
        <br />`;
    }

    if (v.location != null &&
        v.location != '') {
        returnHTML += `<span class="fluidLongTextFlex text-warning"
                style="font-size:14px">${v.location}</span>
            <br />`;
    }

    if (v.job_type != null &&
        v.job_type != '') {
        returnHTML += `<span class="fluidLongTextFlex text-info"
                style="font-size:14px">${v.job_type}</span>
            <br />`;
    }

    if (v.description != null &&
        v.description != "No Description" &&
        v.description != "") {
        returnHTML += `<hr class="mx-5" style="color:white;" />
            <span class="fluidUserLongTextFlex"
                style="font-size:15px;">${v.description}</span>
            <br />
            <hr class="mx-5" style="color:white;" />`;

    } else {
        returnHTML += `<hr class="smallestDivider mx-auto" style="color:white;" />`;
    }

    if (v.salary_currency != null &&
        v.salary_currency != "") {
        let salary = v.salary_currency.toString();

        if (v.max_salary != 0 &&
            v.min_salary != 0) {
            salary = "~" +
                salary +
                (Math.floor(v.max_salary + v.min_salary) / 2).toLocaleString();

        } else if (v.min_salary != 0 &&
            v.max_salary == 0) {
            salary +=
                v.min_salary.toLocaleString() +
                "+";

        } else {
            salary = "up to " +
                salary +
                v.max_salary.toLocaleString();
        }

        if (salary != "0") {
            returnHTML += `
            <span class="text-info"
            style="font-size:15px;font-weight: bolder;">Salary:</span><span class="fluidLongTextFlex"
                style="font-size:15px;"> ${salary}</span>
            <br />
            <hr class="mx-5" style="color:white;" />`;
        }
    }

    returnHTML += `
    <button data-action="viewJob" 
            class="btn-linkUserMini rounded bg-primary" 
            data-id="${v.id}"
            onclick="viewJob(event);">View
    </button>
        `;

    if (!savedJobs.includes(v.id)) {
        returnHTML += `
    <button data-action="toggleJobDash" 
            class="btn-linkUserMini rounded bg-success" 
            data-id="${v.id}"
            onclick="toggleJob(event);">Save</button>`;
    } else {
        returnHTML += `
    <button data-action="toggleJobDash" 
            class="btn-linkUserMini-longer rounded bg-danger"
            data-id="${v.id}"
            onclick="toggleJob(event);">Un-save</button>`;
    }

    return returnHTML + `<br />
        <span class="fluidUserLongTextFlex text-info">${v.posted_time_utc}</span><br />
        <span class="fluidUserLongTextFlex text-success">${v.api_source}</span>
    </div>`;
}