#!/usr/bin/env python3
import time, os, random, json
from multiprocessing import Process, Lock

file = "./db"


def search(f):
    time.sleep(random.randint(0, 3))
    with open(f) as f1:
        ret = json.load(f1)
    print("%s查到%s张票" % (os.getpid(), ret["count"]))


def buy(f):
    time.sleep(random.randint(0, 3))
    with open(f, "r") as f1:
        ret = json.load(f1)
        if ret["count"] > 0:
            time.sleep(random.randint(0, 3))
            with open(f, "w") as f2:
                ret["count"] -= 1
                json.dump(ret, f2)
                print("%s抢到1张票" % os.getpid())
        else:
            print("%s票已经卖完" % os.getpid())


def run(f, l):
    search(f)
    with l:
        buy(f)


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=run, args=(file, lock))
        p.start()
