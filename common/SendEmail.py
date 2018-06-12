# -*- coding: utf-8 -*-
# 从config.ini读取邮件参数，将测试报告和日志附件发送邮件
# SMTP发送带附件的邮件
import os
import smtplib
import threading
import time
import zipfile
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import APITest_tool.readConfig as rc
from APITest_tool.common.PrintLog import MyLog

# localReadConfig = rc.ReadConfig()
# 实例化Log模块的MyLog类
log = MyLog.get_log()
logger = log.logger


'''
# __init__()初始实例时，会不能马上读取更新后的config.ini
class Email:
    def __init__(self):
        self.localReadConfig = rc.ReadConfig()
        global host, user, password, port, sender, title, content
        host = self.localReadConfig.getEmail("mail_host")
        user = self.localReadConfig.getEmail("mail_user")
        password = self.localReadConfig.getEmail("mail_pass")
        port = self.localReadConfig.getEmail("mail_port")
        sender = self.localReadConfig.getEmail("sender")
        title = self.localReadConfig.getEmail("subject")
        content = self.localReadConfig.getEmail("content")
        self.value = self.localReadConfig.getEmail("receiver")
        self.ifsuccess = 0
        self.sendErrorMsg = ''
        
        self.receiver = []
        # 收信人列表，依次遍历字符创，以/符号区别一个元素
        for i in str(self.value).split("/"):
            self.receiver.append(i)
        # 邮件主题加上时间
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = title + " " + date
        self.mylog = MyLog()
        self.log = self.mylog.get_log()
        self.logger = self.log.logger
        # self.msg = MIMEMultipart('mixed')

        # ------------Python SMTP发送带附件的邮件-------------
        # 1）创建一个带附件的实例
        self.msg = MIMEMultipart()

    # 2）邮件主体：From、To、Subject
    def config_header(self):
        self.msg['from'] = sender
        # join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串，str.join(sequence)
        # 邮件收信人以分号隔开
        self.msg['to'] = ";".join(self.receiver)
        self.msg['subject'] = self.subject

    # 3）邮件正文内容：content
    def config_content(self):
        content_plain = MIMEText(content, 'plain', 'utf-8')
        self.msg.attach(content_plain)

    def config_file(self):
        if self.check_file():
            reportpath =self.mylog.get_logPath()
            now = time.strftime("%Y-%m-%d %H_%M_%S")
            # zippath = os.path.join(rc.excelDir, "result", now + "_result.zip")
            zippath = os.path.join(rc.proDir, "result", now + "_result.zip")
            # 压缩文件
            # 打包目录文件/文件夹为zip（未压缩）
            # files = glob.glob(reportpath + '/*')
            f = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
            """
            for file in files:
                f.write(file)
            f.close()
            """
            pre_len = len(os.path.dirname(reportpath))
            for parent, dirname, files in os.walk(reportpath):
                for file in files:
                    pathfile = os.path.join(parent, file)
                    # 截取相对路径打包
                    arcname = pathfile[pre_len:].strip(os.path.sep)
                    f.write(pathfile, arcname)
            f.close()

            # 4）添加附件，可构造多个附件实例
            # 添加压缩后的报告文件为附件
            reportfile = open(zippath, 'rb').read()
            attach = MIMEText(reportfile, 'base64', 'utf-8')
            attach['Content-Type'] = 'application/octet-stream'
            # filename可以任意写，其为邮件中的附件名字
            attach['Content-Disposition'] = 'attachment; filename="test.zip"'
            try:
                self.msg.attach(attach)
            except Exception as e:
                logger.info("附件添加失败")
                logger.error(e)
        else:
            logger.debug("check_file():False")

    def check_file(self):
        reportpath = self.mylog.get_logPath()
        # os.stat()系统调用时用来返回相关文件的系统状态信息
        # os.stat().st_size获取文件大小,os.stat(reportpath).st_size != 0 或 os.stat(reportpath).st_size == 0
        if os.path.isdir(reportpath) and not os.stat(reportpath) == 0:
            return True
        else:
            logger.info("报告地址错误")
            return False

    # 5）SMTP发送邮件
    # smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
    # SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])
    def send_email(self):
        
        self.config_header()
        self.config_content()
        self.config_file()
        try:
            # 发件的第三方邮箱使用SMTP服务，使用ssl连接
            smtp = smtplib.SMTP_SSL(host, int(port))
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())
            smtp.quit()
            self.logger.info("The test report has been sent to developer by email.")
            self.ifsuccess = 1
        except smtplib.SMTPException as ex:
            self.logger.error(str(ex))
            self.sendErrorMsg = str(ex)
            self.ifsuccess = 0
'''


