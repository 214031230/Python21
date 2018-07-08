#!/usr/bin/env python3
# 三个装饰器函数
# classmethod
# 如果某一个类中的方法 并没有用到这个类的实例中的具体属性，只是用到了类中的静态变量就使用类方法


class Person:
    Country = '中国人'

    @classmethod       #把func变成了一个类方法
    def func(cls):     # cls是指向类的内存空间
        print('当前的角色的国籍是%s'% cls.Country)


alex = Person()
alex.func()
Person.func()

# staticmethod
# 如果 一个方法 既不会用到对象中的属性也不会用到类中的属性就应该被定义为一个静态方法


class Student:
    @staticmethod
    def login():
        name = input('name : ')
        pwd = input('pwd : ')
        if name == "" and pwd == "":
            print('实例化')

# Student.login_model()


# property
# 将一个函数伪装成为属性，在面向对象中动作被称为方法，但有些时候一些名词也用作方法。为了严谨可以把名词函数修改成属性


# 示例1：圆形类
# 方法 动词 —— 动作或者技能
# 名词 圆的面积 圆的周长 圆的半径
# 将一个函数伪装成为属性 @property
from math import pi
class Circle:
    def __init__(self,r):
        self.r = r

    @property
    def area(self):
        return self.r ** 2 * pi

    @property
    def perimeter(self):
        return self.r * 2 * pi



c = Circle(3)
print(c.area)
print(c.perimeter)

# 示例2：property 在__私有属性中的应用


class Goods:
    """计算商品打折后的价格"""
    def __init__(self, price, discount):
        self.__price = price  # 价格为私有属性
        self.discount = discount

    @property
    def price(self):
        """
        计算商品打折后的价格
        :return: 返回打折后的价格
        """
        return self.__price * self.discount

    @price.setter
    def price(self, newprice):
        """
        修改商品的价格
        :param newprice:
        :return:
        """
        self.__price = newprice

    @price.deleter
    def price(self):
        """
        删除商品的价格
        :return:
        """
        del self.__price


apple = Goods(8, 0.7)  # 实例化一个苹果对象
print(apple.price)
apple.price = 10    # 修改苹果的价格，私有属性无法修改。所以用到了property
print(apple.price)
print(apple.__dict__)
del apple.price
print(apple.__dict__)
print(apple.price)

import abc


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def sleep(self):
        pass


class Dog(Animal):
    def eat(self):
        pass

    def sleep(self):
        pass

d1 = Dog()

