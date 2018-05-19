#!/usr/bin/env python3
import pickle


def load(filename):
    """
    文件反序列化
    :return:
    """
    with open(filename, "rb") as f1:
        return pickle.load(f1)


def dump(obj, filename):
    """
    序列化到文件中
    :return:
    """
    with open(filename, "wb") as f1:
        pickle.dump(obj, f1)

