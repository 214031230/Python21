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

def fun1():
    pass
str_func = "%s " % (fun1,)
print(str_func)
