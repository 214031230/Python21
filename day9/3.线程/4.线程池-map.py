#!/usr/bin/env python3
# map用法

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time


def func(i):
    time.sleep(1)
    print("%s thread is running" % i)


if __name__ == '__main__':
    t = ThreadPoolExecutor(5)
    t.map(func,range(20))   # map取代了for+submit
    t.shutdown()    # 和join用法一样
    print("done")