# -*- coding: utf-8 -*-
# codecs:用来读取中文文件
# configparser:使用模块中的RawConfigParser()、ConfigParser()或SafeConfigParser()方法，对指定的配置文件做增删改查操作
import os
import configparser
import readConfig as rc

# proDir = os.path.split(os.path.realpath(__file__))[0]
# 使用join()拼接config.ini文件的完整路径
# configPath = os.path.join(proDir, "config.ini")

proDir = rc.proDir
configPath = rc.configPath


class UpdateConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        # 解决读取含有中文配置config.ini显示乱码问题
        self.cf.read(configPath, encoding="utf-8-sig")

    def updateConfig(self, test_programe, test_module, test_case, test_workbook, email_host, email_port, email_account,
                     email_password, email_receiver, email_subject, email_content, test_tester, on_off):
        Programe = str(test_programe)
        Module = str(test_module)
        Excel = str(test_case)
        Workbook = str(test_workbook)
        Host = str(email_host)
        Port = str(email_port)
        Account = str(email_account)
        Password = str(email_password)
        Receiver = str(email_receiver)
        Subject = str(email_subject)
        Content = str(email_content)
        Tester = str(test_tester)
        Switch = str(on_off)
        # 先判断传入数据是否为空值
        # 其中，项目名、模块名、用例路径、工作簿、邮箱开关为必填项
        # 其他输入框可置空但不能完全为空格
        if len(Programe) != 0 and Programe.strip() != '':
            self.cf.set("ABOUT", "test_programe", Programe)
        if len(Module) != 0 and Module.strip() != '':
            self.cf.set("ABOUT", "test_module", Module)
        if len(Excel) != 0 and Excel.strip() != 0:
            self.cf.set("TESTCASE", "excel_path", Excel)
        if len(Workbook) != 0 and Workbook.strip() != '':
            self.cf.set("TESTCASE", "excel_index", Workbook)
        if Host.strip() != '':
            self.cf.set("EMAIL", "mail_host", Host)
        if Port.strip() != '':
            self.cf.set("EMAIL", "mail_port", Port)
        if Account.strip() != '':
            self.cf.set("EMAIL", "mail_user", Account)
            self.cf.set("EMAIL", "sender", Account)
        if Password.strip() != '':
            self.cf.set("EMAIL", "mail_pass", Password)
        if Receiver.strip() != '':
            self.cf.set("EMAIL", "receiver", Receiver)
        if Subject.strip() != '':
            self.cf.set("EMAIL", "subject", Subject)
        if Content.strip() != '':
            self.cf.set("EMAIL", "content", Content)
        if Tester.strip() != '':
            self.cf.set("EMAIL", "testuser", Tester)
        if len(Switch) != 0 and Switch.strip() != '':
            self.cf.set("EMAIL", "on_off", Switch)

        self.cf.write(open(configPath, "r+"))
