#!/usr/bin/env python3
import sys
import os
import importlib
import requests

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

if __name__ == '__main__':
    from conf import settings

    # server_info 用来存储插件返回的信息
    server_info = {}
    # 循环所有插件，不在配置文件中的插件不会生效
    for k, v in settings.PLUGINS_ITEMS.items():
        # 插件路径格式为：src.plugins.board.Board  切割后拿到插件模块 和 插件对应的类
        module_path, cls_name = v.rsplit(".", maxsplit=1)
        # 使用importlib导入字符串格式的插件
        m = importlib.import_module(module_path)
        # 使用反射执行类拿到类对象
        obj = getattr(m, cls_name)()
        # 执行对象方法拿到硬件信息
        ret = obj.process()
        # 把硬件信息以字典格式保存起来
        server_info[k] = ret

    # 使用requests 发送post请求。把采集到客户端信息发送给api
    requests.post(
        url=settings.API,
        data=server_info,
    )
    print(server_info)
    