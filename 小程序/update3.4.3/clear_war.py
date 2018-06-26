#!/usr/bin/env python3
import os
from concurrent.futures import ThreadPoolExecutor

path_list = "./path_list"
group = "58.116.52.250"

def clear(file_path):
    os.system("ansible %s -m shell -a\"rm -rf %s/*;ls %s\"" % (group,file_path,file_path))

if __name__ == '__main__':
    t = ThreadPoolExecutor(50)
    with open(path_list) as f:
        for i in f:
            i = i.strip()
            t.submit(clear,i)