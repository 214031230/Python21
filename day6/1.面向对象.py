#!/usr/bin/env python3
# 一切皆对象
# 类
# 新式类
    # 在py3中所有类都是新式类
# 经典类
    # 在py2中只有类本身继承了object类才叫做新式类，默认是经典类

# 声明类
# class Person:
#     country = "中国"  # 静态属性
#
#     def __init__(self, name, age, sex):  # 初始化对象  在实例化时自动将对象/实例本身传给__init__的第一个参数。
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def eat(self):  # 动态属性或方法
#         return "%s在吃饭" % self.name
# 访问类的属性
# print(Person.country)
# print(Person.__dict__)  # 查看类具有的属性和方法

# 实例化 实例化会自动执行__init__方法，可以用它来为每个实例对象定制自己的特征
# spf = Person("spf", 18, "男")  # 类名() 就等于在执行Person.__init__(),执行完__init__()就会返回一个对象。这个对象类似一个字典，存着属于这个人本身的一些属性和方法。

# 访问类的属性和方法
# print(Person.eat(spf))
# print(spf.eat())

# 人狗大战
class Person:
    def __init__(self, name, sex, hp, dps, bag=[]):
        """
        人的特性
        :param name:  昵称
        :param sex: 年龄
        :param hp: 血量
        :param dps: 攻击力
        :param bag: 背包
        """
        self.name = name
        self.sex = sex
        self.hp = hp
        self.dps = dps
        self.bag = bag

    def hit(self, dog):
        """
        方法：人打狗
        :param dog: 实例化的狗
        :return:
        """
        dog.hp -= self.dps
        print("Info：{0}打了{1},{1}掉了{2}血，剩余{3}血".format(self.name, dog.name, self.dps, dog.hp))

class Dog:
    def __init__(self, name, kind, hp, dps):
        """
        人的特性
        :param name:  昵称
        :param kind: 品种
        :param hp: 血量
        :param dps: 攻击力
        """
        self.name = name
        self.kind = kind
        self.hp = hp
        self.dps = dps

    def hit(self, person):
        """
        方法：狗咬人
        :param person: 实例化后的人
        :return:
        """
        person.hp -= self.dps
        print("Info：{0}咬了{1},{1}掉了{2}血，剩余{3}血".format(self.name, person.name, self.dps, person.hp))


alex = Person("金角大王", "男", 5000, 300)
hsq = Dog("旺财", "哈士奇", 50000, 500)

alex.hit(hsq)  # Info：金角大王打了旺财,旺财掉了300血，剩余49700血
hsq.hit(alex)  # Info：旺财咬了金角大王,金角大王掉了500血，剩余4500血

print(alex.hp)  # 4500
print(hsq.hp)  # 47900


# 类实现圆面积
from math import pi
class Yuan:
    def __init__(self,r):
        """
        圆的属性
        :param r: 半径
        """
        self.r = r
    def mj(self):
        """
        求圆面积方法
        :return: 圆面积
        """
        return pi * self.r ** 2
    def zj(self):
        """
        求圆的周长
        :return: 圆周长
        """
        return 2 * pi * self.r
yuna1 = Yuan(5)
print(yuna1.mj())


