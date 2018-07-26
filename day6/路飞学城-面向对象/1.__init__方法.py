#!/usr/bin/env python3
# 面向过程语言：流程化编程，实现一个功能在进行下一个功能
    # 优点：复杂事情简单化
    # 缺点：扩展性差
# 面向对象语言：
    # 优点：扩展性好
    # 缺点：编程难度高

# 现实世界中：先有对象在有类
# 代码世界中：先有类在有对象
# 站的角度不同定义类也不同
# 定义类不需要调用会执行类中的代码


# 对象：特征与技能的结合体
# 类：一系列对象相似的特征与技能的结合体
# class Person:
#     def talk(self):
#         print("in talk")
#     print("==run==")
#
# # 调用类会返回一个对象
# spf = Person()
# print(type(spf))  # <class '__main__.Person'>
# print(Person.__dict__)  # 查看类的名称空间
# print(spf.__dict__) # 查看对象的名称空间
#
# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def jiao(self):
#         print("%s叫" % self.name)
# h2 = Dog("哈士奇") # 相当于 Dog.__init__(h2, "哈士奇")
# print(Dog.__dict__)  # 查看类的名称空间
# print(h2.__dict__)  # 查看对象的名称空间
#
# # 增
# h2.kind = "藏獒"
# print(h2.__dict__)
# # 删
# del h2.name
# print(h2.__dict__)
# # 改
# h2.kind = "雪橇"
# print(h2.kind)
# # 查
# print(h2.__dict__["kind"])

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print("%s说：" % self.name)


# p1 = Person("spf")
# p2 = Person("wxx")
#
# print(p1.talk)
# print(p2.talk)

# def sq11(host,name,pwd,db.json,sql):
#     print("增加SQL")
# def sq12(host,name,pwd,db.json,sql2):
#     print("删除SQL")
#
# class Sql:
#     def __init__(self, host, name, pwd, db.json):
#         self.host = host
#         self.name = name
#         self.pwd = pwd
#         self.db.json = db.json
#     def sql_add(self,sql):
#         print("增加sql%s" % sql)
#     def sql_dql(self,sql):
#         print("删除sql %s" % sql)
# s1 = Sql("192.168.1.1","root","123","test")
# s1.sql_add("select *")
# s1.sql_dql("del *")



# 统计实例化对象的个数

#
# class Person:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Person.count += 1
#
#
# # p1 = Person("alex")
# # p2 = Person("spf")
# # p3 = Person("wxx")
# # print(Person.count)
#
# # 王者荣耀游戏
#
# class Yingxiong:
#     kind = "英雄"
#     def __init__(self, name, hp, dps):
#         self.name = name
#         self.hp = hp
#         self.dps = dps
#
#     def kill(self,jiaose):
#         jiaose.hp -= self.dps
#
#
# class Yeguai:
#     kind = "野怪"
#     def __init__(self, name, hp, dps):
#         self.name = name
#         self.hp = hp
#         self.dps = dps
#
#     def kill(self,jiaose):
#         jiaose.hp -= self.dps
#
# yase = Yingxiong("亚瑟", 100,20)
# lbb = Yeguai("蓝爸爸", 50, 10)
# print(lbb.hp)
# yase.kill(lbb)
# print(lbb.hp)


