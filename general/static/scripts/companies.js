const companyDashboardPath = '/companies';
const companyViewExtra = '/view_company/';

let previousPageNumber = 0;
let currentPageNumber = 1;

let currentSearchTerm = "";
let previousSearchTerm = "";

let currentSearchLocation = "";
let previousSearchLocation = "";

let currentSearchDistance = 30;
let previousSearchDistance = 30;

let companyMaxJobPages = -1;
let companyMaxJobSearchPages = -1;

let companyListedJobCountElement = $("#listedJobCount");

const scrapedDataElement = $('#rawScrapedData');
const companiesDashboard = $("#companiesDashboard");
const companyWebsiteInput = $("#companyWebsite");
const companyMaxPagesCount = $("#maxPagesCount");
const companyShowJobsButton = $("#showCompanyJobs");
const loadCompanyJobsElement = $("#loadCompanyJobs");
const companyJobsCardElement = $(".userProfilesListLink");

const companySearchKeyword = $("#companySearchKeyword");

let searchTimer = null;
let refreshTimer = null;

let savedJobs = [];
let savedCompanies = [];

/**
 * Load companies when page is fully loaded.
 * Add pagination controls and hook onto clicks
 * Hook onto search keyword text box
 * Start event timer to maintain dashboard responsiveness
 */
$(document).ready(() => {
    //IIFE to call an async function and set the savedCompanies array
    (async () => await retrieveSavedCompanies()
        .then(r => savedCompanies = r.data)
    )();

    if (window.location.pathname.includes(companyDashboardPath)) {
        if ($("#loadingSpinner") != undefined) {
            $("#loadingSpinner").show();
        }

        displayCompanies();

        //Pagination
        //Hook onto click
        const currentPageElements = $("li.page-item");

        $(currentPageElements).on("click", e => {
            // console.log("Hook Click1");
            if ($("#loadingSpinner") != undefined) {
                $("#loadingSpinner").show();
            }

            if ($(e.target).closest("ul").attr("id") == "pagination-bottom") {
                if ($(e.target).closest('li').attr('data-page-number') != '1') {
                    hookPaginationControls(e, true);
                }

            } else {
                if ($(e.target).closest('li').attr('data-page-number') != '1') {
                    hookPaginationControls(e);
                }
            }
        });

        //Convert event hooks to a timer check instead
        searchTimer = setTimeout(checkCompanySearchChanged, 1000);

        //Filter Searches
        if (companySearchKeyword != undefined) {
            $(companySearchKeyword).on("keyup change", e => {
                currentSearchTerm = cleanString($(e.target).val());
                // console.debug(currentSearchTerm);
                if (previousSearchTerm == currentSearchTerm) {
                    if ($("#loadingSpinner") != undefined) {
                        $("#loadingSpinner").hide();
                    }
                    return;
                }

                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").show();
                }
            });
        }

        if (companySearchKeyword != undefined ||
            $(companySearchKeyword).val().length != 0) {
            currentSearchTerm = cleanString($(companySearchKeyword).val());

            if ($("#loadingSpinner") != undefined) {
                $("#loadingSpinner").show();
            }
        }

        if (previousSearchTerm == currentSearchTerm) {
            if ($("#loadingSpinner") != undefined) {
                $("#loadingSpinner").hide();
            }
            return;
        }

        if ($("#loadingSpinner") != undefined) {
            $("#loadingSpinner").show();
        }

    } else if (window.location.pathname.includes(companyViewExtra)) {
        //IIFE to call an async function and set the savedJobs array
        //Job dashboard integration within view Company page
        (async () => await retrieveSavedJobs()
            .then(r => savedJobs = r.data)
        )();

        //Enable tooltips for copying website link.
        if (companyWebsiteInput != undefined) {
            $(companyWebsiteInput).on('input', () => adjustInputWidth());
            $(companyWebsiteInput).tooltip();
        }

        //Set Max Pages provided by the server.
        if (companyMaxPagesCount != undefined) {
            companyMaxJobPages = cleanHTMLString($(companyMaxPagesCount).attr("data-max-pages"));
        }

        //Pagination for jobs:
        //Hook onto click to show jobs and pagination controls        
        //Fix auto-formatting for show jobs button
        if (companyShowJobsButton != undefined &&
            loadCompanyJobsElement != undefined) {
            $(companyShowJobsButton).html('Show Jobs');

            $(companyShowJobsButton).on('click', () => {
                if ($(companyShowJobsButton).text() == "Show Jobs") {

                    if ($("#loadingSpinner") != undefined) {
                        $("#loadingSpinner").show();
                    }

                    $(companyShowJobsButton).text('Hide Jobs');
                    $(companyShowJobsButton).attr({ 'class': 'btnAction rounded bg-danger text-white px-4' });

                    generateCompanyJobsDashboard(true);

                    $("html").animate({
                        scrollTop:
                            $(companyShowJobsButton).offset().top +
                            $(companyShowJobsButton).height() +
                            25
                    }, 1000);
                    // Set focus on the element
                    //$(e.target).focus();

                } else {
                    clearTimeout(searchTimer);

                    $(loadCompanyJobsElement).empty();

                    $("#searchControlsShowJobs").remove();
                    $("#pagination-top").remove();
                    $("#pagination-bottom").remove();
                    $("#placeholderShowJobs").remove();

                    $(companyShowJobsButton).text('Show Jobs');
                    $(companyShowJobsButton).attr({ 'class': 'btnAction rounded bg-primary text-white px-4' });
                }
            });

        }
    }
});

