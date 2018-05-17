#!/usr/bin/env python3
# import os
# sums = 0
# def func(dirs):
#     global sums
#     file_list = os.listdir(dirs)
#     for i in file_list:
#         if os.path.isdir(os.path.join(dirs, i)):
#             return func(os.path.join(dirs, i))
#         else:
#             print("%s:%s" % (os.path.join(dirs, i), os.path.getsize(os.path.join(dirs, i))))
#             sums += os.path.getsize(os.path.join(dirs, i))
#     return sums
# print(func("../day5"))


# def Person(name, sex, hp, dps):
#     dic = {"name": name, "sex": sex, "hp": hp, "dps": dps}
#     def attack(dog):
#         dog["hp"] -= dic["hp"]
#         print("%s打了%s,%s掉了%s的血,%s剩余了%s的血" % (dic["name"], dog["name"], dog["name"], dic["dps"], dog["name"], dog["hp"]))
#     dic["attack"] = attack
#     return dic
#
#
# def Dog(name, kind, hp, dps):
#     dic = {"name": name, "kind": kind, "hp": hp, "dps": dps}
#     def yao(person):
#         person["hp"] -= dic["hp"]
#         print("%s咬了%s,%s掉了%s的血,%s剩余了%s的血" % (dic["name"], person["name"], person["name"], dic["dps"], person["name"], person["hp"]))
#     dic["yao"] = yao
#     return dic
#
#
# alex = Person("alex", "男", 150, 5)
# dog1 = Dog("旺财", "藏獒", 200, 100)
#
# alex["attack"](dog1)
# print(dog1)
# dog1["yao"](alex)
# print(alex)

# class Person:
#     def __init__(self, name, sex, hp, dps):
#         self.name = name
#         self.sex = sex
#         self.hp = hp
#         self.dps = dps
#
#     def attack(self, dog):
#         dog.hp -= self.dps
#         print("%s打了%s,%s掉了%s的血,%s剩余了%s的血" % (self.name, dog.name, dog.name, self.dps, dog.name, dog.hp))
#
#
# class Dog:
#     def __init__(self, name, kind, hp, dps):
#         self.name = name
#         self.kind = kind
#         self.hp = hp
#         self.dps = dps
#
#     def yao(self, person):
#         person.hp -= self.dps
#         print("%s咬了%s,%s掉了%s的血,%s剩余了%s的血" % (self.name, person.name, person.name, self.dps, person.name, person.hp))
#
#
# alex = Person("alex", "男", 500, 10)
# dog1 = Dog("二哈", "藏獒", 1000, 200)
# dog1.yao(alex)
# print(alex.__dict__)
# # 属性的查
# print(alex.dps)
# # 属性的修改
# alex.name = "alex2"
# # 属性的增加
# alex.bag = []
# print(alex.__dict__)
# # 属性的删除
# del alex.bag
# print(alex.__dict__)


# class Yuan:
#     def __init__(self, r, pai=3.14):
#         self.r = r
#         self.pai = pai
#
#     def mj(self):
#         return self.pai * self.r ** 2
#
#     def zc(self):
#         return self.pai * self.r * 2
#
#
# y1 = Yuan(3)
# y1.mj()  # Yuan.mj(y1)
#
#
# class Yuanhuan:
#     def __init__(self, outer_r, inner_r):
#         self.outer = Yuan(outer_r)
#         self.inner = Yuan(inner_r)
#
#     def mj(self):
#         return self.outer.mj() - self.inner.mj()
#
#     def zc(self):
#         return self.outer.zc() + self.inner.zc()
#
#
# ret = Yuanhuan(10, 5)
# print(ret.mj())
# print(ret.zc())
# 批量移动文件
# import os,shutil
# for i in os.listdir("课件"):
#     if "png" in i:
#         print(i)
#         shutil.move("课件/%s" % i, "课件/图/")

