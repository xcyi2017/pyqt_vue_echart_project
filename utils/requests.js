import { QWebChannel } from './qwebchannel'

const model = 'eng'
if (model === 'pro') {
    window.qt = {
        webChannelTransport: {
            send() {
                console.log(`
              QWebChannel simulator activated !
            `)
            }
        }
    }
}

export var callBackDict = {
    messageShow: null,
    newMessage: null,
}

export var qtWebChannel = null;  //导出qtWebChannel，供其他页面调用
new QWebChannel(qt.webChannelTransport, (channel) => {
    // all published objects are available in channel.objects under
    // the identifier set in their attached WebChannel.id property
    console.log(channel.objects)
    qtWebChannel = channel.objects.bridge;
    callBack()
    // 进入回调地狱
});

// 回调地狱
function callBack() {
    console.log("初始化")
    qtWebChannel.connectSignal.connect(connectSignalCallBack)
}

function connectSignalCallBack(jsonString) {
    /*
    res: {
        code: 200/400 400就是后台有问题
        func: string 在mount中载入
        data: Dict 传入到view函数中
    }
    */
    const res = JSON.parse(jsonString)
    console.info(res)
    if (res.code === 400) {
        console.log(res)
        return
    }
    callBackDict[res.func](res.data)
}