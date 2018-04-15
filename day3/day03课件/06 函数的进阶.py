# name = 'alex'
# age = 12
# def func1():
#     name1 = 'wusir'
#     age1 = 34
# func1()
# print(name1)
#临时名称空间:临时名称空间，局部名称空间，存入函数里面的变量与值的关系，随着函数的执行结束，临时名称空间消失。

#名称空间：全局名称空间，局部名称空间，内置名称空间。
#作用域：
    # 全局作用域：全局名称空间，内置名称空间。
    # 局部作用域：局部名称空间

#加载顺序，取值顺序。
#加载顺序：内置名称空间 ----> 全局名称空间----> 局部名称空间(函数执行时)
#取值顺序：局部名称空间 ---> 全局名称空间 ----> 内置名称空间
# name1 = 'wusir'
# def func1():
#     print(name1)
#     def func2():
#         print('****',name1)
#     func2()
# func1()

# name1 = 'wusir'
# def func1():
#     name2 = 'laonanhai'
#     print(globals())
#     print(locals())
# func1()

#关键字：global nonlocal
# count = 1
# def func1():
#     count = count + 1
#     print(count)
#global 1,声明一个全局变量
       #2，更改一个全局变量
# name = 'wusir'
# def func1():
#     global name
#     name = 'alex'
#     return
# func1()
# print(name)

#nonlocal

# def func1():
#     name1 = 'alex'
#     print('+',name1)
#     def inner():
#         nonlocal name1
#         name1= 'wusir'
#         print('*',name1)
#         def inner1():
#             pass
#     inner()
#     print('%',name1)
# func1()

#函数名
#1，可以互相赋值。

# def func1():
#     print(666)
#
# f1 = func1
# f1()

#2,函数名可以当成函数的参数

# def func1():
#     print(666)
#
#
# def func2(argv):
#     argv()
#     print(777)
#
# func2(func1)

#3，可以当成容器类数据类型的参数

# def func1():
#     print(666)
#
# def func2():
#     print(777)
#
# def func3():
#     print(888)
#
# l1 = [func1, func2, func3]
# for i in l1:
#     i()

#4,函数名可以当成函数的返回值
#
# def func1():
#     print(666)
#
# def func2(argv):
#     print(777)
#     return argv
#
# ret = func2(func1)
# ret()

# 闭包 内层函数对外层函数非全局变量的引用，叫做闭包
#闭包的好处：如果python 检测到闭包，
# 他有一个机制，你的局部作用域不会随着函数的结束而结束。
# def wrapper():
#     name1 = '老男孩'
#     def inner():
#         print(name1)
#     inner()
# wrapper()

#
# def wrapper():
#     name1 = '老男孩'
#     def inner():
#         print(name1)
#     inner()
#     print(inner.__closure__)  # cell
# wrapper()
# 判断是不是闭包
# name1 = '老男孩'
# def wrapper():
#     def inner():
#         print(name1)
#     inner()
#     print(inner.__closure__)  # None
# wrapper()

# name = 'alex'
# def wrapper(argv):
#     def inner():
#         print(argv)
#     inner()
#     print(inner.__closure__)  # cell
# wrapper(name)
from urllib.request import urlopen
# def index():
#     url = "http://www.cnblogs.com/jin-xin/articles/8259929.html"
#     def get():
#         return urlopen(url).read()
#     return get
# name1 = 'alex'
# content1 = index()()
# content2 = index()()
# print(content1)