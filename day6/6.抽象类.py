#!/usr/bin/env python3
# 子类继承父类，必须使用父类方法的名称。目的是实现方法名统一
import abc
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass

class Dog(Animal):
    def run(self):
        print("in runing")

D1 = Dog()
D1.run()