#!/usr/bin/env python3
import time
count = 1
while True:
    with open("tmp", mode="a") as f1:
        f1.write("我是第%s行\n" % (count,))
    count += 1
    time.sleep(1)