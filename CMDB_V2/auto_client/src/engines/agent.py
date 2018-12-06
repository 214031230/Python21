#!/usr/bin/env python3
from .base import Base
from src.plugins import get_server_info


class AgentHandle(Base):
    """
    Agent模式采集器
    """

    def cmd(self, command, hostname=None):
        """
        使用subprocess执行采集器命令
        :param command: 命令
        :param hostname: 需要采集的主机，agent模式不需要hostname
        :return:
        """
        import subprocess
        return subprocess.getoutput(command)

    def handler(self):
        """
        执行采集器插件获取采集的数据
        :return: 
        """
        print("agent", get_server_info(self))
