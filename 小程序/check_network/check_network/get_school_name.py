#!/usr/bin/env python
# -*- encode:utf-8 -*-
import time

print("正在处理中，请稍后...")
print(time.strftime("%Y-%m-%d"))
with open("cy_ip_list", encoding="utf-8") as f1, open("error_list", encoding="utf-8") as f2:
    for i in f2:
        i = i.strip()
        # print("准备匹配的IP", i)
        for ip in f1:
            # print("进行%s匹配" % (count, ))
            if i in ip.strip():
                print(ip.strip())
                break
        f1.seek(0)


