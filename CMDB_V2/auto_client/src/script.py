#!/usr/bin/env python3
from config import settings
from lib.module_string import import_string


def run():
    """
    根据配置文件处理不同的采集器模式
    1. 获取配置文件采集器模块路径
    2. 传递给import_string方法返回一个采集器对象
    3. 执行对象的handle方法获取采集器数据
    :return: 
    """
    module_path = settings.ENGINES_DICT.get(settings.ENGINE)  # src.engines.ssh.SSHHandle
    obj = import_string(module_path)
    obj.handler()
