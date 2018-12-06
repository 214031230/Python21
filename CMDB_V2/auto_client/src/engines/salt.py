#!/usr/bin/env python3
from .base import Base
from src.plugins import get_server_info


class SaltHandle(Base):
    def cmd(self, command, hostname=None):
        """
        使用Salt执行采集器命令
        :param command: 命令
        :param hostname: 需要采集的主机
        :return:
        """
        import salt.client
        local = salt.client.LocalClient()
        result = local.cmd(hostname, 'cmd.run', [command])
        return result[hostname]

    def handler(self):
        """
        执行采集器插件获取采集的数据
        :return: 
        """
        print("salt", get_server_info(self))
