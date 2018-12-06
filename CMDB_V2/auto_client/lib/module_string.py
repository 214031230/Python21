#!/usr/bin/env python3
import importlib


def import_string(path):
    """
    1. 把采集器路径切割成两部分，采集器路径和类
    2. 使用importlib模块导入字符串格式的模块
    3. 使用反射根据模块获取类
    4. 类加() 返回一个类对象即采集器对象
    :param path: 采集器模块路径，配置文件中配置的
    :return: 
    """
    module, cls = path.rsplit(".", maxsplit=1)  # module=src.engines.ssh | cls=SSHHandle
    module = importlib.import_module(module)
    cls = getattr(module, cls)
    return cls()