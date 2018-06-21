#!/usr/bin/env python3
# def max(a,b):return a if a > b else b
# # print(max(3,4))
# def func(*args, **kwargs):
#     print(*args)
#     print(*kwargs)
#
# func(1,2,3,a=3,b=5)
# l1 = [1, 2, 3, 4]
# t1 = (1, 2, 3, 4)
# l2 = ['alex', 'wusir', 4]
# dic1 = {'name1': 'alex'}
# dic2 = {'name2': 'laonanhai'}
#
# def func(*args, **kwargs):
#     print(*args)
#     print(*kwargs)
#
# func(*l1,*t1,*l2,**dic1,**dic2)

# name = 123
#
# def func():
#     global name
#     name += 456
#     print(globals())
#     print(locals())
#
# func()
# print(globals())
# def add_b():
#     b = 42
#     def do_global():
#         b = 10
#         print(b)
#         def dd_nonlocal():
#             nonlocal b
#             b = b + 20
#             print(b)
#         dd_nonlocal()
#         print(b)
#     do_global()
#     print(b)
# add_b()
# 10
# 30
# 30
# 42
# import time
# def timer(func):
#     def inner(*args, **kwargs):
#         strat = time.time()
#         ret = func(*args, **kwargs)
#         print("运行了%s" % (time.time() - strat))
#         return ret
#     return inner
#
#
# @timer
# def fun():
#     time.sleep(1)
#     print("in fun")
#
#
# fun()
#
# def wrapper1(f):  # f = inner2
#     def inner1():
#         print("我是wrapper1")
#         f()  # inner2()
#         print("我是wrapper1")
#     return inner1
#
# def wrapper2(f): # f = func
#     def inner2():
#         print("我是wrapper2")
#         f()  # func()
#         print("我是wrapper2")
#     return inner2
#
# @wrapper1  # func = wrapper1(func)= wrapper1(inner2) = inner1
# @wrapper2  # func = wrapper2(func) = inner2
# def func():
#     print("我是func")
# func()  #  func = inner1 = inner1()
# lst = [1,2,3]
# lst1 = iter(lst)
# print(dir(lst1))
# print(range(10))

# def generator():
#     for i in range(10):
#         yield i
# g = generator()
# print(next(g))
# print(next(g))\
# import time
# def listen_file():
#     with open("a.txt") as f:
#         while 1:
#             ret = f.readline()
#             if ret.strip():
#                 yield ret.strip()
#                 f.seek(0,2)
#                 time.sleep(1)
# g = listen_file()
# for i in g:
#     print(i)

# def func():
#     print(11111)
#     ret1 = yield 1
#     print(22222, 'ret1 :', ret1)
#     ret2 = yield 2
#     print(33333, 'ret2 :', ret2)
#     yield 3
#
# g = func()
# print(g.__next__())
# print("----")
# print(g.send("aaa"))

# def func():
#     sums = 0
#     agv = 0
#     day = 0
#     while  True:
#         money = yield agv
#         sums += money
#         day += 1
#         agv = sums // day
#
# g = func()
# print(next(g))
# print(g.send(50))
# print(g.send(100))
# print(g.send(150))

# age_list = ["鸡蛋%s"%i for i in range(10)]
# print(age_list)
# laomuji = (i for i in range(10))
# print(laomuji.__next__())

# ret = sum(i for i in range(10))
# print(ret)
# ret = sum([i for i in range(10)])
# print(ret)

# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1 = (i for i in g)
# g2 = (i for i in g1)
#
# print(list(g1))
# print(list(g2))

# def add(n,i): # 定义一个求和函数
#     return n+i # 返回和
#
# def test(): # 生成器函数，里面有4个值0,1,2,3
#     for i in range(4):
#         yield i
#
# g=test() # g = 生成器
# for n in [1,10]: # 列表里面有2个数字 1 和 10
#     g = (add(n, i) for i in g)
#     # n = 1
#     # g=(add(n,i) for i in g)
#     # n = 10
#     # g=(add(n,i) for i in g)
#
#
# print(list(g)) # g = (add(n,i) for i in (add(10,i) for i in g)) --> (add(n,i) for i in (add(10,i) for i in (0,1,2,3,4))) -->
#                #  (add(10,i) for i in (10,11,12,13) --->(20,21,22,23) --->[20,21,22,23]



# print(format('test', '<20'))
# print(format('test', '>20'))
# print(format('test', '^20'))



# print(all([1,2,3,4,5]))
# print(all([0,1,2,3,4,5]))
# print(all(['a',1,2,3,4,5]))
# print(all(['',1,2,3,4,5]))
# print(any([0,None,False]))
#
# ret = zip([1,2,3,4,5],('a','b','c','d'),(4,5))
# for i in ret:
#     print(i)



# lst = [1, 4, 6, 7, 9, 12, 17]
# def fun(x):
#     if x % 2 == 0:
#         return x
#
# ret = filter(lambda x: x % 2 == 0, lst)
# print(list(ret))
#
# l = ['test', None, '', 'str', '  ', 'END']
#
# ret = filter(lambda x: bool(x) == True and bool(x.strip()) == True, l)
# print(list(ret))
#
# l = [1,2,3]
# ret = map(lambda x:x * 2, l)
# print(list(ret))

# s = (('a'), ('b')), (('c'), ('d'))
# ret = map(lambda x:{x[0]:x[1]},zip((('a'), ('b')), (('c'), ('d'))))
# print(list(ret))
import os


with open("./info") as f, open("./new_info", "a") as f1:
    for i in f:
        line = i.replace("坏人","好人")
        f1.write(line)


os.rename("./new_info", "./info")



l = []
l.extend(['111',222,333])
print(l)


l = ['老男孩', 'alex', 'wusir', 'taibai', 'ritian']
l[1:3] = [111,222,333,444]
print(l)












