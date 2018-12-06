#!/usr/bin/env python3


class Base:
    """
    派生类需要实现以下方法，否则会报错
    """

    def cmd(self, command, hostname=None):
        """
        执行采集器命令
        :param command: 命令
        :param hostname: 需要采集的主机
        :return:
        """
        raise NotImplementedError("cmd must be implemented")

    def handler(self):
        """
        执行采集器插件获取采集的数据
        :return: 
        """
        raise NotImplementedError("handler must be implemented")
