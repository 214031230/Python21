#!/usr/bin/env python3
"""
类继承方式判断采集器类型
from .base import BasePlugins
class Basic(BasePlugins):
    @classmethod
    def initial(cls):
        return cls()
    
    def process(self):
        self.exec_cmd("命令")
        return "Base process"
"""


class Basic:
    """
    基本监控
    """
    @classmethod
    def initial(cls):
        """
        在执行process之前自定义一些操作
        :return: 
        """
        return cls()
    
    def process(self, exec_cmd, debug):
        """
        使用函数传参方式执行
        :param exec_cmd: 选择采集器模式，执行命令
        :return:
        """
        if debug:
            output = {
                'os_platform': "linux",
                'os_version': "CentOS release 6.6 (Final)\nKernel \r on an \m",
                'hostname': 'c1.com'
            }
        else:
            output = {
                'os_platform': exec_cmd("uname").strip(),
                'os_version': exec_cmd("cat /etc/issue").strip().split('\n')[0],
                'hostname': exec_cmd("hostname").strip(),
            }
        return output
    