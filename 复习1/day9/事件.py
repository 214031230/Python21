#!/usr/bin/env python3
from multiprocessing import Process, Event
import time
import random


def car(num, evn):
    while 1:
        if not evn.is_set():
            print("红灯亮了，%s请等待" % num)
            evn.wait()
            print("绿灯亮了，%s请通过" % num)
            time.sleep(random.randint(1, 3))
            if not evn.is_set():
                continue
            print("%s走远了" % num)
            break


def deng(evn, num):
    while 1:
        time.sleep(num)
        if evn.is_set():
            evn.clear()
        else:
            evn.set()


if __name__ == '__main__':
    e = Event()
    p1 = Process(target=deng, args=(e, 3))
    for i in range(10):
        p = Process(target=car, args=(i, e))
        p.start()
    p1.start()
    print("==========")