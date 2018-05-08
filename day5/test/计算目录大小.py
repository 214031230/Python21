#!/usr/bin/env python3
import os
print("*" * 50)
sums = 0
def func(dirs):
    dir_list = os.listdir(dirs)
    global sums
    for i in dir_list:
        if os.path.isdir(os.path.join(dirs, i)):
            func(os.path.join(dirs, i))
        else:
            print("%s:%s" % (i,os.path.getsize(os.path.join(dirs, i))))
            sums += os.path.getsize(os.path.join(dirs, i))
    return sums
print(func("../test"))