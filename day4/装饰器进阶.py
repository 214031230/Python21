#!/usr/bin/env python3
# 带参数的装饰器

# FLAG = False
# def outer(flag):
#     def wrapper(f):
#         def inner(*args, **kwargs):
#             if flag == True:
#                 print("star_wrapper")
#                 f()
#                 print("end_wrapper")
#             else:
#                 f()
#         return inner
#     return wrapper
#
# @outer(FLAG) # func = outer(flag) -->  wrapper(func) -->inner()
# def func():
#     print("func")
#
# func()

# import time
# user_status = {"alex": False}
#
# def login(f):
#     def inner(name):
#         if user_status[name] == False:
#             print("请登录")
#             user_status[name] = True
#             f(name)
#         else:
#             print("登录成功")
#             f(name)
#     return inner
#
#
# def timmer(f):
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         res = f(*args, **kwargs)
#         end_time = time.time()
#         print(end_time - start_time)
#         return res
#     return inner
#
# @login
# @timmer
# def func(name):
#     print("start_func")
#     print(func)
#     time.sleep(0.1)
#     print("end_func")
#
# func("alex")



# li = [1,2,3,4,-5,10]
#
# li1 = [i % 2 for i in li]
# print(li1)
# print([i for i in range(30) if i % 3 == 0])
#
# print([i for i in range(30) if i % 3 == 0])
#
# def demo():
#     for i in range(4):
#         yield i
# g=demo()
# g1=(i for i in g)
# g2=(i for i in g1)
# print(list(g1))
# print(list(g2))

# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
#
# #  next
# #  for
# #  list
#
# # for n in [1,10]:
# #     g=(add(n,i) for i in g)
# n = 1
# g=(add(n,i) for i in g)
# n = 10
# g=(add(10,i) for i in (10,11,12,13))
#
# # print(list(add(n,i) for i in g))



#
# def func1():
#     print(1111)
#     yield 1
#     print(2222)
#     yield 2
#     print(3333)
#     yield 3
# g = func1()
# print(next(g))
# import time
# for i in range(1, 101, 2):
#     time.sleep(0.1)
#     res = "\r%s %% %s" % (i, "#"*i)
#     print(res, end="")

# 现有两元组(('a'),('b')),(('c'),('d')),请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]
# t1 = (('a'),('b'))
# t2 = (('c'),('d'))
# res = zip(t1,t2)

