#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Manager,Process,Lock
def work(d,lock):
    with lock: #不加锁而操作共享的数据,肯定会出现数据错乱
        d['count']-=1

if __name__ == '__main__':
    lock=Lock()
    m = Manager()
    dic = m.dict({'count':100})
    #dic = {'count':100}
    p_l=[]
    for i in range(50):
        p=Process(target=work,args=(dic,lock))
        p_l.append(p)
        p.start()
    for p in p_l:
        p.join()
    print(dic)