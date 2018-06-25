#!/usr/bin/env python3
import os
for name in os.listdir("./tongji/tongji"):
    with open("./tongji/tongji/%s" % name, encoding="utf-8") as f:
        for i in f:
            if i.startswith("0"):
                print(name)