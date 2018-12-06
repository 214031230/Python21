#!/usr/bin/env python3
from config import settings
from lib.module_string import import_string


def get_server_info(handler, hostname=None):
    """
    循环所有的采集器插件并执行，拿到结果生成字典，返回。
    :param handler: 采集器引擎
    :return: info
    """
    info = {}
    for name, name_path in settings.PLUGINS_DICT.items():
        """
        name = cpu
        name_path = src.plugins.cpu.CPU
        """
        cls = import_string(name_path)
        result = cls.process(handler, hostname)
        info[name] = result
    return info
