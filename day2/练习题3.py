#!/usr/bin/env python3
# # 1，写代码，有如下列表，按照要求实现每一个功能
# li = ['alex','wusir','eric','rain','alex']
# # 1)计算列表的长度并输出
# print(len(li))
# # 2)列表中追加元素’seven’,并输出添加后的列表
# li.append("seven")
# print(li)
# # 3)请在列表的第1个位置插入元素’Tony’,并输出添加后的列表
# li.insert(1, "Tony")
# print(li)
# # 4)请修改列表第2个位置的元素为’Kelly’,并输出修改后的列表
# li[1] = "Kelly"
# print(li)
# # 5)请将列表l2=[1,’a’,3,4,’heart’]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# l2=[1,2,3,4]
# li.extend(l2)
# print(li)
# # 6)请将字符串s = ‘qwert’的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# s = "qwert"
# li.extend(s)
# print(li)
# # 7)请删除列表中的元素’eric’,并输出添加后的列表
# li.remove("eric")
# print(li)
# # 8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# list
# print(li.pop(1))
# print(li)
# # 9)请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:5]
# print(li)
# # 10)请将列表所有得元素反转，并输出反转后的列表
# li.reverse()
# print(li)
# # 11)请计算出‘alex’元素在列表li中出现的次数，并输出该次数。
# print(li.count("alex"))

# 2，写代码，有如下列表，利用切片实现每一个功能
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# # 1)通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# li1 = li[:3]
# print(li1)
# # 2)通过对li列表的切片形成新的列表l2,l2 = [’a’,4,’b’]
# li2 = li[3:6]
# print(li2)
# # 3)通过对li列表的切片形成新的列表l3,l3 = [’1,2,4,5]
# li3 = li[::2]
# print(li3)
# # 4)通过对li列表的切片形成新的列表l4,l4 = [3,’a’,’b’]
# li4 = li[1:6:2]
# print(li4)
# # 5)通过对li列表的切片形成新的列表l5,l5 = [‘c’]
# li5 = li[-1]
# print(li5)
# # 6)通过对li列表的切片形成新的列表l6,l6 = [‘b’,’a’,3]
# li6 = li[-3::-2]
# print(li6)
# 3,写代码，有如下列表，按照要求实现每一个功能。
lis = [2,3,"k",["qwe",20,["k1",["tt",3,"1"]],89],"ab","abv"]
# 1)将列表lis中的’tt’变成大写（用两种方式）。
# lis[3][2][1][0] = "TT"
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis)

# 2)将列表中的数字3变成字符串’100’（用两种方式）。
# lis[3][2][1][1] = lis[3][2][1][1] + 97
# print(lis)
# 3)将列表中的字符串’1’变成数字101（用两种方式）。
# print(lis[3][2][1][2])
# lis[3][2][1][2] = int(lis[3][2][1][2] + "01")
# print(lis)
# 4,请用代码实现：
# li = ["alex", "ecir", "rain"]
# # 利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
# s = "_".join(li)
# print(s)
# 5,查找列表li中的元素，移除每个元素的空格，并找出以’A’或者’a’开头，并以’c’结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
# li = [‘taibai ’,’alexC’,’AbC ’,’egon’,’ Ritian’,’ Wusir’,’  aqc’]

# li = ["taibai "," alexC"," AbC "," egon", " Ritian"," Wusir"," aqc"]
# li1 = []
# for i in li:
#     i = i.strip()
#     if i.startswith("A") or i.startswith("a") and i.endswith("c"):
#         li1.append(i)
# print(li1)

# 6、开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["苍老师","东京热",”武藤兰”,”波多野结衣”]
# li = ["苍老师","东京热","武藤兰","波多野结衣"]
# 则将用户输入的内容中的敏感词汇替换成***，并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
# while True:
#     res = input("请评论：")
#     if res in li:
#         res1 = res.replace("%s" % (res), "***")
#         print(res1)
#     else:
#         li.append(res)
# 7，有如下列表li = [1,3,4’,alex’,[3,7,8,’taibai’],5,’ritian’]
li = [1,3,4,"alex",[3,7,8,'taibai'],5,"ritian"]
# 循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
# 我想要的结果是(用两种方法实现，其中一种用range做)：
# for i in li:
#     if type(i) != list:
#         print(i)
#     else:
#         for j in i:
#             print(j)
# for i in range(len(li)):
#     if type(li[i]) != list:
#         print(li[i])
#     else:
#         for j in li[i]:
#             print(j)
# 1
# 3
# 4
# ‘alex’
# 3
# 7,
# 8
# ‘taibai’
# 5
# ritian
#
# 明日默写内容
# 1，将列表的增删改查不同的方法全部写出来，
# 例如：增：有三种，append：在后面添加。Insert按照索引添加，expend：迭代着添加。
# 2，默写第七题的两个方法实现的代码。
