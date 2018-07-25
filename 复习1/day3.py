#!/usr/bin/env python3
file = "./dbfile"


# with open(file,"a") as f:
#     for i in range(10):
#         f.write(str(i))
# with open(file, "rb") as f:
#     for i in f:
#         print(i)
# handle = open(file)
# text = handle.read(3)
# print(text)
# handle.close()

# f1 = open(file, encoding='utf-8')
# print(f1.readlines())
# f1.close()


# f1 = open(file, "r")
# f1.seek(0, 2)
# print(f1.tell())
# f1.close()

# s = "中国"
# b1 = s.encode("utf-8")

#
# with open(file, "ab") as f:
#     f.write("中国")


# 文件的改
# 1，打开原文件，产生文件句柄。
# 2，创建新文件，产生文件句柄。
# 3，读取原文件，进行修改，写入新文件。
# 4，将原文件删除。
# 5，新文件重命名原文件。
# import os
# with open(file, encoding="utf-8") as f, open("new_tmp", "a", encoding="utf-8") as f1:
#     for i in f:
#         ret = i.replace("0", "A")
#         f1.write(ret)
#
# os.remove(file)
# os.rename("new_tmp", "dbfile")
#
# def foo(x, y):
#     return x * y
#
#
# print(foo(y=5, x=6))

# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# def max1(a, b): return a if a > b else b
#
#
# print(max1(3, 4))


# def foo(*args, **kwargs):
#     print(*args)
#     print(args)
#     print(*kwargs)
#     print(kwargs)
#
#
# foo(1, 2, 3, 4, a=5, b=5)

# def fun():
#     name = "spf"
#     print(globals())
#     print(locals())
# fun()

#
# def add_b():
#     b = 42
#
#     def do_global():
#         b = 10
#         print(b)  # 10
#
#         def dd_nonlocal():
#             nonlocal b
#             b = b + 20 # 30
#             print(b)
#
#         dd_nonlocal()
#         print(b)  # 10
#
#     do_global()
#     print(b) # 42
#
#
# add_b()


# def wrapper(fun):
#     def inner(*args,**kwargs):
#         # 装饰器前的代码
#         ret = fun(*args, **kwargs)
#         # 装饰器后的代码
#         return ret
#     return inner
# flag = True
#
#
# def outer(flag):
#     def wrapper(fun):
#         def inner(*args, **kwargs):
#             if flag:
#                 print("功能A")
#                 res = fun(*args, **kwargs)
#                 print("功能B")
#                 return res
#             else:
#                 return fun(*args, **kwargs)
#
#         return inner
#
#     return wrapper
#
#
# @outer(flag)
# def fun():
#     print("我是fun")
#
#
# fun()


#  多个装饰器装饰一个函数
# def wrapper1(f):  # f = inner2
#     def inner1():
#         print("我是wrapper1")
#         f()  # inner2()
#         print("我是wrapper1")
#
#     return inner1
#
#
# def wrapper2(f):  # f = func
#     def inner2():
#         print("我是wrapper2")
#         f()  # func()
#         print("我是wrapper2")
#
#     return inner2
#
#
# @wrapper1  # func = wrapper1(func)= wrapper1(inner2) = inner1
# @wrapper2  # func = wrapper2(func) = inner2
# def func():
#     print("我是func")
#
#
# func()  # func = inner1 = inner1()
# lst = [1,2,3]
# print(dir(lst))


# def foo(x, y=[]):  # x = 2  y =[]   # x = 2 y = [1,2,3]
#     for i in range(x):  # 0,1       # 0,1
#         y.append(i*i)   # y =[0,1]  # [1,2,3,0,1]
#     print(y)
#
#
# foo(2)
# foo(2, [1, 2, 3])

# lst = [1, 2, 3]
# print(dir(iter(lst)))

#
# def gent(count):
#     for i in range(count):
#         yield i
#
#
# g1 = gent(10)
# # print(list(g1))
# while 1:
#     try:
#         print(g1.__next__())
#     except StopIteration:
#         break


# def gent(count):
#     for i in range(count):
#         yield "生产了%s件衣服" % i
#
#
# g = gent(2000)
#
# # 取10件
# for i in range(10):
#     print(g.__next__())
#
# for j in range(10):
#     print(g.__next__())

def wrapper(fun):
    def inner(*args, **kwargs):
        g = fun(*args, **kwargs)
        g.__next__()
        return g

    return inner


#
#
# @wrapper
# def fun():
#     print("1111")
#     ret = yield 1
#     print("2222", ret)
#     ret2 = yield 2
#     print("3333", ret2)
#     yield 3
#
#
# g = fun()
# print(g.send("a"))
# print(g.send("b"))


# @wrapper
# def fun():
#     sums = 0
#     day = 0
#     avg = 0
#     while 1:
#         money = yield avg
#         sums += money
#         day += 1
#         avg = sums/day
#
#
# g = fun()
# print(g.send(50))
# print(g.send(100))
# print(g.send(300))


# lst = [i for i in range(10)]
# print(lst)
# gst = (i for i in range(10))
# print(gst.__next__())

def add(n, i):  # 定义一个求和函数
    return n + i  # 返回和


def test():  # 生成器函数，里面有4个值0,1,2,3
    for i in range(4):
        yield i


g = test()  # g = 生成器
for n in [1, 10]:  # 列表里面有2个数字 1 和 10
    g = (add(n, i) for i in g)
    # n = 1
    # g=(add(n,i) for i in g)
    # n = 10
    # g=(add(n,i) for i in g) (add(10,i) for i in g)

print(list(g))
# g = (add(n,i) for i in (add(10,i) for i in g)) --> (add(n,i) for i in (add(10,i) for i in (0,1,2,3,4))) -->
#  (add(10,i) for i in (10,11,12,13) --->(20,21,22,23) --->[20,21,22,23]
