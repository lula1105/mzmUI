# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.action_chains import *
import datetime
from utils.loggers import *



class basicPage(object):
    # 初始化页面的操作
    def __init__(self):
        """
        构造函数，创建必要的实例变量
        """
        self.driver = None
        #self.log = Logs().get_log()  # 初始化一个log对象

    #初始化浏览器
    pytest.fixture(scope='session',autouse=True)
    def openBrowser(self,browser='chrome'):
        self.browser=browser.lower()
        if self.browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.driver == 'ie':
            self.driver = webdriver.Ie()
        elif self.driver == 'edge':
            self.driver =webdriver.Edge()
        else:
            self.log.info("不支持，请在此添加其他浏览器代码实现！")
        #窗口最大化
        self.driver.maximize_window()
        #隐式等待
        self.driver.implicitly_wait(10)
        return  self.driver


    #请求网址url
    def get(self,url):
        self.driver.get(url)

    #封装find_element()
    def get_by(self,type,*value):
        if type=='id':
            try:
                locator=self.driver.find_element(By.ID,*value)
            except NoSuchElementException as e:
                self.log.error("无法查找到元素By.ID" + value)
        elif type == 'name':
            try:
                locator = self.driver.find_element(By.NAME, *value)
            except NoSuchElementException as e:
                logging.info("无法查找到元素By.NAME" + value)
        elif type == 'classname':
            try:
                locator = self.driver.find_element(By.CLASS_NAME, *value)
            except NoSuchElementException as e:
                self.log.error("无法查找到元素By.CLASS_NAME" + value)
        elif type == 'tagname':
            try:
                locator = self.driver.find_element(By.TAG_NAME, *value)
            except NoSuchElementException as e:
                self.log.error("无法查找到元素By.TAG_NAME" + value)
        elif type == 'linktext':
            try:
                locator = self.driver.find_element(By.LINK_TEXT, *value)
            except NoSuchElementException as e:
                self.log.error("无法查找到元素By.TAG_NAME" + value)
        elif type == 'partiallinktext':
            try:
                locator = self.driver.find_element(By.PARTIAL_LINK_TEXT, *value)
            except NoSuchElementException as e:
                self.log.error("无法查找到元素By.TAG_NAME" + value)
        elif type == 'css':
            try:
                locator = self.driver.find_element(By.CSS_SELECTOR, *value)
            except NoSuchElementException as e:
                self.log.error("无法查找到元素By.TAG_NAME" + value)
        elif type == 'xpath':
            try:
                locator = self.driver.find_element(By.XPATH, *value)
            except NoSuchElementException as e:
                self.log.error("无法查找到元素By.TAG_NAME" + value)
        else:
            raise BaseException(f'定位的类型{type}不支持')
        return locator

    def sendKeys(self,type,element,text=''):
        try:
            self.get_by(type,element).send_keys(text)
        except Exception as e:
            self.log.error(f"在元素{element}输入{text}失败")
    #def sendKeys(self,loc,txt):
    #    self.locator(loc).send_keys(txt)
    def click(self,type,locator):
        try:
            self.get_by(type,locator).click()
        except Exception as e:
            self.log.error(f"在元素{locator}点击失败")

    def clear(self,type,locator):
        try:
            self.get_by(type,locator).clear()
        except Exception as e:
            self.log.error(f"在元素{locator}清空文本失败")

    def isSelected(self,type, locator):
        '''判断元素是否被选中，返回bool布尔值'''
        ele = self.get_by(type,locator)
        r = ele.is_selected()  # 判断元素是否被选中并返回
        return r

    def isOrNoElementExist(self,checktype,type, locator):
        if checktype =='contains':
            try:
                self.get_by(type, locator)
                return True
            except:
                return False
        else:
            try:
                self.get_by(type, locator)
                return False
            except:
                return True

    def is_title(self, _title=''):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_ls(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title=''):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text=''):
        '''返回bool值'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
            try:
                result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator, _text))
                return result
            except:
                return False

    def is_value_in_element(self, locator, _value=''):
        '''返回bool值,value为空字符串，返回Fasle'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=("id","value1")')
            try:
                result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator, _value))
                return result
            except:
                return False

    def is_alert(self, timeout=10):
        try:
            result = WebDriverWait(self.driver, timeout,self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self, type,locator):
        '''获取文本'''
        try:
            t = self.get_by(type,locator).text
            return t
        except:
            print('获取text失败，返回”“')
            return ""

    def get_attribute(self, type,locator, name):
        '''获取属性'''
        try:
            element = self.get_by(type,locator)
            return element.get_attribute(name)
        except:
            print('获取%属性失败，返回""' % name)
            return ""

    def js_focus_element(self,type, locator):
        '''聚焦元素'''
        target = self.get_by(type,locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = 'window.scrollTo(0,0)'
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        '''滚动到底部'''
        js = 'window.scrollTo(%s,document.body.scrollHeight)' % x
        self.driver.execute_script(js)

    def into_iframe(self, element):
        """
        进入iframe
        :param element:  ?
        :return:
        """
        try:
            ele = self.driver.find_element(element)
            self.driver.switch_to.frame(ele)
        except Exception as e:
            self.log.error("切换框架frame失败！")


    def switch_handle(self, window_name):
        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        r = self.is_alert()
        if not r:
            print('alert不存在')
        else:
            return r

    def move_to_element(self,type, locator):
        '''鼠标悬停操作'''
        ele = self.get_up(type,locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def error_screenshots(self, screenshots_path,name):
        """
        保存截图
        :param name:根据被调用传入的名字,生成png的图片
        :return:
        """
        try:
            file_path = screenshots_path
            times = datetime.datetime.now().strftime('%m-%d-%H-%M-%S')
            filename = file_path + times + '{}.png'.format(name)

            self.driver.get_screenshot_as_file(filename)
            logging.info("正在保存图片:{}".format(filename))
        except Exception as e:
            logging.error('图片报存错误:{}'.format(e))
            raise

    def getImage(self, image_name):
        """
        生成用例失败的截图
        :param image_name: 截图的名称
        :return:
        """
        try:
            nowTime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            NewPicture = ImagePath + '\\' + nowTime + '_' + image_name + '.png'  # 保存图片为png格式
            self.driver.get_screenshot_as_file(NewPicture)
        except Exception as e:
            self.log.error(u'截图失败！')
    def quit(self):
        """
        退出浏览器
        :return:
        """
        try:
            self.driver.quit()
        except Exception as e:
            self.log.error("退出浏览器失败！")

        # 后退
    def back(self):
        self.driver.back()

    # 前进
    def forword(self):
        self.driver.forword()
