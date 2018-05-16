#!/usr/bin/env python3
import json


def dump(dic, t_name):
    """
    把字典序列化到内存中
    :param dic: 字典，存储表数据
    :param t_name:  表名称
    :return:
    """
    f = open(t_name, mode="w")
    json.dump(dic, f)
    f.close()


def load(t_name):
    """
    把表内容反序列化成字典
    :param t_name: 表名称
    :return: 返回一个字典
    """
    f = open(t_name)
    dic = json.load(f)
    f.close()
    return dic