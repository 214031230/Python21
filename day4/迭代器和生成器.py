#!/usr/bin/env python3
# 迭代器 iterator
# 凡是可以使用for循环取值的都是可迭代的
# 列表，字典，元组，字符串，集合，range，文件句柄，enumerate等都是可迭代对象
# # 如何查看对象是否可迭代 dir
# lst = [1, 2, 3]
# print(dir(lst))  # 含有'__iter__'方法就是可迭代的
#
# # 怎么把可迭代对象变成迭代器
# lst_iter = iter(lst)
# lst_iter1 = lst.__iter__()
# # 备注：上面lst_iter 和 lst_iter1是两个生成器
#
# # 如何查看lst_iter是不是迭代器
# print(dir(lst_iter))  # 含有__iter__方法和__next__方法的就是迭代器

# 如何迭代器中取值?
# 第一种 ：next  随时都可以停止 最后一次会报错
# print(next(lst_iter))  # 结果 1
# print(lst_iter.__next__())  # 结果 2
# print(next(lst_iter))  # 结果 3
#
# # 解决取不到值会报错StopIteration， try except异常捕捉
# while True:
#     try:
#         print(next(lst_iter))  # lst_iter.__next__()
#     except StopIteration:
#         break
#
# # 第二种 ：for循环 从头到尾遍历一次 不遇到break、return不会停止
# for i in lst_iter:
#     print(i)
#
# # 第三种 ：list tuple 数据类型的强转  会把所有的数据都加载到内存里 非常的浪费内存
# print(lst_iter)
# print(list(lst_iter))

# 问题 : ranger(100)是迭代器吗？
# range(100) 不是迭代器，但是一个可迭代对象。使用iter可以变成迭代器

# py2 range 不管range多少 会生成一个列表 这个列表将用来存储所有的值
# py3 range 不管range多少 都不会实际的生成任何一个值

# 可迭代协议 ：内部含有__iter__方法的都是可迭代的
# 迭代器协议 ：内部含有__iter__方法和__next__方法的都是迭代器

# 迭代器的优势:
#     节省内存
#     取一个值就能进行接下来的计算 ，而不需要等到所有的值都计算出来才开始接下来的运算 —— 快

# 迭代器的特性:惰性运算



# # 生成器 Generator
# # 自己写的迭代器 就是一个生成器
# # 两种自己写生成器(迭代器)的机制：生成器函数 生成器表达式
# # 生成器函数
# def generator():
#     for i in range(10):
#         yield i
# g = generator()
#
# while True:  # 通过循环取生成器里面的所有值
#     try:
#         print(next(g))
#     except StopIteration:
#         break
#
# # 示例，生产20000件衣服。
# def generator():
#     for i in range(1, 20001):
#         yield "制作第%s件衣服" % (i,)
# g = generator()
#
# # 取10件衣服
# for i in range(1, 11):
#     print(next(g))
#
#
# # 凡是带有yield的函数就是一个生成器函数
# def func():
#     print('****')
#     yield 1
#     print('^^^^')
#     yield 2   # 记录当前所在的位置，等待下一次next来触发函数的状态
#
# g = func()
# print('--',next(g))
# print('--',next(g))
# # 生成器函数的调用不会触发代码的执行，而是会返回一个生成器(迭代器)
# # 想要生成器函数执行，需要用next
# def cloth_g(num):
#     for i in range(num):
#         yield 'cloth%s'%i
#
#
# g = cloth_g(1000)
# print(next(g))
# print(next(g))
# print(next(g))


# 生成器示例 文件监听
# 监听函数
# import time
# def listen_file(filename):
#     with open(filename) as f1:
#         while True:
#             # f1.seek(0, 2)  # 光标移到文件尾部
#             res = f1.readline()  # 每次只读一行，readline 会一直读如果已经到最后一行则返回空。readline不会停止所以用readline
#             if res.strip():
#                 f1.seek(0, 2)
#                 yield res.strip()
#             time.sleep(0.1)  # 0.5秒获取一次监听
# g = listen_file("tmp")
# for i in g:
#     print(i)
#
# # 循环写文件
# import time
# count = 1
# while True:
#     with open("tmp", mode="a") as f1:
#         f1.write("我是第%s行\n" % (count,))
#     count += 1
#     time.sleep(1)


# send关键字
# def func():
#     print(11111)
#     ret1 = yield 1
#     print(22222, 'ret1 :', ret1)
#     ret2 = yield 2
#     print(33333, 'ret2 :', ret2)
#     yield 3
#
# g = func()
# print(next(g))  # 结果是 11111
# print(g.send('alex'))  # 在执行next的过程中 传递一个参数给yield1
# print(g.send('金老板'))  # 在执行next的过程中 传递一个参数给yield2
# #send 获取下一个值的效果和next基本一致
#只是在获取下一个值的时候，给上一yield的位置传递一个数据
#使用send的注意事项
    # 第一次使用生成器的时候 是用next获取下一个值
    # 最后一个yield不能接受外部的值
