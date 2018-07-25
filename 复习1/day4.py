#!/usr/bin/env python3
# print(bin(100))
# print(hex(100))
# min()

# lst = ["spf", "wxx", "zmm"]
# for k, v in enumerate(lst, 1):
#     print(k, v)
# print(all([1, 2, 3, 4, 5]))
# print(all([0, 1, 2, 3, 4, 5]))
# print(all(['a', 1, 2, 3, 4, 5]))
# print(all(['', 1, 2, 3, 4, 5]))
# print(any([0, None, False,True]))

# ret = zip((1,2,3),("spf","wxx"),"ABC")
# print(list(ret))

# ret = filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5])
# print(list(ret))
# ret = map(lambda x: x * x, [1, 2, 3, 4, 5])
# print(list(ret))
# l = ['test', None, '', 'str', '  ', 'END']
# print(list(filter(lambda x: x if x and x.strip() else False, l)))
# print(list(map(lambda x: x if x and x.strip() else False, l)))

# l = [1, -4, -2, 3, -5, 6, 5]
# l.sort()
# print(l)
# new_l = sorted(l, key=abs, reverse=True)
# print(new_l)

# eval()
# eval('print(123)')
# exec('print(123)')
# print(eval('1+2-3*20/(2+3)'))
# print(exec('1+2-3*20/(2+3)'))

# import time
# for i in range(1,101):
#     print("\r%s %%%s" % (i, "#"*i), end="")
#     time.sleep(0.3)

# print(hash("12313123"))
# print(hash("12313123"))
# print(id("45"))
# print(id("45"))
# print(dir("s"))
# 现有两元组(('a'), ('b')), (('c'), ('d')), 请使用python中匿名函数生成列表[{'a': 'c'}, {'b': 'd'}]
#
# print(list(map(lambda x:{x[0]:x[1]},zip((('a'), ('b')), (('c'), ('d'))))))

# def multipliers():
#     return [lambda x:i*x for i in range(4)] #
#
# print([m(2) for m in multipliers()])
# for m in multipliers()
# lambda x:i*x for i in range(4)
# [lambda x:0*x,lambda x:1*x,lambda x:2*x,lambda x:3*x]
# for m in multipliers()
# m(2) lambda x:0*2  2
# m(2) lambda x:1*2  3
# m(2) lambda x:2*2  4
# m(2) lambda x:3*2  6
# print(6*5*4*3*2*1)
# def fun(num):
#     if num == 1: return 1
#     return fun(num-1)*num
"""
def fun(6): 720
    if 6 == 1:return 1
    return fun(6-1)*6
def fun(5): 120
    if 5 == 1:return 1
    return fun(5-1)*5
def fun(4): 24
    if 4 == 1:return 1
    return fun(4-1)*4
def fun(3): 6 
    if 3 == 1:return 1
    return fun(3-1)*3
def fun(2):  2 
    if 2 == 1:return 1
    return fun(2-1)*2
def fun(1): 1 
    if 1 == 1:return 1
"""
# print(fun(6))
# li = [1, [2, [3, [4, [5]]]]]
#
# def foo(lst):
#     for i in lst:
#         if type(i) == list:
#             foo(i)
#         else:
#             print(i)
# foo(li)

lst = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]


# def func(lst, num, start=0, end=None):
#     end = len(lst) - 1 if end is None else end
#     if start > end: return None
#     mid = (end - start) // 2 + start
#     if lst[mid] > num:
#         return func(lst, num, start, mid - 1)
#     elif lst[mid] < num:
#         return func(lst, num, mid + 1, end)
#     else:
#         return mid
#
#
# print(func(lst, 48))


