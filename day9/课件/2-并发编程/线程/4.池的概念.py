#!/usr/bin/env python
# -*- coding:utf-8 -*-

# cpu的个数+1  进程数
# cpu的个数*5  线程数

# 池的概念

# 20个线程
# 10000
# import time
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def func(num):
#     print(num)
#     time.sleep(1)
#     print(num)
# if __name__ == '__main__':
#     t = ThreadPoolExecutor(20)
#     for i in range(100):
#         t.submit(func,i)
#     t.shutdown()  # join整个池子
#     print('done')

# import os,time,random
# from concurrent.futures import ThreadPoolExecutor
# def task(n):
#     print('%s is runing' %os.getpid(),n)
#     time.sleep(random.randint(1,3))
#     return n**2
# if __name__ == '__main__':
#     executor=ThreadPoolExecutor(max_workers=3)
#     # for i in range(11):
#     #     future=executor.submit(task,i)
#     executor.map(task,range(1,12)) #map取代了for+submit

# callback回调函数
# 我有10个http的网页请求
# 我要把这10个网页的上信息分析了

# import time
# import random
# from concurrent.futures import ThreadPoolExecutor
# from threading import current_thread
# urls=[
#         'https://www.baidu.com',
#         'https://www.python.org',
#         'https://www.openstack.org',
#         'https://help.github.com/',
#         'http://www.sina.com.cn/'
#         'http://www.cnblogs.com/'
#         'http://www.sogou.com/'
#         'http://www.sohu.com/'
#     ]
#
# def analies(content):
#     print('分析网页',current_thread())
#     print(content.result())
#
# def get_url(url):
#     print('爬取网页',current_thread())
#     time.sleep(random.uniform(1,3))
#     # analies(url*10)
#     return url*10
#
# t = ThreadPoolExecutor(3)
# print('主线程',current_thread())
# for url in urls:
#     t.submit(get_url,url).add_done_callback(analies)

# concurrent.futures callback是由子线程做的








