#!/usr/bin/env python3
from threading import Thread
import os

# def run():
#     print("%s in running" % os.getpid())
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = Thread(target=run)
#         t.start()
from multiprocessing import Process
import random
import time
n = 100


def run():
    time.sleep(random.randint(1, 3))
    global n
    n -= 1
    print(n)


def demo():
    while 1:
        time.sleep(1)
        print("守护线程is running")


if __name__ == '__main__':
    t1 = Thread(target=demo)
    t1.daemon = True
    t1.start()

    for i in range(100):
        t = Thread(target=run)
        t.start()

    print("主线程 is runinng")


