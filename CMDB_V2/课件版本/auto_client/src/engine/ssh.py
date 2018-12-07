#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json
import paramiko
from config import settings
from .base import BaseHandler
from src.plugins import get_server_info
from .base import SaltAndSSHHandler
from concurrent.futures import ThreadPoolExecutor


class SSHHandler(BaseHandler):

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

    def handler(self):
        """
        处理SSH/SALT模式下的资产采集
        1. 通过api获取需要采集的主机列表
        2. 使用线程池实现并发处理
        3. 把所有的主机交给task方法去采集
        :return:
        """
        r1 = requests.get(url=self.asset_api)
        hostname_list = r1.json()
        print(hostname_list)
        pool = ThreadPoolExecutor(20)
        for hostname in hostname_list:
            pool.submit(self.task, hostname)

    def task(self, hostname):
        """
        执行采集器，拿到采集结果汇报给API
        1. 执行所有的采集器拿到info
        2. 汇报info给api
        :param hostname:
        :return:
        """
        print("11111111111111111111111")
        info = get_server_info(self, hostname)
        r1 = requests.post(
            url=self.asset_api,
            data=json.dumps(info).encode('utf-8'),
            headers={
                'Content-Type': 'application/json'
            }
        )
        print(r1)
