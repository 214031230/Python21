#!/usr/bin/env python3
# 1.写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]
#
#
# def fun1():
#     l1 = ["红心", "草花", "黑桃", "方块"]
#     l2 = []
#     for i in range(53):
#         if i == 0:
#             pass
#         else:
#             for x in l1:
#                 l2.append((x, i))
#     return l2
#
#
# print(fun1())

#
# 2.写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如:min_max(2,5,7,8,4)
# 返回:{‘max’:8,’min’:2}
#
#
# def fun2(*args):
#     dic = {"max": max(args),
#            "min": min(args)}
#     return dic
#
#
# print(fun2(2,234,23,4,1,5,2,3,523,4))

# 3.
# 写函数，专门计算图形的面积
# 其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
# 调用函数area(‘圆形’, 圆半径)  返回圆的面积
# 调用函数area(‘正方形’, 边长)  返回正方形的面积
# 调用函数area(‘长方形’, 长，宽)  返回长方形的面积
#
#

#
# def area(graphic, argv1, argv2 = 0):
#     if graphic == "圆形":
#         def round():
#             print (2*3.14*argv1)
#         round()
#     elif graphic == "正方形":
#         def square():
#             print(argv1*argv1)
#         square()
#     elif graphic == "长方形":
#         def rectangle():
#             print(argv1*argv2)
#         rectangle()
#
# area("正方形",4)

# 4.写函数，传入一个参数n，返回n的阶乘
# 例如:cal(7)
# 计算7*6*5*4*3*2*1

# def fun3(n):
#     count = 1
#     sums = 1
#     while count <= n:
#         sums = sums * count
#         count += 1
#     return sums
# print(fun3(4))
# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件)
# 要求登录成功一次，后续的函数都无需再输入用户名和密码

# 5、编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果（升级题）

# from urllib.request import urlopen


# def geturl(url):
#     def inner():
#         return urlopen(url).read()
#     return inner
#
# geturl = geturl("http://www.baidu.com")
# print(geturl())
# print(geturl())


# 5.1.为题目3编写装饰器，实现缓存网页内容的功能：（升级题）
# 具体：实现下载的页面存放于文件中，如果网页有对应的缓存文件，
# 就优先从文件中读取网页内容，否则，就去下载，然后存到文件中
# from urllib.request import urlopen
#
#
# def geturl(url):
#     with open("./file/tmp_url", encoding="utf-8") as f1, open("./file/tmp_url", mode="a", encoding="utf-8") as f2:
#         for i in f1:
#             if url in i:
#                 tmp_url = i.split("分隔符")
#                 return "缓存内容：%s" % (tmp_url,)
#         else:
#             f2.write("%s分隔符%s\n" % (url, urlopen(url).read()))
#             return urlopen(url).read()
#
# while True:
#     usl_name = input("请输入网址：")
#     if "http" in usl_name:
#         res = geturl(usl_name)
#         print(res)
#     else:
#         res = geturl("http://%s" % (usl_name,))
#         print(res)


# 6给每个函数写一个记录日志的功能，
# 功能要求：每一次调用函数之前，要将函数名称，时间节点记录到log的日志中。
# 所需模块：
# import time
# struct_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time))

# import time
#
#
# def wrapper_log(func):
#     def inner():
#         with open("./file/fun_run.log",mode="a",encoding="utf-8") as f1:
#             timer = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#             f1.write("%s运行了：%s\n" % (timer, func))
#         func()
#     return inner
#
#
# @wrapper_log
# def fun1():
#     print("你好！")
#
#
# fun1()


def w1(func):
    def inner():
        print("w1")
        func()
    return inner

def w2(func):
    def inner():
        print("w2")
        func()
    return inner

@w1
@w2
def fun1():
    print("fun1")

fun1()



