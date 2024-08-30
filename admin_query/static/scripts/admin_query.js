const adminQueryPath = '/admin_query';
const adminQueryViewExtra = adminQueryPath + '/view_extra/';

let endpointParamBodyInputs = new Map();
const formUniqueKeySuffix = "-prmBdyKey";
/**
 * Continue loading data from REST when the page is loaded.
 * Adds Event Handlers to form change events.
 */
$(document).ready(() => {
    if (window.location.pathname == adminQueryPath) {
        displayAPIKey();
        $("#API").on("change", () => displayAPIKey());
        $("#APIKey").on("change", () => displayLastAccessAPIKey());
        $("#Endpoint").on("change", () => {
            displayNiceDescriptionAPIEndpoint();
            displayAPIEndpointAdditionalCounts();
            displayParamsAPIEndpoint();
            displayBodiesAPIEndpoint();
            displayExtraDocsAPIEndpoint();
            endpointParamBodyInputs.clear();
        });

        $("#APIKeyAuto").on("change", () => checkAutomaticAPIKey());
        $("input#SubmitButton").on('click', event => {
            event.preventDefault();
            //Empty the actively displayed tab just in-case there are form inputs.
            $('#endpointInformationTab').empty();
            addHiddenFormElements();
            $("#manualCacheSendQuery").submit();
        });

        $("input#cancel").on('click', event => {
            event.preventDefault();
        });

        // Set API Key Auto to True
        $("#APIKeyAuto").prop("checked", true);
        checkAutomaticAPIKey();
        // Pre-load a preset config from server
        checkServerSettingsToLoad();
    } else if (window.location.pathname.includes(adminQueryViewExtra)) {
        displayExtraDocument();
    }
});

/**
 * Pre-loads a specific endpoint and params from the server to load on the client-side menu settings
 * returns Object from REST endpoint:
 *  current_active_tab: Boolean
 *  api_key_auto: Boolean
 *  api: String Value
 *  endpoint: String Value
 *  input_json: Object K,V pairs for corresponding endpoint parameters
 * Modifies the DOM
 * @returns {void}
 */
