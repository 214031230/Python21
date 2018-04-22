#!/usr/bin/env python3
# f1 = open("log1", "r", encoding="UTF-8")
# res = f1.read()
# print(res)
# f1.close()

# 推荐方法，只占用一行内存
# f4 = open("log1", "r", encoding="UTF-8")
# for i in f4:
#     print(i)
# f4.close()

# f2 = open("/Users/xuxu/Desktop/python自动化21期/Python21/day3/log1", "r", encoding="UTF-8")
# res = f2.read()
# print(res)
# f2.close()

# f3 = open("log1", "r", encoding="UTF-8")
# res = f3.readlines()
# for i in res:
#     print(i)
# f3.close()
#
# f5 = open("log1", "rb")
# print(f5.read())
# f5.close()

# s1 = "123131312312312313"
# l1 = [1, 2, 3, 4, 5, 6, 6, 4, 3, 2, 2, 1]
#
#
# def my_len(s):
#     count = 0
#     for i in s:
#         count += 1
#     return count
#
#
# print(my_len(s1))
# print(my_len(l1))


# def fun1(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# print(fun1(1, 3))

# 打开旧文件，产生句柄
# 打开新文件，产生句柄
# 读取旧文件，写入到新文件
# 删除旧文件，把新文件重命名为旧文件
# import os
#
# with open("log1", "r") as f1, open("log2", "w") as f2:
#     for i in f1:
#         f2.write(i.replace("1", "a"))
# os.remove("log1")
# os.rename("log2", "log1")


# def fun1(user, sex="男"):
#     with open("user_info", "a", encoding="utf-8") as f1:
#         f1.write("{}{}\n".format(user, sex))
#
#
# while True:
#     user = input("姓名：")
#     sex = input("性别：")
#     if not sex:
#         fun1(user)
#     else:
#         fun1(user, sex)
# print(globals())
# print(locals())

# def func():
#     print('in func')
#
# f = func
# f()
# def f1():
#     print('f1')
#
# def func1(argv):
#     argv()
#     return argv
#
# f = func1(f1)
# f()

# 可以当做函数的参数和返回值
#
# def wrapper():
#     def inner():
#         name1 = 'alex'
#         print(name1)
# wrapper()
#
#
# def wrapper():
#     def inner():
#         name1 = 'alex'
#         print(name1)
#
# res = wrapper()

# s = "中国"
# s1 = s.encode("gbk")
# print(s1)
# s1 = b'\xd6\xd0\xb9\xfa' # gbk 的二进制 bytes
# s2 = s1.decode("gbk")  # uncode
# print(s2)
# s3 = s2.encode("utf-8")
# print(s3)

# count = 1
# def fun1():
#     global count
#     count += 1
# fun1()
# print(count)

# def func2(argv):
#     print(777)
#     return argv
# print(func2(3))

# import time
#
# # 不带参数的装饰器，函数性能测试
# # def timer(argv):
# #     def inner():
# #         start_time = time.time()
# #         argv()
# #         end_time = time.time()
# #         res = end_time - start_time
# #         return res
# #     return inner
# #
# # @timer # fun1 = timer(fun1)
# # def fun1():
# #     print("Hello Word!")
# #     time.sleep(1)
# #
# #
# # print(fun1())
#
# # 带参数的装饰器，函数性能测试
# def timer(argv):
#     def inner():
#         start_time = time.time()
#         argv()
#         end_time = time.time()
#         res = end_time - start_time
#         return res
#     return inner
#
# @timer # fun1 = timer(fun1)
# def fun1(argv):
#     print(argv)
#     time.sleep(1)
#
#
# print(fun1())

# for n in "xyz":
#     print(n)
# s1 = "afs234ljL   dfljdfs   LJJ#$ LJDFl"
# print(s1.index("#"))

#被装饰函数带返回值
# import time
# def timer(f1):
#     def inner():
#         start_time = time.time()
#         f1()
#         end_time = time.time()
#         print('此函数的执行效率%s' %(end_time-start_time))
#     return inner
#
#
# # timer(f1) = inner
# @timer  # func1 = timer(func1)
# def func1():
#     print('晚上回去吃烧烤....')
#     time.sleep(0.3)
# func1()


# def fun1():
#     return 789
# res = fun1
# print(res())

# def fun1():
#     b = 10
#     def inner():
#         nonlocal b
#         b += 1
#         print(b)
#     return inner
#
# fun1 = fun1()
# fun1()
# fun1()

# a = 1
# def fun1(argv):
#     a = 2
#     print(a)
# fun1(a)

# dic1 = {}
#
# dic2 = {123:345}
#
# # dic3 = {[1,2,3]:'uestc'}
#
# dic4 = {(1,2,3):'uestc'}
# print(dic4)

# Kvps = {"1": 1,"2": 2}
#
# theCopy = Kvps
#
# Kvps["1"] = 5
#
# sum = Kvps["1"] + theCopy["1"]
#
# print(sum)

# a = "a"
# print(a < "b")

