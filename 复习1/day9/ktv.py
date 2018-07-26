#!/usr/bin/env python3
from multiprocessing import Process, Semaphore
import random
import time


def go_ktv(user, s):
    with s:
        print("%s进入ktv" % user)
        time.sleep(random.randint(1, 3))
    print("%s离开ktv" % user)


if __name__ == '__main__':
    s = Semaphore(2)
    lst = []
    for i in range(10):
        p = Process(target=go_ktv, args=(i, s))
        p.start()
        lst.append(p)
    for i in lst: i.join()
    print("关门了")

