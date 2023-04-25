import sys

from PyQt5.QtCore import QUrl, QFileInfo, Qt
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineDownloadItem
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

from src.api_router import ApiRouter

from ui.ui_app_ui import Ui_Form


class WinForm(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)

        self.__api_router: ApiRouter = ApiRouter()
        self.__web: QWebEngineView = QWebEngineView(self)
        # self.__thread_worker: QThread = QThread()
        self.__channel: QWebChannel = QWebChannel(self.__web)

        self.setupUi(self)

        # self.init_worker_thread()
        self.init_webengine()

        self.scrollArea.setWidget(self.__web)

    def init_webengine(self) -> None:
        # 屏蔽右击菜单
        self.__web.setContextMenuPolicy(Qt.NoContextMenu)

        self.__api_router.receiveMsgFromClient.connect(self.on_receive_message_from_js)
        self.__channel.registerObject("context", self.__api_router)
        self.__web.page().setWebChannel(self.__channel)
        html_url: QUrl = QUrl('http://localhost:8080')
        # html_url: QUrl = QUrl("qrc:/web/dist/index.html")
        self.__web.load(html_url)

        # 保存图片
        self.__web.page().profile().downloadRequested.connect(self.on_download_request)

    def on_download_request(self, download: QWebEngineDownloadItem):
        download.downloadProgress.connect(self._download_progress)
        download.finished.connect(lambda: print("下载完成"))

        # 下载文件的保存路径及文件名
        old_path: str = download.path()
        suffix: str = QFileInfo(old_path).suffix()
        # 下载文件类型
        file_type: str = download.mimeType()
        # 后缀切割
        unknown_suffix: str = file_type.split("/")[-1]
        path, _ = QFileDialog.getSaveFileName(self, "保存图片", old_path, f".*{unknown_suffix};;.*{suffix}")

        if path:
            download.setPath(path)
            download.accept()

    def _download_progress(self, bytes_received: int, bytes_total: int):
        print(f"{bytes_received=},{bytes_total=}")

    def on_receive_message_from_js(self, data: str):
        print(f"从js获得数据", data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WinForm()
    window.show()
    sys.exit(app.exec_())
