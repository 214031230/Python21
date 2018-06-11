#!/usr/bin/env python3
# 主线程结束了之后守护线程也同时结束
# 守护线程会等待主线程完全结束之后才结束
from threading import Thread
import time
import os
import random

def run():
    while 1:
        print("守护进程is running")

def func():
    time.sleep(random.randint(1,3))
    print("子线程is running")


if __name__ == '__main__':
    ts = Thread(target=run)
    ts.daemon = True
    ts.start()

    for i in range(10):
        t = Thread(target=func)
        t.start()
    print("主进程running")