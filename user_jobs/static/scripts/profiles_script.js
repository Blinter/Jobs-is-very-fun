let savedJobs = new Map();
let savedCompanies = new Map();

/**
 * Check path and run respective functions
 */
$(document).ready(() => {
    if (window.location.pathname === '/user_dashboard')
        getProfiles();
    else if (window.location.pathname.match('/profile/')) {
        refreshProfileDashboard(+window.location.pathname.slice('/profile/'.length));
    }
});

/**
 * Refreshes the profile dashboard
 * Modifies the DOM
 * @returns {void}
 */
const refreshDashboard = () => refreshProfileDashboard(+window.location.pathname.slice('/profile/'.length));

/**
 * Refreshes the profile dashboard
 * Queries the server to receive SavedJobs and SavedCompany data for the specified ID.
 * Modifies the DOM
 * @param {?number} profileId - Profile ID to query the server
 * @returns {void}
 */
async function refreshProfileDashboard(profileId) {

    await retrieveSavedDataUserProfileComplete(profileId)
        .then(r => {
            savedJobs.clear();
            savedCompanies.clear();

            if (r == null ||
                r.data == null) {
                return;
            }

            for (item of r.data[0]) {
                const listName = item.list_name == null || item.list_name === "" ? "Unnamed" : item.list_name;
                if (!savedJobs.has(listName)) {
                    savedJobs.set(listName, []);
                }
                savedJobs.get(listName).push(item);
            }
            for (item of r.data[1]) {
                const listName = item.list_name == null || item.list_name === "" ? "Unnamed" : item.list_name;
                if (!savedCompanies.has(listName)) {
                    savedCompanies.set(listName, []);
                }
                savedCompanies.get(listName).push(item);
            }

            sortSavedCompanies();
            sortSavedJobs();

            quickRefreshSavedJobsDisplayData();
            quickRefreshSavedCompaniesDisplayData();
        }
        );
}

/**
 * Creates a add new profile menu for the user when the "Add New" button is
 * clicked.
 * Modifies the DOM.
 * @param {object} e - Event Handler from the click event
 * @returns {void}
 */
async function addNewProfileMenu(e) {
    const parent = $(e.target).parent();
    $(e.target).remove();

    const profileInputText = $("<input>")
        .attr({
            "name": "addNewProfileName",
            "type": "text",
            "placeholder": "New Profile Name"
        })
        .addClass("newProfileInput");

    $(parent).append($(profileInputText));

    $(parent).append($("<br>"));

    const submitButton = $("<button>")
        .addClass("btn-ProfileSubmit rounded bg-primary placeholder-wave")
        .text("Create Profile");

    const cancelButton = $("<button>")
        .addClass("btn-ProfileCancel rounded bg-danger")
        .text("Cancel");

    $(parent).append($(submitButton));
    $(parent).append($(cancelButton));

    //Remove all the children from the parent element (li)
    $(cancelButton).on("click", function (event) {
        $(parent).empty();

        //Create the divider from previous HTML
        const divider = $("<hr>")
            .addClass("smallestDivider mx-auto")
            .css({ "color": "white" });

        //Create the new button previously removed
        const addNewButton = $("<button>")
            .addClass("btnAction rounded placeholder-wave")
            .text("Add New");

        //Append Previous divider
        $(parent).append($(divider));

        //Append button
        $(parent).append($(addNewButton));

        //Add back the original onClick Event
        $(addNewButton).on("click", (newEvent) => addNewProfileMenu(newEvent));

        cleanUpProfileList();
    });

    $(submitButton).on("click", () => {
        const inputText = $(profileInputText).val();
        if (inputText.length === 0) {
            //Apply error styles if there is no input for the Profile Name.
            $(profileInputText).css({
                "background-color": "yellow",
                "color": "red",
                "font-style": "bold",
                "border": "3px dashed red",
                "padding-top": "7px",
                "padding-bottom": "7px",
                "padding-left": "0px",
                "padding-right": "0px"
            })
                //Change placeholder to direct next action to user to fix the error.
                .attr({ "placeholder": "New Profile Name must be filled." })
                //Update the element.
                .change();

            //Remove the error styling if Profile Name has been typed in.
            $(profileInputText).on("change keydown paste input", function () {
                //Check for change in input value.
                if ($(profileInputText).val().length !== 0) {
                    //Disable listen event once length has been input.
                    $(profileInputText).off("change keydown paste input");

                    //Update style for input text box so that error styling
                    // is removed.
                    $(profileInputText).css({
                        "background-color": "white",
                        "color": "black",
                        "font-style": "normal",
                        "border": "0px white",
                        "padding-top": "10px",
                        "padding-bottom": "10px",
                        "padding-left": "3px",
                        "padding-right": "3px"
                    })
                        //Change placeholder back to normal.
                        .attr({ "placeholder": "New Profile Name" })
                        //Update the element.
                        .change();
                }
            });

            //End function early
            return;
        }

        //Make the profile by sending a PUT request to the server.
        createProfileName(inputText).then(response => {
            if ((response != null ||
                response.status != null) &&
                // maximum profile limit
                response.status === 226) {
                //Re-enable the submit button.
                //Apply error styles if there is no input for the Profile Name.
                $(profileInputText).css({
                    "background-color": "tan",
                    "color": "gray",
                    "font-style": "bolder",
                    "border": "2px dashed red",
                    "padding-top": "7px",
                    "padding-bottom": "7px",
                    "padding-left": "0px",
                    "padding-right": "0px"
                })
                    //Change placeholder to direct next action to user to fix the error.
                    .attr({
                        "placeholder":
                            (response != null &&
                                response.status != null &&
                                response.status === 226 ? "Maximum Profiles reached." :
                                "Profile name conflict.")
                    })
                    //Empty the name
                    .val('')
                    //Update the element.
                    .change();

                //Remove the error styling if Profile Name has been typed in.
                $(profileInputText).on("change keydown paste input", function () {
                    //Check for change in input value.
                    if ($(profileInputText).val().length !== 0) {
                        //Disable listen event once length has been input.
                        $(profileInputText).off("change keydown paste input");

                        //Update style for input text box so that error styling
                        // is removed.
                        $(profileInputText).css({
                            "background-color": "white",
                            "color": "black",
                            "font-style": "normal",
                            "border": "0px white",
                            "padding-top": "10px",
                            "padding-bottom": "10px",
                            "padding-left": "3px",
                            "padding-right": "3px"
                        })
                            //Change placeholder back to normal.
                            .attr({ "placeholder": "New Profile Name" })
                            //Update the element.
                            .change();
                    }
                });

                //End function early
                return;
            }

            //Add the new profile name
            displayNewProfile(response.data);

            //Delete the previous controls from the DOM
            $(parent).remove();

            const profilesList = $(".userProfilesList");

            const newItem = $("<li>").addClass("userProfilesControls");

            //Append Previous divider to the main list
            $(profilesList).append(
                $(newItem).append($("<hr>")
                    .addClass("smallestDivider mx-auto")
                    .css({ "color": "white" }))
                    .append(
                        $("<button>")
                            .addClass("btnAction rounded placeholder-wave")
                            .text("Add New")
                            .on("click", (newEvent) => addNewProfileMenu(newEvent))
                    ));

            cleanUpProfileList();
        });
    });
}

/**
 * Update the active profile status from a profile dashboard
 * Modifies the DOM
 * @returns {void}
 */
function toggleProfileFromUserDash() {
    //locate Activatation status by checking for class, as set by the server upon initial load.
    const activateToggle = $(".btnDeactivateProfile").length === 0;
    toggleProfile(
        undefined,
        +window.location.pathname.slice('/profile/'.length),
        activateToggle)
        .then(r => {
            if (r != null &&
                r.status === 205) {
                if (activateToggle) {
                    $(".btnActivateProfile")
                        .attr({ 'class': 'btnDeactivateProfile mx-auto mt-1 rounded' })
                        .text('Deactivate');
                } else {
                    $(".btnDeactivateProfile")
                        .attr({ 'class': 'btnActivateProfile mx-auto mt-1 rounded' })
                        .text('Activate');
                }
            } else {
                console.error("Problem changing status on profile");
            }
        });
}

/**
 * Add profiles to the DOM from object received by the server.
 * @param {Promise} data - Profile data received from the server
 * @returns {void}
 */
