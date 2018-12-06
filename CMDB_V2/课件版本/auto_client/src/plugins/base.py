#!/usr/bin/python
# -*- coding:utf-8 -*-
from config import settings

class BasePlugin(object):

    def __init__(self):
        self.debug = settings.DEBUG
        self.base_dir = settings.BASEDIR

    def get_os(self,handler,host):
        # return handler.cmd('查看系统的命令',host)
        return 'linux'

    def process(self,hander,hostname):
        os = self.get_os(hander,hostname)
        if os == 'windows':
            return self.win(hander,hostname)
        else:
            return self.linux(hander,hostname)

    def win(self,hander,hostname):
        raise NotImplementedError('win must be implemented ')

    def linux(self, hander, hostname):
        raise NotImplementedError('linux must be implemented ')