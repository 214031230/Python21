#!/usr/bin/env python3
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age =age
#
#     def talk(self):
#         print("我叫%s今年%s岁" % (self.name,self.age))
#
#
# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def wang(self):
#         print("我叫%s今年%s岁" % (self.name, self.age))
#
#
# p1 = Person("xm",18)
# d1 = Dog("金毛",6)
# p1.talk()
# d1.wang()
#
# print(Person.__dict__)
# from math import pi
#
#
# class Yuan:
#     def __init__(self, r):
#         self.r = r
#
#     def mj(self):
#         """
#         求圆面积
#         :return: 圆面积
#         """
#         return pi * self.r ** 2
#
#     def zc(self):
#         """
#         求圆周长
#         :return: 圆周长
#         """
#         return 2 * pi * self.r
#
#
# class YH:
#     def __init__(self, outre_r, inner_r):
#         self.outer = Yuan(outre_r)
#         self.inner = Yuan(inner_r)
#
#     def mj(self):
#         return self.outer.mj() - self.inner.mj()
#
#     def zc(self):
#         return self.outer.zc() - self.inner.zc()
#
#
# yh1 = YH(10, 5)
# print(yh1.zc())
# y1 = Yuan(3)
# print(y1.mj())
# print(y1.zc())
# class YH(Yuan):
#     def __init__(self, r):
#         super().__init__(r)

# class Person:
#     COUNTRY = "中国"
#
#     def __init__(self, name, age, sex="男"):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def say(self):
#         print("""
#             个人信息
#             ---------
#             Name:%s
#             age :%s
#             sex :%s
#         """ % (self.name, self.age, self.sex))
#
#
# spf = Person("孙鹏飞", "18")
# spf.say()
# print(spf.COUNTRY)

#
# class Animal:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def hit(self):
#         print(self.name)
#
#
# class Person(Animal):
#     def __init__(self, name, age, sex, job):
#         super().__init__(name, age, sex)
#         self.job = job
#
#     def say(self):
#         print("%s说" % self.name)
#
#     def hit(self):
#         super().hit()
#
#
# class Dog(Animal):
#     def __init__(self, name, age, sex, bind):
#         super().__init__(name, age, sex)
#         self.bind = bind
#
#     def wang(self):
#         print("%s旺" % self.name)
#
#     def hit(self):
#         super().hit()


# p1 = Person("小米", 18, "男", "IT")
# d1 = Dog("啦啦啦", 3, "公", "金毛")
#
# p1.say()
# d1.wang()


# class A:
#     def func(self):
#         print("in A")
#
#
# class B(A):  # 单继承
#     def func(self):
#         print("in B")
#
#
# class C(A):
#     def func(self):
#         print("in C")
#
#
# class D(B, C):  # 多继承
#     def func(self):
#         print("in D")
#
#
# print(D.__bases__)
# print(D.mro())


# 类内方法的调用过程
# class Foo:
#     def __init__(self):  # 第二步 找到父类的__init__ 这时候self = s 即 Son类的对象
#         self.func()   # 第三步执行父类s.func()
#
#     def func(self):
#         print('in Foo')
#
#
# class Son(Foo):
#     def func(self):  # 第四步 执行func方法
#         print('in son')
#
#
# s = Son()  # 实例化类，第一步去执行__init__函数由于Son没有__init__,会去父类找__init__


# class Foo:
#     def __init__(self):  # 第二步 找到父类的__init__ 这时候self = s 即 Son类的对象
#         self.__func()    # 第三步 类在定义的过程中已经把私有属性变形为 self._Foo__func
#                          # 第四步 执行self._Foo__func
#
#     def __func(self):   # 类在定义的时候变形为 _Foo__func
#         print('in Foo')
#
#
# class Son(Foo):
#     def __func(self):    # _Son__func
#         print('in son')
#
#     def start(self):
#         self.__func()


# s = Son()  # 实例化类，第一步去执行__init__函数由于Son没有__init,会去父类找__init__

#
# class Person:
#     country = "chain"
#
#     @classmethod
#     def say(cls):
#         print(cls.country)
#
#     @staticmethod
#     def static():
#         print("我是静态方法")
#
#
# p = Person()
# p.say()
# p.static()
# Person.static()
# Person.say()


#
# from math import pi
# class Yuan:
#     def __init__(self, r):
#         self.r = r
#     @property
#     def mj(self):
#         """
#         求圆面积
#         :return: 圆面积
#         """
#         return pi * self.r ** 2
#     @property
#     def zc(self):
#         """
#         求圆周长
#         :return: 圆周长
#         """
#         return 2 * pi * self.r
#
#
# y = Yuan(2)
# print(y.zc)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def say():
        print("in say")

    def talk(self):
        print("%s in talk" % self.name)


# while 1:
#     fun = input(">>>:").strip()
#     p = Person("spf", 18)
#     if hasattr(p, fun):
#         getattr(p, fun)()
def fun():
    print("in fun")


import sys

# print(sys.modules[__name__])

# getattr(sys.modules[__name__], "fun")()
p = Person("name", 18)
setattr(p, "name", "wxx")