async function checkServerSettingsToLoad() {
    const endpointInfo = $('#endpointInformationTab');
    if ($(endpointInfo) == undefined) {
        console.error("displayExtraDocsAPIEndpoint could not find the information element.");
        return;
    }

    const apiForm = $("#API");
    if ($(apiForm) == undefined) {
        console.error("(checkServerSettingsToLoad) API element cannot be found.");
        return;
    }

    const apiEndpointForm = $("#Endpoint");
    if ($(apiEndpointForm) == undefined) {
        console.error("(checkServerSettingsToLoad) Endpoint element cannot be found.");
        return;
    }

    const previousSettings = await getPreviousSettings()
        .then(response => {
            if (response == undefined ||
                response.data == undefined)
                return undefined;
            //console.debug(response.data);
            //console.debug(response.data.input_json);

            //Filter does not work with option elements, so .each must be used.
            if (response.data.api != undefined &&
                response.data.api.length != 0) {
                $(apiForm).off("change");
                $(apiForm)
                    .children()
                    .each((undefined, v) => {
                        if ($(v).val() == response.data.api) {
                            $(v).prop('selected', true);
                        }
                    });
                $(apiForm).change();
            }
            // Set API Key Auto to previously loaded setting.
            $("#APIKeyAuto").prop("checked", response.data.api_key_auto);
            return response.data;
        })

    if (previousSettings != undefined && previousSettings.api != undefined) {
        await getAPIEndpointsNameIdOnly(previousSettings.api)
            .then(response => {
                if (response == undefined ||
                    response.data == undefined ||
                    response.data.length == 0) {
                    console.error("(checkServerSettingsToLoad) getAPIEndpointsNameIdOnly Response did not return anything.");
                    return;
                }

                $(apiEndpointForm).off('change');
                $(apiEndpointForm).children().remove();

                // console.debug("Received Active Tab as: " + 
                //     previousSettings.current_active_tab);
                // console.debug("Received Active Endpoint as: " + 
                //     previousSettings.endpoint);
                $(apiEndpointForm).attr('disabled', true);

                response.data.forEach(endpointItem => {
                    $(apiEndpointForm).append($("<option>")
                        .text(endpointItem.nice_name)
                        .val(endpointItem.id));
                    // console.debug("ADDING " + 
                    //     endpointItem.nice_name + 
                    //     "(" + endpointItem.id + ")")
                });

                $(endpointInfo).text('Loading settings from server...');

                setTimeout(() => {
                    // console.debug("SETTING " +
                    //     "(" + previousSettings.endpoint + ")")
                    $(apiEndpointForm).val(previousSettings.endpoint)
                    $('#endpointControlButtons').children().each((undefined, tabElement) =>
                        $(tabElement).attr('id') == previousSettings.current_active_tab ?
                            $(tabElement).attr({
                                "class": "btn-EndpointActiveTabItem btn-success text-light active",
                                "disabled": true
                            }) :
                            $(tabElement).text().includes("(0)") ?
                                $(tabElement).attr({
                                    "class": "btn-EndpointDisabledTabItem btn-success text-light bg-black",
                                    'disabled': true,
                                }) :
                                $(tabElement).attr({
                                    "class": "btn-EndpointTabItem bg-muted text-light",
                                    "disabled": false
                                })
                    );

                    //When the endpoints are loaded, load the counts for the endpoint as well.
                    displayAPIEndpointAdditionalCounts();

                    //Show information if the active tab is switched to Description.
                    displayNiceDescriptionAPIEndpoint();

                    //Show information if the active tab is switched to Params.
                    displayParamsAPIEndpoint();

                    //Show information if the active tab is switched to Body.
                    displayBodiesAPIEndpoint();

                    //Show information if the active tab is switched to Docs.
                    displayExtraDocsAPIEndpoint();

                    //When the counts for endpoints are loaded, disable buttons that don't have any items listed.
                    updateEndpointControlsDisable();

                    endpointParamBodyInputs = new Map([...Object.entries(previousSettings.input_json)]);

                    $("#Endpoint").on("change", () => {
                        displayNiceDescriptionAPIEndpoint();
                        displayAPIEndpointAdditionalCounts();
                        displayParamsAPIEndpoint();
                        displayBodiesAPIEndpoint();
                        displayExtraDocsAPIEndpoint();
                        endpointParamBodyInputs.clear();
                    });

                    $(apiEndpointForm).attr('disabled', false);
                }, 1200);
            });
    }

    $(apiForm).on("change", () => displayAPIKey());
}

/**
 * Checks if the Automatic API Key is enabled and hides or shows API Key and Proxy elements
 * Modifies the DOM
 * @returns {void}
 */
function checkAutomaticAPIKey() {
    if ($('#APIKeyAuto') == undefined)
        return;

    if ($('#APIKeyAuto').is(':checked')) {
        if ($("#apiKeyToggleHiddenDiv") != undefined)
            $("#apiKeyToggleHiddenDiv").hide();

        if ($("#apiKeyDividerToggleHiddenHR") != undefined)
            $("#apiKeyDividerToggleHiddenHR").hide();

        if ($("#Proxy") != undefined)
            $("#Proxy").hide();

        if ($("#APIKey") != undefined)
            $("#APIKey").hide();

        if ($('#lastAccessDateTime') != undefined)
            $('#lastAccessDateTime').hide();

        if ($('.lastAccessTimeText') != undefined)
            $('.lastAccessTimeText').hide();

        if ($('#refreshAPIKeyList') != undefined)
            $('#refreshAPIKeyList').hide();

        if ($('label[for="Proxy"]') != undefined)
            $('label[for="Proxy"]').hide();

        if ($('label[for="APIKey"]') != undefined)
            $('label[for="APIKey"]').hide();

    } else {
        if ($("#apiKeyToggleHiddenDiv") != undefined)
            $("#apiKeyToggleHiddenDiv").show();

        if ($("#apiKeyDividerToggleHiddenHR") != undefined)
            $("#apiKeyDividerToggleHiddenHR").show();

        if ($("#Proxy") != undefined)
            $("#Proxy").show();

        if ($("#APIKey") != undefined)
            $("#APIKey").show();

        if ($('#lastAccessDateTime') != undefined)
            $('#lastAccessDateTime').show();

        if ($('.lastAccessTimeText') != undefined)
            $('.lastAccessTimeText').show();

        if ($('#refreshAPIKeyList') != undefined)
            $('#refreshAPIKeyList').show();

        if ($('label[for="Proxy"]') != undefined)
            $('label[for="Proxy"]').show();

        if ($('label[for="APIKey"]') != undefined)
            $('label[for="APIKey"]').show();
    }
}

