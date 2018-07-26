#!/usr/bin/env python3
from multiprocessing import Process, Queue
import os
import random
import time


def buy(q):
    try:
        time.sleep(random.randint(1, 3))
        ret = q.get_nowait()
        if ret:
            print("%s抢到了%s" % (os.getpid(), ret))
    except:
        pass


def add(q, user):
    time.sleep(random.randint(1, 3))
    print("增加了1张票")
    q.put("票%s" % user)


if __name__ == '__main__':
    q = Queue()
    for j in range(8):
        p = Process(target=add, args=(q,j))
        p.start()

    lst = []
    for i in range(10):
        p = Process(target=buy, args=(q,))
        p.start()
        lst.append(p)
    for i in lst: i.join()
    print("抢光了")
