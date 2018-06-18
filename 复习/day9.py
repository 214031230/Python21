#!/usr/bin/env python3
# # 开启进程
#
# from multiprocessing import Process
# import time
# import os
# import random
#
#
# def run(n):
#     time.sleep(random.random())
#     print("%s:%s" % (n, os.getpid()))
#
#
# start = time.time()
#
#
# if __name__ == '__main__':
#     lst = []
#     for i in range(10):
#         p = Process(target=run, args=(i, ))
#         p.start()
#         lst.append(p)
#     for p in lst:p.join()
#     print("main is running")
# print(time.time()-start)

# 开启线程
# from threading import Thread
# import time
# import os
# import random
#
#
# def run(n):
#     time.sleep(random.random())
#     print("%s:%s" % (n, os.getpid()))
#
#
# start = time.time()
#
#
# if __name__ == '__main__':
#     lst = []
#     for i in range(10):
#         t = Thread(target=run, args=(i, ))
#         t.start()
#         lst.append(t)
#     for t in lst:t.join()
#     print("main is running")
# print(time.time()-start)


# from concurrent.futures import ThreadPoolExecutor
#
#
# def run(n):
#     print("*"*n)
#
#
# if __name__ == '__main__':
#     s = ThreadPoolExecutor(20)
#     for i in range(100):
#         s.submit(run, i)
#     s.shutdown()
#     print("main is running")
# from multiprocessing import JoinableQueue,Process
# from time import sleep
# from random import randint
#
#
# def eat(name, q):
#     while 1:
#         ret = q.get()
#         if not ret:break
#         print("游客%s吃了1个%s" % (name, ret))
#
#
# def make(name, food, q):
#     for i in range(5):
#         sleep(randint(1,3))
#         print("%s做了1个%s" % (name, food))
#         q.put(food)
#
#
# if __name__ == '__main__':
#     q = JoinableQueue()
#     p1 = Process(target=make, args=("包师傅", "包子", q))
#     p2 = Process(target=make, args=("汤师傅", "粥", q))
#     p1.start()
#     p2.start()
#     for i in range(10):
#         pp = Process(target=eat, args=(i, q))
#         pp.start()
#     p1.join()
#     p2.join()


# import socketserver
#
#
# class MyServer(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         addr = self.client_address
#         while 1:
#             msg = conn.recv(1024).decode("utf-8")
#             if msg.lower() == "q":break
#             print("%s %s" % (addr, msg))
#         conn.close()
#
#
# server = socketserver.ThreadingTCPServer(("127.0.0.1",9001), MyServer)
# server.serve_forever()
# import os
# from multiprocessing import Process,Lock,Semaphore
# import time
# import json
# import random
#
#
# def func():
#     while 1:
#         time.sleep(random.random())
#         print("抢票中")
#
#
# def run(lock):
#     time.sleep(random.randint(1, 3))
#     with lock:
#         f = open("./info", mode="r")
#         ret = json.load(f)
#         f.close()
#         if ret["count"] > 0:
#             print("%s抢到了一张票" % os.getpid())
#             ret["count"] -= 1
#             f = open("./info", mode="w")
#             json.dump(ret, f)
#             f.close()
#         else:
#             print("票已经被强光了")
#
#
# if __name__ == '__main__':
#     p1 = Process(target=func)
#     p1.daemon = True
#     p1.start()
#     # l = Lock()
#     l = Semaphore(2)
#     lst = []
#     for i in range(10):
#         p = Process(target=run, args=(l, ))
#         p.start()
#         lst.append(p)
#     for p in lst:p.join()
from multiprocessing import Process,Event
import time
import random
def run(e):
    if e.is_set:
        time.sleep(random.randint(3,5))
        print("可以通行了")
    else:
        print("请等一等")
        e.wait()

def stop(e):
    while 1:
        if e.is_set:
            time.sleep(1)
            print("TRUE")
            e.clear()
            time.sleep(1)
        else:
            time.sleep(1)
            print("False")
            e.set()
            time.sleep(1)


if __name__ == '__main__':
    e = Event()

    p1 = Process(target=stop, args=(e, ))
    p1.daemon = True
    p1.start()

    lst = []
    for i in range(10):
        p = Process(target=run, args=(e, ))
        p.start()
        lst.append(p)
    for p in lst:p.join()