function displayProfiles(data) {
    const profilesList = $(".userProfilesList");

    if (data.length === 0) {
        $(profilesList)
            .append(generateProfileControls());

        cleanUpProfileList();
        return;
    }

    let firstProfile = false;
    for (profile of data) {
        // console.log(profile);
        const newProfile = $("<li>").addClass("userProfilesListLink");
        if (firstProfile)
            $(newProfile).append($("<hr>")
                .addClass('smallDivider mx-auto')
                .css({ 'color': 'white' }));

        if (!firstProfile)
            firstProfile = true;

        $(newProfile).append(profile.name);
        $(newProfile).append($("<br>"));

        const viewButton = $("<button class='btn-link rounded'>")
            .append("View");

        //(IIFE) Invoked function expression to pass profile data
        (profileData =>
            $(viewButton).on("click", () => location.href = `/profile/${profileData.id}`)
        )(profile); //Pass profile variable and call right away

        $(newProfile).append($(viewButton));
        $(newProfile).append(" ");

        // New
        // console.log(profile);
        const activateButton = profile.active ?
            $("<button class='btn-link-ActivatedProfile rounded' data-id='" + profile.id.toString() + "'>")
                .append("Deactivate") :
            $("<button class='btn-link-DeactivatedProfile rounded' data-id='" + profile.id.toString() + "'>")
                .append("Activate");

        //(IIFE) Invoked function expression to pass profile data
        (function (tempProfileData) {
            $(activateButton).on("click", event => {
                //Send an axios request to the server and check for a successful response
                const activateToggle = $(event.target).hasClass("btn-link-DeactivatedProfile");
                toggleProfile(
                    tempProfileData.name,
                    tempProfileData.id != null ?
                        tempProfileData.id :
                        +$(event.target).attr("data-id"),
                    activateToggle)
                    .then(r => {
                        // console.log(r);
                        if (r != null &&
                            r.status === 205) {
                            if (activateToggle) {
                                //Deactivate other activated profiles first, 
                                //skip if it's the current click target.
                                $("button.btn-link-ActivatedProfile").each((i, v) => {
                                    if ($(v) !== $(event.target)) {
                                        $(v)
                                            .attr({ 'class': 'btn-link-DeactivatedProfile rounded' })
                                            .text('Activate');
                                    }
                                });
                                $(event.target)
                                    .attr({ 'class': 'btn-link-ActivatedProfile rounded' })
                                    .text('Deactivate');
                            } else {
                                $(event.target)
                                    .attr({ 'class': 'btn-link-DeactivatedProfile rounded' })
                                    .text('Activate');
                            }
                        } else {
                            console.error("Problem changing status on profile");
                        }
                    });
            })
        })(profile); //Pass profile variable

        $(newProfile).append(activateButton);
        $(profilesList).append(newProfile);
        $(newProfile).append($(activateButton));
        $(newProfile).append(" ");

        // End New

        const editButton = $("<button>")
            .addClass("btn-link-edit rounded")
            .append("Edit");

        //(IIFE) Invoked function expression to pass profile data
        (function (profileData) {
            $(editButton).on("click", () => {
                //Empty the LI
                $(newProfile).empty();

                //Replace the text with a text input box
                generateEditProfileControls($(newProfile), profileData)
            })
        })(profile); //Pass profile variable and call right away        

        $(newProfile).append($(editButton));
        $(newProfile).append(" ");

        const deleteButton = $("<button class='btn-link-delete rounded'>")
            .append("Delete");

        //(IIFE) Invoked function expression to pass profile data
        (function (temp_profile) {
            $(deleteButton).on("click", () => {
                //Send an axios request to the server and check for a successful
                //delete
                if (deleteProfileId(temp_profile.id)) {
                    //Remove the selected profile
                    $(newProfile).remove();
                    //Clean up the profile list by removing the top divider if
                    //it exists.
                    cleanUpProfileList();
                }
            })
        })(profile); //Pass profile variable

        $(newProfile).append(deleteButton);
        $(profilesList).append(newProfile);
    }

    $(profilesList).append(generateProfileControls());
}

/**
 * Add profile to the DOM from profile generated by the client.
 * Modifies the DOM
 * @param {Promise} data - New profile data received by the server
 * @returns {void}
 */
function displayNewProfile(data) {
    const profilesList = $(".userProfilesList");
    if (data == null ||
        data.length !== 1)
        return;

    const profile = data[0];

    const newProfile = $("<li>").addClass("userProfilesListLink");

    $(newProfile).append($("<hr class='smallDivider mx-auto' style='color:white;'/>"));
    $(newProfile).append(profile.name);

    $(newProfile).append($("<br>"));

    const viewButton = $("<button class='btn-link rounded'>")
        .append("View");

    //(IIFE) Invoked function expression to pass profile data
    (profileData =>
        $(viewButton).on("click", () => location.href = `/profile/${profileData.id}`)
    )(profile); //Pass profile variable and call right away

    $(newProfile).append($(viewButton));
    $(newProfile).append(" ");

    const activateButton = profile.active ?
        $("<button class='btn-link-ActivatedProfile rounded' data-id='" + profile.id.toString() + "'>")
            .append("Deactivate") :
        $("<button class='btn-link-DeactivatedProfile rounded' data-id='" + profile.id.toString() + "'>")
            .append("Activate");

    //(IIFE) Invoked function expression to pass profile data
    (function (tempProfileData) {
        $(activateButton).on("click", event => {
            //Send an axios request to the server and check for a successful response
            const activateToggle = $(event.target).hasClass("btn-link-DeactivatedProfile");
            toggleProfile(
                tempProfileData.name,
                tempProfileData.id != null ?
                    tempProfileData.id :
                    +$(event.target).attr("data-id"),
                activateToggle)
                .then(r => {
                    if (r != null &&
                        r.status === 205) {
                        if (activateToggle) {
                            //Deactivate other activated profiles first, 
                            //skip if it's the current click target.
                            $("button.btn-link-ActivatedProfile").each((i, v) => {
                                if ($(v) !== $(event.target)) {
                                    $(v)
                                        .attr({ 'class': 'btn-link-DeactivatedProfile rounded' })
                                        .text('Activate');
                                }
                            });
                            $(event.target)
                                .attr({ 'class': 'btn-link-ActivatedProfile rounded' })
                                .text('Deactivate');
                        } else {
                            $(event.target)
                                .attr({ 'class': 'btn-link-DeactivatedProfile rounded' })
                                .text('Activate');
                        }
                    } else {
                        console.error("Problem changing status on profile");
                    }
                });
        })
    })(profile); //Pass profile variable

    $(newProfile).append(activateButton);
    $(profilesList).append(newProfile);
    $(newProfile).append($(activateButton));
    $(newProfile).append(" ");

    // End New

    const editButton = $("<button>")
        .addClass("btn-link-edit rounded")
        .append("Edit");

    //(IIFE) Invoked function expression to pass profile data
    (function (profileData) {
        $(editButton).on("click", () => {
            //Empty the LI
            $(newProfile).empty();

            //Replace the text with a text input box
            generateEditProfileControls($(newProfile), profileData)
        })
    })(profile); //Pass profile variable and call right away        

    $(newProfile).append($(editButton));
    $(newProfile).append(" ");

    const deleteButton = $("<button class='btn-link-delete rounded'>")
        .append("Delete");

    //(IIFE) Invoked function expression to pass profile data
    (function (temp_profile) {
        $(deleteButton).on("click", () => {
            //Send an axios request to the server and check for a successful
            //delete
            if (deleteProfileId(temp_profile.id)) {
                //Remove the selected profile
                $(newProfile).remove();
                //Clean up the profile list by removing the top divider if
                //it exists.
                cleanUpProfileList();
            }
        })
    })(profile); //Pass profile variable

    $(newProfile).append(deleteButton);
    $(profilesList).append(newProfile);
}

/**
 * Create add new profile controls
 * Modifies the DOM
 * @return {object}
 */
function generateProfileControls() {
    const profileLI = $("<li>")
        .addClass('userProfilesControls');

    $(profileLI).append($("<hr>")
        .addClass('smallestDivider mx-auto')
        .css({ 'color': 'white' }));

    const newButton = $("<button>")
        .text("Add New")
        .addClass("btnAction rounded placeholder-wave")
        .on("click", (event) => addNewProfileMenu(event));

    $(profileLI).append(newButton);

    return profileLI;
}

/**
 * Create edit profile controls when a profile is viewed. 
 * Scrolls to the top of the webpage.
 * Modifies the DOM.
 * @param {object} event - Event Handler from the click event
 * @returns {void}
 */
