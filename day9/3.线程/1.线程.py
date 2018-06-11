#!/usr/bin/env python3
# 什么是进程 ：计算机资源分配的最小单位
# 什么是线程 ：CPU调度的最小单位
# 多个线程之间的数据时共享的

# 线程和进程的关系 ：每一个进程中都至少有一个线程
# python中线程的特点
"""
    GIL锁  全局解释器锁
    解释器的锅 Cpython解释器的问题
    在同一个进程中 同一个时刻 只能有一个线程被CPU执行
    导致高计算型 代码 不适合用python的多线程来解决
    用多进程或者分布式来解决高计算型代码

"""

# 启动多个线程
from threading import Thread
import time
import os
import random

n = 100


def func():
    global n
    n -= 1
    print(n)


if __name__ == '__main__':
    lst = []
    for i in range(100):
        t = Thread(target=func)
        t.start()
        lst.append(t)
    for t in lst:t.join()
    print("主进程running")



