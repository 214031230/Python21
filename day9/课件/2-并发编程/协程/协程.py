#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 进程 计算机中资源分配的最小单位   cpu+1
# 线程 CPU 调度最小单位            cpu*5
# 协程 把一个线程拆分成几个         500

# 进程 线程 都是操作系统在调度
# 协程 是程序级别调度

# 减轻了操作系统的负担、增强了用户对程序的可控性
# from gevent import monkey;monkey.patch_all()
# import gevent
# import time
# def eat(name):
#     print('%s eat 1' %name)
#     time.sleep(2)
#     print('%s eat 2' %name)
#
# def play(name):
#     print('%s play 1' %name)
#     time.sleep(1)
#     print('%s play 2' %name)
#
#
# g1=gevent.spawn(eat,'egon')
# g2=gevent.spawn(play,name='egon')
# g1.join()
# g2.join()
# # gevent.joinall([g1,g2])
# print('主')

from gevent import monkey;monkey.patch_all()
import gevent
import requests
import time


def get_page(url):
    print('GET: %s' %url)
    response=requests.get(url)
    if response.status_code == 200:
        print('%d bytes received from %s' %(len(response.text),url))


start_time=time.time()
gevent.joinall([
    gevent.spawn(get_page,'https://www.python.org/'),
    gevent.spawn(get_page,'https://www.yahoo.com/'),
    gevent.spawn(get_page,'https://github.com/'),
])
stop_time=time.time()
print('run time is %s' %(stop_time-start_time))