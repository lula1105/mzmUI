# -*- coding: utf-8 -*-
import utils.readYaml as readY
import os
from config import config
from utils.basic_Page import basicPage
import time


# print(os.getcwd())
# print(os.path.dirname(__file__))
# 当前路径的上⼀个路径
# print(os.path.dirname(os.path.dirname(__file__)))

#登录操作步骤
#testStep 是操作步骤，check 登录成功后检查点
class loginPageLocators(basicPage):
    def __init__(self):
        self.yamlreader = None
        self.findType=None
        self.eleLoc=None
        self.checkType=None
    def loginAction(self, userName, passWord):
        beforePath = os.path.dirname(os.path.dirname(__file__))
        #获取维护元素定位的yaml文件
        filePath = beforePath + "\\testElemntYaml\\adminLoginEle.yaml"
        self.yamlreader = readY.ReadYaml().read_oneYamlData(filePath)
        #继承basicpage后实例化类
        bp = basicPage()
        #初始化浏览器驱动打开浏览器
        bp.openBrowser(browser='chrome')
        # 打开地址
        url = config.host + self.yamlreader["testinfo"]["url"]
        bp.get(url)
        # 查找账户输入框,在用户名输入数据
        findType = self.yamlreader["testStep"][0]["find_type"]
        eleLoc = self.yamlreader["testStep"][0]["element_info"]
        bp.sendKeys(findType, eleLoc, userName)
        # 在密码输入框输入数据
        findType = self.yamlreader["testStep"][1]["find_type"]
        eleLoc = self.yamlreader["testStep"][1]["element_info"]
        bp.sendKeys(findType, eleLoc, passWord)
        # 点击确定
        findType = self.yamlreader["testStep"][2]["find_type"]
        eleLoc = self.yamlreader["testStep"][2]["element_info"]
        bp.click(findType, eleLoc)
        # 检查登录后，当前环境是否是dev环境
        # 强制等待5秒
        time.sleep(5)
        findType = self.yamlreader["Check"][0]["find_type"]
        eleLoc = self.yamlreader["Check"][0]["element_info"]
        checkType=self.yamlreader['Check'][0]['check_type']
        #检查元素是否存在
        flag=bp.isOrNoElementExist(checkType,findType, eleLoc)
        assert flag == True
        return bp

