/**
 * Retrieves Graph Data for Active Jobs
 * @returns {Promise}
 */
async function getJobsDatabaseStatistics() {
    try {
        return await axios.get(
            "/get_active_jobs_home/", {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("Get Graph Data Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Saves a Job ID to a user's profile
 * @param {?number} jobId - Job ID of the saved job to toggle.
 * @param {?boolean} toggle - True if saving, False if un-saving
 * @param {?number} profileId - Profile ID of the profile to toggle.
 * @returns {Promise}
 */
async function toggleJobProfileUpdate(jobId = undefined, toggle = undefined, profileId = undefined) {
    try {
        if (toggle) {
            return await axios.put(
                "/save_job/" +
                cleanString(profileId.toString()) + "/" +
                cleanString(jobId.toString())
            );
        } else {
            return await axios.delete(
                "/unsave_job/" +
                cleanString(profileId.toString()) + "/" +
                cleanString(jobId.toString())
            );
        }

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("toggleJobProfileUpdate Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Saves a Company ID to a user's profile
 * @param {?number} companyId - Company ID of the saved company to toggle.
 * @param {?boolean} toggle - True if saving, False if un-saving
 * @param {?number} profileId - Profile ID of the profile to toggle.
 * @returns {Promise}
 */
async function toggleCompanyProfileUpdate(companyId = undefined, toggle = undefined, profileId = undefined) {
    try {
        if (toggle) {
            return await axios.put(
                "/save_company/" +
                cleanString(profileId.toString()) + "/" +
                cleanString(companyId.toString())
            );
        } else {
            return await axios.delete(
                "/unsave_company/" +
                cleanString(profileId.toString()) + "/" +
                cleanString(companyId.toString())
            );
        }

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("toggleCompanyProfileUpdate Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Saves a Job ID to an active user's profile
 * @param {?number} jobId - Job ID of the saved job to toggle.
 * @param {?boolean} toggle - True if saving, False if un-saving
 * @returns {Promise}
 */
async function toggleJobActiveProfileUpdate(jobId = undefined, toggle = undefined) {
    try {
        if (toggle) {
            return await axios.put(
                "/save_job_active/" +
                cleanString(jobId.toString())
            );
        } else {
            return await axios.delete(
                "/unsave_job_active/" +
                cleanString(jobId.toString())
            );
        }

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;
        else if (exception.response.status == 417 ||
            exception.response.status == 403)
            return exception;

        console.warn("toggleJobActiveProfileUpdate Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Saves a Company ID to an active user's profile
 * @param {?number} companyId - Company ID of the saved company to toggle.
 * @param {?boolean} toggle - True if saving, False if un-saving
 * @returns {Promise}
 */
async function toggleCompanyActiveProfileUpdate(companyId = undefined, toggle = undefined) {
    try {
        if (toggle) {
            return await axios.put(
                "/save_company_active/" +
                cleanString(companyId.toString())
            );
        } else {
            return await axios.delete(
                "/unsave_company_active/" +
                cleanString(companyId.toString())
            );
        }

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;
        else if (exception.response.status == 417 ||
            exception.response.status == 403)
            return exception;

        console.warn("toggleCompanyActiveProfileUpdate Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Loads saved jobs from active user's profile to the client.
 * @returns {Promise}
 */
async function retrieveSavedJobs() {
    try {
        return await axios.get(
            "/retrieve_saved_jobs"
        );

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("retrieveSavedJobs Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Loads saved companies from active user's profile to the client.
 * @returns {Promise}
 */
async function retrieveSavedCompanies() {
    try {
        return await axios.get(
            "/retrieve_saved_companies"
        );

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("retrieveSavedCompanies Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Loads saved jobs and companies from active user's profile to the client.
 * @returns {Promise}
 */
async function retrieveSavedData() {
    try {
        return await axios.get(
            "/retrieve_saved_data"
        );

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("retrieveSavedData Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Loads saved jobs and companies with data from a selected user's profile to the client.
 * @returns {Promise}
 */
async function retrieveSavedDataUserProfileComplete(profileId) {
    try {
        return await axios.get(
            "/retrieve_saved_data_complete_profile/" +
            cleanString(profileId.toString())
        );

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("retrieveSavedData Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Loads saved jobs and companies with data from active user's profile to the client.
 * @returns {Promise}
 */
async function retrieveSavedDataComplete() {
    try {
        return await axios.get(
            "/retrieve_saved_data_complete"
        );

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("retrieveSavedData Exception");
        console.error(exception);
        throw exception;
    }
}
