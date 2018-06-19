#!/usr/bin/env python3
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         print("%s说:你好" % self.name)
#
#
# xiaoming = Person("小米", 30)
# xiaoming.talk()
# from math import pi
#
#
# class Yuan:
#     def __init__(self, r):
#         self.r = r
#         self.pi = pi
#
#     def mj(self):
#         return self.pi*self.r**2
#
#     def zc(self):
#         return self.pi*self.r*2
#
#
# class YuanHuan:
#     def __init__(self, outer_r, inner_r):
#         self.outer = Yuan(outer_r)
#         self.inner = Yuan(inner_r)
#
#     def mj(self):
#         return self.outer.mj() - self.inner.mj()
#
#     def zc(self):
#         return self.outer.zc() - self.inner.zc()
#
#
# yh1 = YuanHuan(5, 3)
# print(yh1.mj())
#
# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# class Person(Animal):
#     def __init__(self,name,age,eat):
#         super().__init__(name,age)
#         self.eat = eat
#
# p = Person(1,2,3)
# print(p.__dict__)

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
# s = Son()  # 实例化类，第一步去执行__init__函数由于Son没有__init,会去父类找__init__
# 类内私有方法的调用过程
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
#
#
# s = Son()  # 实例化类，第一步去执行__init__函数由于Son没有__init,会去父类找__init__
# s.start()
# import hashlib
#
#
# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.__password = password
#
#     def __md5(self):
#         md5obj = hashlib.md5()
#         md5obj.update(self.__password.encode("utf-8"))
#         return md5obj.hexdigest()
#
#     def login(self):
#         if self.name == "spf" and self.__md5() == "202cb962ac59075b964b07152d234b70":
#             return "登录成功！"
#
#
# spf = User("spf", "123")
# print(spf.login())


