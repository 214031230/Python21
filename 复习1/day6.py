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
