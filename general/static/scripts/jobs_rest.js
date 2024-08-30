/**
 * Retrieves generic jobs from the REST Endpoint
 * @param {?number} pageNumber - Page Number
 * @returns {Promise}
 */
async function getJobs(pageNumber = 0) {
    try {
        return await axios.get(
            "/get_jobs/" +
            cleanString(pageNumber.toString()), {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("Get Jobs Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Search Jobs optionally with a searchTerm or searchLocation or searchDistance
 * @param {?string} searchTerm - Keyword for Search Term
 * @param {?string} searchLocation - Location String of a city, state, country, subregion, or region.
 * @param {?number} searchDistance - Locations around the location to include in the search.
 * @param {?number} pageNumber - Page Number
 * @returns {Promise}
 */
async function searchJobs(
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
                "/get_jobs/" +
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
                "/search_jobs_k/" +
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
                "/search_jobs_l/" +
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
                "/search_jobs_ld/" +
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
                "/search_jobs_kl/" +
                cleanString(searchTerm.toString()) +
                "/" +
                cleanString(searchLocation.toString()) +
                "/" +
                cleanString(pageNumber.toString()), {
                headers: { 'Content-Type': 'application/json' },
            });

        } else {
            return await axios.get(
                "/search_jobs_kld/" +
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

        console.warn("Search Keyword and Location Jobs Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves previous search queries and returns a response
 * @returns {Promise}
 */
async function retrievePreviousSearchJob() {
    try {
        return await axios.get(
            "/retrieve_last_search_job", {
            headers: { 'Content-Type': 'application/json' },
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 404)
            return undefined;

        console.warn("retrievePreviousSearchJob Exception");
        console.error(exception);
        throw exception;
    }
}