function generateEditProfileControlsFromUserDash(event) {
    window.scrollTo(0, 0);
    $(".userControlsTitleText").css({
        'margin-bottom': '30px',
        'margin-top': '30px'
    });
    let profileName = cleanHTMLString($(event.target).attr("data-label"));
    const profileEditInputText = $("<input>")
        .attr({
            "name": "changeExistingProfileName",
            "type": "text",
            "placeholder": "Edit Profile Name"
        })
        .addClass("editProfileInputFromProfileDash")
        .val(profileName);

    const editSubmitButton = $("<button>")
        .addClass("btn-EditProfileSubmitFromProfileDashboard rounded placeholder-wave")
        .text("Edit Profile");

    $(editSubmitButton).on("click", async () => {
        if ($(profileEditInputText).val().length === 0) {
            //Apply error styles if there is no input for the new profile name.
            $(profileEditInputText).css({
                "background-color": "yellow",
                "color": "red",
                "font-style": "bold",
                "border": "2px dashed red",
                "padding-top": "-1px",
                "padding-bottom": "-1px",
                "padding-left": "0px",
                "padding-right": "0px"
            })
                //Change placeholder to direct next action to user to fix the error.
                .attr({ "placeholder": "Profile Name must be filled." })
                //Update the element.
                .change();

            //Remove the error styling if profile name has been typed in.
            $(profileEditInputText).on("change keydown paste input", () => {
                //Check for change in input value.
                if ($(profileEditInputText).val().length !== 0) {
                    //Disable listen event once length has been input.
                    $(profileEditInputText).off("change keydown paste input");

                    //Update style for input text box so that error styling
                    // is removed.
                    $(profileEditInputText).css({
                        "background-color": "white",
                        "color": "black",
                        "font-style": "normal",
                        "border": "0px white",
                        "padding-top": "0px",
                        "padding-bottom": "0px",
                        "padding-left": "3px",
                        "padding-right": "3px"
                    })
                        //Change placeholder back to normal.
                        .attr({ "placeholder": "Edit Profile Name" })
                        //Update the element.
                        .change();
                }
            });

            //End function early
            return;
        }

        //Referenced boolean to check for change in an inner scope function.
        let patchComplete = [false];
        try {
            await editProfileName($(profileEditInputText).val(),
                cleanHTMLString($(event.target).attr("data-id")))
                .then(response => {
                    if (response != null &&
                        response.status === 205) {
                        // Update profileName
                        profileName = $(profileEditInputText).val();
                        patchComplete[0] = true;
                    }
                });

        } catch (exception) {
            if (exception == null ||
                exception.response.status === 404)
                return;

            //Server reported a conflict in name. Input must be a different
            // profile name.
            if (exception.response.status === 409) {
                $(profileEditInputText)
                    .css({
                        "background-color": "yellow",
                        "color": "red",
                        "font-style": "bold",
                        "border": "2px dashed red",
                        "padding-top": "-1px",
                        "padding-bottom": "-1px",
                        "padding-left": "0px",
                        "padding-right": "0px"
                    })
                    .attr({ "placeholder": "Profile name conflict. Try again." })
                    .val('');

                $(profileEditInputText).on("change keydown paste input", () => {
                    //Check for change in input value.
                    if ($(profileEditInputText).val().length !== 0) {
                        //Disable listen event once the key has been input.
                        $(profileEditInputText).off("change keydown paste input");

                        //Update style for input textbox so that error styling
                        // is removed.
                        $(profileEditInputText).css({
                            "background-color": "white",
                            "color": "black",
                            "font-style": "normal",
                            "border": "0px white",
                            "padding-top": "0px",
                            "padding-bottom": "0px",
                            "padding-left": "3px",
                            "padding-right": "3px"
                        })
                            //Change placeholder back to normal.
                            .attr({ "placeholder": "Edit Profile Name" })
                            //Update the element.
                            .change();
                    }
                });

                return;
                //Server reports no change in profile name.

            } else if (exception.response.status === 304) {
                $(profileEditInputText)
                    .css({
                        "background-color": "yellow",
                        "color": "red",
                        "font-style": "bold",
                        "border": "2px dashed red",
                        "padding-top": "-1px",
                        "padding-bottom": "-1px",
                        "padding-left": "0px",
                        "padding-right": "0px"
                    })
                    .attr({ "placeholder": "No change detected. Try again." })
                    .val('');

                $(profileEditInputText).on("change keydown paste input", () => {
                    //Check for change in input value.
                    if ($(profileEditInputText).val().length !== 0) {
                        //Disable listen event once length has been input.
                        $(profileEditInputText).off("change keydown paste input");

                        //Update style for input text box so that error styling
                        // is removed.
                        $(profileEditInputText).css({
                            "background-color": "white",
                            "color": "black",
                            "font-style": "normal",
                            "border": "0px white",
                            "padding-top": "0px",
                            "padding-bottom": "0px",
                            "padding-left": "3px",
                            "padding-right": "3px"
                        })
                            //Change placeholder back to normal.
                            .attr({ "placeholder": "Edit Profile Name" })
                            //Update the element.
                            .change();
                    }
                });

                return;
            }
            //Debug for any other exceptions.
            console.warn("Edit Profile Name from Profile Dash Exception");
            console.error(exception);
        }

        //Check if there was a successful change in the previous code block.
        if (!patchComplete[0])
            return;

        //Remove the edit profile controls and display the Profile again.
        $('#profileNameEditBody').empty();

        $('.userControlsTitleText').empty();
        $(".userControlsTitleText").css({
            'margin-bottom': '-20px',
            'margin-top': '0px'
        });
        $('.userControlsTitleText').text(profileName);

        //Disable the edit name button event and update changes.
        $('.btnEditProfileName').off('click');

        $('.btnEditProfileName').attr({
            'data-label': profileName.toString()
        });

        $('.btn-EditProfileSubmitFromProfileDashboard').remove();
        $('.btn-EditProfileCancelFromProfileDashboard').remove();
        $('#profileNameEditBody').hide();
        $("#dividerBeforeEditName").show();
        $('.btnEditProfileName').show();
    });

    const cancelButton = $("<button>")
        .addClass("btn-EditProfileCancelFromProfileDashboard rounded")
        .text("Cancel");

    //Redisplay the profile, with no side effects.
    $(cancelButton).on("click", () => {
        $(".userControlsTitleText").css({
            'margin-bottom': '-20px',
            'margin-top': '0px'
        }).change();

        $('.userControlsTitleText').empty();
        $('.userControlsTitleText').text(profileName);

        $('.btn-EditProfileSubmitFromProfileDashboard').remove();
        $('.btn-EditProfileCancelFromProfileDashboard').remove();

        $('#profileNameEditBody').hide();
        $("#dividerBeforeEditName").show();
        $('.btnEditProfileName').show();
    });

    $('.userControlsTitleText').empty();
    $('.userControlsTitleText').append($(profileEditInputText));

    $("#dividerBeforeEditName").hide();
    $('.btnEditProfileName').hide();

    $('#profileNameEditBody').append($(editSubmitButton));
    $('#profileNameEditBody').append(" ");
    $('#profileNameEditBody').append($(cancelButton));
}

/**
 * Create edit profile controls. Modifies the DOM.
 * From the user dashboard
 * @param {object} parent - The LI parent to append to.
 * @param {Promise} profile - The profile object to be edited, and re-displayed.
 * @returns {void}
 */
