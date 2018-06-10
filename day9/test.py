#!/usr/bin/env python3
import os
import time
import json
import random
from multiprocessing import Process,Lock


# def fun(num):
#     print(num, os.getpid())
#     time.sleep(num)
#
#
# p = Process(target=fun, args=(10,))
# p.start()
# print(os.getpid())

# 开启多个子进程
# def fun(num):
#     time.sleep(1)
#     print(num, os.getpid())
#
#
# if __name__ == '__main__':
#     lst = []
#     for i in range(10):
#         p = Process(target=fun, args=(i,))
#         p.start()
#         lst.append(p)
#     for p in lst:p.join()
#     print("所有子进程已经执行完毕")

# 抢票

def search():
    with open("test_db") as f:
        time.sleep(random.random())
        res = json.load(f)
        print("%s剩余票数：%s" % (os.getpid(), res["count"]))


def get():
    with open("test_db") as f:
        time.sleep(random.random())
        res = json.loads(f.read())
        if res["count"] > 0:
            res["count"] -= 1
            time.sleep(random.random())
            print("%s:购买成功" % os.getpid())
            with open("test_db", "w") as f:
                json.dump(res, f)


def run(lock):
    search()
    lock.acquire()
    get()
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=run, args=(lock,))
        p.start()
