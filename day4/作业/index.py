#!/usr/bin/env python3

def file_to_list(table, db="my_db"):
    with open("./%s/%s" % (db, table)) as f1:
        n = 0
        t_info = []
        for i in f1:
            if n == 0:
                t_title = i.strip().split(",")
            else:
                info = i.strip().split(",")
                t_info.append(info)
            n += 1
    return t_title, t_info

def select(num, t_title, t_info):
    if num == "*":
        print("{:<8} {:<8} {:<8} {:<16} {}".format(*t_title))
        for i in t_info:
            print("{:<8} {:<8} {:<8} {:<16} {}".format(*i))
    if num == "name":
        print("{:<8}".format(t_title[1]))
        for i in t_info:
            print("{:<8}".format(i[1]))

# cmd = "select * from user_info"
while True:
    cmd = input(">>>")
    cmd_res = cmd.strip().split()
    res = file_to_list(cmd_res[3])
    select(cmd_res[1], res[0], res[1])


# print("{:>8} {:>8} {:>8} {:>8} {:>8} {:>8}".format(*))


