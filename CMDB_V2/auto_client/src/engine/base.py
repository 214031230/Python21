#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import json
import traceback
from concurrent.futures import ThreadPoolExecutor
from src.plugins import get_server_info
from config import settings


class BaseHandler(object):
    """
    使用基类约束派生类
    """
    def __init__(self):
        """
        初始化属性，派生类都会用到
        """
        self.asset_api = settings.ASSET_API

    def cmd(self, command, hostname=None):
        """
        约束所有的派生类都必须实现cmd方法
        根据不同的引擎执行对应的方法执行对应的命令
        :return:
        """
        raise NotImplementedError('cmd must be implemented')

    def handler(self):
        """
        约束所有的派生类都必须实现handler方法
        :return:
        """
        raise NotImplementedError('handler must be implemented')


class SshAndSalt(BaseHandler):
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
        try:
            info = get_server_info(self, hostname)
            r1 = requests.post(
                url=self.asset_api,
                data=json.dumps(info).encode('utf-8'),
                headers={
                    'Content-Type': 'application/json'
                }
            )
            print(r1)
        except Exception as e:
            msg = traceback.format_exc()
            print(msg)
