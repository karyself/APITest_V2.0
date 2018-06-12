# APITest_V2.0
## 框架
Python + Requests 实现的接口自动化测试框架</br>
configparser对指定的配置文件进行增删改查</br>
xlrd读取测试用例Excel，实现数据驱动</br>
unittest + HTMLTestRunner生成测试用例，执行生成HTML格式的测试报告</br>
logging执行过程输出日志</br>
email发送邮件，可附件发送测试报告、日志</br>
Tkinter将框架装饰成GUI工具</br>

## 工程结构
脚本由Python语言编写，整个工程是个Python package，如图所示。将公共方法封装成单个模块，保存在common目录下。</br>
![Alt text](C:/Users/Administrator/Desktop/dir.png)</br>
__init__.py：默认为空</br>
config.ini：配置文件，保存项目相关、测试用例、邮件相关等常用参数</br>
readConfig.py：读取配置文件（当前是以绝对路径打开config.ini）</br>
updateConfig.py：更新配置文件</br>
run_tests.py：工具控制台界面，实现脚本的整体调用，可单独执行</br>
APITest.py：工具GUI界面，调用run_tests.py方法，执行测试</br>
common/__init__.py：默认为空</br>
common/ReadExcel.py：读取Excel表格指定工作簿的单元格值</br>
common/RequestAPI.py：模拟http请求及响应检验</br>
common/PrintLog.py：输出日志</br>
common/SendEmail.py：发送邮件</br>
common/HTMLTestRunner_test.py：修改HTMLTestRunner.py部分地方，使报告显示更为美观</br>
common/codeIMG.py：将icon.ico转换成icon.py文件，作为GUI的ICON</br>
