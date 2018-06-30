#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor


def eat(num):
    return num


def play(num):
    print(num.result())


if __name__ == '__main__':
    t = ThreadPoolExecutor(2)
    for i in range(10):
        t.submit(eat, i).add_done_callback(play)
