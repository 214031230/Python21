#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import requests
from .base import BaseHandler
from ..plugins import get_server_info


class AgentHandler(BaseHandler):

    def cmd(self,command,hostname=None):
        import subprocess
        return subprocess.getoutput(command)

    def handler(self):
        """
        处理Agent模式下的资产采集：网卡、内存、硬盘
        :return:
        """
        # 1. 通过调用get_server_info获取所有的资产信息：网卡、内存、硬盘
        info = get_server_info(self)
        # 2. 发送到api
        r1 = requests.post(
            url=self.asset_api,
            data=json.dumps(info).encode('utf-8'),
            headers={
                'Content-Type':'application/json'
            }
        )
        print(r1)