function generateEditProfileControls(parent, profile) {
    const profileEditInputText = $("<input>")
        .attr({
            "name": "changeExistingProfileName",
            "type": "text",
            "placeholder": "Edit Profile Name"
        })
        .addClass("editProfileInput")
        .val(profile.name);

    const editSubmitButton = $("<button>")
        .addClass("btn-EditProfileSubmit rounded bg-primary placeholder-wave")
        .text("Edit Profile");

    $(editSubmitButton).on("click", async () => {
        if ($(profileEditInputText).val().length === 0) {
            //Apply error styles if there is no input for the new profile name.
            $(profileEditInputText).css({
                "background-color": "yellow",
                "color": "red",
                "font-style": "bold",
                "border": "2px dashed red",
                "padding-top": "-1px",
                "padding-bottom": "-1px",
                "padding-left": "0px",
                "padding-right": "0px"
            })
                //Change placeholder to direct next action to user to fix the error.
                .attr({ "placeholder": "Profile Name must be filled." })
                //Update the element.
                .change();

            //Remove the error styling if profile name has been typed in.
            $(profileEditInputText).on("change keydown paste input", () => {
                //Check for change in input value.
                if ($(profileEditInputText).val().length !== 0) {
                    //Disable listen event once length has been input.
                    $(profileEditInputText).off("change keydown paste input");

                    //Update style for input text box so that error styling
                    // is removed.
                    $(profileEditInputText).css({
                        "background-color": "white",
                        "color": "black",
                        "font-style": "normal",
                        "border": "0px white",
                        "padding-top": "0px",
                        "padding-bottom": "0px",
                        "padding-left": "3px",
                        "padding-right": "3px"
                    })
                        //Change placeholder back to normal.
                        .attr({ "placeholder": "Edit Profile Name" })
                        //Update the element.
                        .change();
                }
            });

            //End function early
            return;
        }

        //Referenced boolean to check for change in an inner scope function.
        let patchComplete = [false];
        try {
            await editProfileName($(profileEditInputText).val(),
                profile.id.toString())
                .then(response => {
                    if (response != null &&
                        response.status === 205) {
                        profile.name = $(profileEditInputText).val();
                        patchComplete[0] = true;
                    }
                });

        } catch (exception) {
            if (exception.response == null ||
                exception.response.status === 404)
                return;

            //Server reported a conflict in name. Input must be a different
            // profile name.
            if (exception.response.status === 409) {
                $(profileEditInputText)
                    .css({
                        "background-color": "yellow",
                        "color": "red",
                        "font-style": "bold",
                        "border": "2px dashed red",
                        "padding-top": "-1px",
                        "padding-bottom": "-1px",
                        "padding-left": "0px",
                        "padding-right": "0px"
                    })
                    .attr({ "placeholder": "Profile name conflict. Try again." })
                    .val('');

                $(profileEditInputText).on("change keydown paste input", () => {
                    //Check for change in input value.
                    if ($(profileEditInputText).val().length !== 0) {
                        //Disable listen event once the key has been input.
                        $(profileEditInputText).off("change keydown paste input");

                        //Update style for input textbox so that error styling
                        // is removed.
                        $(profileEditInputText).css({
                            "background-color": "white",
                            "color": "black",
                            "font-style": "normal",
                            "border": "0px white",
                            "padding-top": "0px",
                            "padding-bottom": "0px",
                            "padding-left": "3px",
                            "padding-right": "3px"
                        })
                            //Change placeholder back to normal.
                            .attr({ "placeholder": "Edit Profile Name" })
                            //Update the element.
                            .change();
                    }
                });

                return;

                //Server reports no change in profile name.
            } else if (exception.response.status === 304) {
                $(profileEditInputText)
                    .css({
                        "background-color": "yellow",
                        "color": "red",
                        "font-style": "bold",
                        "border": "2px dashed red",
                        "padding-top": "-1px",
                        "padding-bottom": "-1px",
                        "padding-left": "0px",
                        "padding-right": "0px"
                    })
                    .attr({ "placeholder": "No change detected. Try again." })
                    .val('');

                $(profileEditInputText).on("change keydown paste input", () => {
                    //Check for change in input value.
                    if ($(profileEditInputText).val().length !== 0) {
                        //Disable listen event once length has been input.
                        $(profileEditInputText).off("change keydown paste input");

                        //Update style for input text box so that error styling
                        // is removed.
                        $(profileEditInputText).css({
                            "background-color": "white",
                            "color": "black",
                            "font-style": "normal",
                            "border": "0px white",
                            "padding-top": "0px",
                            "padding-bottom": "0px",
                            "padding-left": "3px",
                            "padding-right": "3px"
                        })
                            //Change placeholder back to normal.
                            .attr({ "placeholder": "Edit Profile Name" })
                            //Update the element.
                            .change();
                    }
                });

                return;
            }

            //Debug for any other exceptions.
            console.warn("Edit Profile Name Exception");
            console.error(exception);
        }

        //Check if there was a successful change in the previous code block.
        if (!patchComplete[0])
            return;

        //Remove the edit profile controls and display the profile again.
        $(parent).empty();

        const newViewButton = $("<button>")
            .addClass("btn-link rounded")
            .append("View");

        const newActivateButton = profile.active ?
            $("<button class='btn-link-ActivatedProfile rounded' id=''>")
                .append("Deactivate") :
            $("<button class='btn-link-DeactivatedProfile rounded'>")
                .append("Activate");

        const newEditButton = $("<button>")
            .addClass("btn-link-edit rounded")
            .append("Edit");

        const newDeleteButton = $("<button>")
            .addClass("btn-link-delete rounded")
            .append("Delete");

        //(IIFE) Invoked function expression to pass profile data
        (profileData =>
            $(newViewButton).on("click", () => location.href = `/profile/${profileData.id}`)
        )(profile); //Pass profile variable and call right away

        //(IIFE) Invoked function expression to pass profile data
        (function (profileData) {
            $(newEditButton).on("click", () => {
                //Empty the LI
                $(parent).empty();

                //Replace the text with a text input box
                generateEditProfileControls($(parent), profileData);
            });

        })(profile); //Pass profile variable and call right away

        //(IIFE) Invoked function expression to pass profile data
        (function (profileData) {
            $(newDeleteButton).on("click", () => {
                //Send an axios request to the server and check for a successful
                //delete
                if (deleteProfileId(profileData.id)) {
                    //Remove the selected profile
                    $(parent).remove();
                    //Clean up the profile list by removing the top divider if
                    //it exists.
                    cleanUpProfileList();
                }
            });

        })(profile); //Pass profile variable and call right away

        $(parent).append($("<hr>")
            .addClass('smallDivider mx-auto')
            .css({ 'color': 'white' }));

        $(parent).append(profile.name);
        $(parent).append($("<br>"));
        $(parent).append($(newViewButton));
        $(parent).append(" ");
        $(parent).append($(newActivateButton));
        $(parent).append(" ");
        $(parent).append($(newEditButton));
        $(parent).append(" ");
        $(parent).append($(newDeleteButton));

        //Cleanup the hr element for the top row.
        cleanUpProfileList();
    });

    const cancelButton = $("<button>")
        .addClass("btn-EditProfileCancel rounded bg-danger")
        .text("Cancel");

    //Redisplay the profile, with no side effects.
    $(cancelButton).on("click", () => {
        $(parent).empty();

        const viewButton = $("<button>")
            .addClass("btn-link rounded")
            .append("View");

        const activateButton = profile.active ?
            $("<button class='btn-link-ActivatedProfile rounded' id=''>")
                .append("Deactivate") :
            $("<button class='btn-link-DeactivatedProfile rounded'>")
                .append("Activate");

        const editButton = $("<button>")
            .addClass("btn-link-edit rounded")
            .append("Edit");

        const deleteButton = $("<button>")
            .addClass("btn-link-delete rounded")
            .append("Delete");

        //(IIFE) Invoked function expression to pass profile data
        (profileData =>
            $(viewButton).on("click", () => location.href = `/profile/${profileData.id}`)
        )(profile); //Pass profile variable and call right away

        //(IIFE) Invoked function expression to pass profile data
        (function (profileData) {
            $(editButton).on("click", () => {
                //Empty the LI
                $(parent).empty();

                //Replace the text with a text input box
                generateEditProfileControls($(parent), profileData);
            });

        })(profile); //Pass profile variable and call right away

        //(IIFE) Invoked function expression to pass profile data
        (function (profileData) {
            $(deleteButton).on("click", () => {
                //Send an axios request to the server and check for a successful
                //delete
                if (deleteProfileId(profileData.id)) {
                    //Remove the selected profile
                    $(parent).remove();
                    //Clean up the profile list by removing the top divider if
                    //it exists.
                    cleanUpProfileList();
                }
            });
        })(profile); //Pass profile variable and call right away

        $(parent).append($("<hr>")
            .addClass('smallDivider mx-auto')
            .css({ 'color': 'white' }));

        $(parent).append(profile.name);
        $(parent).append($("<br>"));
        $(parent).append($(viewButton));
        $(parent).append(" ");
        $(parent).append($(activateButton));
        $(parent).append(" ");
        $(parent).append($(editButton));
        $(parent).append(" ");
        $(parent).append($(deleteButton));

        cleanUpProfileList();
    });

    $(parent).append($("<hr>")
        .addClass('smallDivider mx-auto')
        .css({ 'color': 'white' }));

    $(parent).append($(profileEditInputText));
    $(parent).append($("<br>"));
    $(parent).append($(editSubmitButton));
    $(parent).append(" ");
    $(parent).append($(cancelButton));

    cleanUpProfileList();
}

/**
 * Deletes a profile from the profile dashboard then directs the user back to user dashboard.
 * Modifies the DOM (by sending the user back to the user dashboard.)
 * @param {number} profileId - Profile ID to delete
 * @returns {void}
 */
function deleteProfileFromUserDash(profileId) {
    //Send an axios request to the server and check for a successful
    //delete
    if (!deleteProfileId(profileId)) {
        showMessage("There was an error deleting the profile. Check the browser console for details.", "danger");
        return;
    }

    location.href = `/user_dashboard`;
}

/**
 * Cleanup Profile list by removing the top-most divider element when DOM is
 * changed.
 * Modifies the DOM.
 * @returns {void}
 */
function cleanUpProfileList() {
    const profileList = $(".userProfilesList");

    if (profileList == null)
        return;

    //console.debug("profileList");
    //console.debug(profileList);
    const profileListChild = $(profileList).children()[0];
    if (profileListChild == null ||
        profileListChild.length === 0)
        return;

    //console.debug("profileListChild");
    //console.debug(profileListChild);
    const dividerElement = $(profileListChild).children()[0];
    if (dividerElement == null ||
        dividerElement.length === 0)
        return;

    //console.debug("dividerElement");
    //console.debug(dividerElement);
    if ($(dividerElement).is("hr")) {
        //console.debug("Cleanup");
        $(dividerElement).remove();
    }
}

/**
 * Creates an element with row data retrieved from the retrieve data complete REST endpoint.
 * @returns {Promise} v - Response data returned from a query
 * @returns {string}
 */
function generateJobRowTemplateProfile(v) {
    let returnHTML = `
    <div class="userJobListLink figure rounded bg-dark mb-2 px-lg-1 px-xl-2 px-xxl-3 py-1 py-lg-2">
        <span style="font-size:17px;">${v.name}</span>
        <br />`;

    if (v.company != null &&
        v.company !== '') {
        returnHTML += `<span class="fluidLongTextFlex text-primary"
                             style="font-size:15px;">${v.company}</span>
        <br />`;
    }

    if (v.location != null &&
        v.location !== '') {
        returnHTML += `<span class="fluidLongTextFlex text-warning"
                             style="font-size:14px">${v.location}</span>
            <br />`;
    }

    if (v.job_type != null &&
        v.job_type !== '') {
        returnHTML += `<span class="fluidLongTextFlex text-info"
                             style="font-size:14px">${v.job_type}</span>
            <br />`;
    }

    if (v.description != null &&
        v.description !== "No Description" &&
        v.description !== "") {
        returnHTML += `<hr class="mx-5" style="color:white;" />
            <span class="fluidUserLongTextFlex"
                  style="font-size:15px;">${v.description}</span>
            <br />
            <hr class="mx-5" style="color:white;" />`;

    } else {
        returnHTML += `<hr class="smallestDivider mx-auto" style="color:white;" />`;
    }

    if (v.salary_currency != null &&
        v.salary_currency !== "") {
        let salary = v.salary_currency.toString();

        if (v.max_salary !== 0 &&
            v.min_salary !== 0) {
            salary = "~" +
                salary +
                (Math.floor(v.max_salary + v.min_salary) / 2).toLocaleString();

        } else if (v.min_salary !== 0 &&
            v.max_salary === 0) {
            salary += v.min_salary.toLocaleString() + "+";

        } else {
            salary = "up to " +
                salary + v.max_salary.toLocaleString();
        }

        if (salary != 0) {
            returnHTML += `
            <span class="text-info"
                  style="font-size:15px;font-weight: bolder;">Salary:</span>
            <span class="fluidLongTextFlex"
                  style="font-size:15px;"> ${salary}</span>
            <br />
            <hr class="mx-5" style="color:white;" />`;
        }
    }

    returnHTML += `<button data-action="viewJob"
                           class="btn-linkUserMini rounded bg-primary" 
                           data-id="${v.id.toString()}"
                           onclick="viewJob(event);">View</button>`;

    returnHTML += `<button data-action="toggleJobProfileDash" 
                           class="btn-linkUserMini-longer rounded bg-danger"
                           data-id="${v.id.toString()}"
                           onclick="toggleJob(event);">Un-save</button>`;

    returnHTML += `<button data-action="editJobProfile" 
                           class="btn-linkUserMini rounded bg-success"
                           data-id="${v.id.toString()}"
                           onclick="editSavedJob(event);">Edit</button>`;

    const tempListName = v.list_name == null || v.list_name === '' ? "Unnamed" : v.list_name.toString();
    const tempOrder = v.order == null || v.order === '' ? "No Order" : v.order.toString();

    returnHTML += `<br />
        <span class="fluidUserLongTextFlex text-info">${new Date(v.posted_time_utc.toString()).toDateString()}</span>
        <hr class="smallestDivider mx-auto" style="color:white;" />
        <div id="savedJobDataDash-${v.id.toString()}">
            <span class="fluidUserLongTextFlex text-info">List Name: </span>
            <span class='fluidUserLongTextFlex' 
                  id='savedJobListName-${v.id.toString()}'>${tempListName}</span>
            | 
            <span class="fluidUserLongTextFlex text-info">Order: </span>
            <span class='fluidUserLongTextFlex' 
                  id='savedJobOrder-${v.id.toString()}'>${tempOrder}</span>
            <br/>
            <span class="fluidUserLongTextFlex text-info">Notes</span>
            <br/>`;

    tempNotes = "Empty";
    if (v.notes != null &&
        v.notes !== "") {
        if (v.notes.length > 80) {
            tempNotes = v.notes.substring(0, 80) + "...";
        } else {
            tempNotes = v.notes;
        }
    }

    returnHTML += `<span class='fluidUserLongTextFlex' 
                         id='savedJobNotes-${v.id.toString()}'>${tempNotes}</span>`;

    return returnHTML + `</div></div>`;
}

