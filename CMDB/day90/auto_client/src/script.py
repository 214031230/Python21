#!/usr/bin/env python3
from lib.config import settings
from src import client


def start():
    """
    判断采集机模式：
    1. AGENT可以直接采集安装采集器的服务器配置
    2. SSH 和 SALT 需要从API获取今日未采集配置的服务器进行采集
    3. 执行采集操作和发送采集数据到API的操作
    :return:
    """
    if settings.MODE == "AGENT":
        obj = client.AgentClient()
    elif settings.MODE == "SSH" or settings.MODE == "SALT":
        obj = client.SaltSshClient()
    else:
        raise Exception("模式不正确！！！")
    obj.exec()
