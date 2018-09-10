#!/usr/bin/env python3
# from threading import Thread
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# import time
# import random
#
#
# def run(n):
#     time.sleep(1)
#     print(n)
#
#
# if __name__ == '__main__':
#     t = ThreadPoolExecutor(5)
#     lst = []
#     for i in range(100):
#         t.submit(run, i)
#     t.shutdown()
#     print("代码执行结束")


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


p = Person("spf")

print(p)


