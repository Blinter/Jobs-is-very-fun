/**
 * Deletes a profile object from the server
 * @param {number} profileID - ID of the profile to delete
 * @returns {boolean} - Result of the delete returned by the server.
 */
async function deleteProfileId(profileID) {
    await axios.delete(
        "/delete_profile_id/" +
        cleanString(profileID.toString()))
        .then(response => {
            if (response == null ||
                response.status == null)
                return false;

            if (response.status === 200)
                return true;
            return false;

        }).catch(exception => { console.error(exception); return false; });
}

/**
 * Grabs a profile object that can be processed in generateProfiles for the DOM.
 * @param {string} newProfileName - Name of new profile to create
 * @return {void}
 */
async function createProfileName(newProfileName) {
    try {
        return await axios.put(
            "/create_profile_name/" +
            cleanString(newProfileName.toString()));

    } catch (exception) {
        //Same name found
        if (exception != null && 
            exception.response != null &&
            exception.response.status == 409)
            return;

        console.warn("Create Profile Name Exception");
        console.error(exception);
        return;
        // throw exception;
    };
}

/**
 * Edits a profile name to reflect changes on the client.
 * @param {string} newProfileName - New name for the profile selected.
 * @param {number} profileId - existing ID of the profile selected.
 * @returns {?Promise}
 */
async function editProfileName(newProfileName, profileId) {
    try {
        return await axios.patch(
            "/change_profile_name_id/" +
            cleanString(profileId.toString()), {
            headers: { 'Content-Type': 'application/json' },
            new_name: cleanString(newProfileName.toString())
        });

    } catch (exception) {
        //Same name found
        if (exception != null &&
            exception.response != null &&
            exception.response.status == 404)
            return undefined;

        console.warn("Edit Profile Name Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Toggles a profile by name or ID. One of the values must be supplied.
 * @param {?string} currentProfileName - Name for the profile
 * @param {?number} profileId - ID of the profile
 * @param {?boolean} activateStatus - True to set current profile as active and deactive other profiles.
 * @returns {?Promise}
 */
async function toggleProfile(
    currentProfileName = undefined,
    profileId = undefined,
    activateStatus = undefined) {
    if (currentProfileName == null &&
        profileId == null) {
        return undefined;
    }
    try {
        return await axios.patch(
            "/toggle_profile/" +
            (activateStatus ? "1" : "0"), {
            headers: { 'Content-Type': 'application/json' },
            profile_name: currentProfileName != null && profileId != null ? cleanStringParam(currentProfileName.toString()) : "",
            profile_id: cleanStringParam(profileId.toString()),
        });

    } catch (exception) {
        //Same name found
        if (exception != null &&
            exception.response != null &&
            exception.response.status == 404)
            return undefined;

        console.warn("Toggle Profile Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Grabs a profile object that can be processed in generateProfiles for the DOM.
 * Modifies the DOM.
 * @returns {void}
 */
async function getProfiles() {
    await axios.get(
        "/get_profiles", {
        headers: { 'Content-Type': 'application/json' }

    }).then(response => {
        if (response == null ||
            response.data == null)
            return;

        $(".userProfilesList").empty();
        displayProfiles(response.data);

    }).catch(exception => { console.error(exception) });
}

/**
 * Grabs a profile data that can be processed by the client
 * @returns {?Promise}
 */
async function getProfilesData() {
    await axios.get(
        "/get_profiles", {
        headers: { 'Content-Type': 'application/json' }

    }).then(response => {
        if (response == null ||
            response.data == null)
            return;

        return response.data;
    }).catch(exception => { console.error(exception) });
}

/**
 * Grabs a profile status that can be processed by the client
 * @returns {?Promise}
 */
async function getProfileStatus() {
    await axios.get(
        "/get_profile_status", {
        headers: { 'Content-Type': 'application/json' }

    }).then(response => {
        if (response == null ||
            response.data == null)
            return;
        return response.data;

    }).catch(exception => { console.error(exception) });
}

/**
 * Sends a request to the server to update the Saved Job details
 * @param {?string} profileId - ID of the Profile
 * @param {?string} jobId - ID of the Job
 * @param {?string} listName - User supplied List name of the job
 * @param {?string} order - User supplied order for the job
 * @param {?string} notes - User supplied notes for the job
 * @returns {?Promise}
 */
async function updateSavedJobData(profileId, jobId, listName, order, notes) {
    if (profileId == null ||
        jobId == null) {
        return;
    }

    if (listName == null || 
        listName === "Unnamed") {
        listName = "";
    }

    if (notes == null) {
        notes = "";
    }
    // console.log("Send Profile ID: " + profileId.toString());
    // console.log("Send Job ID: " + jobId.toString());
    // console.log("Send List Name: " + listName.toString());
    // console.log("Send Order: " + order.toString());
    // console.log("Send Notes: " + notes.toString());

    return await axios.patch(
        "/update_saved_job/" +
        cleanString(profileId.toString()) + "/" +
        cleanString(jobId.toString()), {
        headers: { 'Content-Type': 'application/json' },
        listName: cleanListName(listName),
        order: order,
        notes: notes,
    });
}

/**
 * Sends a request to the server to update the Saved Company details
 * @param {?string} profileId - ID of the Profile
 * @param {?string} companyId - ID of the Company
 * @param {?string} listName - User supplied List name of the company
 * @param {?string} order - User supplied order for the company
 * @param {?string} notes - User supplied notes for the company
 * @returns {?Promise}
 */
async function updateSavedCompanyData(profileId, companyId, listName, order, notes) {
    if (profileId == null ||
        companyId == null) {
        return;
    }

    if (listName == null || 
        listName === "Unnamed") {
        listName = "";
    }

    if (notes == null) {
        notes = "";
    }
    // console.log("Send Profile ID: " + profileId.toString());
    // console.log("Send Company ID: " + companyId.toString());
    // console.log("Send List Name: " + listName.toString());
    // console.log("Send Order: " + order.toString());
    // console.log("Send Notes: " + notes.toString());

    return await axios.patch(
        "/update_saved_company/" +
        cleanString(profileId.toString()) + "/" +
        cleanString(companyId.toString()), {
        headers: { 'Content-Type': 'application/json' },
        listName: cleanListName(listName),
        order: order,
        notes: notes,
    });
}