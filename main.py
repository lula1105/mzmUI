# -*- coding: utf-8 -*-


import os
import pytest
import datetime


def run_all():
    # -s：显示用例中的输出
    # -v：输出更详细的用例执行信息
    # __file__：本文件
    # 生成YYYY-mm-dd-HHMMSS的时间戳
    now = datetime.datetime.now()
    time_str = now.strftime("%Y-%m-%d-%H%M%S")
    # pytest.main(['--alluredir','./report'])
    # 此处命令 --alluredir 生成了报告的原始文件
    pytest.main(["-vs", "--alluredir", "./Report/{}xml".format(time_str)])
    # 此处命令 allure generate 将前面生成的json文件转换为html的报告
    os.system("allure generate ./Report/{}xml -o ./Report/{}html --clean".format(time_str, time_str))
    # 生成的报告index.html不能直接用Chrome打开，打开后看不到内容，需要用allure open打开才能渲染出样式和显示内容
    #os.system("allure open ./Report/{}html".format(time_str))




if __name__ == '__main__':
    run_all()

