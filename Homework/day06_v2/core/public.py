#!/usr/bin/env python3
from core import my_pickle
from conf.config import userinfo


def print_log(meg, meg_type="info"):
    """
    打印带颜色的日志
    :param meg: 日志信息
    :param meg_type:  日志类型
    :return:
    """
    if meg_type == "info":
        print("\033[0;36;0mINFO：%s\033[0m" % meg)
    elif meg_type is None:
        print("\033[0;36;0m%s\033[0m" % meg)
    elif meg_type is "menus":
        print("\033[0;35;0m%s\033[0m" % meg)
    elif meg_type == "error":
        print("\033[0;31;0mERROR：%s\033[0m" % meg)
    else:
        return "Error：参数不正确"


def create_user(name, user_type):
    """
    创建用户登录权限
    :param name:  用户名
    :param user_type: 用户类型
    :return:
    """
    ret1 = my_pickle.load(userinfo)
    ret1["name"].append(name)
    ret1["password"].append("123456")
    ret1["type"].append(user_type)


def check_show(file, name):
    """
    检测是否创建
    :param file:
    :param name:
    :return:
    """
    ret = my_pickle.load(file)
    if not ret:
        print_log("还未创建%s" % name, "error")
    return ret


def create_info(file, school_obj, obj, argv):
    """
    创建班级和课程
    :param file: 表文件
    :param school_obj: 学校对象
    :param obj: 班级或者课程对象
    :param argv: 字段属性
    :return:
    """
    ret = my_pickle.load(file)
    if not ret.get(school_obj.name):
        ret[school_obj.name] = school_obj
    info = getattr(ret[school_obj.name], argv)
    if obj.name in info:
        print_log("%s已经存在！" % obj.name, "error")
        return
    info2 = getattr(ret[school_obj.name], argv)
    info2[obj.name] = obj
    my_pickle.dump(ret, file)


def create_info_user(file, school_obj, course_obj, obj):
    ret = my_pickle.load(file)
    school_obj.course = course_obj
    ret[obj.name] = school_obj
    my_pickle.dump(ret, file)
    create_user(obj.name, "TeacherManager")