/**
 * Checks if a value in any of the search controls are changed
 * Hides the spinner if there was no change.
 * Modifies the DOM.
 * @returns {boolean}
 */
async function checkCompanySearchChanged() {
    if (checkKeywordChange()) {
        //Reset company search pages number for new change.
        //companyMaxJobSearchPages = -1;
        companyMaxJobPages = -1;
        await displayCompanies().then(() => {
            if (searchTimer != undefined) {
                clearTimeout(searchTimer);
            }
            searchTimer = setTimeout(checkCompanySearchChanged, 1000);
        });

    } else {
        if ($("#loadingSpinner") != undefined) {
            $("#loadingSpinner").hide();
        }
        if (searchTimer != undefined) {
            clearTimeout(searchTimer);
        }
        searchTimer = setTimeout(checkCompanySearchChanged, 1000);
    }
}

/**
 * Checks if a value in any of the search controls are changed
 * Hides the spinner if there was no change.
 * Modifies the DOM.
 * @returns {boolean}
 */
async function checkCompanySearchJobsChanged(companyId) {
    if (checkKeywordChange() |
        checkLocationChange() |
        checkDistanceChange()) {
        //Reset company search pages number for new change.
        companyMaxJobSearchPages = -1;
        //companyMaxJobPages = -1;
        await displayCompanyJobs(companyId, false, false)
            .then(() => {
                if (searchTimer != undefined) {
                    clearTimeout(searchTimer);
                }
                searchTimer = setTimeout(() => {
                    checkCompanySearchJobsChanged(companyId);
                }, 1000);
            });

    } else {
        if ($("#loadingSpinner") != undefined) {
            $("#loadingSpinner").hide();
        }
        if (searchTimer != undefined) {
            clearTimeout(searchTimer);
        }
        searchTimer = setTimeout(() => {
            checkCompanySearchJobsChanged(companyId);
        }, 1000);
    }
}

/**
 * Reset the distance tooltip to show the correct value.
 * Modifies the DOM.
 * @returns {void}
 */
