#!/usr/bin/env python3
# 管道 + 锁  == 队列
# 管道也是一个可以实现进程之间通信的模型
# 但是管道没有锁，数据不安全

# 消息中间件
# memcache
# rabitmq
# kafka —— 大数据相关
# redis

# 队列抢票
from multiprocessing import Process,Queue
import os


def buy():

    try:
        ret = q.get_nowait()
        print("%s：抢到了%s" %(os.getpid(),ret))
    except:pass


if __name__ == '__main__':
    q = Queue()
    q.put("北京-许昌")
    lst = []
    for i in range(10):
        p = Process(target=buy)
        p.start()
        lst.append(p)
    for p in lst:p.join()
    print("shouqin了")
