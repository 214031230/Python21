#!/usr/bin/env python3
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

class Wuqi:
    def __init__(self, name, dps, price):
        """
        武器的属性
        :param name: 名称
        :param dps: 攻击力
        :param price: 价格
        """
        self.name = name
        self.dps = dps
        self.price = price
    def baozi(self,dog):
        """
        武器：毒包子
        :param dog:  狗对象
        :return:
        """
        dog.hp -= self.dps
        print("%s吃了%s掉了%s血剩余%s血" % (dog.name, self.name, self.dps, dog.hp))


roubaozi = Wuqi("肉包子", 5000, 3000)
alex = Person("金角大王", "男", 5000, 300, [5000])
hsq = Dog("旺财", "哈士奇", 50000, 500)

if alex.bag[0] >= roubaozi.price:
    alex.wuqi = roubaozi
    alex.wuqi.baozi(hsq)

# 求圆环面积和周长
from math import pi
class Yuan:
    """
    圆面积和圆周长
    """
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

class Yuanhuan:
    """
    圆环的面积和周长
    """
    def __init__(self, outer_r, inner_r):
        """
        圆环的属性
        :param outer_r: 大圆的半径
        :param inner_r: 小圆的半径
        """
        self.outer = Yuan(outer_r)
        self.inner = Yuan(inner_r)
    def yh_mj(self):
        """
        求圆环的面积，大圆-小圆
        :return:
        """
        return self.outer.mj() - self.inner.mj()
    def yh_zc(self):
        """
        求圆环的周长
        :return:
        """
        return self.outer.zj() + self.inner.zj()

yh1 = Yuanhuan(10, 5)
print(yh1.yh_mj())
print(yh1.yh_zc())