# x = 43
# ch = "A"
# y = 1
# # print(x >= y and ch < "b" and y)
# print(x >= y and ch < "b" and y )
# #  False and True and y

# min = 2 if 2 > 3 else 3
# print(min)
#512 256 128 64 32 16 8 4 2 1
#
# k=1000
# while k>1:
#     print(k)
#     k=k/2

# for i in range(3):
#     print(i)
# tu = (1, 2, 3)
# tu1 = list(tu)
# print(tu1)
# dic = dict.fromkeys(['barry','alex',],[])
# dic['barry'].append(666)
# print(dic)
# l = [1,1,2,2,3,4,5,5,6,6,7,8]
# l = set(l)
# print(list(l))

# l1 = [1,[22,33,44],3,4,]
# l2 = l1
# l3 = l1.copy()
# l1.append(666)
# l1[1].append('55')
# print(l1,l2,l3)

# l1 = [1,[22,33,44,55],3,4,666]
# l2 = [1,[22,33,44,55],3,4,666]
# l3 = [1,[22,33,44,55],3,4]
# a = "1,2,3"
# li = a.split(",")
# print(li)
#
# li1 = ["1", "2", "3"]
# count = 0
# for i in li1:
#     li1[count] = int(i)
#     count += 1
# print(li1)

#   [1,4,9,16,25,36,64,81,100]
# l1 = []
# for i in range(100):
#     l1.append(i)
#
# l2 = []
# sums = 0
# for i in l1:
#     if i % 2 == 1:
#         sums += i
#         l2.append(sums)
#         if sums == 100:
#             break
#
# print(l2)
# a = 1
#
# def func1():
#     global a
#     a += 1
#     print(a)
# func1()
#
#
# def wrapper():
#     a = 1
#     def inner():
#         nonlocal a
#         a += 1
#         print(a)
#     inner()
# wrapper()
# def extendList(val,list=[]):
#
#     list.append(val)
#     return list
#
# list1 = extendList(10)
# print(list1)

# li1 = []
# #
# li1.append(1)
# li2 = li1
# li1.append(2)
# li3 = li1
#
#
# print(li1) # []  #[1,2]
# print(li2) # [1]  #[1,2]
# print(li3) # [2]  #[1,2]
#
# li1 = []
# li1.append(1)
# print(li1)

# print(li1.append(2))
# print(li1)
import  copy

# li1 = [[1, 2, 3]]
# li2 = li1
# # li3 = copy.deepcopy(li1)
# # li1.append(1)  # [[1, 2, 3],1]
#
# li1[0].append(4) # [[1, 2, 3,4],1]
# print(li1)
# print(li2)
# print(li3)
# """
# def fun():
#     print("测试")
#
# def fun2():
#     fun()
#     print("123")
# def fun3():
#     fun()
#     print("123"
# """


# def fun(argv):
#     def inner(*args):
#         argv(*args)
#         print("测试")
#     return inner
#
# @fun
# def fun2(name, password):
#     print(name)
#     print(password)
# fun2("wxx","123")

# dic = {1:2}
# print(dic.get(1,1))

# def fun1(argv):
#     def inner():
#         username = input(">:")
#         pasword = input(">:")
#         if username == "wxx" and pasword == "123":
#             argv()
#     return inner
# @fun1
# def fun2():
#     print("fun2")
# @fun1
# def fun3():
#     print("fun3")
# fun2()


# user_status = {"user": None, "status": False}
#
# print(user_status["user"] and user_status["status"])
# def fun1():
#     if user_status["user"] and user_status["status"]:
#         username = input(">>")
#         password = input(">>")
#         if username == "wxx" and password == "123":
#             print("登录成功！")
#             user_status["user"] = username
#             user_status["status"] = True
#     else:
#         print("登录成功！")
# while True:
#     fun1()

# if None:
#     print(123)
# else:
#     print(456)

# user_status = {"user": None, "status": False}
# while True:
#     if user_status["user"] and user_status["status"]:
#             username = input(">>")
#             password = input(">>")
#             if username == "wxx" and password == "123":
#                 print("登录成功！")
#                 user_status["user"] = username
#                 user_status["status"] = True
#         else:
#             print("登录成功！")

# a = False
# while True:
#     if a:
#         print(a)
#     else:
#         a = True

#
#
#
# def Before(request,kargs):
#     print('before')
#
#
# def After(request,kargs):
#     print("after")
#
#
# def Filter(before_func, after_func):
#     def outer(main_func):
#         def wrapper(request, kargs):
#             before_result = before_func(request, kargs)
#             if(before_result != None):
#                 return before_result
#             main_result = main_func(request, kargs)
#             if(main_result != None):
#                 return main_result
#             after_result = after_func(request, kargs)
#             if(after_result != None):
#                 return after_result
#         return wrapper
#     return outer
#
#
# @Filter(Before, After) # Index = Filter(Before,After)
# def Index(request,kargs):
#     print("index")
#
#
# Index("123", "456")


# def wrapper(func1):
#     def inner(*args, **kwargs):
#         print("我是装饰器wrapper")
#         res = func1(*args, **kwargs)
#         if res != None:
#             return res
#     return inner


