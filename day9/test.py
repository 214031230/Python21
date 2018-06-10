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
#
# def search():
#     with open("test_db") as f:
#         time.sleep(random.random())
#         res = json.load(f)
#         print("%s剩余票数：%s" % (os.getpid(), res["count"]))
#
#
# def get():
#     with open("test_db") as f:
#         time.sleep(random.random())
#         res = json.loads(f.read())
#         if res["count"] > 0:
#             res["count"] -= 1
#             time.sleep(random.random())
#             print("%s:购买成功" % os.getpid())
#             with open("test_db", "w") as f:
#                 json.dump(res, f)
#
#
# def run(lock):
#     search()
#     lock.acquire()
#     get()
#     lock.release()
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10):
#         p = Process(target=run, args=(lock,))
#         p.start()




# 开启多进程
# from multiprocessing import Process
import os
import time


# def func():
#     time.sleep(random.randint(1,3))
#     print(os.getpid())
#
#
# if __name__ == '__main__':
#     lst = []
#     for i in range(10):
#         p = Process(target=func)
#         p.start()
#         lst.append(p)
#     for p in lst:p.join()
#     print("主进程end")

# 开启多线程
# from threading import Thread
# import os
# import time
#
#
# def func():
#     time.sleep(random.randint(1,3))
#     print(os.getpid())
#
#
# if __name__ == '__main__':
#     lst = []
#     for i in range(10):
#         t = Thread(target=func)
#         t.start()
#         lst.append(t)
#     for t in lst:t.join()
#     print("主线程end")

# 开启协程
import gevent


def eat():
    print("eat1...")
    gevent.sleep(2)
    print("eat2...")


def play():
    print("plat1...")
    gevent.sleep(1)
    print("plat2...")


if __name__ == '__main__':
    g = gevent.spawn(eat)
    g1 = gevent.spawn(play)
    g.join()
    g1.join()





























