#!/usr/bin/env python3
import os
import importlib
from . import globals_settings


class Setting:
    """
    globals_settings 配置文件获取
    settings 配置文件获取
    """

    def __init__(self):
        """
        globals_settings：
            1. 循环读globals_settings，取到里面的每一列
            2. 只有是大写的配置文件才生效
            3. 设置k = 参数key
            4. 设置v = 参数value
            5. 设置self.k = v
        settings：
            1. 去环境变量中读取settings的文件路径
            2. 使用importlib加载字符串格式模块
            4. 循环读md_settings，取到里面的每一列
            5. 只有是大写的配置文件才生效
            6. 设置k = 参数key
            7. 设置v = 参数value
            8. 设置self.k = v
        """
        for item in dir(globals_settings):
            if item.isupper():
                k = item
                v = getattr(globals_settings, item)
                setattr(self, k, v)
        md_settings_path = os.environ.get("auto_client_settings")
        md_settings = importlib.import_module(md_settings_path)
        for item in dir(md_settings):
            if item.isupper():
                k = item
                v = getattr(md_settings, item)
                if k == "PLUGINS_ITEMS":
                    self.PLUGINS_ITEMS.update(v)
                else:
                    setattr(self, k, v)


settings = Setting()
