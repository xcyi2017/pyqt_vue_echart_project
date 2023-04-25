import json
from typing import List

import pandas as pd
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QMutex
from PyQt5.QtWidgets import QFileDialog
from pandas import DataFrame


class Worker(QObject):
    task_finished = pyqtSignal(dict)
    error_message = pyqtSignal()

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.__m_mutex: QMutex = QMutex()
        self.__m_task_list: List[dict] = []

    def get_data(self) -> dict:
        data: dict = {}
        try:
            path, _ = QFileDialog.getOpenFileName()
            dat: DataFrame = pd.read_excel(path, sheet_name="时间应力")
            data = dat.to_dict('list')
        except Exception as e:
            self.error_message.emit()
        finally:
            return data

    def get_data_1(self) -> dict:
        data: dict = {}
        try:
            path, _ = QFileDialog.getOpenFileName()
            dat: DataFrame = pd.read_excel(path, sheet_name="处理1")
            data = json.loads(dat.to_json(orient='table'))
            print(f"{data=}")
        except Exception as e:
            self.error_message.emit()
        finally:
            return data

    @pyqtSlot()
    def do_task(self) -> None:
        # while self.__m_b_start:

        task_info: dict = self.pop_task()
        # print(f"task_info;{task_info}")
        response: dict = {}
        # print("do_task")
        if str(task_info.get("action", "")) == "send-msg":
            response = self.format_response(task_info, "Get Msg", {})
            # print(f"do_task:response{response}")
        elif str(task_info.get("action", "")) == "get-data":
            data: dict = self.get_data()
            response = self.format_response(task_info, "get-data", data)
            self.task_finished.emit(response)
        elif str(task_info.get("action", "")) == "get-data-1":
            data: dict = self.get_data_1()
            response = self.format_response(task_info, "get-data-1", data)
            self.task_finished.emit(response)

    def pop_task(self) -> dict:
        # print("pop_task_start")
        self.__m_mutex.lock()
        task_info: dict = {}
        if len(self.__m_task_list) > 0:
            task_info = self.__m_task_list.pop()
        self.__m_mutex.unlock()
        # print("pop_task_end")
        return task_info

    def add_task(self, task_info: dict) -> None:
        # print("add_task_start")
        self.__m_mutex.lock()
        self.__m_task_list.insert(0, task_info)
        self.__m_mutex.unlock()
        # print("add_task_end")

    @staticmethod
    def format_response(task_info: dict, signal: str, data: dict) -> dict:
        response: dict = {"id": task_info["id"], "signal": signal, "msg": task_info["data"], "data": data}
        return response
