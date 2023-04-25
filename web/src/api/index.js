import ApiClient from '../plugins/webBridge';

const apiClient = new ApiClient("context", "request_from_client", "responseFromServer");
apiClient.addResponseListener();

export function sendMsg(msg) {
    return apiClient.send({
        action: 'send-msg',
        data: msg
    });
}

export function openFile(msg) {
    return apiClient.send({
        action: "get-data",
        data: msg
    })
}


export function openFile_1(msg) {
    return apiClient.send({
        action: "get-data-1",
        data: msg
    })
}

export function sendSyncMsg(msg) {
    return apiClient.send({
        action: 'send-msg-sync',
        data: msg
    });
}

function _addMsgListener(callback) {
    apiClient.on("receiveMsgFromServer", callback);
}

function _removeMsgListener(callback) {
    apiClient.off("receiveMsgFromServer", callback);
}

export const msgListener = {
    add: _addMsgListener,
    remove: _removeMsgListener
};