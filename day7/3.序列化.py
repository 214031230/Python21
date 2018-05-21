#!/usr/bin/env python3
# 什么叫序列化呢？
    # 数据类型 —> 字符串的过程
# 什么时候要用序列化呢？
    # 数据从内存到文件
    # 数据在网络上传输  字节 - 字符串 - 字典
# python中的序列化模块都有哪些？
    # json   通用的 支持的数据类型 list tuple dict
    # pickle python中通用的 支持几乎所有python中的数据类型
    # shelve python中使用的便捷的序列化工具

# json
# dumps loads
# 内存读写
# import json
# dic = {"k": 'v'}
# json_dic = json.dumps(dic)   # 字典转字符串的过程 ——序列化
# print(json_dic)
# print(json.loads(json_dic))  # 字符串转回其他数据类型 —— 反序列化

# dump load
# 文件读写
# dic = {"k": 'v'}
# with open('test.json', 'w') as f:
#     json.dump(dic, f)
#     # json.dump(dic, f)       # 在json中 dump默认不支持dump多条数据
#
# with open('test.json') as f:
#     print(json.load(f))      # 从文件中反序列化


# 如果要dump多条数据，每一条数据线dumps一下 编程字符串 然后打开文件 write写进文件里 \n
# 读取的时候按照标志读取或者按行读，读出来之后 再使用loads
# with open('test.json', 'w') as f:
#     str_dic = json.dumps(dic)
#     f.write(str_dic+'\n')
#     f.write(str_dic+'\n')
#     f.write(str_dic+'\n')
#     f.write(str_dic+'\n')
#
# with open('test.json') as f:
#     for line in f:
#         print(json.loads(line.strip()))


# pickle
# pickle 和 json用法一致。但是pickle可以dump多条数据
# 1.pickle支持更多的数据类型
# 2.pickle的结果是二进制
# 3.pickle在和文件交互的时候可以被多次load
# import pickle
#
#
# class A:
#     def __init__(self,name):
#         self.name = name
#
# alex = A('alex')
# print(pickle.dumps(alex))
# with open('test.pkl', 'wb') as f:
#     pickle.dump(alex, f)
#     pickle.dump(alex, f)     # 可以dump多条数据
#     pickle.dump(alex, f)     # 可以dump多条数据
#
# with open('test.pkl', 'rb') as f:
#     while True:  # 通过循环取出所有的数据
#         try:
#             obj = pickle.load(f)
#             print(obj.name)
#         except EOFError:
#             break


# shelve
# shelve也是python提供给我们的序列化工具，比pickle用起来更简单一些。
# shelve只提供给我们一个open方法，是用key来访问的，使用起来和字典类似。
# import shelve
# f = shelve.open('shelve_file')
# f['key'] = {'int':10, 'float':9.5, 'string':'Sample data'}  #直接对文件句柄操作，就可以存入数据
# f.close()
#
# import shelve
# f1 = shelve.open('shelve_file')
# existing = f1['key']  #取出数据的时候也只需要直接用key获取即可，但是如果key不存在会报错
# f1.close()
# print(existing)

import pickle


class MyPickle:
    @staticmethod
    def load_iter(filename):
        """
        反序列化
        :param filename: 反序列化的文件路径
        :return: 一个存放反序列化数据的生成器
        """
        with open(filename, "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break

    @staticmethod
    def load(filename):
        """
        反序列化
        :param filename: 反序列化的文件路径
        :return: 一个列表，列表存储一个或者多个反序列化后的数据
        """
        result = []
        with open(filename, "rb") as f:
            while True:
                try:
                    result.append(pickle.load(f))
                except EOFError:
                    break
        return result

    @staticmethod
    def dump(obj, filename):
        """
        序列化
        :param obj: 需要进行序列化的对象
        :param filename: 序列化后文件存储路径
        :return:
        """
        with open(filename, "ab") as f:
            pickle.dump(obj, f)