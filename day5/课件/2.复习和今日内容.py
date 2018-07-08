# 装饰器的进阶
    # 给装饰器加上一个开关  - 从外部传了一个参数到装饰器内
    # 多个装饰器装饰同一个函数 - 套娃
        # 每个装饰器都完成一个独立的功能
        # 功能与功能之间互相分离
        # 同一个函数需要两个或以上额外的功能
# def wrapper1(func):
#     def inner(*args,**kwargs):
#         '''执行a代码'''
#         ret = func(*args,**kwargs)
#         '''执行b代码'''
#         return ret
#     return inner
#
# def wrapper2(func):
#     def inner(*args,**kwargs):
#         '''执行c代码'''
#         ret = func(*args,**kwargs)
#         '''执行d代码'''
#         return ret
#     return inner
#
# @wrapper1
# @wrapper2
# def func():pass

# a c func d b

# timmer login_model
# timmer logger

# 生成器和迭代器
# 迭代器 : iter next
# 可以被for循环 节省内存空间 它没有所谓的索引取值的概念 当前的值和下一个值- 公式
# 生成器和迭代器本质上是一样的
    # yield函数
        # 执行生成器函数 会得到一个生成器 不会执行这个函数中的代码
        # 有几个yield,就能从中取出多少个值
    # 生成器表达式
        # 生成器表达式也会返回一个生成器 也不会直接被执行
        # for循环里有几个符合条件的值生成器就返回多少值
    # 每一个生成器都会从头开始取值,当取到最后的时候,生成器中就没有值了
        # 一个生成器只能用一次
# def fff():
#     for i in range(10):
#         yield i
# g2 = (i**i for i in range(20))
# g = fff()
# print(next(g))
# print(next(g))
# print(next(g))

# print(next(fff()))
# print(next(fff()))
# print(next(fff()))
# for i in fff():
#     print(i)

# 如果现在明白 可以趁热打铁 先巩固一下
# 如果不明白 先放一放
    # 框架和项目 homework(计算器)(SQL模拟器)
    # 毕业的时候 找工作之前 再刷一次面试题
# 要相信计算是不会出错
# python11期

# 内置函数和匿名函数
# map filter sorted max min zip
# def func(n):
#     if n%2 == 0:
#         return True
# ret = filter(func,range(20))
# ret = filter(lambda n: True if n%2 == 0 else False ,range(20))
# ret = filter(lambda n: n%2 == 0 ,range(20))


# 常用模块
