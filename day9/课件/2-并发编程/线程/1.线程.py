#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 什么是进程 ：是计算机资源分配的最小单位
# 什么是线程
# 线程和进程的关系 ：
    # 每一个进程中都至少有一个线程
# python中线程的特点
# 其他语言中线程的特点
# import os
# import time
# from threading import Thread
# n = 100
# def func(i):
#     global n
#     time.sleep(1)
#     n -= 1
#     print(os.getpid(),'thread%s'%i)
# t_l = []
# for i in range(100):
#     t = Thread(target=func,args=(i,))
#     t.start()
#     t_l.append(t)
# for t in t_l:t.join()
# print('main : ',n)

# 每个进程里至少有一个主线程负责执行代码
# 在主线程中可以再开启一个新的线程
# 在同一个进程中就有两个线程同时在工作了
# 线程才是CPU调度的最小单位
# 多个线程之间的数据时共享的

# GIL锁  全局解释器锁
# 解释器的锅 Cpython解释器的问题
# 在同一个进程中 同一个时刻 只能有一个线程被CPU执行
# 导致高计算型 代码 不适合用python的多线程来解决
# 用多进程或者分布式来解决高计算型代码



























