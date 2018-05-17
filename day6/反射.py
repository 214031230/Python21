#!/usr/bin/env python3
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def call(self):
#         print("我是反射%s" %self.name)
#
# p1 = Person("alex")
# choice = input(">>>:")
# # p1.choice()
#
# getattr(p1, choice)() # getattr(p1, choice) =  p1.call
# import pickle
#
# class Porson:
#     def __init__(self, name):
#         self.name = name
#
#
# p1 = Porson("wxx")
# with open("test.pkl", "ab") as f1:
#     pickle.dump(p1, f1)
#
# with open("test.pkl", "rb") as f1:
#     for i in f1:
#         ret = pickle.load(f1)
#         print(ret)





# import json
#
# class A:
#     def func(self):
#         print("in A")
# dic = {1:2}
#
# # f = open("test.json", "w")
# # json.dump(A, f)
# # f.close()
#
# # f2 = open("test.json", "r")
# # ret = json.load(f2)
# # f2.close()
# # print(type(ret))
#
# obj = A()
# import pickle
# f = open("test1.pkl", "wb")
# pickle.dump(obj, f)
# f.close()


# import shelve
# f = shelve.open("test2.she")


