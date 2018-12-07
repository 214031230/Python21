#!/usr/bin/python
# -*- coding:utf-8 -*-
from config import settings
from lib.module_string import import_string


def get_server_info(handler, hostname=None):
    """
    循环所有的插件，获取所有的资产信息，然后返回
    1. 循环读取配置文件获取采集器的名称和模块路径
    2. 传递采集器路径给import_string模块返回采集器对象
    3. 拿到采集对象执行process方法拿到采集结果
    4. 把采集结果生成字典反复
    :param handler: 采集器引擎 agent/ssh/salt
    :param hostname: 需要采集的主机名
    :return: info
    """
    info = {}
    for name, path in settings.PLUGIN_DICT.items():
        info["aaa"] = "777"
        cls = import_string(path)
        obj = cls()
        print(name, path)
        result = obj.process(handler, hostname)
        info[name] = result

    print(info)
    return info
