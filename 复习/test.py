#!/usr/bin/env python3
count = 1
import time
while True:
    with open("a.txt","a") as f:
        count += 1
        f.write("%saaaaaaaaaaaa\n" % count)
        time.sleep(1)
