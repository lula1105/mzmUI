# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from config.config import *

class Logs:
    # logging模块默认设置的日志级别是warning，而debug和info的级别是低于warning的，所以不会打印这两种日志信息
    def __init__(self, logger=None):
        # 1.定义日志收集器
        # 创建日志器logger对象以及日志级别
        self.logger = logging.getLogger(logger)  # 初始化日志类，定义一个日志收集器
        self.logger.setLevel(logging.DEBUG)  # 设置收集器的级别，不设定的话，默认收集warning及以上级别的日志
        # self.logger.setLevel("DEBUG")  # 也可以设置日志级别

        # self.logTime = datetime.now().strftime("%Y_%m_%d_%H_%M")
        self.logTime = datetime.now().strftime("%Y_%m_%d")
        self.logPath = LogPath
        self.logName = self.logPath + self.logTime + '.log'
        # self.logName = r'../logs\{}.log'.format(time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime()))  # r是防止字符转转义，保留原有的样子（注意：返回上一次的路径是两个..）

        # 创建处理器handler以及日志级别
        # conlHandler = logging.StreamHandler()  # 此处理器是输出到控制台
        fileHandler = logging.FileHandler(self.logName, 'a', encoding='utf-8')  # 此处理器是输出到文件
        # conlHandler.setLevel('DEBUG')  # 设置控制台输出日志级别ERROR 或DEBUG
        fileHandler.setLevel('INFO')  # 设置文件输出日志级别  ERROR'

        # 设置日志输出格式
        # %(asctime)s:打印日志的时间, %(filename)s:打印当前执行程序名, %(levelname)s:打印日志级别名称,
        # %(lineno)s:打印日志的当前行号, %(message)s:打印日志信息, %(name)s:Logger的名字
        # conlFormatter = logging.Formatter(
        #     "%(asctime)s-%(lineno)d-[%(levelname)s]-[msg]: %(message)s")  # 输出到控制台的格式
        fileFormatter = logging.Formatter(
            "%(asctime)s-%(name)s-%(lineno)d-[%(levelname)s]-[msg]: %(message)s")  # 输出到文件中的格式

        # 用setFormatter()将上面设置的formatter配置到handler中
       #  conlHandler.setFormatter(conlFormatter)  # 配置控制台日志输出格式
        fileHandler.setFormatter(fileFormatter)  # 配置文件日志输出格式

        # 用addHandler()将配置好格式的Haddler添加到logger中,进行过滤
        # self.logger.addHandler(conlHandler)
        self.logger.addHandler(fileHandler)

        #  添加下面一句，在记录日志之后移除句柄
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)

        # 关闭处理器
        # conlHandler.close()
        fileHandler.close()

    def get_log(self):
        return self.logger