#!/usr/bin/env python3
# 面向对象的3大特性
# 1、继承
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
        """
        人的特性
        :param name:  昵称
        :param sex: 年龄
        :param hp: 血量
        :param dps: 攻击力
        :param bag: 背包
        """
        # Animal.__init__(name, hp, dps)
        super().__init__(name, hp, dps)
        self.sex = sex
        self.bag = bag


class Dog(Animal):
    def __init__(self, name, kind, hp, dps):
        """
        人的特性
        :param name:  昵称
        :param kind: 品种
        :param hp: 血量
        :param dps: 攻击力
        """
        super().__init__(name, hp, dps)
        self.kind = kind


alex = Person("金角大王", "男", 5000, 300)
hsq = Dog("旺财", "哈士奇", 50000, 500)

alex.hit(hsq)  # Info：金角大王打了旺财,旺财掉了300血，剩余49700血
hsq.hit(alex)  # Info：旺财咬了金角大王,金角大王掉了500血，剩余4500血

print(alex.hp)  # 4500
print(hsq.hp)  # 47900
# 2、多态
# 3、封装