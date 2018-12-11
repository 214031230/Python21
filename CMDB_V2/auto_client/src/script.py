#!/usr/bin/python
# -*- coding:utf-8 -*-
from config import settings
from lib.module_string import import_string


def run():
    """
    采集资产的入口
    1. 读取配置文件，获取当前采集器的模块路径。eq: src.engine.agent.AgentHandler
    2. 把模块路径交给import_string模块进行解析，拿到采集器对象
    3. 支持采集器对象的handler方法
    :return:
    """
    engine_path = settings.ENGINE_HANDLERS.get(settings.ENGINE)
    cls = import_string(engine_path)
    obj = cls()
    obj.handler()
