# -*- coding: utf-8 -*-
import pytest
import utils.readYaml as readY
import os
import logging
from pageStep import serach_groupPage
import allure

try:
    beforePath = os.path.dirname(os.path.dirname(__file__))
    logging.info("-----beforePath-----------" + beforePath)
    # 获取维护测试数据和检查点定位的yaml文件
    filePath = beforePath + "\\testDataYaml\\searchGroupData.yaml"
    testDataAndcheck = readY.ReadYaml().read_oneYamlData(filePath)
except FileNotFoundError as file:
    log = logging()
    log.error("文件不存在：{0}".format(filePath))


@allure.feature("登录后查询集团数据")
class TestSearchGroup:

    @pytest.mark.parametrize('args', testDataAndcheck)
    def test_serach_group(self, args):
        groupName = args.get('data').get('groupName')
        loginEmai = args.get('data').get('loginEmai')
        checkType = args.get('check').get('check_type')
        checkFindType = args.get('check').get('find_type')
        checkEle = args.get('check').get('element_info')
        # 初始化查询集团后执行搜索集团且检查搜索结果
        serach_groupPage.searchGroup().opreateSearchGroupAndCheck(groupName, loginEmai, checkType, checkFindType, checkEle)

    def teardown(self):
        logging.info("搜素集团测试用例执行完成")
