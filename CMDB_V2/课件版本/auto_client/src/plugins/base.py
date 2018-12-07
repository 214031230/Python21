#!/usr/bin/python
# -*- coding:utf-8 -*-
from config import settings


class BasePlugin(object):
    """
    采集器的基类，规范抽象方法。
    """

    def __init__(self):
        """
        初始化属性，所有采集器都会用到的属性，这样在派生类中不需要重复导入settings
        """
        self.debug = settings.DEBUG
        self.base_dir = settings.BASEDIR

    def get_os(self, handler, hostname):
        """
        获取操作系统版本
        代码未实现
        :param handler: 采集器引擎 ssh/agent/salt
        :param hostname: 需要采集的主机
        :return: 操作系统版本
        """
        # return handler.cmd('查看系统的命令',host)
        return 'linux'

    def process(self, handler, hostname):
        """
        执行采集器，获取采集结果
        1. 根据操作系统版本，执行对应的采集器
        2. 如果是windows执行            return self.win(hander, hostname)
        3. 如果是linux执行            return self.linux(hander, hostname)
        :param handler:
        :param hostname: 需要采集的主机
        :return: 采集结果
        """
        os = self.get_os(handler, hostname)
        if os == 'windows':
            return self.win(handler, hostname)
        else:
            return self.linux(handler, hostname)

    def win(self, handler, hostname):
        """
        约束所有的派生类都必须实现cmd方法
        根据不同的引擎执行对应的方法执行对应的命令
        :param handler:  采集器引擎  agent/ssh/salt
        :param hostname:  需要采集的主机
        :return: 
        """
        raise NotImplementedError('win must be implemented ')

    def linux(self, handler, hostname):
        """
        约束所有的派生类都必须实现cmd方法
        根据不同的引擎执行对应的方法执行对应的命令
        :param handler:  采集器引擎  agent/ssh/salt
        :param hostname:  需要采集的主机
        :return: 
        """
        raise NotImplementedError('linux must be implemented ')
