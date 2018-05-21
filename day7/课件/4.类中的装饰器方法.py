# classmethod staticmethod property
# 三个装饰器函数
# 圆形类
# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#
#     @property
#     def area(self):
#         return self.r ** 2 * pi
#
#     @property
#     def perimeter(self):
#         return self.r * 2 * pi
#
# # 方法 动词 —— 动作或者技能
# # 名词 圆的面积 圆的周长 圆的班级
# # 将一个函数伪装成为属性 @property
#
# c = Circle(3)
# print(c.area)
# print(c.perimeter)

# property __私有的名字

# class Goods:
#     def __init__(self,price,discount):
#         self.__price = price
#         self.discount = discount
#     @property
#     def price(self):
#         return self.__price * self.discount
#     @price.setter
#     def price(self,newprice):
#         self.__price = newprice
#     @price.deleter
#     def price(self):
#         del self.__price
# apple = Goods(8,0.7)
# print(apple.price)
# apple.price = 10
# print(apple.price)
# print(apple.__dict__)
# del apple.price
# print(apple.__dict__)
# print(apple.price)

# class Person:
#     Country = '中国人'
#     @classmethod       #把func变成了一个类方法
#     def func(cls):     # cls是指向类的内存空间
#         print('当前的角色的国籍是%s'%cls.Country)

# alex = Person()
# alex.func()
# Person.func()
# 如果某一个类中的方法 并没有用到这个类的实例中的具体属性
# 只是用到了类中的静态变量 就使用类方法


# 如果 一个方法 既不会用到对象中的属性也不会用到类中的属性
# 就应该被定义为一个静态方法

# class Person:
#     Country = '中国人'
#     @classmethod       #把func变成了一个类方法
#     def func(cls):     # cls是指向类的内存空间
#         print('当前的角色的国籍是%s'%cls.Country)
class Student:
    @staticmethod
    def login():
        name = input('name : ')
        pwd = input('pwd : ')
        if name =='' and pwd =='':
            print('实例化')

Student.login()