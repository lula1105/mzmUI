# -*- coding: utf-8 -*-
from pageStep.adminLoginPage import loginPageLocators
import utils.readYaml as readY
import os
from utils.basic_Page import  basicPage
#运营端管理员登录

class admin_login(basicPage):
    def __init__(self):
        super().__init__()
        self.yamlreader=None
        beforePath=os.path.dirname(os.path.dirname(__file__))
        #获取输入的数据
        filePath = beforePath + "\\testDataYaml\\adminLoginData.yaml"
        self.yamlreader= readY.ReadYaml().read_oneYamlData(filePath)
    def login(self):
        username=self.yamlreader["data"]["userName"]
        password=self.yamlreader["data"]["passWord"]
        lp=loginPageLocators()
        lp=lp.loginAction(username,password)
        return lp





