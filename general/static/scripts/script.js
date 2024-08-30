/**
 * Shows a message to the client that was sent from the server.
 */
$(document).ready(() => {
    setTimeout(() => {
        if ($(".flashed_msgs") != undefined)
            $(".flashed_msgs").remove();

    }, 3500);
});


/**
 * Encodes string so it can be sent as a path parameter for a query to a REST endpoint.
 * @param {string} input - String input to clean
 * @returns {String} input - String to clean
 */
function cleanString(input) {
    return encodeURIComponent(input);
}

/**
 * Clean string and return the cleaned output for sending to the server, outside of a Path parameter.
 * @param {string} - input - String to clean
 * @returns {string} - Cleaned String
 */
function cleanStringParam(input) {
    return input.trim().replace(/[^\w\s]/gi, '');
}

/**
 * Clean string and return the cleaned output in order to set this string as an ID in a DOM element.
 * @param {string} - input - String to clean
 * @returns {string} - Cleaned String
 */
function cleanListName(input) {
    return input.trim().replace(/[^\w\s]/gi, '').replace(" ", "_");
}

/**
 * Clean string and return the cleaned output for JS functions.
 * @param {string} input - String input to clean
 * @returns {string}
 */
function cleanHTMLString(input) {
    return input.trim().replace(/[^\w\s.-]/g, '');
}

/**
 * Escape string and return the cleaned output for Text output
 * @param {string} str - String input to clean
 * @returns {string}
 */
function escapeHTML(str) {
    return str.replace(/[&<>'"]/g, tag => ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        "'": '&#39;',
        '"': '&quot;'
    }[tag] || tag));
}

/**
 * Saves or Removes a job from the user's profile.
 * When user clicks on the 'save' or 'un-save' button.
 * Handles method calls from the Job dashboard, profile dashboard, and a specific Company's page.
 * Modifies the DOM
 * @param {object} event
 * @returns {void}
 */
