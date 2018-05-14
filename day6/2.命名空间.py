#!/usr/bin/env python3
# 创建一个类就会创建一个类的名称空间，用来存储类中定义的所有名字，这些名字称为类的属性
# 静态属性就是直接在类中定义的变量
# 动态属性就是定义在类中的方法
#
# 创建一个对象/实例就会创建一个对象/实例的名称空间，存放对象/实例的名字，称为对象/实例的属性
# 在obj.name会先从obj自己的名称空间里找name，找不到则去类中找，类也找不到就找父类...最后都找不到就抛出异常

class Person:
    person = "人"
    name = "wxx"  # 当init对象命名空间中没有name的时候会找类命名空间中的name
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
p1 = Person("spf", 18, "男")
print(p1.name)
