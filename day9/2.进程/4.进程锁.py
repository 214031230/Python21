#!/usr/bin/env python3
# 示例火车票
# 问题：多个人同时购买火车票，大家都查到了1张票，进行购买的时候都对同一张
# 火车票进行操作，这样就会存在多人购买同一张火车票的问题。需要对购买操作进行加锁

from multiprocessing import Process,Lock
import time
import random
import os
import json
dbfile = "./db"


def search():
    time.sleep(random.random())
    with open(dbfile) as f:
        ret = json.load(f)
        print("%s:查到%s张票" % (os.getpid(), ret["count"]))


def buy():
    time.sleep(random.random())
    with open(dbfile) as f:
        ret = json.load(f)
    if ret["count"] > 0:
        ret["count"] -= 1
        with open(dbfile, "w") as f:
            json.dump(ret, f)
        print("\033[31;0m%s:购买1张票\033[0m" % os.getpid())


def run(lock):
    search()
    with lock:
        buy()


if __name__ == '__main__':
    lock = Lock()
    lst = []
    for i in range(10):
        p = Process(target=run, args=(lock,))
        p.start()
        lst.append(p)
    for p in lst:p.join()
    with open(dbfile, "w") as f:
        dic = {"count": 2}
        json.dump(dic,f)