async function toggleJob(event) {
    event.preventDefault();
    const selectedJobId = $(event.target).attr('data-id');
    if (selectedJobId == undefined) {
        console.error("Clicked save/un-save on an unspecified Job ID");
        return;
    }
    await (window.location.pathname.includes('/profile') ?
        toggleJobProfileUpdate(
            selectedJobId,
            $(event.target).text() == "Save",
            +window.location.pathname.slice('/profile/'.length)) :
        toggleJobActiveProfileUpdate(
            selectedJobId,
            $(event.target).text() == "Save"))
        .then(r => {
            if (r == undefined ||
                r.status == undefined) {
                console.error("toggleJob Exception (No Data returned from server)");
                return;
            }
            if (r.status == 200) {
                //Dashboard styling
                if ($(event.target).attr('data-action') == "toggleJobDash" ||
                    $(event.target).attr('data-action') == "toggleJobCompanyDash") {
                    if ($(event.target).text() == "Save") {
                        $(event.target)
                            .attr({ 'class': 'btn-linkUserMini-longer rounded bg-danger' })
                            .text('Un-save');
                        if (!savedJobs.includes(+selectedJobId)) {
                            savedJobs.push(+selectedJobId);
                        }
                    } else {
                        $(event.target)
                            .attr({ 'class': 'btn-linkUserMini rounded bg-success' })
                            .text('Save');
                        if (savedJobs.includes(+selectedJobId)) {
                            savedJobs = savedJobs.filter(v => v != +selectedJobId);
                        }
                    }
                } else if ($(event.target).attr('data-action') == "toggleJobProfileDash") {
                    if ($(event.target).text() == "Save") {
                        //Save clicked
                        //Replace previously displayed delete button with Edit button
                        $(event.target)
                            .parent()
                            .children('button')
                            .filter((i, v) => $(v).attr('data-action') == 'quickDeleteJobProfile')
                            .attr({
                                'class': 'btn-linkUserMini rounded bg-success',
                                'data-action': 'editJobProfile',
                                'onclick': 'editSavedJob(event);',
                            })
                            .text('Edit');

                        $(event.target)
                            .attr({
                                'class': 'btn-linkUserMini-longer rounded bg-danger',
                                // 'data-action': "toggleJobProfileDash",
                                // 'data-id': selectedJobId.toString(),
                                // 'onclick': "toggleJob(event);"
                            })
                            .text('Un-save');

                        if (savedJobs.has('Unnamed')) {
                            for (const i of savedJobs.get('Unnamed')) {
                                if (i.id == +selectedJobId) {
                                    i.order = null;
                                    i.list_name = null;
                                    savedJobs.set('Unnamed', savedJobs.get('Unnamed').filter(v => v.id != +selectedJobId));
                                    savedJobs.get('Unnamed').push(i);
                                    break;
                                }
                            }
                        }

                        //Add job back to default list (Previous data relocated to unnamed list)

                        //Regenerate job data dashboard
                        $("#savedJobDataDash-" + selectedJobId)
                            .append(
                                regenerateJobDashData(
                                    retrieveSavedJobData(
                                        +selectedJobId,
                                        "Unnamed",
                                    )
                                )
                            );

                        //Refresh entire Job dashboard div
                        quickRefreshSavedJobsDisplayData();
                    } else {
                        //Unsave Clicked
                        $("#savedJobDataDash-" + selectedJobId)
                            .empty()
                            .append("Pending Deletion");

                        $(event.target)
                            .attr({ 'class': 'btn-linkUserMini rounded bg-success' })
                            .text('Save');

                        //Cancel current Edit
                        const cancelButton = $(event.target)
                            .parent()
                            .children('button')
                            .filter((i, v) => $(v).attr('data-action') == 'cancelEditJobProfile');

                        if ($(cancelButton) != undefined) {
                            $(cancelButton).remove();
                        }

                        //Switch Done button to delete
                        const doneButton = $(event.target)
                            .parent()
                            .children('button')
                            .filter((i, v) => $(v).attr('data-action') == 'completeUpdateSavedJobProfile');

                        if ($(doneButton) != undefined) {
                            $(doneButton)
                                .off('click')
                                .attr({
                                    'class': 'btn-linkUserMini-longer rounded bg-warning',
                                    'data-action': 'quickDeleteJobProfile',
                                    'onclick': 'deleteUnsavedJob(event);',
                                })
                                .text('Delete');
                        }

                        //Switch Edit button to delete
                        const editButton = $(event.target)
                            .parent()
                            .children('button')
                            .filter((i, v) => $(v).attr('data-action') == 'editJobProfile');

                        if ($(editButton) != undefined) {
                            $(editButton)
                                .off('click')
                                .attr({
                                    'class': 'btn-linkUserMini-longer rounded bg-warning',
                                    'data-action': 'quickDeleteJobProfile',
                                    'onclick': 'deleteUnsavedJob(event);',
                                })
                                .text('Delete');
                        }

                        //Change Edit/Done button to (quick) delete instead.
                        $(event.target)
                            .parent()
                            .children('button')
                            .filter((i, v) => $(v).attr('data-action') == 'cancelEditJobProfile')
                            .remove();

                        //Button -> Parent (Job Card) -> Parent (List Div) -> Attr (ID)
                        const listName = $(event.target).parent('div').parent('div').attr('id').replace('jobList-', '');

                        let found = false;
                        if (savedJobs.has(listName)) {
                            for (const i of savedJobs.get(listName)) {
                                if (i.id == +selectedJobId) {
                                    i.order = null;
                                    i.listName = null;
                                    found = i;
                                    if (savedJobs.has("Unnamed")) {
                                        let nestedFound = false;
                                        for (const j of savedJobs.get("Unnamed")) {
                                            if (j.id == +selectedJobId) {
                                                nestedFound = true;
                                                break;
                                            }
                                        }
                                        if (!nestedFound) {
                                            //Move job to unsaved (Temporarily - cleared when page is reloaded.)
                                            if (!savedJobs.has("Unnamed")) {
                                                savedJobs.set("Unnamed", [i]);
                                            } else {
                                                savedJobs.get("Unnamed").push(i);
                                            }
                                        }
                                    }
                                    break;
                                }
                            }
                        }
                        if (found != false) {
                            if (listName != "Unnamed") {
                                if (!savedJobs.has("Unnamed")) {
                                    savedJobs.set("Unnamed", [found]);
                                } else {
                                    savedJobs.get("Unnamed").push(found);
                                }

                                savedJobs.set(listName, savedJobs.get(listName).filter(v => v.id != +selectedJobId));
                                if (savedJobs.get(listName).length == 0) {
                                    savedJobs.delete(listName);
                                }
                            }
                        }
                    }
                } else {
                    //View Job Styling
                    if ($(event.target).text() == "Save") {
                        $(event.target)
                            .attr({ 'class': 'btnAction rounded bg-danger' })
                            .text('Un-save');
                        if (!savedJobs.includes(+selectedJobId)) {
                            savedJobs.push(+selectedJobId);
                        }
                    } else {
                        $(event.target)
                            .attr({ 'class': 'btnAction rounded bg-success' })
                            .text('Save');
                        if (savedJobs.includes(+selectedJobId)) {
                            savedJobs = savedJobs.filter(v => v != +selectedJobId);
                        }
                    }
                }
            } else if (r.status === 417) {
                alert("You have no active profile");
            } else if (r.status === 403) {
                alert("You're not logged in");
            }
        });
}


