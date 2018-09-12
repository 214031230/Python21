#!/usr/bin/env python3
file = r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\小程序\sql_tongji\name_ip.txt"
with open(file, encoding="utf-8") as f, open("new_school_list", "a", encoding="utf-8") as f1:
    for i in f:
        if i.strip():
            name, ip = i.split()
            name = name.strip('"')
            ip = ip.strip('"').split(":")[1].split("//")[1]
            print(name, ip)
            f1.write("%s  %s\n" % (name, ip))
