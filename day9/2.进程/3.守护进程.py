#!/usr/bin/env python3
# 守护进程
# 守护进程也是一个子进程
# 当主进程的“代码”执行完毕之后自动结束的子进程叫做守护进程
from multiprocessing import Process
import time
import random
import os


def func():
    while 1:
        time.sleep(0.3)
        print("守护进程running",os.getpid())


def play():
    time.sleep(random.randint(0,3))
    print("子进程running",os.getpid())


if __name__ == '__main__':
    p = Process(target=func)
    p.daemon = True  # 把子进程设置成守护进程
    p.start()
    lst = []    # 如果有多个子进程 不能在start一个进程之后就立刻join，把所有的进程放到列表中，等待所有进程都start之后再逐一join
    for i in range(10):
        p1 = Process(target=play)
        p1.start()
        lst.append(p1)
    for p in lst:p.join()

    print("主进程ending")