/**
 * Saves or Removes a company from the user's profile.
 * When user clicks on the 'save' or 'un-save' button.
 * Handles method calls from the Company dashboard, profile dashboard, and a specific Job's page.
 * Modifies the DOM
 * @param {object} event
 * @returns {void}
 */
async function toggleCompany(event) {
    event.preventDefault();
    const selectedCompanyId = $(event.target).attr('data-id');
    if (selectedCompanyId == undefined) {
        console.error("Clicked save/un-save on an unspecified Company ID");
        return;
    }
    await (window.location.pathname.includes('/profile') ?
        toggleCompanyProfileUpdate(
            selectedCompanyId,
            $(event.target).text() == "Save",
            +window.location.pathname.slice('/profile/'.length)) :
        toggleCompanyActiveProfileUpdate(
            selectedCompanyId,
            $(event.target).text() == "Save"))
        .then(r => {
            if (r == undefined ||
                r.status == undefined) {
                console.error("toggleCompany Exception (No Data returned from server)");
                return;
            }
            if (r.status == 200) {
                //Dashboard styling
                if ($(event.target).attr('data-action') == "viewJobSingle" ||
                    $(event.target).attr('data-action') == "toggleCompanyDash" ||
                    $(event.target).attr('data-action') == "toggleJobCompanyDash") {
                    if ($(event.target).text() == "Save") {
                        $(event.target)
                            .attr({ 'class': 'btn-linkUserMini-longer rounded bg-danger' })
                            .text('Un-save');
                        if (!savedCompanies.includes(+selectedCompanyId)) {
                            savedCompanies.push(+selectedCompanyId);
                        }
                    } else {
                        $(event.target)
                            .attr({ 'class': 'btn-linkUserMini rounded bg-success' })
                            .text('Save');
                        if (savedCompanies.includes(+selectedCompanyId)) {
                            savedCompanies = savedCompanies.filter(v => v != +selectedCompanyId);
                        }
                    }
                } else if ($(event.target).attr('data-action') == "toggleCompanyProfileDash") {
                    if ($(event.target).text() == "Save") {
                        //Save clicked
                        //Replace previously displayed delete button with Edit button
                        $(event.target)
                            .parent()
                            .children('button')
                            .filter((i, v) => $(v).attr('data-action') == 'quickDeleteCompanyProfile')
                            .attr({
                                'class': 'btn-linkUserMini rounded bg-success',
                                'data-action': 'editCompanyProfile',
                                'onclick': 'editSavedCompany(event);',
                            })
                            .text('Edit');
                        $(event.target)
                            .attr({
                                'class': 'btn-linkUserMini-longer rounded bg-danger',
                                // 'data-action': "toggleCompanyProfileDash",
                                // 'data-id': selectedCompanyId.toString(),
                                // 'onclick': "toggleCompany(event);"
                            })
                            .text('Un-save');
                        if (savedCompanies.has('Unnamed')) {
                            for (const i of savedCompanies.get('Unnamed')) {
                                if (i.id == +selectedCompanyId) {
                                    i.order = null;
                                    i.list_name = null;
                                    savedCompanies.set('Unnamed', savedCompanies.get('Unnamed').filter(v => v.id != +selectedCompanyId));
                                    savedCompanies.get('Unnamed').push(i);
                                    break;
                                }
                            }
                        }
                        //Add company back to default list (Previous data relocated to unnamed list)
                        //Regenerate company data dashboard
                        $("#savedCompanyDataDash-" + selectedCompanyId)
                            .append(
                                regenerateCompanyDashData(
                                    retrieveSavedCompanyData(
                                        +selectedCompanyId,
                                        "Unnamed",
                                    )
                                )
                            );
                        //Refresh entire Company dashboard div
                        quickRefreshSavedCompaniesDisplayData();
                    } else {
                        //Unsave Clicked
                        $("#savedCompanyDataDash-" + selectedCompanyId)
                            .empty()
                            .append("Pending Deletion");
                        $(event.target)
                            .attr({ 'class': 'btn-linkUserMini rounded bg-success' })
                            .text('Save');
                        //Cancel current Edit
                        const cancelButton = $(event.target)
                            .parent()
                            .children('button')
                            .filter((i, v) => $(v).attr('data-action') == 'cancelEditCompanyProfile');
                        if ($(cancelButton) != undefined) {
                            $(cancelButton).remove();
                        }
                        //Switch Done button to delete
                        const doneButton = $(event.target)
                            .parent()
                            .children('button')
                            .filter((i, v) => $(v).attr('data-action') == 'completeUpdateSavedCompanyProfile');
                        if ($(doneButton) != undefined) {
                            $(doneButton)
                                .off('click')
                                .attr({
                                    'class': 'btn-linkUserMini-longer rounded bg-warning',
                                    'data-action': 'quickDeleteCompanyProfile',
                                    'onclick': 'deleteUnsavedCompany(event);',
                                })
                                .text('Delete');
                        }
                        //Switch Edit button to delete
                        const editButton = $(event.target)
                            .parent()
                            .children('button')
                            .filter((i, v) => $(v).attr('data-action') == 'editCompanyProfile');
                        if ($(editButton) != undefined) {
                            $(editButton)
                                .off('click')
                                .attr({
                                    'class': 'btn-linkUserMini-longer rounded bg-warning',
                                    'data-action': 'quickDeleteCompanyProfile',
                                    'onclick': 'deleteUnsavedCompany(event);',
                                })
                                .text('Delete');
                        }
                        //Change Edit/Done button to (quick) delete instead.
                        $(event.target)
                            .parent()
                            .children('button')
                            .filter((i, v) => $(v).attr('data-action') == 'cancelEditCompanyProfile')
                            .remove();
                        //Button -> Parent (Company Card) -> Parent (List Div) -> Attr (ID)
                        const listName = $(event.target).parent('div').parent('div').attr('id').replace('companyList-', '');
                        let found = false;
                        if (savedCompanies.has(listName)) {
                            for (const i of savedCompanies.get(listName)) {
                                if (i.id == +selectedCompanyId) {
                                    i.order = null;
                                    i.listName = null;
                                    found = i;
                                    if (savedCompanies.has("Unnamed")) {
                                        let nestedFound = false;
                                        for (const j of savedCompanies.get("Unnamed")) {
                                            if (j.id == +selectedCompanyId) {
                                                nestedFound = true;
                                                break;
                                            }
                                        }
                                        if (!nestedFound) {
                                            //Move company to unsaved (Temporarily - cleared when page is reloaded.)
                                            if (!savedCompanies.has("Unnamed")) {
                                                savedCompanies.set("Unnamed", [i]);
                                            } else {
                                                savedCompanies.get("Unnamed").push(i);
                                            }
                                        }
                                    }
                                    break;
                                }
                            }
                        }
                        if (found != false) {
                            if (listName != "Unnamed") {
                                if (!savedCompanies.has("Unnamed")) {
                                    savedCompanies.set("Unnamed", [found]);
                                } else {
                                    savedCompanies.get("Unnamed").push(found);
                                }
                                savedCompanies.set(listName, savedCompanies.get(listName).filter(v => v.id != +selectedCompanyId));
                                if (savedCompanies.get(listName).length == 0) {
                                    savedCompanies.delete(listName);
                                }
                            }
                        }
                    }
                } else {
                    //View Company Styling
                    if ($(event.target).text() == "Save") {
                        $(event.target)
                            .attr({ 'class': 'btnAction rounded bg-danger' })
                            .text('Un-save');
                        if (!savedCompanies.includes(+selectedCompanyId)) {
                            savedCompanies.push(+selectedCompanyId);
                        }
                    } else {
                        $(event.target)
                            .attr({ 'class': 'btnAction rounded bg-success' })
                            .text('Save');
                        if (savedCompanies.includes(+selectedCompanyId)) {
                            savedCompanies = savedCompanies.filter(v => v != +selectedCompanyId);
                        }
                    }
                }
            } else if (r.status === 417) {
                alert("You have no active profile");
            } else if (r.status === 403) {
                alert("You're not logged in");
            }
        });
}