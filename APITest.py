# -*- coding: utf-8 -*-
# Tkinter实现接口测试工具GUI，提供对config.ini的修改，并执行脚本
import Tkinter
import base64
import os
import time
from Tkconstants import *
from tkMessageBox import *

import readConfig as rc
import updateConfig
from APITest_tool.common.PrintLog import MyLog
from APITest_tool.common.icon import img
from run_tests import MyTest

# 获取config.ini配置文件里的参数值，用来填充表单
localReadConfig = rc.ReadConfig()
Programe = localReadConfig.getTestAbout("test_programe")
Module = localReadConfig.getTestAbout("test_module")
Excel = localReadConfig.getTestCase("excel_path")
Index = localReadConfig.getTestCase("excel_index")
Host = localReadConfig.getEmail("mail_host")
Port = localReadConfig.getEmail("mail_port")
Account = localReadConfig.getEmail("mail_user")
Password = localReadConfig.getEmail("mail_pass")
Receiver = localReadConfig.getEmail("receiver")
Subject = localReadConfig.getEmail("subject")
Content = localReadConfig.getEmail("content")
Tester = localReadConfig.getEmail("testuser")
Switch= localReadConfig.getEmail("on_off")

update = updateConfig.UpdateConfig()
mylog = MyLog()
log = mylog.get_log()
logger = log.logger
run = MyTest.get_test()


def send_mail():
    on_off = int(switch.get())
    if on_off == 1:
        logger.info("邮箱发送开关为ON")
    else:
        logger.info("邮箱发送开关为OFF")


# os.stat()系统调用时用来返回相关文件的系统状态信息
# os.stat().st_size获取文件大小,os.stat(reportpath).st_size != 0 或 os.stat(reportpath).st_size == 0


def callback():
    if askyesno("Verify", "Really quit?"):
        showerror("Yes", 'Not yet implemented')
    else:
        showinfo("No", "Quit has been cancelled")


def testResult():
    # resultPath = log.get_logPath()
    logPath = ''
    try:
        run_test()
        logPath = mylog.get_logPath()
    except Exception, e:
        logger.error("错误:执行失败,"+ str(e))

    if os.path.isdir(logPath) and not os.stat(logPath) == 0:
        showinfo("测试反馈", "测试结果：%s" % logPath +
                 "\n说明：\n1.脚本执行结束，请访问目录查看测试报告、日志；\n2.重新打开工具执行脚本。"
                 + "\n\n邮件发送情况：%s" % run.Send_Email_Msg)
        logger.info("测试报告/日志所在路径：%s" % logPath)
        root.destroy()
    else:
        logger.error("未有测试文档输出")


def run_test():
    # 获取输入框值
    test_programe = programeName.get()
    test_module = moduleName.get()
    test_case = excel.get()
    test_workbook = workbook.get()
    email_host = host.get()
    email_port = port.get()
    email_account = account.get()
    email_password = password.get()
    email_receiver = receiver.get()
    email_subject = subject.get()
    email_content = content.get()
    test_tester = tester.get()
    on_off = switch.get()
    # 修改config.ini
    update.updateConfig(test_programe, test_module, test_case, test_workbook, email_host, email_port, email_account,
                       email_password, email_receiver, email_subject, email_content, test_tester, on_off)
    # 执行run_tests.py
    time.sleep(3)
    run.run_tests()
    # time.sleep(3)


# 实例化Tkinter的Tk类
root = Tkinter.Tk()
# 修改应用界面图标

tmp = open("tmp.ico", "wb+")
tmp.write(base64.b64decode(img))
tmp.close()
root.iconbitmap("tmp.ico")
os.remove("tmp.ico")

# 创建一个窗口
# root.iconbitmap("icon.py")
root.title("接口测试工具V2.0")
root.geometry('600x650')
root.resizable(width=False, height=False)

# 创建控件，每个控件最后要加上.pack()，否则控件无法显示
# 创建Frame，作为容器来布局窗体，Frame(跟对象, [属性列表])
# 最外层窗体，方便调整样式
frm = Tkinter.Frame(root)
Tkinter.Label(root, text='接口测试', font=('Arial', 30)).pack()

# Entry控件，绑定变量 var=StringVar()    lb=Entry(根对象, textvariable = var)
programeName = Tkinter.StringVar()
moduleName = Tkinter.StringVar()
excel = Tkinter.StringVar()
workbook = Tkinter.StringVar()
host = Tkinter.StringVar()
port = Tkinter.StringVar()
account = Tkinter.StringVar()
password = Tkinter.StringVar()
# sender = Tkinter.StringVar()
receiver = Tkinter.StringVar()
subject = Tkinter.StringVar()
content = Tkinter.StringVar()
tester = Tkinter.StringVar()
# switch = Tkinter.IntVar()
switch = Tkinter.StringVar()

# 显示文本和位图
# sticky=W+E+N+S, padx=5, pady=5  居中，四周外延5个长度
#  项目相关、测试用例
about = Tkinter.Frame(frm)
Tkinter.Label(about, text='测试数据', font=('Arial', 20)).grid(row=0, column=0)
Tkinter.Label(about, text='项目：', font=('Arial', 15)).grid(row=1, column=0, sticky=E)
Tkinter.Entry(about, textvariable=programeName).grid(row=1, column=1)

