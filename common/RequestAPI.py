# -*- coding: utf-8 -*-
# 将http请求及响应检验方法提取出来，可做公共模块调用
import requests


class testAPI(object):
    def __init__(self, method, url, data):
        self.method = method
        # self.url = server + route
        self.url = url
        self.data = data

    @property
    def testAPI(self):
        # 根据不同的访问方式来请求接口
        try:
            if self.method == 'post':
                # 通过python获取到json格式的字符串后，可以通过eval函数转换成dict格式
                r = requests.post(self.url, data=eval(self.data))
                # r = requests.post(self.url, data=json.dumps(eval(self.data)))
            elif self.method == 'get':
                r = requests.get(self.url, params=eval(self.data))
            return r
        except Exception, e:
            print 'error:', e

    def getCode(self):
        # 获取访问接口的状态码
        code = self.testAPI.json()['code']
        return code

    def getJson(self):
        # 获取返回信息的json数据
        # json_data = self.testAPI.json()
        json_data = self.testAPI.text
        return json_data


'''
class testLogin(unittest.TestCase):
    def testLoginApi(self):
        """ 测试testAPI()方法 """

        api = testAPI('post', 'http://172.16.36.233:7757/service/user/login',
                      '{"type":0,"uid":"teacher","passwd":"123456","ttype":7,"tid":""}')
        # apicode = api.getCode()
        apijson = api.getJson()
        print apijson


if __name__ == '__main__':
    unittest.main(verbosity=2)
'''