/**
 * Load all saved parameters and bodies into the form before submit.
 * If an input is already contained, then remove it first.
 * Modifies the DOM.
 * @returns {void}
 */
function addHiddenFormElements() {
    const currentForm = $("#manualCacheSendQuery");
    //Send active tab to server so it can be stored in the session as well.
    const newHiddenInputActiveTab = $("<input>");
    $(newHiddenInputActiveTab).attr({
        'id': 'currentActiveTab',
        'name': 'currentActiveTab',
        'type': 'hidden',
        'value': $(".btn-EndpointActiveTabItem").attr("id")
    });

    $(currentForm).append($(newHiddenInputActiveTab));
    endpointParamBodyInputs.forEach((v, k) => {
        //If the form inputs are appended already, remove them first.
        if ($(currentForm).children(
            "#" + k + formUniqueKeySuffix) != undefined)
            $(currentForm).children(
                "#" + k + formUniqueKeySuffix).remove();

        const newHiddenInput = $("<input>");
        $(newHiddenInput).attr({
            'id': k + formUniqueKeySuffix,
            'name': k + formUniqueKeySuffix,
            'type': 'hidden',
            'value': v
        });
        $(currentForm).append($(newHiddenInput));
    });
}

/**
 * Continue loading contents of the documentation data from REST after the page is loaded.
 * Modifies the DOM.
 * @returns {void}
 */
async function displayExtraDocument() {
    const documentHolder = $(".extraDocumentationBody");
    if ($(documentHolder) == undefined) {
        console.error("Could not find element holder to load in document data.");
        return;
    }

    const documentId = window.location.pathname.replace(adminQueryViewExtra, "");
    await getAPIExtraDocumentData(documentId)
        .then(response => {
            $(documentHolder).empty();
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                console.error("getAPIExtraDocumentData response did not return anything.");
                return;
            }
            $(documentHolder).append(escapeHTML(response.data));
        });
}

/**
 * Loads API Keys for when an API List URL is displayed. Modifies the DOM.
 * The API Key's last access time is also updated
 * @returns {void}
 */
async function displayAPIKey() {
    if ($("#API") == undefined)
        return;

    await getAPIKeyandIds($("#API :selected").val())
        .then(response => {
            const apiKeyForm = $("#APIKey");
            $(apiKeyForm).children().remove();
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                console.warn("displayAPIKey response did not return anything. No API Keys available.");                
                $(apiKeyForm).append($("<option>")
                    .text("None")
                    .val("No Keys"));
                return;
            }
            response.data.forEach(apiKeyItem =>
                $(apiKeyForm).append($("<option>")
                    .text(apiKeyItem.key)
                    .val(apiKeyItem.id)));
            //Chain currently selected endpoint list for API ID.
            displayAPIEndpointsNameIdOnly();
            //API keys will change and update when a new endpoint is selected, update the last_access as well.
            //API keys are generally shared between the endpoints so the value changed event is not called.
            displayLastAccessAPIKey();
        });
}

/**
 * Reset the endpoint form control button's active tab and disable buttons with no count.
 * Reset back to default button when the active tab should be disabled.
 * Modifies the DOM.
 * @returns {void}
 */