function resetDistanceTooltip() {
    const searchLocationDistance = $('#distanceMiles');

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
 * Locks control buttons
 * @returns {void}
 */
function lockFormControls() {
    $("#companySearchKeyword").prop('disabled', true);
    $(".page-link").prop('disabled', true);
    $(".page-item").prop('disabled', true);
}
/**
 * Unlocks control buttons
 * @returns {void}
 */
function unlockFormControls() {
    $("#companySearchKeyword").prop('disabled', false);
    $(".page-link").prop('disabled', false);
    $(".page-item").prop('disabled', false);
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
    if (currentSearchLocation == "") {
        if ($('#distanceMiles') != undefined) {
            $('#distanceMiles').hide();
        }
        if ($('#distanceMilesLabel') != undefined) {
            $('#distanceMilesLabel').hide();
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
    if (currentSearchDistance == previousSearchDistance) {
        return false;
    }

    // console.debug("Distance Change");
    return true;
}

/**
 * Updates the width of a job link using a hidden element.
 * Modifies the DOM.
 * @returns {void}
 */
function adjustInputWidth() {
    const input = document.getElementById('companyWebsite');
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
    // Adjust for extremely long links
    input.style.width = Math.min(768, (textWidth + 10)) + 'px';
}

/**
 * Shows a tooltip for the user when hovering a company link
 * Allows user to copy the text to the clipboard.
 * Modifies the user's clipboard.
 * @returns {void}
 */
function copyToClipboard() {
    const companyWebsiteElement = document.getElementById('companyWebsite');
    if (companyWebsiteElement == undefined) {
        console.error('Element with id "companyWebsite" not found.');
        return;
    }

    const jCompanyWebsiteElement = $('#companyWebsite');
    if (jCompanyWebsiteElement == undefined) {
        console.error('Element with id "companyWebsite" not found.');
        return;
    }

    // Ensure the element is an input or textarea
    if (companyWebsiteElement.tagName !== 'INPUT' &&
        companyWebsiteElement.tagName !== 'TEXTAREA') {
        console.error('Element with id "companyWebsite" is not an input or textarea.');
        return;
    }

    companyWebsiteElement.select();
    companyWebsiteElement.setSelectionRange(0, 99999);

    navigator.clipboard.writeText(companyWebsiteElement.value)
        .catch(function (err) {
            console.error('Async: Could not copy text: ', err);
        });
    $(jCompanyWebsiteElement)
        .attr({ 'data-bs-title': 'Copied to clipboard!' })
        .tooltip('dispose')
        .tooltip('show');

    setTimeout(function () {
        $(jCompanyWebsiteElement)
            .attr('data-bs-title', 'Click to copy to clipboard')
            .tooltip('dispose')
            .tooltip();
    }, 3000);

}

/**
 * Updates pagination controls when a page control item is clicked.
 * Modifies the DOM.
 * @param {object} e - Event
 * @param {?boolean} bottom - Scroll to bottom after load
 * @returns {void}
 */
function hookPaginationControls(e, bottom = false) {
    // console.debug("Clicked");
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

    if (window.location.pathname.includes(companyViewExtra)) {
        displayCompanyJobs(
            cleanHTMLString($(companyShowJobsButton).attr('data-company-id')),
            bottom);

    } else {
        displayCompanies(bottom);
    }
}

/**
 * Re-numbers the pages and disables page controls based on currentPageNumber or pageMax.
 * Function is compatible with both view company and company board pages.
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
            // console.log("Hook Click2");
            $("#loadingSpinner").show();
            hookPaginationControls(e);
        });

        $(newPreviousLIBottom).on("click", e => {
            // console.log("Hook Click3");
            $("#loadingSpinner").show();
            hookPaginationControls(e, true);
        });
    }

    // console.debug(
    //     "companyMaxJobPages: " +
    //     companyMaxJobPages.toString() +
    //     " companyMaxJobSearchPages: " +
    //     companyMaxJobSearchPages.toString() +
    //     " pageMax: " +
    //     pageMax.toString()
    // )

    //Interchange between company jobs and companies pagination
    // fix for searched terms
    if (companyMaxJobPages != -1 &&
        pageMax == -1 &&
        currentSearchTerm == '' &&
        currentSearchLocation == '') {
        pageMax = companyMaxJobPages;

    } else if (companyMaxJobSearchPages != -1) {
        pageMax = companyMaxJobSearchPages;
    }

    //Set default in loop condition to ignore -1 value.
    let loopMaxPages = Math.max(6, (currentPageNumber + 3));

    //Loop max Page Min Fix
    if (companyMaxJobPages != -1 &&
        currentSearchTerm == '' &&
        currentSearchLocation == '') {
        loopMaxPages = Math.min(companyMaxJobPages + 1, loopMaxPages);
        // console.log("33loopMaxPages: " + loopMaxPages.toString());

    } else if ((currentSearchTerm != '' ||
        currentSearchLocation != '') &&
        companyMaxJobSearchPages != -1) {
        loopMaxPages = Math.min(companyMaxJobSearchPages + 1, loopMaxPages);
        // console.log("22loopMaxPages: " + loopMaxPages.toString());
    }

    let loopMinPages = Math.max(1, (currentPageNumber - 2));
    // console.debug(loopMinPages.toString());

    //if companyMaxJobPages is set and is less than 5, page number element count will decrease.
    if (companyMaxJobPages > 1 &&
        companyMaxJobPages < 5 &&
        currentSearchTerm == '' &&
        currentSearchLocation == '') {
        loopMinPages = 1;
    }
    // console.debug(loopMinPages.toString());

    //Iterate and always display 5 page numbers, centering the currently selected page unless
    //  page 2 or below are selected.

    // console.log("loopMaxPages: " + loopMaxPages.toString());
    if (loopMaxPages == 2) {
        if (currentPageElementsTop != undefined &&
            $(currentPageElementsTop).is(":visible")) {
            $(currentPageElementsTop).hide();
        }
        if (currentPageElementsBottom != undefined &&
            $(currentPageElementsBottom).is(":visible")) {
            $(currentPageElementsBottom).hide();
        }
        return;
    } else {
        if (currentPageElementsTop != undefined &&
            $(currentPageElementsTop).is(":hidden")) {
            $(currentPageElementsTop).show();
        }
        if ($(currentPageElementsBottom) != undefined &&
            $(currentPageElementsBottom).is(":hidden")) {
            $(currentPageElementsBottom).show();
        }
    }
    for (let i = loopMinPages; i < loopMaxPages; i++) {
        const newLITop = $("<li>");

        if (currentPageNumber != i) {
            $(newLITop)
                .attr({
                    'class': 'page-item',
                    'data-page-number': i.toString()
                });

        } else {
            //Set active attribute if the current page number is the currently generated page-item.
            $(newLITop)
                .attr({
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
            $(newLinkTop)
                .attr({
                    'class': 'page-link',
                    'disabled': 'disabled'
                })
                .css({
                    'cursor': 'not-allowed'
                });

        } else {
            $(newLinkTop)
                .attr({
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
        // console.log("Hook here");
        if (currentPageNumber != i &&
            (pageMax == -1 ||
                i <= pageMax)) {
            $(newLITop).on("click", e => {
                // console.log("Hook Click4");
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").show();
                }
                hookPaginationControls(e);
            });

            $(newLIBottom).on("click", e => {
                // console.log("Hook Click5");
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").show();
                }
                hookPaginationControls(e, true);
            });
        }
    }

    const newNextLITop = $("<li>")
        .attr({
            'class': 'page-item',
            'id': 'page-next-top',
            'data-page-number': "+1"
        });

    const newNextLIBottom = $("<li>")
        .attr({
            'class': 'page-item',
            'id': 'page-next-bottom',
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
            // console.log("Hook Click6");
            if ($("#loadingSpinner") != undefined) {
                $("#loadingSpinner").show();
            }
            hookPaginationControls(e);
        });
        $(newNextLinkBottom).on("click", e => {
            // console.log("Hook Click7");
            if ($("#loadingSpinner") != undefined) {
                $("#loadingSpinner").show();
            }
            hookPaginationControls(e, true);
        });
    }
}

/**
 * Generate Company Jobs Dashboard
 * @param {?boolean} freshGenerate - True if it is a fresh generation of job controls, and force refresh.
 * @returns {void}
 */
function generateCompanyJobsDashboard(freshGenerate = false) {
    if (companyMaxPagesCount == undefined)
        return;

    //Set companyMaxJobPages to maximum pages set by server.
    const maxPages = cleanHTMLString($(companyMaxPagesCount).attr("data-max-pages"));

    if (maxPages == undefined ||
        maxPages == "")
        return;

    if (maxPages != undefined)
        companyMaxJobPages = +maxPages;

    const companyId = cleanHTMLString($(companyShowJobsButton).attr('data-company-id'));

    if (companyId == undefined ||
        companyId == "")
        return;

    //Check for listedJobCount and generate search controls if there is more than one job listing.
    if (companyListedJobCountElement != undefined &&
        +cleanHTMLString($(companyListedJobCountElement).text()) > 1) {
        $(generatePlaceHolder() + generateSearchControls())
            .insertBefore($(loadCompanyJobsElement));

    } else {
        $(generatePlaceHolder()).insertBefore($(loadCompanyJobsElement));
    }

    //Check if pagination controls need to be displayed.
    //Bottom pagination will be chained after displayCompanyJobs.
    // then append page controls footer later after displayCompanyJobs function.
    if (companyMaxJobSearchPages > 1 ||
        (companyMaxJobSearchPages == -1 &&
            companyMaxJobPages > 1)) {

        $(generateCompanyJobsPaginationControls("Top", Math.max(companyMaxJobPages, companyMaxJobSearchPages)))
            .insertBefore($(loadCompanyJobsElement));
    }

    //Convert event hooks to a timer check instead
    searchTimer = setTimeout(() => {
        checkCompanySearchJobsChanged(companyId);
    }, 1000);

    //Filter Searches
    const searchKeyword = $("#jobSearchKeyword");
    if (searchKeyword != undefined) {
        $(searchKeyword).on("keyup change", e => {
            currentSearchTerm = cleanString($(e.target).val());
            // console.debug(currentSearchTerm);
            if (previousSearchTerm == currentSearchTerm) {
                $("#loadingSpinner").hide();
                return;
            }

            $("#loadingSpinner").show();
        });
    }

    //Filter Locations
    const searchLocation = $("#jobSearchLocation");
    const searchLocationDistance = $('#distanceMiles');

    const searchLocationDistanceLabel = $('#distanceMilesLabel');
    if (searchLocation != undefined) {
        $(searchLocation).on("keyup change", e => {
            currentSearchLocation = cleanString($(e.target).val());

            if (searchLocationDistance != undefined &&
                searchLocationDistanceLabel != undefined) {
                if (currentSearchLocation == "" ||
                    currentSearchLocation.length <= 1) {
                    $(searchLocationDistance).hide();
                    $(searchLocationDistanceLabel).hide();

                } else {
                    $(searchLocationDistance).show();
                    $(searchLocationDistanceLabel).show();
                }
            }

            if (previousSearchTerm == currentSearchLocation) {
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").hide();
                }
                return;
            }
            if ($("#loadingSpinner") != undefined) {
                $("#loadingSpinner").show();
            }
        });
    }

    //Filter Distance
    if (searchLocationDistance != undefined) {
        $(searchLocationDistance).on("input click", e => {
            if ($(searchLocationDistance) != undefined &&
                $(searchLocationDistance).is(":hidden")) {
                return;
            }

            if ($("#loadingSpinner") != undefined) {
                $("#loadingSpinner").show();
            }
            const currentDistanceString = $(searchLocationDistance).val();

            currentSearchDistance = +currentDistanceString;
            if (searchLocationDistance != undefined) {
                $(searchLocationDistance)
                    .attr({ 'data-bs-title': 'Miles: ' + currentDistanceString })
                    .tooltip('dispose')
                    .tooltip('show');
                if ($(searchLocationDistance).is(":visible")) {
                    $(searchLocationDistance).tooltip();
                }
            }

            if (previousSearchDistance == currentSearchDistance) {
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").hide();
                }
                return;
            }
        });
    }

    if (searchLocationDistance != undefined &&
        $(searchLocationDistance).is(":visible")) {
        $(searchLocationDistance).tooltip();
    }

    if (searchLocationDistance != undefined) {
        $(searchLocationDistance).tooltip();
    }

    // Append Jobs
    displayCompanyJobs(companyId, false, freshGenerate);
}

/**
 * Returns an HR element as a string with the ID of placeholderShowJobs.
 * @returns {string}
 */
function generatePlaceHolder() {
    return `<hr id="placeholderShowJobs" class="smallestDivider mx-auto" style="color:white;" />`;
}

/**
 * Returns search elements as a string which can be appended to an HTML page.
 * @returns {string}
 */
function generateSearchControls() {
    return `<div class="container bg-none pt-2 mb-3 mb-md-2" id="searchControlsShowJobs">
    <div class="row mb-6">
        <div class="col-12 col-md-12 col-lg-6 mb-2 mb-lg-0 px-1 px-lg-0 pb-1">
            <div class="input-group">
                <span class="input-group-text">Keywords</span>
                <input class="manualQueryFormText form-control form-control-sm manualQueryFormTextBody"
                       type="text" placeholder="Job Title (e.g. Senior Software Engineer)" id="jobSearchKeyword">
                </input>
            </div>
        </div>
        <div class="col-12 col-md-12 col-lg-6 mb-2 mb-lg-0 px-lg-0 px-1">
            <div class="input-group">
                <span class="input-group-text">Location</span>
                <input class="manualQueryFormText form-control form-control-sm manualQueryFormTextBody"
                       type="text" placeholder="City, State, Country, or Remote" id="jobSearchLocation">
                </input>
                <input type="range" class="form-range" min="0" max="300"
                       value="30" step="5" id="distanceMiles"
                       name="distanceMiles" list="markers"
                       style="display:none" data-bs-toggle="tooltip"
                       data-bs-placement="top"
                       data-bs-custom-class="custom-tooltip"
                       data-bs-title="Miles: 30">
                </input>
                <label for="distanceMiles"
                       class="manualQueryFormText text-white justify-content-center mx-auto"
                       id="distanceMilesLabel"
                       style="display:none">Distance (miles)
                </label>
            </div>
        </div>
    </div>
    <div class="text-center" id="loadingSpinner">
        <div class="spinner-border text-success" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
        <br />
    </div>
</div>`;
}

/**
 * Returns pagination control elements as a string which can be appended to the HTML of a page.
 * @param {?string} ariaLabelPosition - Specify "Top" or "Bottom" when generating ID and labels for page number controls.
 * @param {?number} maxJobPages - Amount of elements for pages to generate
 * @returns {string}
 */
function generateCompanyJobsPaginationControls(ariaLabelPosition = "Top", maxJobPages = -1) {
    if (maxJobPages < 2 ||
        (ariaLabelPosition != "Top" &&
            ariaLabelPosition != "Bottom")) {
        return;
    }
    let returnHTML = `<nav aria-label="Company Jobs Pagination ${ariaLabelPosition}" class="row justify-content-center row-cols-auto">
      <div class="col-auto">
            <ul class="mx-auto pagination pagination-sm justify-content-center"
                id="pagination-${ariaLabelPosition.toLowerCase()}">
                  <li class="page-item"
                      id="page-previous-${ariaLabelPosition.toLowerCase()}"
                      data-page-number="-1">
                        <a class="page-link"
                           style="cursor:not-allowed;">
                              Previous
                        </a>
                  </li>
                  <li class="page-item active"
                      aria-current="page"
                      data-page-number="1">
                        <span class="page-link"
                              style="cursor:not-allowed;">1</span>
                  </li>`;

    for (let i = 2; i != Math.min(6, maxJobPages + 1); i++) {
        returnHTML += `<li class="page-item"
                        data-page-number="${i.toString()}">
                          <a
                             class="page-link">
                                ${i.toString()}
                          </a>
                    </li>`;
    }

    return returnHTML + `<li class="page-item"
                      id="page-next-${ariaLabelPosition.toLowerCase()}"
                      data-page-number="+1">
                        <a
                           class="page-link">
                              Next
                        </a>
                  </li>
            </ul>
      </div>
</nav>`;
}


/**
 * Load jobs data for a company from REST
 * Modifies the DOM.
 * @param {?number} companyId - ID of the Company
 * @param {?boolean} bottom - true or false to scroll the window to the bottom after loading items.
 * @param {?boolean} freshGenerate - true or false to force the DOM to regenerate (When show jobs button is re-clicked.)
 * @returns {void}
 */
async function displayCompanyJobs(
    companyId = -1,
    bottom = false,
    freshGenerate = false) {
    if (loadCompanyJobsElement == undefined) {
        // console.error("Could not find element to load in jobs data.");
        return;
    }

    //Force generation when the DOM has previously been cleared.
    if (!freshGenerate) {
        //Do not query again if the search term is the same and the page number is the same as the last queried.
        if (
            //Search Terms
            previousSearchTerm != undefined &&
            previousSearchTerm == currentSearchTerm &&

            //Search Locations
            previousSearchLocation != undefined &&
            previousSearchLocation == currentSearchLocation &&

            //Search Location Distance
            previousSearchDistance != undefined &&
            previousSearchDistance == currentSearchDistance &&

            previousPageNumber == currentPageNumber) {
            // console.debug("Returning from previous " +
            //     "searchTerm=current " +
            //     "searchLocation=current " +
            //     "searchDistance=current " +
            //     "and previouspagenumber==current");

            return;
        }

        //Reset the page numbering when a new term is searched, defaulting to page 1.
        if (previousSearchTerm != currentSearchTerm ||
            previousSearchLocation != currentSearchLocation) {
            // console.debug("Search Term Check: " + previousSearchTerm + " != " + currentSearchTerm + "\n" +
            //     "Search Location Check: " + previousSearchLocation + " != " + previousSearchLocation);
            currentPageNumber = 1;
            previousSearchDistance = 30;
            // console.debug(previousSearchDistance + " = 30 - a");

            if ($('#distanceMiles') != undefined &&
                $('#distanceMiles').is(":visible")) {
                $('#distanceMiles').val('30');
                resetDistanceTooltip();
            }

        } else if (previousSearchDistance != currentSearchDistance) {
            currentPageNumber = 1;
        }
    }

    $(loadCompanyJobsElement).html('');

    //Check if Search terms are specified and default to a general query instead.
    if ((currentSearchTerm == undefined ||
        typeof currentSearchTerm != "string" ||
        currentSearchTerm.length < 1) &&
        (currentSearchLocation == undefined ||
            typeof currentSearchLocation != "string" ||
            currentSearchLocation.length < 1)) {

        await getCompanyJobs(
            companyId,
            currentPageNumber)
            .then(r => {
                populateJobs(r, bottom);
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").hide();
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
                //Fail-safe event to make sure current search has been successfully processed.
                if (refreshTimer != undefined) {
                    clearTimeout(refreshTimer);
                }

                refreshTimer = setTimeout(checkSearchQueryBase, 1000);
            });

    } else {
        // if (currentSearchTerm != '') {
        //     console.debug("Send Term: " + currentSearchTerm);
        // }
        // if (currentSearchLocation != '') {
        //     console.debug("Send Location: " + currentSearchLocation);
        // }
        await searchCompanyJobs(
            companyId,
            currentSearchTerm,
            currentSearchLocation,
            currentSearchDistance,
            currentPageNumber)
            .then(r => {
                populateJobs(r, bottom);
                // console.debug(previousSearchDistance + " = " + currentSearchDistance + "c");

                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").hide();
                }

                previousSearchTerm = currentSearchTerm;
                previousSearchLocation = currentSearchLocation;
                previousSearchDistance = currentSearchDistance;

                previousPageNumber = currentPageNumber;

            }).then(() => {
                //Fail-safe event to make sure current search has been successfully processed.
                if (refreshTimer != undefined)
                    clearTimeout(refreshTimer);

                refreshTimer = setTimeout(checkSearchQueryFull, 1000);
            });
    }

    if (bottom) {
        window.scrollTo(0, document.body.scrollHeight);
    }

    // Finally, append bottom pagination controls.
    if (companyMaxJobSearchPages > 1 ||
        (companyMaxJobSearchPages == -1 &&
            companyMaxJobPages > 1)) {
        $(generateCompanyJobsPaginationControls(
            "Bottom",
            Math.max(companyMaxJobPages, companyMaxJobSearchPages)))
            .insertAfter($(".userJobListLink").last(),
                Math.max(companyMaxJobPages, companyMaxJobSearchPages));
    }

    renumberPaginationControls();
}


