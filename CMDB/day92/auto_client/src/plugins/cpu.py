#!/usr/bin/env python3
class Cpu:
    """
    CPU监控
    """
    @classmethod
    def initial(cls):
        """
        在执行process之前自定义一些操作
        :return: 
        """
        return cls()
    
    def process(self, exec_cmd, debug):
        if debug:
            pass
        else:
            exec_cmd("命令")
            return "CPU process"