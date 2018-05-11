#!/usr/bin/env python3
import os
import time
print(time.strftime("%x"))
os.system("clear")
print("正在处理中，请稍后...")
ret = os.popen("ansible xiaoji -m shell -a'w'|grep UN|awk '{print $1}'").read()
with open("error_list", mode="a") as f:
    f.write(ret)
with open("cy_ip_list") as f1, open("error_list") as f2:
    count = 0
    for i in f2:
        i = i.strip()
        for ip in f1:
            if count == 0:
                print(ip.strip())
            if i in ip:
                print(ip.strip())
                f1.seek(0)
                break
            count += 1
os.remove("error_list")


