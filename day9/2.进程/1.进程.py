#!/usr/bin/env python3
# 什么是进程 ：运行中的程序
# 进程是操作系统中资源分配的最小单位
# 进程与进程之间都是异步的
# 开启一个进程是有时间开销的
# 启动多个进程
# from multiprocessing import Process
# import os
# import time
# import random
#
#
# def func():
#     time.sleep(random.randint(0,3))
#     print("run",os.getpid())
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=func)
#         p.start()



# 程序开始执行就会产生一个主进程
# python中可以主进程中用代码启动一个进程 —— 子进程
# 同时主进程也被称为父进程
# 父子进程之间的代码执行是异步的，各自执行自己的
# 父子进程之间的数据不可以共享
# 主进程会等待子进程结束之后再结束
from multiprocessing import Process
import os
import time
import random


def func():
    time.sleep(random.randint(0,3))
    print("run",os.getpid())


if __name__ == '__main__':
    for i in range(10):
        p = Process(target=func)
        p.start()
    print("主进程ending")    # 开启子进程需要消耗时间，print的时间不固定

