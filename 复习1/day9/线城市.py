#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import random

# def run(i):
#     time.sleep(1)
#     print("%s is running" % i)
#
#
# if __name__ == '__main__':
#     p = ThreadPoolExecutor(5)
#     # for i in range(20):
#     #     p.submit(run, i)
#     p.map(run, range(20))
#     p.shutdown()
#     print("主线程ending")


def get(num):
    time.sleep(random.randint(1,3))
    return num


def handel(data):
    time.sleep(random.randint(1,3))
    print(data.result())


if __name__ == '__main__':
    t = ThreadPoolExecutor(5)
    for i in range(20):
        t.submit(get, i).add_done_callback(handel)
    t.shutdown()
    print("主线程ending")