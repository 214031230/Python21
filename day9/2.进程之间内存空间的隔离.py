#!/usr/bin/env python3
from multiprocessing import Process
import time
n = 10


def task():
    global n
    n = 0
    print(n)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    print(p.is_alive()) # 查看子进程状态
    p.join()    # 子进程运行完毕才会执行主进程
    print(p.is_alive()) # 查看子进程状态
    print(n)
