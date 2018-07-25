#!/usr/bin/env python3
import time
count = 0
while 1:
    with open("./log", encoding="utf-8", mode="a") as f:
        f.write("我是%s\r" % count)
    count += 1
    time.sleep(1)

