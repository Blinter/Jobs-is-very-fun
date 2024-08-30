/**
 * Retrieves Mongo Scrape Storage Contents
 * @returns {Promise}
 */
async function getAPIMongoScrapeDocumentStorageAll() {
    try {
        const response = await axios.get(
            '/admin_rest/get_mongo_scrape_storage_all', {
            headers: { 'Content-Type': 'application/json' }
        });
        return response;

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;
        console.warn("Get Mongo Scrape Document Data for view document Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves Mongo Scrape Storage Contents ordered by 
 * 
 * Either:
 * query_time_desc
 * query_time_asc
 * id_desc
 * id_asc
 * time_desc
 * time_asc
 * code_desc
 * code_asc
 * length_desc
 * length_asc
 * 
 * @param {string} order_type - Query order type described in previous documentation
 * @param {?number} pageNumber - Page Number
 * @returns {Promise}
 */
async function getAPIMongoScrapeDocumentStorageList(order_type = "query_time_desc", pageNumber = 0) {
    try {
        return await axios.get(
            '/admin_rest/get_mongo_scrape_storage/' +
            cleanString(order_type.toString()) +
            '/' +
            pageNumber.toString(), {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;
            
        console.warn("Get Mongo Scrape Document Data for view document Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves Mongo Storage data based on a search string
 * @param {?string} mongoScrapeSearchString
 * @returns {Promise}
 */
async function getMongoScrapeStorageSearch(mongoScrapeSearchString) {
    if (mongoScrapeSearchString == undefined ||
        mongoScrapeSearchString.length == 0) {
        console.error("getMongoScrapeStorageSearch called with no input");
        return undefined;
    }

    try {
        const response = await axios.get(
            "/admin_rest/get_mongo_scrape_storage_search", {
            headers: { 'Content-Type': 'application/json' },
        });
        return response;

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;
        console.warn("Get Mongo Scrape Storage Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves Mongo Scrape Response contents when the full response button is clicked.
 * @param {?string} MongoScrapeDocumentId - ID of the Mongo Document to retrieve data.
 * @returns {Promise}
 */
async function getAPIMongoScrapeDocumentData(MongoScrapeDocumentId) {
    if (MongoScrapeDocumentId == undefined ||
        MongoScrapeDocumentId.length == 0) {
        console.error("getAPIMongoScrapeDocumentData called with no input");
        return undefined;
    }

    try {
        const response = await axios.get(
            '/admin_rest/get_mongo_scrape_doc/' +
            cleanString(MongoScrapeDocumentId), {
            headers: { 'Content-Type': 'application/json' }
        });
        return response;

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;
        console.warn("Get Mongo Scrape Document Data for view document Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Submits a request to the server to delete a MongoScrapeStorage ID and clear the data from the MongoDB.
 * @param {?string} mongoScrapeStorageId - ID of the Mongo ScrapeStorage ID to delete.
 * @returns {Promise}
 */
async function sendMongoScrapeStorageDelete(mongoScrapeStorageId) {
    if (mongoScrapeStorageId == undefined ||
        mongoScrapeStorageId.length == 0) {
        console.error("sendMongoScrapeStorageDelete called with no input");
        return undefined;
    }

    try {
        return await axios.delete(
            '/admin_rest/delete_mongo_scrape_storage/' +
            cleanString(mongoScrapeStorageId), {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("sendMongoScrapeStorage Delete Request Exception");
        console.error(exception);
        throw exception;
    }
}