#!/usr/bin/env python3
import os
# 把文件转换成列表，方便处理。返回值为文件第一行（title）和 文件内容
def file_to_list(table):
    with open("./my_db/%s" % table) as f1:
        n = 0
        t_info = []
        for i in f1:
            line = i.strip()
            if n == 0:
                global t_title
                t_title = line.split(",")
            else:
                info = line.split(",")
                t_info.append(info)
            n += 1
    return t_title, t_info

def select(num,table):
    res = file_to_list(table)
    num_list = num.split(",")
    if len(num_list) == 1:
        for i in res[0]:
            if i == "*":
                print("{:<8} {:<8} {:<8} {:<16} {}".format(*res[0]))
                for i in res[1]:
                    print("{:<8} {:<8} {:<8} {:<16} {}".format(*i))
            elif num in res[0]:
                    index = res[0].index(num)
                    print("{:<8}".format(res[0][index]))
                    for i in res[1]:
                        print("{:<8}".format(i[index]))
    elif len(num_list) == 2:
        if num_list[0] in res[0] and num_list[0] in res[0]:
            index0 = res[0].index(num_list[0])
            index1 = res[0].index(num_list[1])
            print("{:<8} {:<8}".format(res[0][index0], res[0][index1]))
            for i in res[1]:
                print("{:<8} {:<8}".format(i[index0], i[index1]))
        else:
            print("列不存在！")
    elif len(num_list) == 3:
        if num_list[0] in res[0] and num_list[1] in res[0] and num_list[2] in res[0]:
            index0 = res[0].index(num_list[0])
            index1 = res[0].index(num_list[1])
            index2 = res[0].index(num_list[2])
            print("{:<8} {:<8} {:<8}".format(res[0][index0], res[0][index1], res[0][index2]))
            for i in res[1]:
                print("{:<8} {:<8} {:<8}".format(i[index0], i[index1], i[index2]))
        else:
            print("列不存在！")
    elif len(num_list) == 4:
        if num_list[0] in res[0] and num_list[1] in res[0] and num_list[2] in res[0] and num_list[3] in res[0]:
            index0 = res[0].index(num_list[0])
            index1 = res[0].index(num_list[1])
            index2 = res[0].index(num_list[2])
            index3 = res[0].index(num_list[3])
            print("{:<8} {:<8} {:<8} {:<8}".format(res[0][index0], res[0][index1], res[0][index2], res[0][index3]))
            for i in res[1]:
                print("{:<8} {:<8} {:<8} {:<8}".format(i[index0], i[index1], i[index2], i[index3]))
        else:
            print("列不存在！")
    elif len(num_list) == 5:
        if num_list[0] in res[0] and num_list[1] in res[0] and num_list[2] in res[0] and num_list[3] in res[0] and num_list[4] in res[0]:
            index0 = res[0].index(num_list[0])
            index1 = res[0].index(num_list[1])
            index2 = res[0].index(num_list[2])
            index3 = res[0].index(num_list[3])
            index4 = res[0].index(num_list[4])
            print("{:<8} {:<8} {:<8} {:<8} {:<8}".format(res[0][index0], res[0][index1], res[0][index2], res[0][index3], res[0][index4]))
            for i in res[1]:
                print("{:<8} {:<8} {:<8} {:<8} {:<8}".format(i[index0], i[index1], i[index2], i[index3], i[index4],))
        else:
            print("列不存在！")
    else:
        print("列不存在！")

def select_where(num,table,where):
    res = file_to_list(table)
    num_list = num.split(",")
    where_list = where.split("=")
    print(where_list)
    input()
    if len(num_list) == 1:
        for i in res[0]:
            if i == "*":
                print("{:<8} {:<8} {:<8} {:<16} {}".format(*res[0]))
                for i in res[1]:
                    print("{:<8} {:<8} {:<8} {:<16} {}".format(*i))
            elif num in res[0]:
                    index = res[0].index(num)
                    print("{:<8}".format(res[0][index]))
                    for i in res[1]:
                        print("{:<8}".format(i[index]))
    elif len(num_list) == 2:
        if num_list[0] in res[0] and num_list[0] in res[0]:
            index0 = res[0].index(num_list[0])
            index1 = res[0].index(num_list[1])
            print("{:<8} {:<8}".format(res[0][index0], res[0][index1]))
            for i in res[1]:
                print("{:<8} {:<8}".format(i[index0], i[index1]))
        else:
            print("列不存在！")
    elif len(num_list) == 3:
        if num_list[0] in res[0] and num_list[1] in res[0] and num_list[2] in res[0]:
            index0 = res[0].index(num_list[0])
            index1 = res[0].index(num_list[1])
            index2 = res[0].index(num_list[2])
            print("{:<8} {:<8} {:<8}".format(res[0][index0], res[0][index1], res[0][index2]))
            for i in res[1]:
                print("{:<8} {:<8} {:<8}".format(i[index0], i[index1], i[index2]))
        else:
            print("列不存在！")
    elif len(num_list) == 4:
        if num_list[0] in res[0] and num_list[1] in res[0] and num_list[2] in res[0] and num_list[3] in res[0]:
            index0 = res[0].index(num_list[0])
            index1 = res[0].index(num_list[1])
            index2 = res[0].index(num_list[2])
            index3 = res[0].index(num_list[3])
            print("{:<8} {:<8} {:<8} {:<8}".format(res[0][index0], res[0][index1], res[0][index2], res[0][index3]))
            for i in res[1]:
                print("{:<8} {:<8} {:<8} {:<8}".format(i[index0], i[index1], i[index2], i[index3]))
        else:
            print("列不存在！")
    elif len(num_list) == 5:
        if num_list[0] in res[0] and num_list[1] in res[0] and num_list[2] in res[0] and num_list[3] in res[0] and num_list[4] in res[0]:
            index0 = res[0].index(num_list[0])
            index1 = res[0].index(num_list[1])
            index2 = res[0].index(num_list[2])
            index3 = res[0].index(num_list[3])
            index4 = res[0].index(num_list[4])
            print("{:<8} {:<8} {:<8} {:<8} {:<8}".format(res[0][index0], res[0][index1], res[0][index2], res[0][index3], res[0][index4]))
            for i in res[1]:
                print("{:<8} {:<8} {:<8} {:<8} {:<8}".format(i[index0], i[index1], i[index2], i[index3], i[index4],))
        else:
            print("列不存在！")
    else:
        print("列不存在！")

def check_sql(cmd):
    action = ["select", "update", "add", "delete", "where"]
    cmd_res = cmd.strip().split()
    if cmd_res[0] in action:
        if cmd_res[2] == "from":
            if os.path.exists("./my_db/%s" % cmd_res[3]) == True:
                if cmd_res[0] == action[0]:select(cmd_res[1], cmd_res[3])
                if cmd_res[0] == action[0] and cmd_res[4] == action[4]: select_where(cmd_res[1], cmd_res[3], cmd_res[5])
                # if cmd_res[1] == action[1]: update()
                # if cmd_res[2] == action[2]: add()
                # if cmd_res[3] == action[3]: delete()
            else:
                print("%s表不存在！" % cmd_res[3])
        else:
            print("语法错误!(form)")
    else:
        print("语法错误！(select/update/add/delete)")
        


# cmd = "select * from user_info"
# cmd = select name, age where age>22
# cmd = select * where job=IT
# cmd = select * where phone like 133
while True:
    cmd = input(">>>")
    check_sql(cmd)




