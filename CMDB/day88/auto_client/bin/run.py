#!/usr/bin/env python3
import sys
import os
import requests

# 配置模块的加载路径
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

# 把用户可以更改的配置文件路径加载到环境变量中,在lib/config/__init__.py中使用
os.environ["auto_client_settings"] = "conf.settings"

from src.plugins import PluginsManager
from lib.config import settings

if __name__ == '__main__':
    # 拿到所有的插件统计的数据
    obj = PluginsManager()
    result = obj.exec_plugins()
    # 使用requests 发送post请求。把采集到客户端信息发送给api
    requests.post(
        url=settings.API,
        data=result,
    )
    print(result)
