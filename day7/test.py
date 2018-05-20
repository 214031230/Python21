#!/usr/bin/env python3
# from math import pi
#
#
# class Hoses:
#     def __init__(self,name,length,width):
#         self.name = name
#         self.__length = length
#         self.__width = width
#
#     @property
#     def tell(self):
#         return "地产：%s 房屋面积：%s" % (self.name, self.__length * self.__width)
#
#
# my_h = Hoses("万达", 10, 10)
# print(my_h.tell)
#
#
# class Yuan:
#     def __init__(self,r):
#         self.r = r
#
#     @property
#     def mj(self):
#         return pi * self.r ** 2
#
#
# y1 = Yuan(3)
# print(y1.mj)

# import pickle
#
#
# class MyPickle:
#     @staticmethod
#     def load_iter(filename):
#         """
#         反序列化
#         :param filename: 反序列化的文件路径
#         :return: 一个存放反序列化数据的生成器
#         """
#         with open(filename, "rb") as f:
#             while True:
#                 try:
#                     yield pickle.load(f)
#                 except EOFError:
#                     break
#
#     @staticmethod
#     def load(filename):
#         """
#         反序列化
#         :param filename: 反序列化的文件路径
#         :return: 一个列表，列表存储一个或者多个反序列化后的数据
#         """
#         result = []
#         with open(filename, "rb") as f:
#             while True:
#                 try:
#                     result.append(pickle.load(f))
#                 except EOFError:
#                     break
#         return result
#
#     @staticmethod
#     def dump(obj, filename):
#         """
#         序列化
#         :param obj: 需要进行序列化的对象
#         :param filename: 序列化后文件存储路径
#         :return:
#         """
#         with open(filename, "ab") as f:
#             pickle.dump(obj, f)


# dic = {"k1": "v1"}
#
# MyPickle.dump(dic, "./file/test.pik")
#
# dic = {"k2": "v2"}
#
# MyPickle.dump(dic, "./file/test.pik")

#
# ret = MyPickle.load("./file/test.pik")
# print(dir(ret))
# for i in ret:
#     print(i)


