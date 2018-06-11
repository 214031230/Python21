#!/usr/bin/env python3
# join  阻塞，等待子进程执行结束，在执行主进程后面的代码
from multiprocessing import Process
import os
import time
import random


def func():
    time.sleep(random.randint(0,3))
    print("发送邮件",os.getpid())


if __name__ == '__main__':
    lst = []
    for i in range(10):
        p = Process(target=func)
        p.start()
        lst.append(p)
    for p in lst:p.join()
    print("所有已经已经发送完毕！！！")