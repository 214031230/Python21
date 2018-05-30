#!/usr/bin/env python3
# import mymodules
# mymodules.api.test

with open(r"./test1", "rb") as f, open("./test", "wb") as f2:
    for i in f:
        f2.write(i)