/**
 * Checks previously sent query against server's latest response, after it has been completed.
 * Modifies the DOM.
 * @returns {void}
 */
async function checkCompanySearchQuery() {
    await retrievePreviousSearchCompany()
        .then(r => {
            if (r == undefined ||
                r.data == undefined) {
                return;
            }

            if (r.data.page_number != undefined &&
                previousPageNumber != cleanString(r.data.page_number)) {
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").show();
                }
                // console.debug("Incorrect Page: [" +
                //     previousPageNumber.toString() + "]!=[" +
                //     cleanString(r.data.page_number).toString() + "]");
                previousPageNumber = cleanString(r.data.page_number);
            }

            if (r.data.search != undefined &&
                previousSearchTerm != cleanString(r.data.search)) {
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").show();
                }
                // console.debug("Incorrect Term: [" +
                //     previousSearchTerm.toString() + "]!=[" +
                //     cleanString(r.data.search).toString() + "]");
                previousSearchTerm = cleanString(r.data.search);
            }

        });
}


/**
 * Checks previously sent query against server's latest response, after it has been completed.
 * Modifies the DOM.
 * @returns {void}
 */
async function checkSearchQueryBase() {
    await retrievePreviousSearchCompany()
        .then(r => {
            if (r == undefined ||
                r.data == undefined) {
                return;
            }

            if (r.data.page_number != undefined &&
                previousPageNumber != cleanString(r.data.page_number)) {
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").show();
                }
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
    await retrievePreviousSearchCompany()
        .then(r => {
            if (r == undefined ||
                r.data == undefined) {
                return;
            }

            if (r.data.page_number != undefined &&
                previousPageNumber != cleanString(r.data.page_number)) {
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").show();
                }
                // console.debug("Incorrect Page: [" +
                //     previousPageNumber.toString() + "]!=[" +
                //     cleanString(r.data.page_number).toString() + "]");
                previousPageNumber = cleanString(r.data.page_number);
            }

            if (r.data.search != undefined &&
                previousSearchTerm != cleanString(r.data.search)) {
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").show();
                }
                // console.debug("Incorrect Term: [" +
                //     previousSearchTerm.toString() + "]!=[" +
                //     cleanString(r.data.search).toString() + "]");
                previousSearchTerm = cleanString(r.data.search);
            }

            if (r.data.location != undefined &&
                previousSearchLocation != cleanString(r.data.location)) {
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").show();
                }
                // console.debug("Incorrect Location: [" +
                //     previousSearchLocation.toString() + "]!=[" +
                //     cleanString(r.data.location).toString() + "]");
                previousSearchLocation = cleanString(r.data.location);
            }

            if (r.data.distance != undefined &&
                cleanString(r.data.distance) != undefined &&
                previousSearchDistance != cleanString(r.data.distance)) {
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").show();
                }

                // console.debug("Incorrect Distance: [" +
                //     previousSearchDistance.toString() + "]!=[" +
                //     cleanString(r.data.distance).toString() + "]");

                previousSearchDistance = cleanString(r.data.distance);
            }
        });
}

