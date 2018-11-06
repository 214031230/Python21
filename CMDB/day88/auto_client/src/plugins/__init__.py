#!/usr/bin/env python3
from lib.config import settings
import importlib
import subprocess
import paramiko
import traceback


# def func():
#     """
#     1. server_info 用来存储插件返回的信息
#     2. 循环所有插件，不在配置文件中的插件不会生效
#     3. 插件路径格式为：src.plugins.board.Board  切割后拿到插件模块 和 插件对应的类
#     4. 使用importlib导入字符串格式的插件
#     5. 使用反射执行类拿到类对象
#     6. 执行对象方法拿到硬件信息
#     7. 把硬件信息以字典格式保存起来
#
#     :return:
#     """
#
#     server_info = {}
#
#     for k, v in settings.PLUGINS_ITEMS.items():
#
#         module_path, cls_name = v.rsplit(".", maxsplit=1)
#         m = importlib.import_module(module_path)
#         obj = getattr(m, cls_name)()
#         ret = obj.process()
#         server_info[k] = ret
#
#     return server_info

class PluginsManager:
    def __init__(self, hosts=None):
        self.mode = settings.MODE
        self.hosts = hosts
        self.plugins_item = settings.PLUGINS_ITEMS
        self.debug = settings.DEBUG
        if self.mode == "SSH":
            self.port = settings.PORT
            self.user = settings.USER
            self.pwd = settings.PASSWORD

    def exec_plugins(self):
        """
            1. server_info 用来存储插件返回的信息
            2. 循环所有插件，不在配置文件中的插件不会生效
            3. 插件路径格式为：src.plugins.board.Board  切割后拿到插件模块 和 插件对应的类
            4. 使用importlib导入字符串格式的插件
            5. 使用反射执行类拿到类对象
                1. 判断这个类是否有initial方法
                    1. 如果有则 obj = cls.initial()  "cls.initial() 返回还是类对象 cls()"
                    2. 如果没有 obj = cls()
            6. 执行对象方法拿到硬件信息
            7. 把硬件信息以字典格式保存起来
        :return:
        """
        server_info = {}
        for k, v in self.plugins_item.items():
            info = {"status": True, "data": None, "msg": None}
            try:
                module_path, cls_name = v.rsplit(".", maxsplit=1)
                m = importlib.import_module(module_path)
                cls = getattr(m, cls_name)
                if hasattr(cls, "initial"):
                    obj = cls.initial()
                else:
                    obj = cls()
                ret = obj.process(self.exec_cmd, self.debug)
                info["data"] = ret
            except Exception as e:
                info["status"] = False
                info["msg"] = traceback.format_exc()
            server_info = info
        return server_info

    def exec_cmd(self, cmd):
        """
        使用函数传参的方式实现
        根据采集器模式来执行不同的命令
        :param cmd:
        :return:
        """
        if self.mode == "AGENT":
            result = subprocess.getoutput(cmd)
        elif self.mode == "SSH":
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=self.hosts, port=self.port, username=self.user, password=self.pwd)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = stdout.read()
            ssh.close()

        elif self.mode == "SALT":
            result = subprocess.getoutput('salt "%s" cmd.run "%s"' % (self.hosts, cmd))
        else:
            raise Exception("模式选择错误：AGENT,SSH,SALT")

        return result

