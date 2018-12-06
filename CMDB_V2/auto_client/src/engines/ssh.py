#!/usr/bin/env python3
from .base import Base
from src.plugins import get_server_info
from config import settings


class SSHHandle(Base):
    def cmd(self, command, hostname=None):
        """
        使用paramiko模块执行采集器命令
        :param command: 命令
        :param hostname: 需要采集的主机
        :return:
        """
        import paramiko

        private_key = paramiko.RSAKey.from_private_key_file(settings.SSH_PRIVATE_KEY)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, pkey=private_key)
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read()
        ssh.close()
        return result

    def handler(self):
        """
        执行采集器插件获取采集的数据
        :return: 
        """
        print("ssh", get_server_info(self))