/**
 * Load companies data into the dashboard after querying 
 * and receiving data from the server using a REST endpoint.
 * Modifies the DOM.
 * @param {?boolean} bottom - true or false to scroll the window to the bottom after loading items.
 * @returns {void}
 */
async function displayCompanies(bottom = false) {

    if (companiesDashboard == undefined) {
        console.error("Could not find element to load in companies data.");
        return;
    }

    //Do not query again if the search term is the same, and the page number is the same as the last queried.
    if (
        //Search Terms
        previousSearchTerm != undefined &&
        previousSearchTerm == currentSearchTerm &&

        previousPageNumber == currentPageNumber) {
        // console.debug("Returning from previous " +
        //     "searchTerm=current " +
        //     "and previouspagenumber==current");

        return;
    }

    $(companiesDashboard).empty();

    //Reset the page numbering when a new term or location is searched, defaulting to page 1.
    if (previousSearchTerm != currentSearchTerm) {
        // console.debug("Search Term Check: " + previousSearchTerm + " != " + currentSearchTerm);
        currentPageNumber = 1;

        renumberPaginationControls();

    }

    //Check if Search terms are specified and default to a general query instead.
    if (currentSearchTerm == undefined ||
        typeof currentSearchTerm != "string" ||
        currentSearchTerm.length < 1) {

        await getCompanies(currentPageNumber)
            .then(r => {
                populateCompanies(r, bottom);
                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").hide();
                }
                if (r == undefined ||
                    r.data == undefined) {
                    return;
                }

                previousSearchTerm = "";
                previousPageNumber = currentPageNumber;
            }).then(() => {
                // Fail-safe event to make sure current search has been successfully processed.
                if (refreshTimer != undefined) {
                    clearTimeout(refreshTimer);
                }

                refreshTimer = setTimeout(checkCompanySearchQuery, 1000);
            });

    } else {
        // if (currentSearchTerm != '') {
        //     console.debug("Send Term: " + currentSearchTerm);
        // }

        await searchCompanies(
            currentSearchTerm,
            currentPageNumber)
            .then(r => {
                populateCompanies(r, bottom);
                // console.debug(previousSearchDistance + " = " + currentSearchDistance + "c");

                if ($("#loadingSpinner") != undefined) {
                    $("#loadingSpinner").hide();
                }

                previousSearchTerm = currentSearchTerm;
                previousPageNumber = currentPageNumber;

            }).then(() => {
                //Fail-safe event to make sure current search has been successfully processed.
                if (refreshTimer != undefined) {
                    clearTimeout(refreshTimer);
                }
                refreshTimer = setTimeout(checkCompanySearchQuery, 1000);
            });
    }

    if (bottom) {
        window.scrollTo(0, document.body.scrollHeight);
    }

}

