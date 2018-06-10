#!/usr/bin/env python3
from multiprocessing import Process
import time
# 方法1:


# def task(name,name1):
#     print("%s1 is runing" % name)
#     time.sleep(1)
#     print("%s2 is runing" % name1)
#
#
# if __name__ == '__main__':
#     p = Process(target=task, args=("spf", "wxx"))
#     p.start()
#     print("主进程 is runing")


# 方法2


# class MyProcess(Process):
#     def __init__(self,name,name1):
#         super().__init__()
#         self.name = name
#         self.name1 = name1
#
#     def run(self):
#         print("%s1 is runing" % self.name)
#         time.sleep(1)
#         print("%s2 is runing" % self.name1)
#
#
# if __name__ == '__main__':
#     p = MyProcess("spf","wxx")
#     p.start()
#     print("主进程 is runing")
