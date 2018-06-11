#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 进程
# 什么是进程 ：运行中的程序
# 什么是程序
# 操作系统 只负责管理调度进程
# 进程是操作系统中资源分配的最小单位
# 每一个运行中的程序都需要有自己的内存、资源
# 都分配给进程 记录执行的状态 管理自己的内存资源

# 在Python中，每一个运行中的程序 都是一个进程
# 一个进程 就能做一件事儿
# 如果有多个进程 —— 就可以做多件事儿
# 如何用python来开启一个进程
# import os
# import time
#
# print(os.getpid())
# time.sleep(1000)

# Process 进程
# multi 多元的
import os
import time
from multiprocessing import Process
def func(num):
    print(num,os.getpid())
    time.sleep(0.5)
    print(num, os.getpid())
    time.sleep(0.5)
    print(num, os.getpid())
    time.sleep(0.5)
    print(num,os.getpid())

if __name__ == '__main__':   # windows
    print(os.getpid())
    p = Process(target=func,args=(10,))   # 创造了一个进程
    p.start() # 开启进程
    print(os.getpid())
    time.sleep(1)
    print(os.getpid(),1)
    time.sleep(1)
    print(os.getpid(), 2)
# 同步 ：
# 异步 ：
# 异步可以有效地提高程序的效率

# 几个概念：
# 子进程 :
# 主进程 : 运行的这个程序
# 父进程 ：

# 关于print的顺序

# 进程与进程之间都是异步的
# 开启一个进程是有时间开销的

# if __name__ == '__main__':为什么？