function updateEndpointControlsDisable() {
    let allButtonsParent = $('#endpointControlButtons');
    if ($(allButtonsParent) == undefined) {
        console.error("Endpoint Tab Control element not found.");
        return;
    }

    $(allButtonsParent).children().each((undefined, tabElement) => {
        if (!$(tabElement).attr('class').includes('btn-EndpointActiveTabItem')) {
            if ($(tabElement).text().includes("(0)")) {
                $(tabElement).attr({
                    "class": "btn-EndpointDisabledTabItem btn-success text-light bg-black",
                    'disabled': true,
                });
            } else {
                $(tabElement).attr({
                    "class": "btn-EndpointTabItem bg-muted text-light",
                    "disabled": false
                });
            }

        } else if ($(tabElement).text().includes("(0)")) {
            //Default back to Description if the selected control has no count and is active.
            $('#endpointButtonShowDescription').attr('class', 'btn-EndpointActiveTabItem btn-success text-light active');

            //Set active back to default
            $(tabElement).attr({
                "class": "btn-EndpointDisabledTabItem btn-success text-light bg-black",
                'disabled': true,
            });

            //Now grab the Endpoint description data and display it to the admin.
            displayNiceDescriptionAPIEndpoint();
        }
    });
}

/**
 * Sets an endpoint's active tab when the admin clicks on a control.
 * Modifies the DOM.
 * @param {object} e - Click Event Handler (onClick parameter must be 'event').
 * @returns {void}
 */
function setActiveEndpointTab(e) {
    let allButtonsParent = $(e.target).parent();
    if ($(allButtonsParent) == undefined) {
        console.error("Endpoint Tab Control element not found.");
        return;
    }

    $(allButtonsParent).children().each((undefined, tabElement) =>
        tabElement == e.target ?
            $(tabElement).attr({
                "class": "btn-EndpointActiveTabItem btn-success text-light active",
                "disabled": true
            }) :
            $(tabElement).text().includes("(0)") ?
                $(tabElement).attr({
                    "class": "btn-EndpointDisabledTabItem btn-success text-light bg-black",
                    'disabled': true,
                }) :
                $(tabElement).attr({
                    "class": "btn-EndpointTabItem bg-muted text-light",
                    "disabled": false
                })
    );

    updateEndpointDetails();
}

/**
 * Loads API Endpoints when an API List URL is displayed. 
 * Modifies the DOM.
 * @returns {void}
 */
async function displayAPIEndpointsNameIdOnly() {
    const selectedAPI = $("#API :selected");
    if ($(selectedAPI) == undefined) {
        console.error("#API form element cannot be found.");
        return;
    }

    await getAPIEndpointsNameIdOnly($(selectedAPI).val())
        .then(response => {
            const apiEndpointForm = $("#Endpoint");
            if ($(apiEndpointForm) == undefined) {
                console.error("Endpoint element cannot be found.");
                return;
            }
            $(apiEndpointForm).children().remove();
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                console.warn("displayAPIEndpointsNameIdOnly Response did not return anything.");
                return;
            }
            response.data.forEach(endpointItem =>
                $(apiEndpointForm).append($("<option>")
                    .text(endpointItem.nice_name)
                    .val(endpointItem.id))
            );

            //Chain retrieving data for currently selected APIEndpoint while displaying description.
            updateEndpointDetails();

            //When the endpoints are loaded, load the counts for the endpoint as well.
            displayAPIEndpointAdditionalCounts();

            //Clear the map since there has been a change in API, old input data is cleared.
            endpointParamBodyInputs.clear();

            //When the counts for endpoints are loaded, disable buttons that don't have any items listed..
            updateEndpointControlsDisable();
        });
}

/**
 * Update an endpoint's description and other details after there is a change in the active tab.
 * Modifies the DOM.
 * @returns {void}
 */
function updateEndpointDetails() {
    //Show information if the active tab is switched to Description.
    displayNiceDescriptionAPIEndpoint();

    //Show information if the active tab is switched to Params.
    displayParamsAPIEndpoint();

    //Show information if the active tab is switched to Body.
    displayBodiesAPIEndpoint();

    //Show information if the active tab is switched to Docs.
    displayExtraDocsAPIEndpoint();

    //Show extra docs if the active tab is switched to Extra Docs.
    if ($(".btn-EndpointActiveTabItem").attr("id") != "endpointButtonShowDescription" &&
        $(".btn-EndpointActiveTabItem").attr("id") != "endpointButtonShowExtraDocs" &&
        $(".btn-EndpointActiveTabItem").attr("id") != "endpointButtonShowBodies" &&
        $(".btn-EndpointActiveTabItem").attr("id") != "endpointButtonShowParams")
        $("#endpointInformationTab").text('Loading...');
}

/**
 * Loads the last access time of a selected API key (Called on select API key change.)
 * Modifies the DOM.
 * @returns {void}
 */
