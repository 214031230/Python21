#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import os
# import time
# import random
# from multiprocessing import Process,Lock
#
# def work(n,lock):
#     lock.acquire()
#     print('%s: %s is running' %(n,os.getpid()))
#     time.sleep(random.random())
#     print('%s:%s is done' %(n,os.getpid()))
#     lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(3):
#         p=Process(target=work,args=(i,lock))
#         p.start()
        # p.join()

# 牺牲效率但是保证了数据的安全

from multiprocessing import Process,Lock
import time,json,random
def search():
    dic=json.load(open('db.json'))
    print('\033[43m剩余票数%s\033[0m' %dic['count'])

def get(num):
    dic=json.load(open('db.json'))
    time.sleep(random.random()) #模拟读数据的网络延迟
    if dic['count'] >0:
        dic['count']-=1
        time.sleep(random.random()) #模拟写数据的网络延迟
        json.dump(dic,open('db.json','w'))
        print('\033[43m%s购票成功\033[0m'%num)

def task(num,lock):
    search()
    lock.acquire()
    get(num)
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(10): #模拟并发100个客户端抢票
        p=Process(target=task,args = (i,lock))
        p.start()






















