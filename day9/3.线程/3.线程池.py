#!/usr/bin/env python3
# 一般情况下开机多进程的个数和线程的个数
"""
    cpu的个数+1  进程数
    cpu的个数*5  线程数
"""

# 开启进程线程池
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# import time
#
#
# def func(i):
#     time.sleep(1)
#     print("%s thread is running" % i)
#
#
# if __name__ == '__main__':
#     t = ThreadPoolExecutor(5)
#     for i in range(20):
#        t.submit(func, i)
#     t.shutdown()    # 和join用法一样
#     print("done")

