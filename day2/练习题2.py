#!/usr/bin/env python3

# 1，有变量name = "aleX leNb" 完成如下操作：
# 1)移除 name 变量对应的值两边的空格,并输出处理结果
# name = "aleX leNb"
# name1 = name.strip()
# print(name1)
# # 2)移除name变量左边的’al’并输出处理结果
# name2 = name.strip("al")
# print(name2)
# # 3)移除name变量右面的’Nb’,并输出处理结果
# name3 = name.rstrip("Nb")
# print(name3)
# # 4)移除name变量开头的a’与最后的’b’,并输出处理结果
# name4 = name.strip("ab")
# print(name4)
# # 5)判断 name 变量是否以 "al" 开头,并输出结果
# print(name.startswith("al"))
# # 6)判断name变量是否以”Nb”结尾,并输出结果
# print(name.endswith("Nb"))
# # 7)将 name 变量对应的值中的 所有的“l” 替换为 “p”,并输出结果
# name5 = name.replace("l", "p")
# print(name5)
# # 8)将name变量对应的值中的第一个’l’替换成’p’,并输出结果
# name6 = name.replace("l", "p", 1)
# print(name6)
# # 9)将 name 变量对应的值根据 所有的“l” 分割,并输出结果。
# print(name.split("l"))
# # 10)将name变量对应的值根据第一个’l’分割,并输出结果。
# print(name.split("l", 1))
# # 11)将 name 变量对应的值变大写,并输出结果
# name6 = name.upper()
# print(name6)
# # 12)将 name 变量对应的值变小写,并输出结果
# name7 = name.lower()
# print(name7)
# # 13)将name变量对应的值首字母’a’大写,并输出结果
# name8 = name.capitalize()
# print(name8)
# # 14)判断name变量对应的值字母’l’出现几次，并输出结果
# print(name.count("l"))
# # 15)如果判断name变量对应的值前四位’l’出现几次,并输出结果
# print(name.count("l", 0, 4))
# str
# # 16)从name变量对应的值中找到’N’对应的索引(如果找不到则报错)，并输出结果
# print(name.index("N"))
# # 17)从name变量对应的值中找到’N’对应的索引(如果找不到则返回-1)输出结果
# print(name.find("N"))
# 18)从name变量对应的值中找到’X le’对应的索引,并输出结果
# name = "aleX leNb"
# for i in 'X le':
#     print(name.find(i, 3))
# # 19)请输出 name 变量对应的值的第 2 个字符?
# print(name[1])
# # 20)请输出 name 变量对应的值的前 3 个字符?
# print(name[0:3])
# # 21)请输出 name 变量对应的值的后 2 个字符?
# print(name[-1:-3:-1])
# # 22)请输出 name 变量对应的值中 “e” 所在索引位置?
# name = "aleX leNb"
# # print(name.find("e"))
# print(name.find("e"))
# print(name.find("e", name.find("e")+1))
# 获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
# a = 'oldboy'
# print(a.rstrip("y"))
# # 2，有字符串s = ‘123a4b5c’
# s = "123a4b5c"
# # 1)通过对li列表的切片形成新的字符串s1,s1 = ‘123’
# s1 = s.split("a")[0]
# print(s1)
# # 2)通过对li列表的切片形成新的字符串s2,s2 = ‘a4b’
# s2 = s.split("3")[1].split("5")[0]
# print(s2)
# 3)通过对li列表的切片形成新的字符串s3,s3 = ‘1345’
# s = "123a4b5c"
# s2 = []
# s3 = s2.append(s.split("2")[0])
# s4 = s2.append(s.split("2")[1].split("a")[0])
# s5 = s2.append(s.split("2")[1].split("a")[1].split("b")[0])
# s6 = s2.append(s.split("2")[1].split("a")[1].split("b")[1].split("c")[0])
# s7 = "".join(s2)
# print(s7)
# s3 = s[::2]
# print(s3)
# # 4)通过对li列表的切片形成字符串s4,s4 = ‘2ab’
# s4 = s[1:6:2]
# print(s4)
# # 5)通过对li列表的切片形成字符串s5,s5 = ‘c’
# s5 = s[-1]
# print(s5)
# 6)通过对li列表的切片形成字符串s6,s6 = ‘ba2’
# s = "123a4b5c"
# s6 = s[-3::-2]
# print(s6)
# 3，使用while和for循环分别打印字符串s=’asdfer’中每个元素。
# s = "asdfer"
# for i in s:
#     print(i)
# print(len(s))
# count = 0
# while count < len(s):
#     print(s[count])
#     count += 1
# 4，实现一个整数加法计算器(两个数相加)：
# while True:
#     num1 = int(input(">>>:").strip())
#     num2 = int(input(">>>:").strip())
#     print(num1 + num2)
# 如：content = input(‘请输入内容:’)  # 如用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。
# while True:
#     res = input(">>>:").strip()
#     n1,n2 = res.split("+")
#     print(int(n1) + int(n2))

# 5，计算用户输入的内容中有几个整数（以个位数为单位）。
# 如：content = input(‘请输入内容：’)   # 如fhdal234slfh98769fjdla
# s = input(">>>:")
# temp = []
# for i in s:
#     if i.isdigit():
#         temp.append(i)
# print(len(temp))
# 明日默写内容：
# 分别用while，for循环输出字符串s = input（‘你想输入的内容’）的每一个字符。

# s = input(">>>:")
# for i in s:
#     print(i)

# s = input(">>>:")
# count = 0
# while count < len(s):
#     print(s[count])
#     count += 1