# print(p.name)

class Foo:
    def __new__(cls, *args, **kwargs):
        print('执行我啦')
        obj = object.__new__(cls)
        print(obj)
        return obj

    def __init__(self):
        print('1', self)


# Foo()

# class Person:
#     __isinstance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__isinstance:
#             obj = object.__new__(cls)
#             cls.__isinstance = obj
#         return cls.__isinstance
#
#     def __init__(self, name):
#         self.name = name
#
#
# p = Person("spf")
# print(id(p))
# p1 = Person("wxx")
# print(id(p1))


class Person:
    __isinstance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__isinstance:
            obj = object.__new__(cls)
            cls.__isinstance = obj
        return cls.__isinstance

    def __init__(self, name):
        self.name = name


#
# p = Person("spf")
# p1 = Person("wxx")
# print(p.name, p1.name)


import json

dic = {"name": "spf"}
# sdic = json.dumps(dic)
# print(sdic, type(sdic))
# print(json.loads(sdic))

# with open("db.json","a",encoding="utf-8") as f, open("db.json", "r", encoding="utf-8") as f1:
# with open("db.json") as f1:
#     print(json.load(f1))

# with open("db.json","a",encoding="utf-8") as f:
#     for i in range(10):
#         ret = json.dumps(dic)
#         f.write(ret+"\n")
#
# with open("db.json", encoding="utf-8") as f:
#     for j in f:
#         print(json.loads(j.strip()))
import pickle

# ret = {}
# with open("db.pkl", "rb") as f, open("db.pkl", "ab") as f1:
#     ret["spf"] = p
#     ret["wxx"] = p2
#     pickle.dump(ret, f1)
#     # try:
#     ret = pickle.load(f)
#     print(ret)
# except EOFError:
#     pass


# ret = pickle.dumps(p)
# print(pickle.loads(ret))
# with open("db.pkl", "ab") as f:
#     pickle.dump(p, f)


p = Person("spf")
p2 = Person("wxx")

# class MyPickle:
#     @staticmethod
#     def load(file_path):
#         with open(file_path, "rb") as f:
#             return pickle.load(f)
#
#     @staticmethod
#     def dump(obj, file_path):
#         with open(file_path, "wb") as f:
#             pickle.dump(obj, f)
#
#
# MyPickle.dump(p, "db.pkl")
# ret = MyPickle.load("db.pkl")
# print(ret.name)


# import hashlib
# # 普通md5加密
# md5obj = hashlib.md5()
# md5obj.update("123".encode("utf-8"))
# print(md5obj.hexdigest())
#
# # 加盐
# md5obj = hashlib.md5("spf".encode("utf-8"))
# md5obj.update("123".encode("utf-8"))
# print(md5obj.hexdigest())
#
# # 动态加盐
# username = "spf"
# md5obj = hashlib.md5(username.encode("utf-8"))
# md5obj.update("123".encode("utf-8"))
# print(md5obj.hexdigest())
import hashlib


class Login:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.__code = "utf-8"

    def __encryption(self):
        """
        mad5加密（动态加盐）
        :return: 加密后的密码
        """
        md5obj = hashlib.md5(self.username.encode(self.__code))
        md5obj.update(self.__password.encode(self.__code))
        return md5obj.hexdigest()

    def login(self):
        """
        登录
        :return: 返回登录状态
        """
        status = True if self.username == "spf" and self.__encryption() == "6b783000a3177ac09ae3706a077d6d80" else False
        return status


# while 1:
#     username = input("User:").strip()
#     password = input("Password:").strip()
#     p = Login(username, password)
#     print(p.login())


# file1 = "./day3.py"
# file2 = "./day4.py"
#
#
# def check_file(file1,file2):
#     """
#     校验文件MAD5
#     :param file1:  第一个文件
#     :param file2:  第二个文件
#     :return: True or False
#     """
#     with open(file1, "rb") as f, open(file2, "rb") as f1:
#         md5obj1 = hashlib.md5()
#         md5obj2 = hashlib.md5()
#         for i in f:
#             md5obj1.update(i)
#         for j in f1:
#             md5obj2.update(j)
#
#         if md5obj1.hexdigest() == md5obj2.hexdigest():
#             return True
#         else:
#             return False
#
# ret = check_file(file1,file2)
# print(ret)


# md5obj = hashlib.md5()
# md5obj.update("123".encode("utf-8"))
# print(md5obj.hexdigest())
# md5obj = hashlib.md5()
# md5obj.update("123".encode("utf-8"))
# print(md5obj.hexdigest())
# try:
#     msg = int(input(">>>:").strip())
#     print(msg)
# except ValueError as e:
#     print(e)
#     print("你输入不是数字！")
# except Exception as e:
#     print(e)
# else:  # 代码顺利结束执行
#     print("代码顺利结束")
# finally:  # 无论如何都执行
#     print("结束了")


# import sys
# print(__file__)
# print(sys.modules[__name__])

# from sys import path as sys_path
# from os import path
# sys_path.insert(0, path.dirname(path.abspath(__file__)))
# from 复习1 import day3
# print(day3.add(3,3))
# print(sys_path)