class Email:
    def __init__(self):
        self.ifsuccess = 0
        self.sendErrorMsg = ''
        self.mylog = MyLog()
        self.log = self.mylog.get_log()
        self.logger = self.log.logger
        # self.msg = MIMEMultipart('mixed')

        # ------------Python SMTP发送带附件的邮件-------------
        # 1）创建一个带附件的实例
        self.msg = MIMEMultipart()

    # 2）邮件主体：From、To、Subject
    def config_header(self, sender, receiver, subject):
        self.msg['from'] = sender
        # join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串，str.join(sequence)
        # 邮件收信人以分号隔开
        self.msg['to'] = ";".join(receiver)
        self.msg['subject'] = subject

    # 3）邮件正文内容：content
    def config_content(self, content):
        content_plain = MIMEText(content, 'plain', 'utf-8')
        self.msg.attach(content_plain)

    def config_file(self):
        if self.check_file():
            reportpath = self.mylog.get_logPath()
            now = time.strftime("%Y-%m-%d %H_%M_%S")
            # zippath = os.path.join(rc.excelDir, "result", now + "_result.zip")
            zippath = os.path.join(rc.proDir, "result", now + "_result.zip")
            # 压缩文件
            # 打包目录文件/文件夹为zip（未压缩）
            # files = glob.glob(reportpath + '/*')
            f = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
            """
            for file in files:
                f.write(file)
            f.close()
            """
            pre_len = len(os.path.dirname(reportpath))
            for parent, dirname, files in os.walk(reportpath):
                for file in files:
                    pathfile = os.path.join(parent, file)
                    # 截取相对路径打包
                    arcname = pathfile[pre_len:].strip(os.path.sep)
                    f.write(pathfile, arcname)
            f.close()

            # 4）添加附件，可构造多个附件实例
            # 添加压缩后的报告文件为附件
            reportfile = open(zippath, 'rb').read()
            attach = MIMEText(reportfile, 'base64', 'utf-8')
            attach['Content-Type'] = 'application/octet-stream'
            # filename可以任意写，其为邮件中的附件名字
            attach['Content-Disposition'] = 'attachment; filename="test.zip"'
            try:
                self.msg.attach(attach)
            except Exception as e:
                logger.info("附件添加失败")
                logger.error(e)
        else:
            logger.debug("check_file():False")

    def check_file(self):
        reportpath = self.mylog.get_logPath()
        # os.stat()系统调用时用来返回相关文件的系统状态信息
        # os.stat().st_size获取文件大小,os.stat(reportpath).st_size != 0 或 os.stat(reportpath).st_size == 0
        if os.path.isdir(reportpath) and not os.stat(reportpath) == 0:
            return True
        else:
            logger.info("报告地址错误")
            return False

    # 5）SMTP发送邮件
    # smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
    # SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])
    def send_email(self):
        localReadConfig = rc.ReadConfig()
        # global host, user, password, port, sender, title, content, receiver, subject
        host = localReadConfig.getEmail("mail_host")
        user = localReadConfig.getEmail("mail_user")
        password = localReadConfig.getEmail("mail_pass")
        port = localReadConfig.getEmail("mail_port")
        sender = localReadConfig.getEmail("sender")
        title = localReadConfig.getEmail("subject")
        content = localReadConfig.getEmail("content")
        value = localReadConfig.getEmail("receiver")
        receiver = []
        # 收信人列表，依次遍历字符创，以/符号区别一个元素
        for i in str(value).split("/"):
            receiver.append(i)
        # 邮件主题加上时间
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subject = title + " " + date

        self.config_header(sender, receiver, subject)
        self.config_content(content)
        self.config_file()
        try:
            # 发件的第三方邮箱使用SMTP服务，使用ssl连接
            smtp = smtplib.SMTP_SSL(host, int(port))
            smtp.login(user, password)
            smtp.sendmail(sender, receiver, self.msg.as_string())
            smtp.quit()
            self.logger.info("The test report has been sent to developer by email.")
            self.ifsuccess = 1
        except smtplib.SMTPException as ex:
            self.logger.error(str(ex))
            self.sendErrorMsg = str(ex)
            self.ifsuccess = 0


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email


''''
if __name__ == "__main__":
    email = MyEmail.get_email()
'''