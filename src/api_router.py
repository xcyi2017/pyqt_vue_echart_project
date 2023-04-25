import json
from typing import Optional

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QJsonDocument, QThread
from PyQt5.QtWidgets import QWidget, QMessageBox

from src.work import Worker


class ApiRouter(QWidget):
    responseFromServer = pyqtSignal(str)  # 服务端的反馈信号
    receiveMsgFromClient = pyqtSignal(str)  # 从客户端接收到的消息
    receiveMsgFromServer = pyqtSignal(str)

    def __init__(self):
        super(ApiRouter, self).__init__()
        self.__m_worker: Optional[Worker] = None
        self.__thread_worker: Optional[QThread] = None

    def __init_worker_thread(self) -> None:
        self.__thread_worker = QThread()
        self.__m_worker = Worker()
        self.__m_worker.moveToThread(self.__thread_worker)

        self.__m_worker.task_finished.connect(self.on_task_finished)
        self.__m_worker.error_message.connect(self.error)

        self.__thread_worker.finished.connect(self.__thread_worker.deleteLater)
        self.__thread_worker.finished.connect(self.__m_worker.deleteLater)
        self.__thread_worker.started.connect(self.__m_worker.do_task)

    def error(self):
        QMessageBox.critical(self, "错误", "数据读取失败", QMessageBox.Yes)

    def send_data_to_client(self, data: str) -> None:
        self.receiveMsgFromClient.emit(data)

    @pyqtSlot(str)
    def request_from_client(self, st: str) -> None:  # 来自客户端的操作
        parse_st: dict = json.loads(st)
        self.__init_worker_thread()
        self.__thread_worker.start()
        self.__m_worker.add_task(parse_st)

    @pyqtSlot(dict)
    def on_task_finished(self, response: dict) -> None:
        self.remove_thread()
        response_json: str = str(QJsonDocument(response).toJson(QJsonDocument.Compact))
        signal: str = str(response["signal"])
        # # print(response_json)
        self.responseFromServer.emit(response_json)
        self.receiveMsgFromClient.emit(signal)

    def remove_thread(self) -> None:
        if self.__thread_worker.isRunning():
            self.__thread_worker.quit()
        self.__thread_worker.wait()