# 想生成器中传递值 有一个激活的过程 第一次必须要用next触发这个生成器

#  示例：移动平均值
# def func_g(num = 0):
#     sums = 0
#     day = 0
#     avg = 0
#     while True:
#         money = yield avg  # 返回avg，并接受seed传进来的money
#         sums += money  # sums = sums + money
#         day += 1
#         avg = sums/day
#
# g = func_g()
# print(next(g))
# print(g.send(50))
# print(g.send(100))
# print(g.send(300))

# 示例：生成器预激活，使用send必须next预激活一下，可以用装饰器来操作预激活
# def wrapper(f): # f = func_g
#     def inner(*args, **kwargs):
#         g = f(*args, **kwargs) # f = func_g
#         next(g)
#         return g  # 必须返回生成器
#     return inner
#
# @wrapper  # func_g = wrapper(func_g)
# def func_g(num = 0):
#     sums = 0
#     day = 0
#     avg = 0
#     while True:
#         money = yield avg  # 返回avg，并接受seed传进来的money
#         sums += money  # sums = sums + money
#         day += 1
#         avg = sums/day
#
# g = func_g()  # func_g  = inner ()
# print(g.send(50))
# print(g.send(100))
# print(g.send(300))
#
# # yield from
# # 普通生成器函数
# def func_g():
#     for i in range(5):
#         yield i
#     print("----------")
#     for i in range(10):
#         yield i
# g = func_g()
#
# # 装逼版生成器函数
# def func_g():
#     yield from range(5)
#     print("----------")
#     yield from range(10)
# g = func_g()
#
# while True:
#     try:
#         print(g.__next__())
#     except StopIteration:
#         break
#
# # 列表推导式和生成器表达式
#
# # 开篇
# #老男孩由于峰哥的强势加盟很快走上了上市之路,alex思来想去决定下几个鸡蛋来报答峰哥
# agg_list = ["鸡蛋%s" % i for i in range(1, 10)]  # 列表推导式
# print(agg_list)
# #峰哥瞅着alex下的一筐鸡蛋,捂住了鼻子,说了句:哥,你还是给我只母鸡吧,我自己回家下
# laomuji = ("鸡蛋%s" % i for i in range(1, 10))   # 生成器表达式
# print(laomuji)
# print(laomuji.__next__())  # 下一个鸡蛋
# print(laomuji.__next__())  # 下二个鸡蛋
# print(laomuji.__next__())  # 下三个鸡蛋
#
#
# # 总结：
# # 1.把列表解析的[]换成()得到的就是生成器表达式
# # 2.列表解析与生成器表达式都是一种便利的编程方式，只不过生成器表达式更节省内存
# # 3.Python不但使用迭代器协议，让for循环变得更加通用。大部分内置函数，也是使用迭代器协议访问对象的。
# # 例如， sum函数是Python的内置函数，该函数使用迭代器协议访问对象，而生成器实现了迭代器协议，所以，我们可以直接这样计算一系列值的和：
# res = sum(i for i in range(1, 101))
# print(res)
# res1 = sum([i for i in range(1, 101)])
# print(res1)
# #
# # 列表解析
# sum([i for i in range(100000000)])  # 内存占用大,机器容易卡死
# # 生成器表达式
# sum(i for i in range(100000000))  # 几乎不占内存
#
#
# # 面试题1
# def demo():
#     for i in range(4):
#         yield i
#
# g=demo() # g 是生成器
#
# g1 = (i for i in g)  # g1 是生成器 (i for i in g) g1(0,1,2,3)
# g2 = (i for i in g1)  # g2 也是生成器  (i for i in (0,1,2,3))
#
# print(list(g1))  # 从g1生成器取值，g1又从g生成器中取值，用list会取出生成器内的所有值
# print(list(g2))  # 从g2生成器取值，g2又从g1生成器中取值，g1又从g中取值。g生成器已经被取完，所以取不到值
#
# # 面试题2
# def add(n,i): # 定义一个求和函数
#     return n+i # 返回和
#
# def test(): # 生成器函数，里面有4个值0,1,2,3
#     for i in range(4):
#         yield i
#
# g=test() # g = 生成器
# for n in [1,10]: # 列表里面有2个数字 1 和 10
#     # g = (add(n, i) for i in g)
#     n = 1
#     g=(add(n,i) for i in g)
#     n = 10
#     g=(add(n,i) for i in g)
#
# print(list(g)) # g = (add(n,i) for i in (add(10,i) for i in g)) --> (add(n,i) for i in (add(10,i) for i in (0,1,2,3,4))) -->
               #  (add(10,i) for i in (10,11,12,13) --->(20,21,22,23) --->[20,21,22,23]