/**
 * Load jobs from a specific company into the dashboard after querying 
 * and receiving data from the server using a REST endpoint.
 * Modifies the DOM
 * @param {Promise} response - Response received from the server containing an array of jobs.
 * @param {?boolean} bottom - Whether or not to scroll ot the bottom, variable is passed to the displayCompanyJobs function.
 * @returns {void}
 */
function populateJobs(
    response,
    bottom = false) {
    if (loadCompanyJobsElement == undefined) {
        console.error("Could not find Load Company Jobs Element");
        return;
    }

    //Empty();
    if (response == undefined ||
        response.data == undefined ||
        response.data.length == 0) {
        //Page back-track here.
        //If there's no results from the server, subtract the page number by 1 and redisplay for that page.
        if (currentPageNumber <= 1) {
            if ($("#pagination-top") != undefined &&
                $("#pagination-top").is(":visible")) {
                $("#pagination-top").hide();
            }
            if ($("#pagination-bottom") != undefined &&
                $("#pagination-bottom").is(":visible")) {
                $("#pagination-bottom").hide();
            }
            if (loadCompanyJobsElement != undefined) {
                companyMaxJobSearchPages = currentPageNumber;
                $(loadCompanyJobsElement).append("No results!");
            }
            // No results found
            //console.warn("displayCompanyJobsDefault response did not return anything.");

        } else {
            if ($("#loadingSpinner") != undefined) {
                $("#loadingSpinner").show();
            }
            previousPageNumber = currentPageNumber;
            currentPageNumber--;
            // console.log("Current Page Number - " + currentPageNumber.toString());
            //track max pages (usually for a search term)
            companyMaxJobSearchPages = currentPageNumber;

            displayCompanyJobs(cleanHTMLString($(companyShowJobsButton).attr('data-company-id')), bottom);
            // renumberPaginationControls(currentPageNumber);
        }

        return;
    }

    response.data.forEach(v => {
        $(loadCompanyJobsElement).append(generateCompanyJobRowTemplate(v));
    });

    if ($("#pagination-top") != undefined &&
        $("#pagination-top").is(":hidden")) {
        $("#pagination-top").show();
    }
    if ($("#pagination-bottom") != undefined &&
        $("#pagination-bottom").is(":hidden")) {
        $("#pagination-bottom").show();
    }
}

