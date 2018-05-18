#!/usr/bin/env python3
import pickle


class MyPickle:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        """
        文件反序列化
        :return:
        """
        with open(self.filename, "rb") as f1:
            return pickle.load(f1)

    def dump(self, obj):
        """
        序列化到文件中
        :return:
        """
        with open(self.filename, "wb") as f1:
            pickle.dump(obj, f1)

