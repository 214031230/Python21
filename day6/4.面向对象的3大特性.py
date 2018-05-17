#!/usr/bin/env python3
# 面向对象的3大特性
# 1、继承
# 继承的定义：继承是一种创建新类的方式，在python中，新建的类可以继承一个或多个父类，父类又可称为基类或超类，新建的类称为派生类或子类
# 继承的作用：1、减少代码的重用 2、提高代码可读性 3、规范编程模式
# 抽象：抽象即抽取类似或者说比较像的部分。是一个从具题到抽象的过程。
# 继承：子类继承了父类的方法和属性
# 派生：子类在父类方法和属性的基础上产生了新的方法和属性

# 人和狗都属于动物
class Animal:
    def __init__(self, name, hp, dps):
        """
        动物的属性
        :param name: 昵称
        :param hp: 血量
        :param dps: 攻击力
        """
        self.name = name
        self.hp = hp
        self.dps = dps

    def hit(self,argv):
        argv.hp -= self.dps
        print("Info：{0}打了{1},{1}掉了{2}血，剩余{3}血".format(self.name, argv.name, self.dps, argv.hp))

class Person(Animal):
    def __init__(self, name, sex, hp, dps, bag=[]):
        # Animal.__init__(name, hp, dps)
        super().__init__(name, hp, dps)
        self.sex = sex
        self.bag = bag


class Dog(Animal):
    def __init__(self, name, kind, hp, dps):
        super().__init__(name, hp, dps)
        self.kind = kind


alex = Person("金角大王", "男", 5000, 300)
hsq = Dog("旺财", "哈士奇", 50000, 500)

alex.hit(hsq)  # Info：金角大王打了旺财,旺财掉了300血，剩余49700血
hsq.hit(alex)  # Info：旺财咬了金角大王,金角大王掉了500血，剩余4500血

print(alex.hp)  # 4500
print(hsq.hp)  # 47900

# 钻石继承  py3中广度优先 py2中深度优先
class A:
    def func(self):
        print("in A")
class B(A):  # 单继承
    def func(self):
        print("in B")
class C(A):
    def func(self):
        print("in C")
class D(B, C):  #  多继承
    def func(self):
        print("in D")
print(D.__bases__)
print(D.mro())  # 查看类的继承顺序

# super
# 在python3中，子类执行父类的方法也可以直接用super方法.
class A:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    def func(self):
        print("in A")
class B(A):
    def __init__(self, name, sex, add):
        # A.__init__(name,sex)
        super().__init__(name, sex)
        self.add = add
    def func(self):
        super().func()
obj = B("spf","男","HN")
obj.func()
print(obj.__dict__)

# 2、多态
# 3、封装