async function displayLastAccessAPIKey() {
    const selectedAPIKey = $("#APIKey :selected");
    if ($(selectedAPIKey) == undefined ||
        $(selectedAPIKey).val() == '') {
        console.warn("displayLastAccessAPIKey could not find a Selected API Key.");
        return;
    }

    const lastAccessLabel = $("#lastAccessDateTime");
    if ($(lastAccessLabel) == undefined) {
        console.error("#lastAccessLabel element was not found.");
        return;
    }

    await getAPIKeyLastAccessOnly($(selectedAPIKey).val())
        .then(response => {
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0)
                $(lastAccessLabel).text('No data');

            else
                $(lastAccessLabel).text(response.data.last_access);
        });

    const selectedProxy = $("#Proxy");
    if ($(selectedProxy) == undefined ||
        $(selectedProxy).val() == '') {
        console.error("displayLastAccessAPIKey could not find a Proxy Element.");
        return;
    }

    //While there is a new API Key being loaded, whenever this async operation is called,
    //we can also change the Proxy Option to display the preferred proxy.
    await getAPIKeyPreferredProxyOnly($(selectedAPIKey).val())
        .then(response => {
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0)
                // No response for preferred proxy, no change, so end the function
                return;

            //Filter does not work with option elements, so .each must be used.
            $(selectedProxy).children()
                .each((undefined, v) => {
                    if ($(v).text() == response.data.preferred_proxy) {
                        $(v).prop('selected', true);
                        return;
                    }
                });
        });
}

/**
 * Loads the nice description of a selected Endpoint (Called on select API Endpoint change.)
 * Modifies the DOM.
 * @returns {void}
 */
async function displayNiceDescriptionAPIEndpoint() {
    const endpointActiveTab = $(".btn-EndpointActiveTabItem");
    if ($(endpointActiveTab) == undefined ||
        $(endpointActiveTab).attr("id") != "endpointButtonShowDescription")
        return;

    const endpointInfo = $('#endpointInformationTab');
    if ($(endpointInfo) == undefined) {
        console.error("displayNiceDescriptionAPIEndpoint could not find the information element.");
        return;
    }

    const selectedEndpointId = $("#Endpoint :selected");
    if ($(selectedEndpointId) == undefined ||
        $(selectedEndpointId).val() == '' ||
        $(selectedEndpointId).length == 0) {
        console.error("displayNiceDescriptionAPIEndpoint could not find a selected endpoint.");
        return;
    }

    await getAPIEndpointNiceDescription($(selectedEndpointId).val())
        .then(response => {
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0 ||
                response.data.nice_description == undefined ||
                response.data.nice_description.length == 0) {
                $(endpointInfo).text('No data');
                return;
            }
            $(endpointInfo).text(response.data.nice_description);
        });
}

/**
 * Loads documents of a selected Endpoint (Called on select API Endpoint change.)
 * Modifies the DOM.
 * @returns {void}
 */
async function displayExtraDocsAPIEndpoint() {
    const endpointActiveTab = $(".btn-EndpointActiveTabItem");
    if ($(endpointActiveTab) == undefined ||
        $(endpointActiveTab).attr("id") != "endpointButtonShowExtraDocs")
        return;

    const endpointInfo = $('#endpointInformationTab');
    if ($(endpointInfo) == undefined) {
        console.error("displayExtraDocsAPIEndpoint could not find the information element.");
        return;
    }

    const selectedEndpointId = $("#Endpoint :selected");
    if ($(selectedEndpointId) == undefined ||
        $(selectedEndpointId).val() == '') {
        console.error("displayExtraDocsAPIEndpoint could not find a selected endpoint.");
        return;
    }

    await getAPIEndpointExtraDocs($(selectedEndpointId).val())
        .then(response => {
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                $(endpointInfo).text('No data');
                return;
            }
            $(endpointInfo).empty();

            response.data.forEach((extraId, index) => {
                const viewDocButton = $("<button class='btn-TableButtonItem px-4'>").text(`View Doc #${(index + 1)}`);
                $(endpointInfo)
                    .append($(viewDocButton))
                    .append("<br>");
                (tempExtraId => {
                    let newWindow = undefined;
                    $(viewDocButton).on('click', event => {
                        event.preventDefault();
                        if ($(viewDocButton).text() != 'Close') {
                            newWindow = window.open(
                                adminQueryPath +
                                "/view_extra/" +
                                tempExtraId.id.toString(),

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
                                "menubar=no");
                            $(viewDocButton).text('Close');

                            let checkWindow = setInterval(() =>
                                (tempNewWindow => {
                                    if (!tempNewWindow.closed)
                                        return;
                                    clearInterval(checkWindow);
                                    $(viewDocButton).text(`View Doc #${(index + 1)}`);
                                })(newWindow)
                                , 2500);

                        } else {
                            $(viewDocButton).text(`View Doc #${(index + 1)}`);

                            if (newWindow == undefined)
                                return;

                            newWindow.close();
                        }
                    })
                })(extraId); //Pass profile variable and call right away.
            });
        });
}

