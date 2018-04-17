#!/usr/bin/env python3
# 2、写函数，接收n个数字，求这些参数数字的和。（动态传参）


# def fun1(*args):
#     sums = 0
#     for i in args:
#         sums += i
#     return sums
#
#
# res = fun1(1, 2, 3, 4)
# print(res)


# 3、读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a = 10
# b = 20
#
#
# def test5(a, b):  # a = 20  b = 10
#         print(a, b)
#
#
# c = test5(b,a)
# print(c) # none



# 4、读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a = 10
# b = 20
#
#
# def test5(a, b): # a = 20 b = 1
#     a = 3
#     b = 5
#     print(a, b) # 3 5
#
#
# c = test5(b,a)
# print(c)

# a = 10
# b = 20
#
#
# def test5(argv1, argv2): # a = 20 b = 1
#     global a
#     a = 3
#     b = 5
#     print(a, b) # 3 5
#
#
# c = test5(a,b)
# print(c)
# print(a,b)
# 1，有函数定义如下：
# def calc(a,b,c,d=1,e=2):
#     return (a+b)*(c-d)+e
# # 请分别写出下列标号代码的输出结果，如果出错请写出Error。
# print(calc(1,2,3,4,5))  # 2
# print(calc(e=4,c=5,a=2,b=3))  # 24
# print(calc(1,2,3)) # 8
# print(calc(1,2,3,e=4)) # 10
# print(calc(1,2,3,d=5,4)) # EROOR



# 2，下面代码打印的结果分别是_________,________,________.
# def extendList(val,list=[]): 
# list.append(val) 
# return list list1 = extendList(10) list2 = extendList(123,[]) list3 = extendList('a')  print('list1=%s'%list1) print('list2=%s'%list2) print('list3=%s'%list3)


def extendList(val,list=[]):
    list.append(val)
    return list

list1 = extendList(10)  # [10]  # list[10]
list2 = extendList(123,[]) # [123]
list3 = extendList('a') # ["a"]
print('list1=%s'%list1)
print('list2=%s'%list2)
print('list3=%s'%list3)

