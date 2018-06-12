# -*- coding: utf-8 -*-
# 读取Excel文件中的数据
# 读取Excel文件里登录部分工作簿用例
# 约定测试用例表格由Number、Name、Server、Route、Method、Data、Code组成
# 调用时，传入表格path、工作簿index
import xlrd


class readExcel(object):
    def __init__(self, path, index):
        self.path = path
        self.index = index

    @property
    def getSheet(self):
        # 获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(self.index)
        return sheet

    @property
    def getRows(self):
        # 获取行数
        row = self.getSheet.nrows
        return row

    @property
    def getCols(self):
        # 获取列数
        col = self.getSheet.ncols
        return col

    # 以下是分别获取每一列的数值，依次遍历每列的每一行数据，并保存在字典中
    @property
    def getNumber(self):
        # 用例序号
        Number = []
        for i in range(1, self.getRows):
            Number.append(int(self.getSheet.cell_value(i, 0)))
        return Number

    @property
    def getName(self):
        # 用例名称
        TestName = []
        for i in range(1, self.getRows):
            TestName.append(self.getSheet.cell_value(i, 1))
        return TestName

    @property
    def getServer(self):
        # 服务器
        TestServer = []
        for i in range(1, self.getRows):
            TestServer.append(self.getSheet.cell_value(i, 2))
        return TestServer

    @property
    def getRoute(self):
        # 接口路径
        TestRoute = []
        for i in range(1, self.getRows):
            TestRoute.append(self.getSheet.cell_value(i, 3))
        return TestRoute

    @property
    def getURL(self):
        # 接口请求URL，Server+Route
        TestURL = []
        for i in range(1, self.getRows):
            TestURL.append(self.getSheet.cell_value(i, 2))
        return TestURL

    @property
    def getMethod(self):
        # 请求方式
        TestMethod = []
        for i in range(1, self.getRows):
            TestMethod.append(self.getSheet.cell_value(i, 3))
        return TestMethod

    @property
    def getData(self):
        # json数据
        TestData = []
        for i in range(1, self.getRows):
            TestData.append(self.getSheet.cell_value(i, 4))
        return TestData

    @property
    def getCode(self):
        # 期望的code值，接口约定
        TestCode = []
        for i in range(1, self.getRows):
            TestCode.append(int(self.getSheet.cell_value(i, 5)))
        return TestCode