/**
 * Updates the count of extra Endpoint Parameters, Bodies and Extra Docs.
 * Modifies the DOM.
 * @returns {void}
 */
async function displayAPIEndpointAdditionalCounts() {
    const endpointControlParamCount = $('#endpointButtonShowParams');
    if ($(endpointControlParamCount) == undefined)
        return;

    const endpointControlBodyCount = $("#endpointButtonShowBodies");
    if ($(endpointControlBodyCount) == undefined)
        return;

    const endpointControlExtraCount = $("#endpointButtonShowExtraDocs");
    if ($(endpointControlExtraCount) == undefined)
        return;

    const selectedEndpointId = $("#Endpoint :selected");
    if ($(selectedEndpointId) == undefined ||
        $(selectedEndpointId).val() == '') {
        console.error("displayAPIEndpointAdditionalCounts could not find a selected endpoint.");
        return;
    }

    await getAPIEndpointExtrasCount($(selectedEndpointId).val())
        .then(response => {
            if (response == undefined ||
                response.data == undefined ||
                response.data.length != 3) {
                $(endpointControlParamCount).text('Params (0)');
                $(endpointControlBodyCount).text('Body (0)');
                $(endpointControlExtraCount).text('Docs (0)');
                return;
            }

            $(endpointControlParamCount).text(`Params (${response.data[0]})`);
            $(endpointControlBodyCount).text(`Body (${response.data[1]})`);
            $(endpointControlExtraCount).text(`Docs (${response.data[2]})`);

            updateEndpointControlsDisable();
        });
}

/**
 * Loads the param endpoint options of a selected Endpoint 
 * Called on select API Endpoint change
 * Modifies the DOM.
 * @returns {void}
 */
async function displayParamsAPIEndpoint() {
    const endpointActiveTab = $(".btn-EndpointActiveTabItem");
    if ($(endpointActiveTab) == undefined ||
        $(endpointActiveTab).attr("id") != "endpointButtonShowParams")
        return;

    const endpointInfo = $('#endpointInformationTab');
    if ($(endpointInfo) == undefined) {
        console.error("displayParamsAPIEndpoint could not find the information element.");
        return;
    }

    const selectedEndpointId = $("#Endpoint :selected");
    if ($(selectedEndpointId) == undefined ||
        $(selectedEndpointId).val() == '') {
        console.error("displayParamsAPIEndpoint could not find a selected endpoint.");
        return;
    }

    await getAPIEndpointParams($(selectedEndpointId).val())
        .then(response => {
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                $(endpointInfo).text('No data');
                return;
            }

            //console.debug(response.data);
            //Set Endpoint Params
            $(endpointInfo).empty();
            const newForm = $('<div class="form-floating-sm bg-none">');
            response.data.forEach(endpointParam => {
                $(newForm).append(
                    $('<label class="text-light mt-2 h1 manualQueryFormText">').attr({
                        'for': endpointParam.param
                    }).text(endpointParam.description));

                const newInput = $('<input class="manualQueryFormText form-control form-control-sm mx-auto manualQueryFormTextBody">')
                    .attr({
                        'id': endpointParam.param,
                        'name': endpointParam.param,
                        'required': endpointParam.required == "1",
                        'type': "text",
                        'placeholder': endpointParam.hint_type + (endpointParam.required == "1" ? " (required)" : " (optional)")
                    })
                    .val(endpointParamBodyInputs.has(endpointParam.param) ?
                        endpointParamBodyInputs.get(endpointParam.param) :
                        endpointParam.default_value);

                if (endpointParam.param != undefined &&
                    !endpointParamBodyInputs.has(endpointParam.param))
                    endpointParamBodyInputs.set(endpointParam.param,
                        endpointParam.default_value == undefined ? '' : endpointParam.default_value);

                $(newForm).append($(newInput));

                ((tempNewInput, tempKey) =>
                    $(tempNewInput).on('keyup change', () =>
                        endpointParamBodyInputs.set(tempKey, $(tempNewInput).val()))
                )(newInput, endpointParam.param);

                $(newForm).append($("<hr class='smallestDivider mx-auto'>").css({ 'color': 'white' }));
            });
            $(endpointInfo).append($(newForm));

            const checkLastDivider = $(newForm).children();

            if (checkLastDivider.length != 0 &&
                $(newForm).children()[$(newForm).children().length - 1].tagName == "HR")
                $(newForm).children()[$(newForm).children().length - 1].remove();
        });
}

