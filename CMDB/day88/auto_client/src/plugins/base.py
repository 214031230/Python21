#!/usr/bin/env python3
from lib.config import settings
import paramiko
import subprocess


class BasePlugins:
    """
    插件使用类继承的方式
    根据采集器模式来执行不同的命令
    """
    def __init__(self):
        pass

    def exec_cmd(self, cmd):
        """
        插件使用类继承的方式
        根据采集器模式来执行不同的命令
        :param cmd:
        :return:
        """
        if settings.MODE == "AGENT":
            result = subprocess.getoutput(cmd)
        elif settings.MODE == "SSH":
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname='192.168.16.72', port=22, username='root', password='redhat')
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = stdout.read()
            ssh.close()

        elif settings.MODE == "SALT":
            result = subprocess.getoutput('salt "c1.com" cmd.run "%s"' %cmd)
        else:
            raise Exception("模式选择错误：AGENT,SSH,SALT")

        return result