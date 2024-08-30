/**
 * Retrieves Mongo Storage Contents
 * @returns {Promise}
 */
async function getAPIMongoDocumentStorageList() {
    try {
        return await axios.get(
            '/admin_rest/get_mongo_storage', {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;
        console.warn("Get Mongo Document Data for view document Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves Mongo Storage data based on an array of types to filter
 * @param {?Array.<number>} apiFilterArray - ID of the API Endpoints to retrieve API Endpoint count data.
 * @param {?Array.<number>} apiFilterArray - ID of the API Endpoints to retrieve API Endpoint count data.
 * @returns {Promise}
 */
async function getMongoStorageFiltered(
    apiFilterArray, 
    apiListFilterArray) {
    if (apiFilterArray == undefined ||
        apiListFilterArray == undefined) {
        console.error("getMongoStorageFiltered called with undefined input");
        return undefined;
    }

    if (apiFilterArray.length == 0) {
        apiFilterArray = [-1];
    }

    if (apiListFilterArray.length == 0) {
        apiListFilterArray = [-1];
    }

    try {
        return await axios.get(
            "/admin_rest/get_mongo_storage_filtered", {
            headers: { 'Content-Type': 'application/json' },
            params: {
                f1: JSON.stringify(apiFilterArray),
                f2: JSON.stringify(apiListFilterArray),
            }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("Get Mongo Storage Filtered for filter array Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Retrieves Mongo Response contents when the full response button is clicked.
 * @param {?string} MongoDocumentId - ID of the Mongo Document to retrieve data.
 * @returns {Promise}
 */
async function getAPIMongoDocumentData(MongoDocumentId) {
    if (MongoDocumentId == undefined ||
        MongoDocumentId.length == 0) {
        console.error("getAPIMongoDocumentData called with no input");
        return undefined;
    }

    try {
        return await axios.get(
            '/admin_rest/get_mongo_doc/' +
            cleanString(MongoDocumentId), {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("Get Mongo Document Data for view document Exception");
        console.error(exception);
        throw exception;
    }
}

/**
 * Submits a request to the server to delete a MongoStorage ID and clear the data from the MongoDB.
 * @param {?string} mongoStorageId - ID of the Mongo Storage ID to delete.
 * @returns {Promise}
 */
async function sendMongoStorageDelete(mongoStorageId) {
    if (mongoStorageId == undefined ||
        mongoStorageId.length == 0) {
        console.error("sendMongoStorageDelete called with no input");
        return undefined;
    }

    try {
        return await axios.delete(
            '/admin_rest/delete_mongo_storage/' +
            cleanString(mongoStorageId), {
            headers: { 'Content-Type': 'application/json' }
        });

    } catch (exception) {
        if (exception.response != undefined &&
            exception.response.status != undefined &&
            exception.response.status == 500)
            return undefined;

        console.warn("sendMongoStorage Delete Request Exception");
        console.error(exception);
        throw exception;
    }
}