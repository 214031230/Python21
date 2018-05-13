#!/usr/bin/env python3
class Person:
    person = "人"
    name = "wxx"  # 当init对象命名空间中没有name的时候会找类命名空间中的name
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
p1 = Person("spf", 18, "男")
print(p1.name)
