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
# def run(e):
#     if e.is_set:
#         time.sleep(random.randint(3,5))
#         print("可以通行了")
#     else:
#         print("请等一等")
#         e.wait()
#
# def stop(e):
#     while 1:
#         if e.is_set:
#             time.sleep(1)
#             print("TRUE")
#             e.clear()
#             time.sleep(1)
#         else:
#             time.sleep(1)
#             print("False")
#             e.set()
#             time.sleep(1)
#
#
# if __name__ == '__main__':
#     e = Event()
#
#     p1 = Process(target=stop, args=(e, ))
#     p1.daemon = True
#     p1.start()
#
#     lst = []
#     for i in range(10):
#         p = Process(target=run, args=(e, ))
#         p.start()
#         lst.append(p)
#     for p in lst:p.join()

# from multiprocessing import Process
# import os
# import time
# import random
#
# def fun():
#     time.sleep(random.randint(0, 3))
#     print(os.getpid())
#
#
# def fun1():
#     while True:
#         time.sleep(1)
#         print("守护进程is running")
#
# if __name__ == '__main__':
#     p1 = Process(target=fun1)
#     p1.daemon = True
#     p1.start()
#     lst = []
#     for i in range(10):
#         p = Process(target=fun)
#         p.start()
#         lst.append(p)
#     for rp in lst:rp.join()

# from threading import Thread
#
# n = 100
# def fun():
#     global n
#     n -= 1
#     print(n)
# if __name__ == '__main__':
#     for i in range(10):
#         p = Thread(target=fun)
#         p.start()

# from multiprocessing import Process,Lock,Semaphore
# import os
# import time
# import random
# import json
# def buy(l):
#     time.sleep(random.random())
#     with open("./info") as f:
#         ret = json.load(f)
#     print("%s查到%s张票" % (os.getpid(), ret["count"]))
#     time.sleep(random.random())
#     with l:
#         with open("./info") as f:
#             ret = json.load(f)
#         if ret["count"] > 0:
#             ret["count"] -= 1
#             with open("./info", "w") as f:
#                 json.dump(ret, f)
#             print("%s够买了一张票" % os.getpid())
#
# if __name__ == '__main__':
#     s = Semaphore(2)
#     for i in range(10):
#         p = Process(target=buy, args=(s,))
#         p.start()

# from multiprocessing import Process,Event,Queue
# import os
# import time
# import random
#
# def eat(q):
#     ret = q.get()
#     print("%s吃了%s" %(os.getpid(), ret))
#
# def make(q, food):
#     while True:
#         q.put("%s" % (food))
#         print("%s制作了1个%s" %(os.getpid(), food))
#         time.sleep(1)
#
# if __name__ == '__main__':
#     q = Queue(1)
#     p1 = Process(target=make, args=(q,"包子"))
#     p1.start()
#     for i in range(10):
#         p = Process(target=eat, args=(q, ))
#         p.start()




# def car_run(e):
#     while True:
#         if not e.is_set():
#             print("%s看见红灯,请停住" %os.getpid())
#             e.wait()
#             print("%s看见绿灯，请通过"% os.getpid())
#             time.sleep(random.randint(3, 6))
#             if not e.is_set():continue
#             print("%s走远了"%os.getpid())
#             break
#
#
# def deng_run(e):
#     while True:
#         time.sleep(3)
#         if e.is_set():
#             e.clear()
#         else:
#             e.set()
#
#
# if __name__ == '__main__':
#     e = Event()
#     deng = Process(target=deng_run, args=(e,))
#     deng.start()
#
#     for i in range(10):
#         car = Process(target=car_run, args=(e, ))
#         car.start()


from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import time
#
#
# def run(i):
#     time.sleep(1)
#     print("线程is running")
#
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(2)
#     pool.map(run, range(10))
# urls = ["www.qq.com", "www.baidu.com", "www.123.com"]
#
# def get(url):
#     time.sleep(random.randint(1, 3))
#     print("获取%s内容" % url)
#     return url
# def info(ret):
#     # return "处理成功%s" % ret.result()
#     time.sleep(random.random())
#     print("处理成功%s" % ret.result())
# if __name__ == '__main__':
#     t = ThreadPoolExecutor(3)
#     for i in urls:
#         t.submit(get, i).add_done_callback(info)

import gevent
from gevent import monkey;monkey.patch_all()

def get():
    print("获取A数据")
    time.sleep(1)
    print("获取B数据")


def put():
    print("处理A数据")
    time.sleep(1)
    print("处理B数据")


if __name__ == '__main__':
    g1 = gevent.spawn(get)
    g2 = gevent.spawn(put)
    # g1.join()
    # g2.join()
    gevent.joinall([g1, g2])

