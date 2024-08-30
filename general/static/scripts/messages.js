/**
 * Clears a specific message that displayed to the user after a certain
 * timeout.
 * @param {object} element - DOM element to remove
 * @returns {void}
 */
function clearMessage(element) {
    $(element).remove();
}

/**
 * Clears all messages that are displayed to the user after a certain timeout.
 * @returns {void}
 */
function clearMessages() {
    $("div.messageContainer").html('');
}

/**
 * Shows a message from client-side requests to the server
 * mimics server-side sent flash messages
 * Modifies the DOM
 * @param {string} message - Message to show to the user
 * @param {string} type - Style based class to use to show message type to the user.
 * @returns {void}
 */
function showMessage(message, type) {
    const messageContainer = $("div.messageContainer")
    const toRemove = ($("<div>")
        .addClass("bg-warning ml-lg-5 my-lg-3 mr-3 mx-lg-5 pl-4 " + 
            "rounded-lg-inverse-pill alertTest alert alert-" + 
            type + 
            "fade show")
        .attr({ "role": "alert" })
        .append($("<strong>").text(message)));
        
    messageContainer.append($(toRemove));
    //Automatically clear messages
    setTimeout(() => clearMessage(toRemove), 3500);
}
