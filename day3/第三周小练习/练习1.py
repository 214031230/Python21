#!/usr/bin/env python3
# 1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
# apple 10 3
# tesla 100000 1
# mac 3000 2
# lenovo 30000 3
# chicken 10 3
# 通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
# li = []
# with open("./file/a.txt", encoding="utf-8", mode="r") as f1:
#     for i in f1:
#         name, price, amount = i.split()
#         li.append({"name": name, "price": price, "amuont": amount})
# print(li)
#
# sums = 0
# for i in li:
#     sums = sums + int(i["price"])
# print(sums)

# 2.有如下文件：
# -------
# alex是老男孩python发起人，创建人。
# alex其实是人妖。
# 谁说alex是sb？
# 你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
# ----------
# 将文件中所有的alex都替换成大写的SB。

# import os
# with open("./file/1.txt") as f1, open("./file/1.txt.bak","a") as f2:
#     for i in f1:
#         f2.write(i.replace("alex", "SB"))
#
# os.remove("./file/1.txt")
# os.rename("./file/1.txt.bak", "./file/1.txt")


# 3.文件2.txt内容：每一行内容分别为商品名字，价钱，个数。 文件内容：
# name:apple price:10 amount:3 year:2012 
# name:tesla price:100000 amount:1 year:2013
#  通过代码，将其构建成这种数据类型： [{'name':'apple','price':10,'amount':3}, {'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。

# li1 = []
# with open("./file/2.txt", encoding="utf-8", mode="r") as f2:
#     for i in f2:
#         x, y, z, h = i.split()
#         x1, x2 = x.split(":")
#         y1, y2 = y.split(":")
#         z1, z2 = z.split(":")
#         li1.append({x1: x2, y1: y2, z1: z2})
#         # for n in "xyz":
#         #     count = 0
#         #     while count < 2:
#         #         n1, n2 = n.split(":")
#         #         li1[count][n1] = n2
#         #         count += 1
#             # li1.append({n1:n2,y1:y2,z1:z2})
# print(li1)
# sums = 0
# for i in li1:
#     sums = sums + int(i["price"])
# print

# 4,文件3.txt内容：每一行内容分别为商品名字，价钱，个数。
# 文件内容： 
# 序号     部门      人数      平均年龄      备注 1
# 1       python    30         26         单身狗 2
# 2       Linux     26         30         没对象 3
# 3       运营部     20         24         女生多 通
# 过代码将其构建成这种数据类型： [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'}

# li1 = []
# with open("./file/3.txt", encoding="utf-8", mode="r") as f2:
#     for i in f2:
#         if "序号" in i:
#             continue
#         res = i.split()
#         li1.append({"序号":res[0], "部门": res[1], "人数": res[2], "平均年龄": res[3], "备注": res[4]})
# print(li1)