# @wrapper
# def fun1():
#     print("我是普通函数fun1")
#
# #
# # @wrapper
# # def fun2(argv):
# #     print("我是带参数的函数fun2,参数：%s" % (argv,))
# #
# #
# # @wrapper
# # def fun3(argv1, argv2):
# #     print("我是带参数和返回值的函数fun3,参数： %s %s" % (argv1, argv2))
# #     return argv1, argv2
# #
# #
# @wrapper
# def fun4(*args, **kwargs):
#     print("我是带动态参数的函数fun4 参数 %s %s" % (args, kwargs))
#     return (args, kwargs)
# #
# # print(fun1())
# # print("-"*50)
# # print(fun2(1))
# # print("-"*50)
# # print(fun3(1,2))
# print("-"*50)
# print(fun4(1,2,3,4,5,x="123",y="456",z="789"))
#
#
# # def fun5(**kwargs):
# #     print(kwargs.values())
# #     return kwargs.values()
# #
# # res = fun5(x="123",age=2,job=3)
# # print(res)


# li1 = ["123"]
# print(li1.pop())\

# def fun1():
#     pass
# str_func = "%s " % (fun1,)
# # print(str_func)
# data = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'Google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             }
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {}
#             },
#             '天通苑': {},
#             '回龙观': {}
#         },
#         '朝阳': {},
#         '东城': {}
#     },
#     '上海': {},
#     '湖北': {},
#     '广东': {}
# }
#
# current_layer = data
# last_layer = []
# while True:
#     for i in current_layer:
#         print(i)
#     choice = input(">>>:")
#     if not choice:continue
#     if choice in current_layer:
#         last_layer.append(current_layer)
#         current_layer = current_layer[choice]
#     elif choice.lower() == "b":
#         if len(last_layer) < 1:
#             print("已经到最顶层")
#         else:
#             current_layer = last_layer.pop()
#     else:
#         print("节点不存在！")

# s = "Abc"
# s1 = s.lower()
# print(s1)
# s2 = s1.upper()
# print(s2)
# s = "  234  22224sd "
# s3 = s1.strip()
# print(s3)
# s4 = s1.center(50, "-")
# print(s4)
# s5 = s.count("2")
# print(s5)
# s6 = s.split("4")
# print(s6)
# s7 = s.replace("2", "3")
# print(s7)
# s = "ABC"
# s8 = s.index("C")
# print(s8)
# s9 = "{}{}".format(1, 2)
# print(s9)
# # s = "123"
# l1 = ["1", "2", "3"]
# # s1 = "_".join(s)
# s2 = "_".join(l1)
# print(s1)
# print(s2)

# s = "ABCEF"
# s1 = s.ljust(6, "-")
# s2 = s.rjust(6, "-")
# print(s1)
# print(s2)
#
# s3 = s.startswith("B")
# print(s3)
# s4 = s.endswith("B", 0, 2)
# print(s4)
#
# s5 = s.find("M")
# print(s5)


# 5，数字，字符串，列表，元祖，字典对应的布尔值的False分别是什么？（5分）
# 数字除了0都是True
# 数字除了空字符串都是 True

# 7，写代码，有如下列表，利用切片实现每一个功能（每题一分，共计4分）
# li = [1,3,2,"a",4,"b",5,"c","s"]
# # 通过对li列表的切片形成新的列表l3,l3 = [’1,2,4,5]
# l3 = li[::2]
# print(l3)
# # 通过对li列表的切片形成新的列表l4,l4 = [3,’a’,’b’]
# l4 = li[1:6:2]
# print(l4)
# # 通过对li列表的切片形成新的列表l5,l5 = [‘c’]
# l5 = li[-2]
# print(list(l5))
# # 通过对li列表的切片形成新的列表l6,l6 = [‘b’,’a’,3]
# l6 = li[1:6:2]
# l6.reverse()
# print(l6)
# 8，组合嵌套题。
# a,写代码，有如下列表，按照要求实现每一个功能（每题3分，写出一种方法得1分，写出两种方法的3分。此题共9分）
# （每个都是一行代码实现）
# lis = [[‘k’,[‘qwe’,20,{‘k1’:[‘tt’,3,’1’]},89],’ab’]]
# 将列表lis中的’tt’变成大写（用两种方式）。
# 将列表中的数字3变成字符串’100’（用两种方式）。
# 将列表中的字符串’1’变成数字101（用两种方式）。
#
#
# b，写代码，有如下字典，按照要求实现每一个功能(5分)
# dic = {‘k1’:’v1’,’k2’:[‘alex’,’sb’],(1,2,3,4,5):{‘k3’:[‘2’,100,’wer’]}}
# 将’k2’对应的值的最后面添加一个元素’23’。
# 将’k2’对应的值的第一个位置插入一个元素’a’。
# 将(1,2,3,4,5)对应的值添加一个键值对’k4’,’v4’。
# 将(1,2,3,4,5)对应的值添加一个键值对(1,2,3),’ok’。
# 将’k3’对应的值的’wer’更改为’qq’。







