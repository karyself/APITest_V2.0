# -*- coding: utf-8 -*-
import logging
from datetime import datetime
import threading
import os
import sys
import APITest_tool.readConfig as rc


class Log:
    def __init__(self):
        global proDir
        # proDir = rc.excelDir
        proDir = rc.proDir
        self.resultPath = os.path.join(proDir, "result")
        if not os.path.exists(self.resultPath):
            os.mkdir(self.resultPath)
        self.logPath = os.path.join(self.resultPath, str(datetime.now().strftime("%Y%m%d_%H%M%S")))
        if not os.path.exists(self.logPath):
            os.mkdir(self.logPath)
        # 获取logging.getLogger("AppName")的logger实例，如果参数为空则返回root logger
        self.logger = logging.getLogger("IVS7.0")

        # 指定log输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

        # 文件日志
        file_handler = logging.FileHandler(os.path.join(self.logPath, "output.log"))
        file_handler.setFormatter(formatter)  # 1)可以通过setFormatter指定输出格式

        # 控制台日志
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.formatter = formatter  # 2)也可以直接给formatter赋值

        # 为logger添加的日志处理器，可以自定义日志处理器让其输出到其它地方
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        # 指定日志的最低输出级别，默认为WARN级别
        self.logger.setLevel(logging.INFO)


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()
        return MyLog.log

    @staticmethod
    def get_resultPath():
        resultPath = MyLog.log.resultPath
        return resultPath

    @staticmethod
    def get_logPath():
        logPath = MyLog.log.logPath
        return logPath
