#!/usr/bin/env python3
import importlib
from repository import models
from .server import Server
from django.conf import settings


class PluginsManage:
    def __init__(self, client_info):
        """
        :param client_info: 取到auto_client传递过来的数据
        """
        self.client_info = client_info
        self.basic = "basic"
        self.board = "board"
        self.plugins_items = settings.PLUGIN_ITEMS

    def exec(self):
        """
        :return:code: 1: 成功 0: 失败
        """
        code = {"code": 1, "msg": None}
        hostname = self.client_info[self.basic]["data"]["hostname"]
        server_obj = models.Server.objects.filter(hostname=hostname).first()

        if not server_obj:
            # 如果对象不存在，则报错（主机名唯一，不进行自动汇报。避免人为错误）
            code["code"] = 0
            code["msg"] = "主机不存在"
            return code

        # 更新服务器基本信息开始
        obj = Server(server_obj, self.client_info[self.basic], self.client_info[self.board])
        obj.process()
        # 更新服务器基本信息结束

        # 更新服务器硬件(内存，硬盘，网卡)开始
        """
        self.plugins_items = {
                        "nic": "api.plugins.nic.Nic",
                        "disk": "api.plugins.disk.Disk",
                        "memory": "api.plugins.memory.Memory",
                }
        """
        for k, v in self.plugins_items.items():
            try:
                model_path, cls = v.rsplit(".", maxsplit=1)
                md = importlib.import_module(model_path)
                cls = getattr(md, cls)
                obj = cls(server_obj, self.client_info[k])
                obj.process()
            except Exception as e:
                code["code"] = 0
                code["msg"] = e
        return code

    # 更新服务器硬件(内存，硬盘，网卡)结束
