import utils.readYaml as readY
import os
from utils.basic_Page import basicPage
from config import config
import time
import allure
from testcase import adminLogin
class searchGroup(basicPage):
    def __init__(self):
        self.yamlreader = None
        self.type=None
        self.eleLoc=None

    def opreateSearchGroupAndCheck(self,groupName,loginEmai,checkType,checkFindType,checkEle):
        beforePath = os.path.dirname(os.path.dirname(__file__))
        #获取维护元素定位的yaml文件
        filePath = beforePath + "\\testElemntYaml\\searchgroupEle.yaml"
        self.yamlreader = readY.read_oneYamlData(self, filePath)
        #类实例化
        #继承basicpage后实例化类
        #bp = basicPage()
        #初始化浏览器驱动打开浏览器
        #bp.openBrowser(browser='chrome')
        bp = adminLogin.admin_login().login()
        with allure.step("打开集团搜索界面"):
            # 打开地址
            url = config.host + self.yamlreader["testinfo"]["url"]
            bp.get(url)
        with allure.step("查找集团编号输入数据"):
            #查找集团编号输入数据
            type = self.yamlreader["testStep"][0]["find_type"]
            eleLoc = self.yamlreader["testStep"][0]["element_info"]
            bp.sendKeys(type, eleLoc, groupName)

        with allure.step("在邮箱输入框输入数据"):
            # 在邮箱输入框输入数据
            type = self.yamlreader["testStep"][1]["find_type"]
            eleLoc = self.yamlreader["testStep"][1]["element_info"]
            bp.sendKeys(type, eleLoc, loginEmai)
        with allure.step("点击搜索"):
            # 点击搜索
            type = self.yamlreader["testStep"][2]["find_type"]
            eleLoc = self.yamlreader["testStep"][2]["element_info"]
            bp.click(type, eleLoc)
            # 检查登录后，当前环境是否是dev环境
            # 强制等待5秒
            time.sleep(5)
        with allure.step("检查查询元素结果"):
            #检查元素是否存在
            flag=bp.isOrNoElementExist(checkType,checkFindType,checkEle)
            #检查查询元素结果
            assert flag == True
        with allure.step("关闭浏览器"):
            bp.quit()

