# -*- coding: utf-8 -*-
# 执行测试用例，并生成测试报告
# 使用discover在指定目录下检索文件，并用run方法执行文件里的用例
import time
import readConfig as rc
from APITest_tool.common.HTMLTestRunner_test import HTMLTestRunner
from APITest_tool.common.PrintLog import MyLog
from APITest_tool.common.SendEmail import MyEmail
# -*- coding: utf-8 -*-
import sys
import unittest
from APITest_Kary.common.RequestAPI import testAPI
from APITest_Kary.common.ReadExcel import readExcel
import threading

# 解决：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe8 in position
# 原因：python2.x的默认编码是ascii，而代码中可能由utf-8的字符导致
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

'''
# 实例化ReadConfig
localReadConfig = rc.ReadConfig()
# 1)获取测试项目、测试模块名，在报告显示
test_programe = localReadConfig.getTestAbout("test_programe")
test_module = localReadConfig.getTestAbout("test_module")
# 2)判断邮件开关，on_off为0发送，为1不发送
on_off = localReadConfig.getEmail("on_off")
'''

# 实例化Log模块的MyLog类
log = MyLog.get_log()
logger = log.logger

# 实例化Email模块的Email类
# email = MyEmail.get_email()


class TestAll(unittest.TestCase):
    """ 测试登录接口，数据从Excel读取 """
    def setUp(self):
        pass

    def test_case_all(self):
        """  Excel表格，一行记录为一条用例 """
        # 登录测试用例，设置表格path、工作簿index
        localReadConfig = rc.ReadConfig()
        excel_path = localReadConfig.getTestCase("excel_path")
        excel_index = localReadConfig.getTestCase("excel_index")
        excel = readExcel(excel_path, int(excel_index))
        number = excel.getNumber
        name = excel.getName
        # server = excel.getServer
        # route = excel.getRoute
        url = excel.getURL
        method = excel.getMethod
        data = excel.getData
        code = excel.getCode
        row = excel.getRows
        # 下面依次遍历每一列的数据，并合成一组请求数据
        # 调用testAPI方法测试
        for i in range(0, row - 1):
            api = testAPI(method[i], url[i], data[i])
            apicode = api.getCode()
            apijson = api.getJson()
            # 判断响应状态码是否与预期一致
            if apicode == code[i]:
                print('{}、{}：测试成功。json数据为：{}'.format(number[i], name[i], apijson))
            else:
                print('{}、{}：测试失败'.format(i + 1, name[i]))

    def tearDown(self):
        pass


'''
# 生成测试报告，保存至Log()生成的文件夹下，及./result/now/
def run_tests():
    filepath = log.logPath
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = filepath + '/' + now + '_result.html'
    try:
        log.logger.info("******** TEST START *********")
        suite = unittest.TestLoader().loadTestsFromTestCase(TestAll)
        f = open(filename, 'wb')
        runner = HTMLTestRunner(stream=f, title=test_programe + ' ' + test_module + ' Test Report',
                            description='Implementation Example with:')
        runner.run(suite)
        f.close()
    except Exception as ex:
        logger.error(str(ex))
    finally:
        # 根据开关，判断是否发送邮件（附件为执行脚本时生成的文件夹zip）
        if int(on_off) == 1:
            email.send_email()
            if email.ifsuccess == 1:
                Send_Email_Msg = '邮件已发送成功！'
                logger.info(Send_Email_Msg)
            else:
                Send_Email_Msg = email.sendMsg
                logger.info(Send_Email_Msg)
        elif int(on_off) == 0:
            logger.info("Doesn't send email to developer.")
        else:
            logger.info("Unknow state.")
        logger.info("******** TEST END *********")
'''


class RunTests():
    def __init__(self):
        self.ifsuccess = 0
        self.Send_Email_Msg = ''
        # self.config = rc.ReadConfig()
        '''
        # 1)获取测试项目、测试模块名，在报告显示
        self.test_programe = self.config.getTestAbout("test_programe")
        self.test_module = self.config.getTestAbout("test_module")
        # 2)判断邮件开关，on_off为0发送，为1不发送
        self.on_off = self.config.getEmail("on_off")
        '''
        # 实例化Email模块的Email类
        # self.email = MyEmail.get_email()

    def run_tests(self):
        config = rc.ReadConfig()
        email = MyEmail.get_email()
        # test_programe = self.config.getTestAbout("test_programe")
        test_programe = config.getTestAbout("test_programe")
        test_module = config.getTestAbout("test_module")
        on_off = config.getEmail("on_off")
        filepath = log.logPath
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filename = filepath + '/' + now + '_result.html'

        try:
            log.logger.info("******** TEST START *********")
            suite = unittest.TestLoader().loadTestsFromTestCase(TestAll)
            f = open(filename, 'wb')
            runner = HTMLTestRunner(stream=f, title=test_programe + ' ' + test_module + ' Test Report',
                                    description='Implementation Example with:')
            runner.run(suite)
            f.close()
        except Exception as ex:
            logger.error(str(ex))
        finally:
            # 根据开关，判断是否发送邮件（附件为执行脚本时生成的文件夹zip）
            if int(on_off) == 1:
                email.send_email()
                # self.ifsuccess = email.ifsuccess
                # self.check_send_email(self.email.ifsuccess)
                if email.ifsuccess == 1:
                    self.Send_Email_Msg = '邮件已发送成功！'
                    logger.info(self.Send_Email_Msg)
                else:
                    self.Send_Email_Msg = '邮件发送失败，' + email.sendErrorMsg
                    logger.info(self.Send_Email_Msg)
            elif int(on_off) == 0:
                logger.info("Doesn't send email to developer.")
                self.Send_Email_Msg = '不发送邮件。'
            else:
                logger.info("Unknow state.")
            logger.info("******** TEST END *********")

    def check_send_email(self, IfSuccess):
        self.ifsuccess = IfSuccess
        if self.ifsuccess == 1:
            self.Send_Email_Msg = '邮件已发送成功！'
            logger.info(self.Send_Email_Msg)
        else:
            self.Send_Email_Msg = '邮件发送失败，' + self.email.sendErrorMsg
            logger.info(self.Send_Email_Msg)
        return self.Send_Email_Msg


class MyTest:
    test = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_test():
        if MyTest.test is None:
            MyTest.mutex.acquire()
            MyTest.test = RunTests()
            MyTest.mutex.release()
        return MyTest.test


if __name__ == "__main__":
    run = MyTest.get_test()
    run.run_tests()

