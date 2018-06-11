#!/usr/bin/env python
# -*- coding:utf-8 -*-
from  multiprocessing import Semaphore
# sem = Semaphore(5)
# sem.acquire()
# print(1)
# sem.acquire()
# print(2)
# sem.acquire()
# print(3)
# sem.acquire()
# print(4)
# sem.acquire()
# print(5)
# sem.acquire()   # 要拿钥匙
# print(6)

from multiprocessing import Process,Semaphore
import time,random

def go_ktv(sem,user):
    sem.acquire()
    print('%s 占到一间ktv小屋' %user)
    time.sleep(random.randint(3,5)) #模拟每个人在ktv中待的时间不同
    sem.release()
    print('%s 走出ktv小屋' % user)

if __name__ == '__main__':
    sem=Semaphore(4)
    p_l=[]
    for i in range(13):
        p=Process(target=go_ktv,args=(sem,'user%s' %i,))
        p.start()
        p_l.append(p)

    for i in p_l:
        i.join()
    print('============》')

# 信号量的本质就是 锁+计数器