#!/usr/bin/env python3
from multiprocessing import Process
import random
import time
import os


def fun(num):
    time.sleep(random.randint(1, 3))
    print("进程%s is running" % num)
    print(os.getpid())


def demo():
    while 1:
        time.sleep(1)
        print("%s守护进程is running" % os.getpid())


if __name__ == '__main__':
    l = []
    p = Process(target=demo)
    p.daemon = True
    p.start()
    for i in range(10):
        p = Process(target=fun, args=(i,))
        p.start()
        l.append(p)
    for i in l: i.join()
    print("主进程is running")


