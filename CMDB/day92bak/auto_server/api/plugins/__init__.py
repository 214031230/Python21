#!/usr/bin/env python3
import importlib
from repository import models
from .server import Server
from django.conf import settings
from django.db import transaction


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
            """
            如果需要自动发现需要在这里修改代码
            """
            # 自动发现开始
            # 增加server表开始
            with transaction.atomic():
                tmp = {}
                tmp.update(self.client_info[self.basic]["data"])
                tmp.update(self.client_info[self.board]["data"])
                server_obj = models.Server.objects.create(**tmp)
                # 增加server表结束

                # 增加硬盘表数据开始
                for i in self.client_info["disk"]["data"].values():
                    i["server_obj"] = server_obj
                    models.Disk.objects.create(**i)
                # 增加硬盘表数据结束

                # 增加内存表数据开始
                for i in self.client_info["memory"]["data"].values():
                    i["server_obj"] = server_obj
                    models.Memory.objects.create(**i)
                # 增加内存表数据结束

                # 增加网卡表数据开始
                for k, v in self.client_info["nic"]["data"].items():
                    v["server_obj"] = server_obj
                    v["name"] = k
                    models.NIC.objects.create(**v)
                # 增加网卡表数据结束
                # 自动发现结束
                # 关闭自动发现开始
                # code["code"] = 0
                # code["msg"] = "主机不存在"
                # 关闭自动发现结束
                return code

        with transaction.atomic():
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