# def func(lst, num, start=0, end=None):  # 开始的时候，从索引为0开始查找
#     end = len(lst) - 1 if end is None else end  # 获取到列表的最大索引
#     if start > end: return None  # 如果起始索引大于最大索引，说明没有找到
#     mid = (end - start) // 2 + start # 获取列表的中间索引
#     if lst[mid] > num: # 判断中间元素和要找元素的大小
#         return func(lst, num, start, end - 1)
#     elif lst[mid] < num:
#         return func(lst, num, start + 1, end)
#     else:
#         return mid
#
#
# print(func(lst, 28))
#
#
# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车战': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }
# # last = []
# # current = menu
# # while 1:
# #     for i in current:
# #         print(i)
# #     choice = input(">>>:").strip()
# #     if not choice:continue
# #     if choice in current:
# #         last.append(current)
# #         current = current[choice]
# #     elif choice.lower() == "b":
# #         if last:
# #             current = last.pop()
# #         else:
# #             print("已经到最顶层")
# #     elif choice == "q":
# #         exit()
# #     else:
# #         print("节点不存在！")
#
#
# def fun(menu):
#     while 1:
#         for i in menu:
#             print(i)
#         choice = input(">>>:").strip()
#         if not choice:continue
#         if choice.lower() == "b": return
#         if choice.lower() == "q": return "q"
#         if choice in menu:
#             ret = fun(menu[choice])
#             if ret == "q":
#                 return "q"
#         else:
#             print("key不存在！")
#
#
# fun(menu)
# import collections
#
# c = collections.Counter("abcdeabcdabcaba")
# print(c)
# # lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 元素大于5的添加到字典k1的列表中，元素小于5的添加字典k2的列表中
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# dic = collections.defaultdict(list)
# for i in lst1:
#     if i > 5:dic["k1"].append(i)
#     else:dic["k2"].append(i)
# print(dic)


# import time
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# import random
# print(random.random())
# print(random.uniform(0, 2))
# print(random.randint(1, 4))
# print(random.randrange(1,10,2))
# print(random.choice([1,2,3,4,5]))
# print(random.sample([1, 2, 3, 4, 5], 2))
# lst2 = [1,2,3,4]
# print(random.shuffle(lst2))
# print(lst2)
# import random
#
#
# def code(num):
#     """
#     随机验证码
#     :param num: 验证码位数
#     :return:
#     """
#     code = ""
#     for i in range(num):
#         digit = random.randint(0, 9)
#         u_isalpha = chr(random.randint(65, 90))
#         l_isalpha = chr(random.randint(97, 122))
#         code += random.choice([str(digit), u_isalpha, l_isalpha])
#     return code
#
#
# print(code(6))
# import sys
# print(sys.version)
# print(sys.path)
# print(sys.platform)
# print(sys.modules)

import os

# print(os.getcwd())
# print(os.listdir("."))
# print(os.stat("./day1.py"))
#
# print(os.name)




# print(os.system("dir ."))
# print(os.popen("dir .").read())
# print(os.environ)

# print(os.path.abspath("."))
# print(os.path.split(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\复习1"))

# print(os.path.exists("./day1.p"))
# import time
# print(os.path.getatime("./day1.py"))
# print(time.strftime("%x %X", time.gmtime(os.path.getatime("./day1.py"))))
import os

#
# import os
# print("*" * 50)
# sums = 0
#
#
# def func(dirs):
#     if not os.path.exists(dirs):return
#     global sums
#     for i in os.listdir(dirs):
#         if os.path.isdir(os.path.join(dirs, i)):
#             func(os.path.join(dirs, i))
#         else:
#             sums += os.path.getsize(os.path.join(dirs, i))
#     return sums
#
# print(func("../复习"))


import re

# ret = re.findall('a', 'eva egon yuan')  # 返回所有满足匹配条件的结果,放在列表里
# print(ret) #结果 : ['a', 'a']


s = "abddd234alfbalf"

print(re.findall("\d", s))
print(re.search("\d", s).group())
print(re.match("[a-z]", s).group())

print(re.sub("\d", "A", s))
print(re.subn("\d", "A", s))

obj = re.compile("\d{1,3}")
print(obj.findall(s))
