/**
 * Populate data received from REST endpoints.
 * Modifies the DOM.
 * @param {Promise} response - Response sent from server
 * @param {?boolean} bottom - true or false to scroll to bottom after load
 * @returns {void}
 */
function populateCompanies(
    response,
    bottom = false) {
    if ($(companiesDashboard) == undefined) {
        console.error("Could not find element to load in companies data.");
        return;
    }

    if (response == undefined ||
        response.data == undefined ||
        response.data.length == 0) {
        //Page back-track here.
        //If there's no results from the server, subtract the page number by 1 and redisplay for that page.
        if (currentPageNumber <= 1) {
            // No results found

            if (companiesDashboard != undefined) {
                if ($("#pagination-top") != undefined &&
                    $("#pagination-top").is(":visible")) {
                    $("#pagination-top").hide();
                }
                if ($("#pagination-bottom") != undefined &&
                    $("#pagination-bottom").is(":visible")) {
                    $("#pagination-bottom").hide();
                }
                $(companiesDashboard).append("No results!");
            }
            //console.warn("displayCompaniesDefault response did not return anything.");

        } else {
            if ($("#loadingSpinner") != undefined) {
                $("#loadingSpinner").show();
            }
            previousPageNumber = currentPageNumber;
            currentPageNumber--;
            //track max pages (usually for a search term)
            companyMaxJobPages = currentPageNumber;

            // console.log("Current Page Number - " + currentPageNumber.toString());
            displayCompanies(bottom);
            renumberPaginationControls(currentPageNumber);
        }

        return;
    }

    response.data.forEach(v => {
        $(companiesDashboard).append(generateCompanyRowTemplate(v));
    });
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
        cleanHTMLString($(event.target).attr('data-id')).toString(),

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
 * Generates HTML required to display companies provided by the server's REST endpoint.
 * Creates an element with row data retrieved from the Get Companies REST endpoint.
 * Maintains proper gutter.
 * @returns {Promise} v - Response data returned from a Company query
 * @returns {string}
 */
function generateCompanyRowTemplate(v) {
    let returnHTML = `
    <div class="userJobListLink figure rounded bg-dark mb-2 px-lg-1 px-xl-2 px-xxl-3 py-1 py-lg-2">
        <span class="text-info" 
              style="font-size:17px;">
            ${v.name}
        </span>
        <br />
        <span class="fluidLongTextFlex"
              style="font-size:16px;font-weight: bolder;">
        Job Count: ${v.job_count}
        </span>
        <br />`;

    if (v.description != undefined &&
        v.description != "No Description") {
        returnHTML += `<hr class="mx-5" style="color:white;" />
            <span class="fluidLongTextFlex"
                style="font-size:15px;">${v.description}</span>
            <br />
            <hr class="mx-5" style="color:white;" />`;

    } else {
        returnHTML += `<hr class="smallestDivider mx-auto" style="color:white;" />`;
    }

    returnHTML += `<button class="btn-linkUserMini rounded bg-primary"
            data-id="${v.id}" onclick="viewCompany(event);">View</button>`;

    if (!savedCompanies.includes(v.id)) {
        returnHTML += `<button data-action="toggleCompanyDash" 
            class="btn-linkUserMini rounded bg-success"
            data-id="${v.id}" 
            onclick="toggleCompany(event);">Save</button>`;
    } else {
        returnHTML += `<button data-action="toggleCompanyDash" 
            class="btn-linkUserMini-longer rounded bg-danger"
            data-id="${v.id}" 
            onclick="toggleCompany(event);">Un-save</button>`;
    }

    return returnHTML + `<br />
    <span class="fluidUserLongTextFlex text-info">${v.last_updated}</span>
    <br />
    </div>`;
}

/**
 * Generates Jobs from the view company route. Respective only to the company being viewed.
 * Creates an element with row data retrieved from the Jobs REST endpoint.
 * @param {Promise} v - Response data returned from a job query
 * @returns {string}
 */
function generateCompanyJobRowTemplate(v) {
    let returnHTML = `
    <div class="userJobListLink figure rounded border border-info bg-black mb-2 px-lg-1 px-xl-2 px-xxl-3 py-1 py-lg-2">
        <span class="text-info"
              style="font-size:17px;">${v.name}</span>
        <br />`;

    if (v.company != undefined &&
        v.company != '') {
        returnHTML += `<span class="fluidLongTextFlex"
        style="font-size:15px;font-weight: bolder;">${v.company}</span>
        <br />`;
    }

    if (v.location != undefined &&
        v.location != '') {
        returnHTML += `<span class="fluidLongTextFlex text-info"
              style="font-size:14px">${v.location}</span>
            <br />`;
    }

    if (v.job_type != undefined &&
        v.job_type != '') {
        returnHTML += `<span class="fluidLongTextFlex text-info"
              style="font-size:14px">${v.job_type}</span>
            <br />`;
    }

    if (v.description != undefined &&
        v.description != "No Description") {
        returnHTML += `<hr class="mx-5" style="color:white;" />
            <span class="fluidLongTextFlex"
                  style="font-size:15px;">${v.description}</span>
            <br />
            <hr class="mx-5" style="color:white;" />`;

    } else {
        returnHTML += `<hr class="smallestDivider mx-auto" style="color:white;" />`;
    }

    returnHTML += `<button data-action="viewJob" data-id="${v.id}" class="btn-linkUserMini rounded bg-primary"
            onclick="viewJob(event);">View</button>`;


    if (!savedJobs.includes(v.id)) {
        returnHTML += `<button data-action="toggleJobCompanyDash" 
            data-id="${v.id}" 
            class="btn-linkUserMini rounded bg-success"
            onclick="toggleJob(event);">Save</button>`;
    } else {
        returnHTML += `<button data-action="toggleJobCompanyDash" 
            data-id="${v.id}" 
            class="btn-linkUserMini-longer rounded bg-danger"
            onclick="toggleJob(event);">Un-save</button>`;
    }

    return returnHTML + `<br />
        <span class="fluidUserLongTextFlex text-info">${v.posted_time_utc}</span><br />
        <span class="fluidUserLongTextFlex text-success">${v.api_source}</span>
    </div>`;
}

/**
 * Opens a popup from a click event and retrieves the 'data-id' of the element as the path parameter
 * when viewing a job.
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