# -*- coding: utf-8 -*-
# codecs:用来读取中文文件
# configparser:使用模块中的RawConfigParser()、ConfigParser()或SafeConfigParser()方法，对指定的配置文件做增删改查操作
import os, sys
import codecs
import configparser

#  os.path.realpath(__file__)返回真实路径；
# os.path.sqlit()返回路径的目录和文件名；
# os.getcwd()得到当前工作的目录
# __file__是用来获取模块所在的路径，这里为…\APITestXXX\readConfig.py
# proDir = os.path.split(os.path.realpath(__file__))[0]
# 使用join()拼接config.ini文件的完整路径
# configPath = os.path.join(proDir, "config.ini")
# 打包成exe后会读取不到相对路径文件，暂把配置文件地址设为绝对路径
configPath = "D:\APITest\config.ini"
proDir = os.path.split(os.path.realpath(configPath))[0]
# exePath = sys.prefix
# configPath = os.path.join(exePath, "\config.ini")

'''
# 获取pyInstaller打包成exe后，程序运行时的真实路径
def getExePath():
    sap = '/'
    if sys.argv[0].find(sap) == -1:
        sap = '\\'
    index = sys.argv.rfind(sap)
    path = sys.argv[0][:index] + sap
    return path
'''


class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()
        self.cf = configparser.ConfigParser()
        # self.cf.read(configPath)
        # 解决读取时候的乱码问题
        self.cf.readfp(codecs.open(configPath, "r", "utf-8-sig"))

    # 为指定的section获取一个选项值
    def getTestAbout(self, name):
        value = self.cf.get("ABOUT", name)
        return value

    def getTestCase(self, name):
        value = self.cf.get("TESTCASE", name)
        return value

    def getDB(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def getHttp(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def getEmail(self, name):
        value = self.cf.get("EMAIL", name)
        return value


# 当前，是在测试用例Excel文件目录下创建一个result的文件夹，里面存放测试报告、log、zip
localReadConfig = ReadConfig()
excelPath = localReadConfig.getTestCase("excel_path")
excelDir = os.path.split(os.path.realpath(excelPath))[0]