Tkinter.Label(about, text='模块：', font=('Arial', 15)).grid(row=2, column=0, sticky=E)
Tkinter.Entry(about, textvariable=moduleName).grid(row=2, column=1)
Tkinter.Label(about, text='Excel：', font=('Arial', 15)).grid(row=1, column=2, sticky=E)
Tkinter.Entry(about, textvariable=excel).grid(row=1, column=3)
Tkinter.Label(about, text='工作簿：', font=('Arial', 15)).grid(row=2, column=2, sticky=E)
Tkinter.Entry(about, textvariable=workbook).grid(row=2, column=3)
about.pack()

# 邮件相关
email = Tkinter.Frame(frm)
Tkinter.Label(email, text='邮件信息', font=('Arial', 20)).grid(row=0, column=0)
Tkinter.Label(email, text='Host：', font=('Arial', 15)).grid(row=1, column=0, sticky=E)
Tkinter.Entry(email, textvariable=host).grid(row=1, column=1)
Tkinter.Label(email, text='Port：', font=('Arial', 15)).grid(row=1, column=2, sticky=E)
Tkinter.Entry(email, textvariable=port).grid(row=1, column=3)
Tkinter.Label(email, text='账号：', font=('Arial', 15)).grid(row=2, column=0, sticky=E)
Tkinter.Entry(email, textvariable=account).grid(row=2, column=1)
Tkinter.Label(email, text='密码：', font=('Arial', 15)).grid(row=2, column=2, sticky=E)
Tkinter.Entry(email, textvariable=password).grid(row=2, column=3)
Tkinter.Label(email, text='收件人：', font=('Arial', 15)).grid(row=3, column=0, sticky=E)
Tkinter.Entry(email, textvariable=receiver).grid(row=3, column=1, columnspan=3, sticky=W + E + N + S, padx=5)
Tkinter.Label(email, text='主题：', font=('Arial', 15)).grid(row=4, column=0, sticky=E)
Tkinter.Entry(email, textvariable=subject).grid(row=4, column=1, rowspan=2, columnspan=3,
                                                sticky=W + E + N + S, padx=5,pady=5)
Tkinter.Label(email, text='内容：', font=('Arial', 15)).grid(row=6, column=0, sticky=E)
Tkinter.Entry(email, textvariable=content).grid(row=6, column=1, rowspan=3, columnspan=3, sticky=W + E + N + S, padx=5,
                                                pady=5)
# Tkinter.Text(email, textvariable=content).grid(row=6, column=1, rowspan=3, columnspan=3,
# sticky=W + E + N + S, padx=5,pady=5)
Tkinter.Label(email, text='测试人员：', font=('Arial', 15)).grid(row=9, column=0, sticky=E)
Tkinter.Entry(email, textvariable=tester).grid(row=9, column=1)
Tkinter.Label(email, text='发送开关：', font=('Arial', 15)).grid(row=10, column=0, sticky=E)
ON = Tkinter.Radiobutton(email, text="ON", font=('Arial', 15), variable=switch, value=1, command=send_mail)
ON.grid(row=10, column=1, sticky=W + E + N + S, padx=5)
OFF = Tkinter.Radiobutton(email, text="OFF", font=('Arial', 15), variable=switch, value=0, command=send_mail)
OFF.grid(row=10, column=2, sticky=W + E + N + S, padx=5)
email.pack()

# 按钮
button = Tkinter.Frame(frm)
Do = Tkinter.Button(button, text="执行", font=('Arial', 15), command=testResult)
Do.grid(row=0, column=0, columnspan=2, sticky=W + E + N + S, padx=10, pady=10)
Exit = Tkinter.Button(button, text="退出", font=('Arial', 15), command=root.destroy)
Exit.grid(row=0, column=2, columnspan=2, sticky=W + E + N + S, padx=10, pady=10)
button.pack()

# text
text = Tkinter.Frame(frm)
scroll = Tkinter.Scrollbar(text)
Explain = Tkinter.Text(text, height=10, width=75)
scroll.pack(side=LEFT, fill=Y)
Explain.pack(side=LEFT, fill=Y)
scroll.config(command=Explain.yview)
Explain.config(yscrollcommand=scroll.set)

explain = """
说明：
    1.项目、模块、Excel、工作簿为必填项，为空时默认使用上次保存的有效数据；
    2.“Excel”输入约定格式的测试用例文件路径;
    3.“工作簿”填写工作簿序号，从0开始为第一个；
    4.邮件发送开关选择OFF时，可不填邮件信息；否则，需要正确填写完整；
    5.Host、Port为第三方邮件提供，需要邮箱开启STMP服务，密码为授权码；
    6.当需要给多人发送邮件时，收件人邮箱之间以英文分号“;”隔开；
    7.点击“执行”，执行脚本后获取测试结果的保存路径；
    8.若想再次执行，需要重新启动exe。
"""
Explain.insert(END, explain)
# To make the widget read-only, you can change the state option from NORMAL to DISABLED
# 如果是DISABLED的话那就无法编辑、插入、删除。需要编辑时改为NORMAL，完成插入、删除后再改回DISABLED
Explain.config(state=DISABLED)
text.pack()

frm.pack()

# 填充表单的默认值
programeName.set(Programe)
moduleName.set(Module)
excel.set(Excel)
workbook.set(Index)
host.set(Host)
port.set(Port)
account.set(Account)
password.set(Password)
receiver.set(Receiver)
subject.set(Subject)
content.set(Content)
tester.set(Tester)
# switch.set(Switch)
switch.set(int(Switch))

# 进入消息循环
root.mainloop()
