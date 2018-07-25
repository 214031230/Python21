#!/usr/bin/env python3
import time


def listen():
    with open("./log", encoding="utf-8", mode="r") as f:
        while 1:
            # f.seek(0, 2)
            ret = f.readline()
            if ret.strip():
                f.seek(0, 2)
                yield ret.strip()
            time.sleep(0.5)


g = listen()
while 1:
    try:
        print(g.__next__())
    except Exception as e:
        print(e)
