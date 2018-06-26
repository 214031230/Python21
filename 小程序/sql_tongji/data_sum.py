#!/usr/bin/env python3
import os
import re

lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for name in os.listdir("./tongji"):
    with open("./tongji/%s" % name, encoding="utf-8") as f:
        for i in f:
            if re.match(r"\d",i):
                ret = i.split()
                lst[0] += int(ret[0])
                lst[1] += int(ret[1])
                lst[2] += int(ret[2])
                lst[5] += int(ret[5])
                lst[6] += int(ret[6])
                lst[7] += int(ret[7])
                lst[10] += int(ret[10])
                lst[11] += int(ret[11])
                lst[12] += int(ret[12])
                lst[15] += int(ret[15])
                lst[16] += int(ret[16])
                lst[17] += int(ret[17])
                lst[20] += int(ret[20])
                lst[21] += int(ret[21])
                lst[22] += int(ret[22])
print(*lst)


