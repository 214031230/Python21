#!/usr/bin/env python3
# 信号量是控制锁的数量，信号量的本质是锁+计数器
from multiprocessing import Process,Semaphore
import time
import random


def go_ktv(user, s):
    with s:
        print("user%s 进入KTV" % user)
        time.sleep(random.randint(1, 3))
    print("-------->user%s 离开了KTV" % user)


if __name__ == '__main__':
    s = Semaphore(4)
    lst = []
    for i in range(10):
        p = Process(target=go_ktv, args=(i,s))
        p.start()
        lst.append(p)
    for p in lst:p.join()
    print("---打烊了---")