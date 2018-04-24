#!/usr/bin/env python3
# import time
# count = 1
# while True:
#     with open("tmp", mode="a") as f1:
#         f1.write("我是第%s行\n" % (count,))
#     count += 1
# #     time.sleep(1)
# def func_g(num = 0):
#     sums = 0
#     day = 0
#     avg = 0
#     while True:
#         yield avg  # 返回avg，并接受seed传进来的money
#           # sums = sums + money
#         # day += 1
#         avg += 1
#         # avg = sums/day
#
#
# g = func_g()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# li = [i for i in range(10) if i % 2 == 0]
# lst = []
# for i in range(10):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst)

# li1 = [lambda x: x*i for i in range(10) if i % 2 == 0]
#
# lst = []
# for i in range(10):
#     if i % 2 == 0:
#         lst.append(lambda x: x*i)
# lst = [lambda x: x*i,lambda x: x*i,lambda x: x*i,lambda x: x*i]
#
# li2 = [2 for m in range(5)]
# lst1 = []
# for i in range(5):
#     lst1.append(2)

# def multipliers():
#     return [lambda x:i*x for i in range(4)]
#
# print([m(2) for m in multipliers()])

# def multipliers():
#     lst = []
#     for i in range(4):
#         lst.append(lambda x:i*x)
#     return lst
# lst = multipliers()
# print([m(2) for m in multipliers()])
#
# lst1 = []
# for m in lst:
#     m = lambda x:3*x
#     m(2)




