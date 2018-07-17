#!/usr/bin/env python3
from multiprocessing import Process, Queue


def producer(name, food, q):
    print("厨师[%s]生产了<food-%s>")


def consumer(name, q):
    print("厨师[%s]生产了<food-%s>")


if __name__ == '__main__':
    q = Queue()
    # 创建生产者们
