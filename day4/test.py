#!/usr/bin/env python3
# import time
# def genrator_fun1():
#     a = 1
#     print('现在定义了a变量')
#     yield a
#     b = 2
#     print('现在又定义了b变量')
#     yield b
#
# g1 = genrator_fun1()
# print('g1 : ',g1)       #打印g1可以发现g1就是一个生成器
# print('-'*20)   #我是华丽的分割线
# print(next(g1))
# time.sleep(1)   #sleep一秒看清执行过程
# print(next(g1))

# 初识生成器函数

# def generator():
#     for i in range(20000):
#         yield "生成了衣服%s" % (i,)
# g = generator()
# print(g.__next__())
# print(next(g))
#
# for i in range(5):
#     print(g.__next__())

#
# import time
#
#
# def tail(filename):
#     f = open(filename)
#     f.seek(0, 2) #从文件末尾算起
#     while True:
#         line = f.readline()  # 读取文件中新的文本行
#         if not line:
#             time.sleep(0.5)
#             continue
#         yield line
#
# tail_g = tail('tmp')
# for line in tail_g:
#     print(line)

# 生成器监听文件输入的例子

#
# def generator():
#     print("A")
#     res1 = yield 1
#     print("B", res1)
#     res2 = yield 2
#     print("C", res2)
#     yield 3
#     print("D")
#     yield 4
# g = generator()
# print(g.__next__())
# print(g.send("我是第一个参数"))
# print(g.send("我是第二个参数"))
# print(g.__next__())

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


g_avg = averager()
next(g_avg)
print(g_avg.send(10))
print(g_avg.send(30))
print(g_avg.send(5))

# 计算移动平均值(1)