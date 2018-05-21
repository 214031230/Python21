#!/usr/bin/env python3
# 什么叫反射？
# 通过字符串数据类型的 变量名 来访问变量的值
# x.y 这样的形式 都可以用反射
# 类名 反射 静态属性

class Foo:
    country = "中国"
obj = Foo()
print(getattr(obj, "country"))

# 对象名 反射 对象属性 和 方法
class Foo:
    country = "中国"
    def __init__(self,name):
        self.name = name
    def func(self):
        print("%s in func" %self.name)
obj = Foo("spf")
getattr(obj, "func")()


# 模块 反射 模块中的名字
import sys
from  mypickle import MyPickle
choice = input(">>>：")
getattr(MyPickle, choice)(obj, "test.pkl")


# 反射 自己所在文件中的名字
from  mypickle import MyPickle
choice = input(">>>：")
ret = getattr(sys.modules[__name__], choice)
ret.dump(obj, "test.pkl")
print(ret.load("test.pkl"))

# 首先 使用getattr取获取一个名字，如果在这个对象的命名空间中没有这个名字 会报错
# getattr的反射好伴侣 hasattr
# 如果使用getattr取获取一个方法，那么只能拿到这个方法的内存地址 加上括号就是执行，当然，括号里的参数可以照传不误
# 如果getattr获取一个属性，那么直接使用反射就可以获取到值


# __new__    构造方法 创建一个对象
# __init__   初始化方法

class Foo:
    def __new__(cls, *args, **kwargs):
        print('执行我啦')
        obj = object.__new__(cls)
        print(obj)
        return obj
    def __init__(self):
        print('1', self)

Foo()

# 先执行new方法，object.new()
# 再执行init

# Foo()  --> python解释器接收到你的python代码
# python解释器替你去做了很多操作
# 包括 主动帮助你 调用 new方法 去创造一个对象 —— 开辟内存空间 —— python语言封装了开辟内存的工作
# object的new方法里 —— 帮你创造了对象
# 调用init用到的self参数 就是new帮你创造的对象

# 什么叫单例模式
# 单例模式 ： 某一类 只有一个实例

class Person:
    __isinstance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__isinstance :
            obj = object.__new__(cls)
            cls.__isinstance = obj
        return cls.__isinstance
    def __init__(self,name):
        self.name = name

alex = Person('alex')
alex.age = 18
egon = Person('egon')
print(egon.age)
print(id(alex))
print(id(egon))
print(alex.name)
print(egon.name)

# __new__生孩子
# 类 ： 生一个小孩__new__ 给这个小孩穿衣服 __init__
# 单例模式下的类 ： 只有一个小孩

# class Person:
#     def __init__(self,name):
#         self.name = name
#     def __str__(self):
#         return 'a object of Person named %s'%self.name
#     # def __hash__(self):
#     #     return 1231212
#     # def __len__(self):
#     #     return 10
# a = Person('alex')
# b = Person('egon')
# # print(len(a))
# # print(hash(a))
# print(a)
# print(b)
# 类中的内置方法 很多都和 内置函数相关

# l = list([1,2,3])   # 实例化
# print(l)