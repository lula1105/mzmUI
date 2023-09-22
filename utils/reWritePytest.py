import pytest
from selenium import webdriver
import os
import allure
_driver=None
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    ��ȡÿ������״̬�Ĺ��Ӻ���
    :param item:
    :param call:
    :return:
    '''
    # ��ȡ���ӷ����ĵ��ý��
    outcome = yield
    rep = outcome.get_result()
    # ������ȡ����call ִ�н����ʧ�ܵ����, ������ setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # ���allure�����ͼ
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('���ʧ�ܽ�ͼ...'):
                allure.attach(_driver.get_screenshot_as_png(), "ʧ�ܽ�ͼ", allure.attachment_type.PNG)

# �������������������ʾ�����ִ�й���
@pytest.fixture(scope="session")
def driver():
    global d
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    d = webdriver.Chrome(options=options)
    yield d
    d.quit()