#!/usr/bin/env python3
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def call(self):
#         print("call%s" %self.name)
#
# p1 = Person("alex")
# choice = input(">>>:")
#
# getattr(p1, choice)() # getattr(p1, choice) =  p1.call
import pickle
class Porson:
    def __init__(self, name):
        self.name = name

p1 = Porson("wxx")
with open("test.pkl", "ab") as f1:
    pickle.dump(p1, f1)

with open("test.pkl", "rb") as f1:
    for i in f1:
        ret = pickle.load(f1)
        print(ret)





