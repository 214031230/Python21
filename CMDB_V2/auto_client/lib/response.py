#!/usr/bin/env python3
class BaseResponse:
    def __init__(self):
        """
        定义采集器插件的返回格式，包括状态、错误信息和数据
        """
        self.status = True
        self.error = None
        self.data = None

    @property
    def dict(self):
        """
        :return: {"status": True, "error": None, "data": None}
        """
        return self.__dict__


