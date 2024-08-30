/**
 * Retrieves generic companies using pagination from the REST Endpoint
 * @param {?number} pageNumber - Page Number
 * @returns {Promise}
 */
async function getCompanies(pageNumber = 0) {
    try {
        return await axios.get(
            "/get_companies/" +
            cleanString(pageNumber.toString()), {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("Get Companies Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Search Companies
 * @param {?string} searchTerm - Keyword for Search Term
 * @param {?number} pageNumber - Paginated Page Number
 * @returns {Promise}
 */
async function searchCompanies(
    searchTerm = undefined,
    pageNumber = 0) {
    try {
        return await axios.get(
            "/search_companies/" +
            cleanString(searchTerm.toString()) +
            "/" +
            pageNumber.toString(), {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;
        console.warn("Search Companies Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Get Company Jobs
 * @param {?number} companyId - ID of Company
 * @param {?number} pageNumber - Paginated Page Number
 * @returns {Promise}
 */
async function getCompanyJobs(
    companyId = -1,
    pageNumber = 0) {
    try {
        return await axios.get(
            "/get_company_jobs/" +
            cleanString(companyId.toString()) +
            "/" +
            cleanString(pageNumber.toString()), {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("Get Company Jobs Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Search Company Jobs
 * @param {?number} companyId - ID of Company
 * @param {?string} searchTerm - Keyword for Search Term
 * @param {?string} searchLocation - Existing Location ID of a city, state, country, subregion, or region.
 * @param {?number} searchDistance - Locations around the location to include in the search.
 * @param {?number} pageNumber - Paginated Page Number
 * @returns {Promise}
 */
async function searchCompanyJobs(
    companyId = undefined,
    searchTerm = undefined,
    searchLocation = undefined,
    searchDistance = undefined,
    pageNumber = 0) {
    try {
        if (
            (searchTerm == undefined ||
                typeof searchTerm != "string" ||
                searchTerm.length == 0 ||
                searchTerm.toString() == "") &&

            (searchLocation == undefined ||
                typeof searchLocation != "string" ||
                searchLocation.length == 0 ||
                searchLocation.toString() == "")) {
            return await axios.get(
                "/get_company_jobs/" +
                cleanString(companyId.toString()) +
                "/" +
                cleanString(pageNumber.toString()), {
                headers: { 'Content-Type': 'application/json' },
            });
        } else if (
            (searchTerm != undefined ||
                typeof searchTerm == "string" ||
                searchTerm.length != 0 ||
                searchTerm.toString() != "") &&

            (searchLocation == undefined ||
                typeof searchLocation != "string" ||
                searchLocation.length == 0 ||
                searchLocation.toString() == "")) {

            return await axios.get(
                "/search_company_jobs_k/" +
                companyId.toString() +
                "/" +
                cleanString(searchTerm.toString()) +
                "/" +
                cleanString(pageNumber.toString()), {
                headers: { 'Content-Type': 'application/json' },
            });

        } else if (
            (searchTerm == undefined ||
                !(typeof searchTerm == "string") ||
                searchTerm.length == 0 ||
                searchTerm.toString() == "") &&

            searchLocation != undefined &&
            typeof searchLocation == "string" &&
            searchLocation.length != 0 &&
            searchLocation.toString() != "" &&

            (searchDistance == undefined ||
                typeof searchDistance != "number" ||
                searchDistance < 0 ||
                searchDistance == 30)) {

            return await axios.get(
                "/search_company_jobs_l/" +
                cleanString(companyId.toString()) +
                "/" +
                cleanString(searchLocation.toString()) +
                "/" +
                cleanString(pageNumber.toString()), {
                headers: { 'Content-Type': 'application/json' },
            });
        } else if ((searchTerm == undefined ||
            !(typeof searchTerm == "string") ||
            searchTerm.length == 0 ||
            searchTerm.toString() == "") &&

            searchLocation != undefined &&
            typeof searchLocation == "string" &&
            searchLocation.length != 0 &&
            searchLocation.toString() != "" &&

            (searchDistance != undefined &&
                typeof searchDistance == "number" &&
                searchDistance >= 0 &&
                searchDistance != 30)) {
            return await axios.get(
                "/search_company_jobs_ld/" +
                cleanString(companyId.toString()) +
                "/" +
                cleanString(searchLocation.toString()) +
                "/" +
                cleanString(searchDistance.toString()) +
                "/" +
                cleanString(pageNumber.toString()), {
                headers: { 'Content-Type': 'application/json' },
            });

        } else if (searchDistance == 30 ||
            searchDistance == undefined ||
            typeof searchDistance != "number" ||
            searchDistance < 0) {
            return await axios.get(
                "/search_company_jobs_kl/" +
                cleanString(companyId.toString()) +
                "/" +
                cleanString(searchTerm.toString()) +
                "/" +
                cleanString(searchLocation.toString()) +
                "/" +
                cleanString(pageNumber.toString()), {
                headers: { 'Content-Type': 'application/json' },
            });

        } else {
            return await axios.get(
                "/search_company_jobs_kld/" +
                cleanString(companyId.toString()) +
                "/" +
                cleanString(searchTerm.toString()) +
                "/" +
                cleanString(searchLocation.toString()) +
                "/" +
                cleanString(searchDistance.toString()) +
                "/" +
                cleanString(pageNumber.toString()), {
                headers: { 'Content-Type': 'application/json' },
            });
        }

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("Search Company Jobs Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves previous search queries and returns a response
 * @returns {Promise}
 */
async function retrievePreviousSearchCompany() {
    try {
        return await axios.get(
            "/retrieve_last_search_company", {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("retrievePreviousSearchCompany Exception");
        console.error(exception);
        throw exception;
    }
}