/**
 * Generates HTML required to display companies provided by the server's REST endpoint.
 * Creates an element with row data retrieved from the Get Companies REST endpoint.
 * @returns {Promise} v - Response data returned from a Company query
 * @returns {string}
 */
function generateCompanyRowTemplateProfile(v) {
    let returnHTML = `
    <div class="userCompanyListLink figure rounded bg-dark mb-2 px-lg-1 px-xl-2 px-xxl-3 py-1 py-lg-2">
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

    if (v.description != null &&
        v.description !== "No Description" &&
        v.description !== "") {
        returnHTML += `<hr class="mx-5" style="color:white;" />
            <span class="fluidLongTextFlex"
                style="font-size:15px;">${v.description}</span>
            <br />
            <hr class="mx-5" style="color:white;" />`;

    } else {
        returnHTML += `<hr class="smallestDivider mx-auto" style="color:white;" />`;
    }

    returnHTML += `<button data-action="viewCompany"
                           class="btn-linkUserMini rounded bg-primary"
                           data-id="${v.id.toString()}" 
                           onclick="viewCompany(event);">View</button>`;

    returnHTML += `<button data-action="toggleCompanyProfileDash" 
                           class="btn-linkUserMini-longer rounded bg-danger"
                           data-id="${v.id.toString()}" 
                           onclick="toggleCompany(event);">Un-save</button>`;

    returnHTML += `<button data-action="editCompanyProfile" 
                           class="btn-linkUserMini rounded bg-success"
                           data-id="${v.id.toString()}"
                           onclick="editSavedCompany(event);">Edit</button>`;

    const tempListName = v.list_name == null || v.list_name === '' ? "Unnamed" : v.list_name.toString();
    const tempOrder = v.order == null || v.order === '' ? "No Order" : v.order.toString();


    returnHTML += `<br />
        <span class="fluidUserLongTextFlex text-info">${new Date(v.last_updated.toString()).toDateString()}</span>
        <hr class="smallestDivider mx-auto" style="color:white;" />
        <div id="savedCompanyDataDash-${v.id.toString()}">
            <span class="fluidUserLongTextFlex text-info">List Name: </span>
            <span class='fluidUserLongTextFlex' 
                  id='savedCompanyListName-${v.id.toString()}'>${tempListName}</span>
            | 
            <span class="fluidUserLongTextFlex text-info">Order: </span>
            <span class='fluidUserLongTextFlex' 
                  id='savedCompanyOrder-${v.id.toString()}'>${tempOrder}</span>
            <br/>
            <span class="fluidUserLongTextFlex text-info">Notes</span>
            <br/>`;

    tempNotes = "Empty";
    if (v.notes != null &&
        v.notes !== "") {
        if (v.notes.length > 80) {
            tempNotes = v.notes.substring(0, 80) + "...";
        } else {
            tempNotes = v.notes;
        }
    }

    returnHTML += `<span class='fluidUserLongTextFlex' 
                         id='savedCompanyNotes-${v.id.toString()}'>${tempNotes}</span>`;

    return returnHTML + `</div></div>`;
}

/**
 * Recreates the element with updated SavedJob data modified by user or data that was received by the server through
 * the REST endpoint.
 * @returns {?Promise} v - Job containing SavedJob Data (Modified by client and updated by server, or original data)
 * @returns {string}
 */
function regenerateJobDashData(v) {
    if (v == null) {
        return;
    }

    tempNotes = "Empty";
    if (v.notes != null &&
        v.notes !== "") {
        if (v.notes.length > 80) {
            tempNotes = v.notes.substring(0, 80) + "...";
        } else {
            tempNotes = v.notes;
        }
    }

    return `<span class="fluidUserLongTextFlex text-info">List Name: </span>
    <span class='fluidUserLongTextFlex' 
          id='savedJobListName-${v.id.toString()}'>${v.list_name == null ? "Unnamed" : v.list_name}</span>
    | 
    <span class="fluidUserLongTextFlex text-info">Order: </span>
    <span class='fluidUserLongTextFlex' 
          id='savedJobOrder-${v.id.toString()}'>${v.order == null ? "No Order" : v.order.toString()}</span>
    <br/>
    <span class="fluidUserLongTextFlex text-info">Notes</span>
    <br/>
    <span class='fluidUserLongTextFlex' 
          id='savedJobNotes-${v.id.toString()}'>${tempNotes}</span>`;
}

/**
 * Recreates the element with updated SavedCompany data modified by user or data that was received by the server through
 * the REST endpoint.
 * @returns {?Promise} v - Company containing SavedCompany Data (Modified by client and updated by server, or original data)
 * @returns {string}
 */
function regenerateCompanyDashData(v) {
    if (v == null) {
        return;
    }

    tempNotes = "Empty";
    if (v.notes != null &&
        v.notes !== "") {
        if (v.notes.length > 80) {
            tempNotes = v.notes.substring(0, 80) + "...";
        } else {
            tempNotes = v.notes;
        }
    }

    return `<span class="fluidUserLongTextFlex text-info">List Name: </span>
    <span class='fluidUserLongTextFlex' 
          id='savedCompanyListName-${v.id.toString()}'>${v.list_name == null ? "Unnamed" : v.list_name}</span>
    | 
    <span class="fluidUserLongTextFlex text-info">Order: </span>
    <span class='fluidUserLongTextFlex' 
          id='savedCompanyOrder-${v.id.toString()}'>${v.order == null ? "No Order" : v.order.toString()}</span>
    <br/>
    <span class="fluidUserLongTextFlex text-info">Notes</span>
    <br/>
    <span class='fluidUserLongTextFlex' 
          id='savedCompanyNotes-${v.id.toString()}'>${tempNotes}</span>`;
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
 * Adds edit buttons to show form elements allowing the user to change list name, order, and notes for the Job.
 * Modifies the DOM
 * @param {object} event - Event when user clicks on the edit button for the respective job.
 * @returns {void}
 */
async function editSavedJob(event) {
    event.preventDefault();
    $(event.target).off("click");

    const cancelButton = $('<button>')
        .attr({
            'data-action': 'cancelEditJobProfile',
            'class': 'btn-linkUserMini-longer rounded bg-warning',
            'data-id': $(event.target).attr("data-id").toString(),
            'onclick': "cancelEditSavedJob(event);",
        })
        .text('Cancel')
        .insertAfter($(event.target));

    $(event.target).attr({
        'class': 'btn-linkUserMini rounded bg-primary',
        'data-action': 'completeUpdateSavedJobProfile',
        'onclick': '',
    }).text('Done');

    $(event.target).off('click');

    $(event.target).on('click', function (event) {
        completeEditSavedJob(event, cancelButton);
    });

    const savedJobId = $(event.target).attr("data-id");
    const dataControls = $("#savedJobDataDash-" + savedJobId);
    const listName = $(dataControls).children("#savedJobListName-" + savedJobId).text();
    const order = $(dataControls).children("#savedJobOrder-" + savedJobId).text();

    const notes = retrieveSavedJobNotes(event, savedJobId);
    $(dataControls).empty()
        .append(generateSavedDataControls(
            listName === "Unnamed" || listName == null ? "" : cleanListName(listName.toString()),
            order === "No Order" || order == null ? "" : order.toString(),
            notes === "Empty" || notes == null ? "" : notes.toString(),
            "JobId-" + savedJobId.toString()));
    // console.log(listName + " " + order + " " + notes);
}

/**
 * Adds edit buttons to show form elements allowing the user to change list name, order, and notes for the Company.
 * Modifies the DOM
 * @param {object} event - Event when user clicks on the edit button for the respective company.
 * @returns {void}
 */
async function editSavedCompany(event) {
    event.preventDefault();
    $(event.target).off("click");

    const cancelButton = $('<button>')
        .attr({
            'data-action': 'cancelEditCompanyProfile',
            'class': 'btn-linkUserMini-longer rounded bg-warning',
            'data-id': $(event.target).attr("data-id").toString(),
            'onclick': "cancelEditSavedCompany(event);",
        })
        .text('Cancel')
        .insertAfter($(event.target));

    $(event.target).attr({
        'class': 'btn-linkUserMini rounded bg-primary',
        'data-action': 'completeUpdateSavedCompanyProfile',
        'onclick': '',
    }).text('Done');

    $(event.target).off('click');

    $(event.target).on('click', function (event) {
        completeEditSavedCompany(event, cancelButton);
    });

    const savedCompanyId = $(event.target).attr("data-id");
    const dataControls = $("#savedCompanyDataDash-" + savedCompanyId);
    const listName = $(dataControls).children("#savedCompanyListName-" + savedCompanyId).text();
    const order = $(dataControls).children("#savedCompanyOrder-" + savedCompanyId).text();

    const notes = retrieveSavedCompanyNotes(event, savedCompanyId);
    $(dataControls).empty()
        .append(generateSavedDataControls(
            listName === "Unnamed" || listName == null ? "" : cleanListName(listName.toString()),
            order === "No Order" || order == null ? "" : order.toString(),
            notes === "Empty" || notes == null ? "" : notes.toString(),
            "CompanyId-" + savedCompanyId.toString()));
    // console.log(listName + " " + order + " " + notes);
}

/**
 * Deletes a job that has already been successfully removed by the user and reflected on the server.
 * If the user accidently deleted a job, user still has the ability to save it again.
 * The job will be saved without any customized data into an unnamed list, since it has been cleared, 
 * but saved in the unnamed list for pending deletion.
 * If the refresh button is clicked or the page has been refreshed, the job will automatically be cleared.
 * Modifies the DOM
 * @param {object} event - Event when user clicks on the delete button for the respective Job that has already been unsaved.
 * @returns {void}
 */
function deleteUnsavedJob(event) {
    event.preventDefault();
    $(event.target).off("click");
    const savedJobId = $(event.target).attr("data-id");
    if ($(event.target).attr('data-action') !== 'quickDeleteJobProfile') {
        // console.error("Delete unsaved job misfire");
        return;
    }

    if (savedJobs.has("Unnamed")) {
        savedJobs.set("Unnamed", savedJobs.get("Unnamed").filter(v => v.id !== +savedJobId));
        if (savedJobs.get("Unnamed").length === 0) {
            savedJobs.delete("Unnamed");
            //Clean up DOM by removing the empty list.
            quickRefreshSavedJobsDisplayData();
        }
    }
    //List Items
    const currentListName = ($(event.target)
        .parent(".userJobListLink")
        .parent(".fluidJobSingleDescription")
        .attr('id'))
        .replace("jobList-", "");

    const remainingListItems = $("#jobList-" + currentListName.toString())
        .children('.userJobListLink');
    //Check if this item is the last in the List.
    if ($(remainingListItems).length === 1) {
        //Clean up DOM by removing the empty list from a refresh.
        quickRefreshSavedJobsDisplayData();
    } else {
        $(event.target).parent().remove();
    }
}

/**
 * Deletes a company that has already been successfully removed by the user and reflected on the server.
 * If the user accidently deleted a company, user still has the ability to save it again.
 * The company will be saved without any customized data into an unnamed list, since it has been cleared, 
 * but saved in the unnamed list for pending deletion.
 * If the refresh button is clicked or the page has been refreshed, the company will automatically be cleared.
 * Modifies the DOM
 * @param {object} event - Event when user clicks on the delete button for the respective Company that has already been unsaved.
 * @returns {void}
 */
function deleteUnsavedCompany(event) {
    event.preventDefault();
    $(event.target).off("click");
    const savedCompanyId = $(event.target).attr("data-id");
    if ($(event.target).attr('data-action') !== 'quickDeleteCompanyProfile') {
        // console.error("Delete unsaved company misfire");
        return;
    }

    if (savedCompanies.has("Unnamed")) {
        savedCompanies.set("Unnamed", savedCompanies.get("Unnamed").filter(v => v.id !== +savedCompanyId));
        if (savedCompanies.get("Unnamed").length === 0) {
            savedCompanies.delete("Unnamed");
            //Clean up DOM by removing the empty list.
            quickRefreshSavedCompaniesDisplayData();
        }
    }
    //List Items
    const currentListName = ($(event.target)
        .parent(".userCompanyListLink")
        .parent(".fluidCompanySingleDescription")
        .attr('id'))
        .replace("companyList-", "");

    const remainingListItems = $("#companyList-" + currentListName.toString())
        .children('.userCompanyListLink');
    //Check if this item is the last in the List.
    if ($(remainingListItems).length === 1) {
        //Clean up DOM by removing the empty list from a refresh.
        quickRefreshSavedCompaniesDisplayData();
    } else {
        $(event.target).parent().remove();
    }
}

/**
 * Cancels an edit action and removes the form controls for the user, regenerating the previously displayed controls,
 * pulling data from the current Map of data.
 * Modifies the DOM
 * @param {object} event - Event when user clicks on the cancel button, discarding any data that was previously in the edit form.
 * @returns {void}
 */
function cancelEditSavedJob(event) {
    event.preventDefault();
    $(event.target).off("click");
    //Find previous data from loaded data and re-apply.
    const savedJobId = $(event.target).attr("data-id");
    $("#savedJobDataDash-" + savedJobId)
        .empty()
        .append(regenerateJobDashData(
            retrieveSavedJobData(
                +savedJobId,
                $(event.target).parent('div').parent('div').attr('id').replace('jobList-', '')
            )
        ));
    $(event.target)
        .parent()
        .children('button')
        .filter((i, v) => $(v).attr('data-action') === 'completeUpdateSavedJobProfile')
        .attr({
            'class': 'btn-linkUserMini rounded bg-success',
            'data-action': 'editJobProfile',
            'onclick': 'editSavedJob(event);',
        })
        .text('Edit');
    $(event.target).remove();
}

/**
 * Cancels an edit action and removes the form controls for the user, regenerating the previously displayed controls,
 * pulling data from the current Map of data.
 * Modifies the DOM
 * @param {object} event - Event when user clicks on the cancel button, discarding any data that was previously in the edit form.
 * @returns {void}
 */
function cancelEditSavedCompany(event) {
    event.preventDefault();
    $(event.target).off("click");
    //Find previous data from loaded data and re-apply.
    const savedCompanyId = $(event.target).attr("data-id");
    $("#savedCompanyDataDash-" + savedCompanyId)
        .empty()
        .append(regenerateCompanyDashData(
            retrieveSavedCompanyData(
                +savedCompanyId,
                $(event.target).parent('div').parent('div').attr('id').replace('companyList-', '')
            )
        ));
    $(event.target)
        .parent()
        .children('button')
        .filter((i, v) => $(v).attr('data-action') === 'completeUpdateSavedCompanyProfile')
        .attr({
            'class': 'btn-linkUserMini rounded bg-success',
            'data-action': 'editCompanyProfile',
            'onclick': 'editSavedCompany(event);',
        })
        .text('Edit');
    $(event.target).remove();
}

/**
 * Creates a responsive form for the user to input data such as list name, order, or notes.
 * Returns an element which can then be appended to the DOM
 * @param {?string} listName - Previous List Name of the Job or Company
 * @param {?string} order - Previous List Name of the Job or Company
 * @param {?string} notes - Previous Notes of the Job or Company
 * @param {?string} prefixId - String containing the ID and a prefix to distinguish form elements between Company or Job.
 * @returns {string}
 */
function generateSavedDataControls(listName = "", order = "", notes = "", prefixId) {
    return `<div class="container bg-none pt-2 mb-2 mb-md-0 justify-content-center align-items-center">
    <div class="row mb-6">
        <div class="col-12 col-md-12 col-lg-6 mb-2 mb-lg-0 px-1 px-lg-0 pb-1">
            <div class="input-group">
                <input class="manualQueryFormText form-control form-control-sm manualQueryFormTextBody"
                       type="text"
                       placeholder="List Name"
                       id="listNameControlInput-${prefixId.toString()}"
                       value="${listName.toString()}">
                </input>
            </div>
        </div>
        <div class="col-12 col-md-12 col-lg-6 mb-2 mb-lg-0 px-lg-0 px-1">
            <div class="input-group">
                <input class="manualQueryFormText form-control form-control-sm manualQueryFormTextBody"
                        type="text"
                        placeholder="Order (0-99)"
                        id="orderControlInput-${prefixId.toString()}"
                        value="${order.toString()}">
                </input>
            </div>
        </div>
    </div>
    <div class="row mb-12">
        <div class="col-12 col-md-12 col-lg-12 mb-2 mb-lg-0 px-lg-0 px-1">
                <textarea class="form-control manualQueryFormTextBody"
                          placeholder="Notes"
                          id="notesControlInput-${prefixId.toString()}">${notes.toString()}</textarea>
        </div>
    </div>
</div>`;
}

/**
 * Completes an edit request by the client, sending to the server a PATCH request,
 * then handles specific responses from the server
 * Removes the cancel button in all cases.
 * Modifies the DOM
 * @param {object} event - Event handler received when user clicks on the Done button after Editing the data for a job.
 * @param {object} cancelButton - Element that contains the cancel button, which will be deleted when Done is clicked.
 * @returns {void}
 */
async function completeEditSavedJob(event, cancelButton) {
    event.preventDefault();
    $(cancelButton).remove();
    const jobId = $(event.target).attr('data-id');
    const profileId = window.location.pathname.slice('/profile/'.length);
    //listName is set to ID for HTML elements in DOM so remove any whitespace.
    const oldListName = $(event.target).parent('div').parent('div').attr('id').replace('jobList-', '');
    const oldOrder = retrieveSavedJobData(jobId, oldListName).order;
    const newListName = cleanListName($("#listNameControlInput-JobId-" + jobId.toString()).val());
    const newOrder = $("#orderControlInput-JobId-" + jobId.toString()).val();
    const newNotes = $("#notesControlInput-JobId-" + jobId.toString()).val();

    await updateSavedJobData(
        profileId,
        jobId,
        newListName,
        newOrder,
        newNotes).then(r => {
            if (r == null ||
                r.status == null) {
                return;
            }

            if (r.status === 205) {
                $(event.target).attr({
                    'class': 'btn-linkUserMini rounded bg-success',
                    'data-action': 'editJobProfile',
                    'onclick': 'editSavedJob(event);',
                })
                    .text('Edit');

                // Side effects - Modifies and sorts Jobs map.
                const updatedJob = updateSavedJobOnMap(jobId, oldListName, newListName, newOrder, newNotes);

                if (updatedJob instanceof Boolean &&
                    !updatedJob) {
                    console.error("Could not update the Saved Jobs");
                    return;
                }

                //Call fast reload if the job list name and order has not been changed.
                if (oldListName === newListName &&
                    oldOrder === newOrder) {
                    // console.log("No order change, no list name change");
                    $("#savedJobDataDash-" + jobId)
                        .empty()
                        .append(
                            regenerateJobDashData(
                                retrieveSavedJobData(
                                    +jobId,
                                    updatedJob.list_name,
                                )
                            )
                        );
                    //Reload only the list of jobs if the 
                    //list name has remained the same but the order has changed.
                } else {
                    //Refresh entire Job dashboard div
                    quickRefreshSavedJobsDisplayData();
                }
            }
        }).catch(r => {
            //Status code from server for no change, not accepted. Accept it on client-side.
            if (r.status === 304) {
                $(event.target).attr({
                    'class': 'btn-linkUserMini rounded bg-success',
                    'data-action': 'editJobProfile',
                    'onclick': 'editSavedJob(event);',
                })
                    .text('Edit');
                $("#savedJobDataDash-" + jobId)
                    .empty()
                    .append(
                        regenerateJobDashData(
                            retrieveSavedJobData(
                                +jobId,
                                oldListName,
                            )
                        )
                    );
                return;
            }
            console.warning("Unhandled Exception");
            console.error(r);
        });
}

/**
 * Completes an edit request by the client, sending to the server a PATCH request,
 * then handles specific responses from the server
 * Removes the cancel button in all cases.
 * Modifies the DOM
 * @param {object} event - Event handler received when user clicks on the Done button after Editing the data for a company.
 * @param {object} cancelButton - Element that contains the cancel button, which will be deleted when Done is clicked.
 * @returns {void}
 */
async function completeEditSavedCompany(event, cancelButton) {
    event.preventDefault();
    $(cancelButton).remove();
    const companyId = $(event.target).attr('data-id');
    const profileId = window.location.pathname.slice('/profile/'.length);
    //listName is set to ID for HTML elements in DOM so remove any whitespace.
    const oldListName = $(event.target).parent('div').parent('div').attr('id').replace('companyList-', '');
    const oldOrder = retrieveSavedCompanyData(companyId, oldListName).order;
    const newListName = cleanListName($("#listNameControlInput-CompanyId-" + companyId.toString()).val());
    const newOrder = $("#orderControlInput-CompanyId-" + companyId.toString()).val();
    const newNotes = $("#notesControlInput-CompanyId-" + companyId.toString()).val();

    await updateSavedCompanyData(
        profileId,
        companyId,
        newListName,
        newOrder,
        newNotes).then(r => {
            if (r == null ||
                r.status == null) {
                return;
            }

            if (r.status === 205) {
                $(event.target).attr({
                    'class': 'btn-linkUserMini rounded bg-success',
                    'data-action': 'editCompanyProfile',
                    'onclick': 'editSavedCompany(event);',
                })
                    .text('Edit');

                // Side effects - Modifies and sorts Jobs map.
                const updatedCompany = updateSavedCompanyOnMap(companyId, oldListName, newListName, newOrder, newNotes);

                if (updatedCompany instanceof Boolean &&
                    !updatedCompany) {
                    console.error("Could not update the Saved Companies");
                    return;
                }

                //Call fast reload if the job list name and order has not been changed.
                if (oldListName === newListName &&
                    oldOrder === newOrder) {
                    // console.log("No order change, no list name change");
                    $("#savedCompanyDataDash-" + companyId)
                        .empty()
                        .append(
                            regenerateCompanyDashData(
                                retrieveSavedCompanyData(
                                    +companyId,
                                    updatedCompany.list_name,
                                )
                            )
                        );
                    //Reload only the list of companies if the 
                    //list name has remained the same but the order has changed.
                } else {
                    //Refresh entire Company dashboard div
                    quickRefreshSavedCompaniesDisplayData();
                }
            }
        }).catch(r => {
            //Status code from server for no change, not accepted. Accept it on client-side.
            if (r.status === 304) {
                $(event.target).attr({
                    'class': 'btn-linkUserMini rounded bg-success',
                    'data-action': 'editCompanyProfile',
                    'onclick': 'editSavedCompany(event);',
                })
                    .text('Edit');
                $("#savedCompanyDataDash-" + companyId)
                    .empty()
                    .append(
                        regenerateCompanyDashData(
                            retrieveSavedCompanyData(
                                +companyId,
                                oldListName,
                            )
                        )
                    );
                return;
            }
            console.warning("Exception");
            console.error(r);
        });
}

/**
 * Empties the Jobs Dashboard and regenerates the data from the currently saved Jobs Map.
 * Modifies the DOM
 * @returns {void}
 */
function quickRefreshSavedJobsDisplayData() {
    $("#profileJobsDashboard").empty();

    savedJobs.keys().forEach((v, i) => {
        if (i != 0) {
            $("#profileJobsDashboard").append('<hr class="smallerDivider mx-auto" style="color:white;" />');
        }

        $("#profileJobsDashboard")
            .append($("<div id='jobList-" + cleanListName(v).toString() + "'>")
                .attr({ 'class': 'fluidJobSingleDescription' })
                .text("List: " + v.toString())
                .append($('<hr class="smallDivider mx-auto" style="color:white;" />'))
                .append($("<br>"))
            );
    });

    savedJobs.forEach((v, k) => {
        v.forEach(i => {
            $("#jobList-" + cleanListName(k).toString()).append(generateJobRowTemplateProfile(i));
        });
    });
}

/**
 * Empties the Company Dashboard and regenerates the data from the currently saved Companies Map.
 * Modifies the DOM
 * @returns {void}
 */
function quickRefreshSavedCompaniesDisplayData() {
    $("#profileCompaniesDashboard").empty();

    savedCompanies.keys().forEach((v, i) => {
        if (i != 0) {
            $("#profileCompaniesDashboard").append('<hr class="smallerDivider mx-auto" style="color:white;" />');
        }

        $("#profileCompaniesDashboard")
            .append($("<div id='companyList-" + cleanListName(v).toString() + "'>")
                .attr({ 'class': 'fluidCompanySingleDescription' })
                .text("List: " + v.toString())
                .append($('<hr class="smallDivider mx-auto" style="color:white;" />'))
                .append($("<br>"))
            );
    });

    savedCompanies.forEach((v, k) => {
        v.forEach(i => {
            $("#companyList-" + cleanListName(k).toString()).append(generateCompanyRowTemplateProfile(i));
        });
    });
}

/**
 * Retrieves job data based on Job ID if it has been previously sent from the server.
 * @param {?number} jobId - Job ID of the Job to retrieve data for.
 * @param {?string} listName - List Name to look for in the Map, to save on iterating through the entire Map.
 * @returns {?object}
 */
function retrieveSavedJobData(jobId, listName) {
    if (!savedJobs.has(listName)) {
        return undefined;
        // console.error("Could not find List Name " + listName.toString() + " in saved jobs");
    }

    let selected_job = undefined;
    for (const i of savedJobs.get(listName)) {
        if (i.id === +jobId) {
            selected_job = i;
            break;
        }
    }

    if (selected_job == null) {
        console.error("Could not find job in map for modification in updateSavedJobOnMap()");
        return undefined;
    }

    return selected_job;
}

/**
 * Retrieves company data based on Company ID if it has been previously sent from the server.
 * @param {?number} companyId - Company ID of the Job to retrieve data for.
 * @param {?string} listName - List Name to look for in the Map, to save on iterating through the entire Map.
 * @returns {?object}
 */
function retrieveSavedCompanyData(companyId, listName) {
    if (!savedCompanies.has(listName)) {
        return undefined;
        // console.error("Could not find List Name " + listName.toString() + " in saved companies");
    }

    let selected_company = undefined;
    for (const i of savedCompanies.get(listName)) {
        if (i.id === +companyId) {
            selected_company = i;
            break;
        }
    }

    if (selected_company == null) {
        console.error("Could not find company in map for modification in updateSavedCompanyOnMap()");
        return undefined;
    }

    return selected_company;
}

/**
 * Updates a SavedJob on the client-side without sending a GET request to the server to retrieve updated changes.
 * Minimizes change to DOM by checking for changed values.
 * Reflects changes sent by the server or displayed by the client if the page were cleanly refreshed.
 * Returns false if there was no change or if the Job data cannot be found.
 * If successful, a data object containing the new data is inserted back into the Map and returned as a result
 * @param {number} jobId - Job ID of the Job
 * @param {string} oldListName - Previous list name of the job used to pull the data from
 * @param {string} newListName - New list name of the job to insert the job into
 * @param {number} newOrder - New order of the job to display for use in sorting
 * @param {string} newNotes - New order of the job to display for use in sorting
 * @returns {boolean|object}
 */
function updateSavedJobOnMap(jobId, oldListName, newListName, newOrder, newNotes) {
    //Find SavedJob from Old List
    let selected_job = undefined;
    for (const i of savedJobs.get(oldListName)) {
        if (i.id === +jobId) {
            selected_job = i;
            break;
        }
    }

    if (selected_job == null) {
        console.error("Could not find job in map for modification in updateSavedJobOnMap()");
        return false;
    }

    //Filter the job out
    savedJobs.set(oldListName, savedJobs.get(oldListName).filter(v => v.id !== selected_job.id));

    //If the list is empty, delete the key.
    if (savedJobs.get(oldListName).length === 0) {
        savedJobs.delete(oldListName);
    }

    if (newListName == null ||
        newListName === "") {
        newListName = "Unnamed";
    }

    if (selected_job.list_name === newListName &&
        selected_job.order === newOrder &&
        selected_job.notes === newNotes) {
        console.error("There was no change in the SavedJob in updateSavedJobOnMap()");
        return false;
    }

    // Make modifications to the Job
    if (selected_job.list_name !== newListName) {
        if (newListName === '' ||
            newListName == null) {
            newListName = null;
        }
        selected_job.list_name = cleanListName(newListName);
    }

    if (selected_job.order !== newOrder) {
        if (newOrder === '' ||
            newOrder == null) {
            newOrder = null;
        }
        selected_job.order = newOrder;
    }

    if (selected_job.notes !== newNotes) {
        if (newNotes === '' ||
            newNotes == null) {
            newNotes = null;
        }
        selected_job.notes = newNotes;
    }

    //Insert the new job back into the map
    if (!savedJobs.has(selected_job.list_name)) {
        savedJobs.set(selected_job.list_name, []);
    }

    savedJobs.get(selected_job.list_name).push(selected_job);

    sortSavedJobs();

    return selected_job;
}

/**
 * Updates a SavedCompany on the client-side without sending a GET request to the server to retrieve updated changes.
 * Minimizes change to DOM by checking for changed values.
 * Reflects changes sent by the server or displayed by the client if the page were cleanly refreshed.
 * Returns false if there was no change or if the Job data cannot be found.
 * If successful, a data object containing the new data is inserted back into the Map and returned as a result
 * @param {number} companyId - Company ID of the Company
 * @param {string} oldListName - Previous list name of the job used to pull the data from
 * @param {string} newListName - New list name of the company to insert the company into
 * @param {number} newOrder - New order of the company to display for use in sorting
 * @param {string} newNotes - New order of the company to display for use in sorting
 * @returns {boolean|object}
 */
function updateSavedCompanyOnMap(companyId, oldListName, newListName, newOrder, newNotes) {
    //Find SavedCompany from Old List
    let selected_company = undefined;
    for (const i of savedCompanies.get(oldListName)) {
        if (i.id === +companyId) {
            selected_company = i;
            break;
        }
    }

    if (selected_company == null) {
        console.error("Could not find company in map for modification in updateSavedCompanyOnMap()");
        return false;
    }

    //Filter the job out
    savedCompanies.set(oldListName, savedCompanies.get(oldListName).filter(v => v.id !== selected_company.id));

    //If the list is empty, delete the key.
    if (savedCompanies.get(oldListName).length === 0) {
        savedCompanies.delete(oldListName);
    }

    if (newListName == null ||
        newListName === "") {
        newListName = "Unnamed";
    }

    if (selected_company.list_name === newListName &&
        selected_company.order === newOrder &&
        selected_company.notes === newNotes) {
        console.error("There was no change in the SavedCompany in updateSavedCompanyOnMap()");
        return false;
    }

    // Make modifications to the Job
    if (selected_company.list_name !== newListName) {
        if (newListName === '' ||
            newListName == null) {
            newListName = null;
        }
        selected_company.list_name = cleanListName(newListName);
    }

    if (selected_company.order !== newOrder) {
        if (newOrder === '' ||
            newOrder == null) {
            newOrder = null;
        }
        selected_company.order = newOrder;
    }

    if (selected_company.notes !== newNotes) {
        if (newNotes === '' ||
            newNotes == null) {
            newNotes = null;
        }
        selected_company.notes = newNotes;
    }

    //Insert the new company back into the map
    if (!savedCompanies.has(selected_company.list_name)) {
        savedCompanies.set(selected_company.list_name, []);
    }

    savedCompanies.get(selected_company.list_name).push(selected_company);

    sortSavedCompanies();

    return selected_company;
}

/**
 * Sorts SavedJobs Map alphabetically,
 * ordering each list name by respective order values,
 * and sending null or empty list names (freshly added) jobs to the back of the array.
 * @returns {void}
 */
function sortSavedJobs() {
    //Sort by key
    //Unnamed is sent to the back
    savedJobs = new Map([...savedJobs.entries()].sort(([a], [b]) => {
        if (a == null ||
            a === "" ||
            a === "Unnamed") {
            return 1;
        }

        if (b == null ||
            b === "" ||
            b === "Unnamed") {
            return -1;
        }

        return a[0].localeCompare(b[0])
    }));

    //Sort Object order by order column as well.
    //Each key is mapped to an array of Objects.
    savedJobs.forEach(v => {
        v.sort((a, b) => {
            if (a.order == null) {
                return 1;
            }

            if (b.order == null) {
                return -1;
            }

            return a.order - b.order
        });
    });
}

/**
 * Sorts SavedCompanies Map alphabetically, 
 * ordering each list name by respective order values,
 * and sending null or empty list names (freshly added) companies to the back of the array.
 * @returns {void}
 */
function sortSavedCompanies() {
    //Sort by key
    //Unnamed is sent to the back
    savedCompanies = new Map([...savedCompanies.entries()].sort(([a], [b]) => {
        if (a == null ||
            a === "" ||
            a === "Unnamed") {
            return 1;
        }

        if (b == null ||
            b === "" ||
            b === "Unnamed") {
            return -1;
        }

        return a[0].localeCompare(b[0])
    }));

    //Sort Object order by order column as well.
    //Each key is mapped to an array of Objects.
    savedCompanies.forEach(v => {
        v.sort((a, b) => {
            if (a.order == null) {
                return 1;
            }

            if (b.order == null) {
                return -1;
            }

            return a.order - b.order
        });
    });
}

/**
 * Returns the selected Job's notes from within the Map instead of the short version shown in the DOM.
 * Uses the event to retrieve the respective list name in order to reduce iterating through the Saved Jobs Map.
 * @param {Event} event - The event handler (User clicked on a button)
 * @param {?number} jobId - The unique Job ID to retrieve
 * @returns {string}
 */
function retrieveSavedJobNotes(event, jobId) {
    if (event == null ||
        jobId == null) {
        console.error("Could not find event, or jobId in retrieveSavedJobNotes.");
        return;
    }
    const listName = $(event.target).parent('div').parent('div').attr('id').replace('jobList-', '');

    if (listName == null) {
        console.error("Could not find list name from event inm retrieveSavedJobNotes.");
        return;
    }
    for (const i of savedJobs.get(listName)) {
        if (i.id === +jobId) {
            if (i.notes === "" ||
                i.notes == null) {
                return "Empty";
            }
            return i.notes;
        }
    }
    return "Empty";
}

/**
 * Returns the selected Company's notes from within the Map instead of the short version shown in the DOM.
 * Uses the event to retrieve the respective list name in order to reduce iterating through the Saved Companies Map.
 * @param {Event} event - The event handler (User clicked on a button)
 * @param {?number} companyId - The unique Company ID to retrieve
 * @returns {string}
 */
function retrieveSavedCompanyNotes(event, companyId) {
    if (event == null ||
        companyId == null) {
        console.error("Could not find event, or companyId in retrieveSavedCompanyNotes.");
        return;
    }
    const listName = $(event.target).parent('div').parent('div').attr('id').replace('companyList-', '');

    if (listName == null) {
        console.error("Could not find list name from event inm retrieveSavedCompanyNotes.");
        return;
    }
    for (const i of savedCompanies.get(listName)) {
        if (i.id === +companyId) {
            if (i.notes === "" ||
                i.notes == null) {
                return "Empty";
            }
            return i.notes;
        }
    }
    return "Empty";
}