# class Person:
#     def __init__(self, name, hp, dps):
#         self.name = name
#         self.hp = hp
#         self.dps = dps
#
#     def hit(self, dog):
#         dog.hp -= self.dps
#         print("%s打了%s.%s掉了%s血,还剩余%s的血" % (self.name,dog.name,dog.name,self.dps,dog.hp ))
#
#
# class Dog:
#     def __init__(self, name, hp, dps):
#         self.name = name
#         self.hp = hp
#         self.dps = dps
#
#     def yao(self,person):
#         person.hp -= self.dps
#         print("%s打了%s.%s掉了%s血,还剩余%s的血" % (self.name,person.name,person.name,self.dps,person.hp))
#
# h2 = Dog("哈士奇",5000,500)
# p1 = Person("alex", 1000, 200)
# h2.yao(p1)
# p1.hit(h2)
# class Animal:
#     def __init__(self, name, hp, dps):
#         self.name = name
#         self.hp = hp
#         self.dps = dps
#
#     def hit(self, ani):
#         ani.hp -= self.dps
#         print("%s打了%s.%s掉了%s血,还剩余%s的血" % (self.name,ani.name,ani.name,self.dps,ani.hp ))
#
#
# class Person(Animal):
#     def kill(self, dog):
#         dog.hp -= 2000
#         print("%s打了%s.%s掉了%s血,还剩余%s的血" % (self.name, dog.name, dog.name, self.dps, dog.hp))
#
#
# class Dog(Animal):
#     def __init__(self, name, hp, dps, kind):
#         super().__init__(name, hp, dps)
#         self.kind = kind
#
#
# h2 = Dog("哈士奇",5000,500,"藏獒")
# p1 = Person("alex", 1000, 200)
# h2.hit(p1)
# p1.hit(h2)
# p1.kill(h2)
# print(h2.kind)
# from cmath import pi
# class Yuan:
#     def __init__(self,r):
#         self.r = r
#     def mj(self):
#         return pi * self.r ** 2
#
# class Yuanhuan:
#     def __init__(self, outer_r, inner_r):
#         self.outer = Yuan(outer_r)
#         self.inner = Yuan(inner_r)
#
#     def mj(self):
#         return self.outer.mj() - self.inner.mj()
#
# y1 = Yuanhuan(5,3)
# print(y1.mj())
# class Animal:
#     def __init__(self, name, hp, dps):
#         self.name = name
#         self.hp = hp
#         self.dps = dps
#
#     def hit(self, ani):
#         ani.hp -= self.dps
#         print("%s打了%s.%s掉了%s血,还剩余%s的血" % (self.name,ani.name,ani.name,self.dps,ani.hp ))
#
# class Person(Animal):
#     def kill(self, dog):
#         dog.hp -= 2000
#         print("%s打了%s.%s掉了%s血,还剩余%s的血" % (self.name, dog.name, dog.name, self.dps, dog.hp))
#
#
# class Dog(Animal):
#     def __init__(self, name, hp, dps, kind):
#         super().__init__(name, hp, dps)
#         self.kind = kind
#
# class Wuqi:
#     def __init__(self, name, dps):
#         self.name = name
#         self.dps = dps
#     def dao(self,dog):
#         dog.hp -= 2000
#         print("%s打了%s.%s掉了%s血,还剩余%s的血" % (self.name, dog.name, dog.name, self.dps, dog.hp))
#
#
#
#
# h2 = Dog("哈士奇",5000,500,"藏獒")
# w1 = Wuqi("肉包子", 2000)
# p1 = Person("alex", 1000, 200)
# p1.wuqi = w1
# p1.wuqi.dao(h2)


# class A:
#     def func(self):
#         print("in A")
#
#
# class B(A):
#     def func(self):
#         print("in B")
#
#
# class C(A):
#     def func(self):
#         print("in C")
#
#
# class D(B):
#     def func(self):
#         print("in D")
#
#
# class E(C,D):
#     def func(self):
#         print("in E")
#
#
# DBCA
# print(E.mro())

# import shelve
# f = shelve.open("test.she")
# f["name"] = ["孙鹏飞"]
#
# print(f["name"])
# f.close()
# import re
# s = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
# print(s.replace(" ", ""))
# print(re.findall("\([^()]+\)", s))
# print(re.findall("", s))

# re1 = re.compile("\([^()]+\)")
# print(re1.search(s))

# class Animal:
#     name = "动物"
#
#     def __init__(self, name):
#         pass
#         # self.name = name
#
#     def talk(self):
#         print("%s说：我是动物！" % self.name)
#
#
# class Person(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         # self.name = name
#
#     def talk(self):
#         # print("%s说：我是人！" % self.name)
#         super().talk()
#
# spf = Person("孙鹏飞")
# spf.talk()






























