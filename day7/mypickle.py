#!/usr/bin/env python3
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