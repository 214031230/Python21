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
s1 = "afs234ljL   dfljdfs   LJJ#$ LJDFl"
print(s1.index("#"))