/**
 * Loads the body endpoint options of a selected Endpoint (Called on select API Endpoint change.)
 * Modifies the DOM.
 * @returns {void}
 */
async function displayBodiesAPIEndpoint() {
    const endpointActiveTab = $(".btn-EndpointActiveTabItem");
    if ($(endpointActiveTab) == undefined ||
        $(endpointActiveTab).attr("id") != "endpointButtonShowBodies")
        return;

    const endpointInfo = $('#endpointInformationTab');
    if ($(endpointInfo) == undefined) {
        console.error("displayBodiesAPIEndpoint could not find the information element.");
        return;
    }

    const selectedEndpointId = $("#Endpoint :selected");
    if ($(selectedEndpointId) == undefined ||
        $(selectedEndpointId).val() == '') {
        console.error("displayBodiesAPIEndpoint could not find a selected endpoint.");
        return;
    }

    await getAPIEndpointBodies($(selectedEndpointId).val())
        .then(response => {
            if (response == undefined ||
                response.data == undefined ||
                response.data.length == 0) {
                $(endpointInfo).text('No data');
                return;
            }

            //Set Endpoint Bodies
            $(endpointInfo).empty();
            const newForm = $('<div class="form-floating-sm bg-none">');

            response.data.forEach(endpointBody => {
                $(newForm).append(
                    $('<label class="text-light mt-2 h1 manualQueryFormText">').attr({
                        'for': endpointBody.key
                    }).text(endpointBody.key_description));
                //endpointParamBodyInputs
                const newInput = $('<input class="manualQueryFormText form-control form-control-sm mx-auto manualQueryFormTextBody">')
                    .attr({
                        'id': endpointBody.key,
                        'name': endpointBody.key,
                        'required': endpointBody.required == "1",
                        'type': "text",
                        'placeholder': endpointBody.value_hint_type + (endpointBody.required == "1" ? " (required)" : " (optional)")
                    }).val(endpointParamBodyInputs.has(endpointBody.key) ?
                        endpointParamBodyInputs.get(endpointBody.key) :
                        endpointBody.value_default);

                if (endpointBody.key != undefined &&
                    !endpointParamBodyInputs.has(endpointBody.key))
                    endpointParamBodyInputs.set(endpointBody.key,
                        endpointBody.value_default == undefined ? '' : endpointBody.value_default);

                $(newForm).append($(newInput));
                ((tempNewInput, tempKey) =>
                    $(tempNewInput).on('keyup change', () =>
                        endpointParamBodyInputs.set(tempKey, $(tempNewInput).val()))
                )(newInput, endpointBody.key);

                $(newForm).append($("<hr class='smallestDivider mx-auto'>").css({ 'color': 'white' }));
            });

            $(endpointInfo).append($(newForm));

            const checkLastDivider = $(newForm).children();

            if (checkLastDivider.length != 0 &&
                $(newForm).children()[$(newForm).children().length - 1].tagName == "HR")
                $(newForm).children()[$(newForm).children().length - 1].remove();
        });
}
