#!/usr/bin/python
# -*- coding:utf-8 -*-
import paramiko
from .base import SshAndSalt


class SSHHandler(SshAndSalt):

    def cmd(self, command, hostname=None):
        """
        调用paramiko远程连接主机并执行命令，依赖rsa
        :param hostname:主机名
        :param command: 要执行的命令
        :return:
        """
        # private_key = paramiko.RSAKey.from_private_key_file(settings.SSH_PRIVATE_KEY)
        # ssh = paramiko.SSHClient()
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, pkey=private_key)
        # stdin, stdout, stderr = ssh.exec_command(command)
        # result = stdout.read()
        # ssh.close()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, port=8997, username="root", password="@@lanpa2017")
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read()
        return result
