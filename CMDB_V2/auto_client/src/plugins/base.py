#!/usr/bin/env python3
class Base:
    def get_os(self, handler, hostname=None):
        """
        获取系统版本
        :return:
        """
        return handler.cmd("xxx", hostname)

    def process(self, handler, hostname=None):
        os_info = self.get_os(handler, hostname)
        if os_info == "windows":
            return self.win(handler, hostname)
        else:
            return self.linux(handler, hostname)

    def win(self, handler, hostname=None):
        raise NotImplementedError("win must be Implemented")

    def linux(self, handler, hostname=None):
        raise NotImplementedError("linux must be Implemented")
