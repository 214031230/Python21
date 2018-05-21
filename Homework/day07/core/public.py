#!/usr/bin/env python3
from core import my_pickle
from conf.config import userinfo


class Public:
    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def check_show(file, name):
        """
        检测是否创建
        :param file:
        :param name:
        :return:
        """
        ret = my_pickle.load(file)
        if not ret:
            Public.print_log("还未创建%s" % name, "error")
        return ret

    @staticmethod
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
            Public.print_log("%s已经存在！" % obj.name, "error")
            return
        info2 = getattr(ret[school_obj.name], argv)
        info2[obj.name] = obj
        my_pickle.dump(ret, file)

    @staticmethod
    def create_info_user(file, school_obj, course_obj, obj):
        ret = my_pickle.load(file)
        school_obj.course = course_obj
        ret[obj.name] = school_obj
        my_pickle.dump(ret, file)
        Public.create_user(obj.name, "TeacherManager")

    @staticmethod
    def login():
        print("\033[0;31;0m")
        print("欢迎访问校园管理系统".center(50, "-"))
        print(">>>请登录：\033[0m")
        count = 0
        while count < 3:
            username = input("\033[0;35;0m>>>请输入用户名：\033[0m").strip()
            password = input("\033[0;35;0m>>>请输入密码：\033[0m").strip()
            if not username or not password:
                print("ERROR:用户名或密码不能为空")
            ret = my_pickle(userinfo)
            user_info = ret.load()
            print(user_info)
            if username in user_info["name"]:
                pwd_index = user_info["name"].index(username)
                if password == user_info["password"][pwd_index]:
                    return username, user_info["type"][pwd_index]
                else:
                    print("ERROR：密码错误")
            else:
                print("ERROR：用户名不存在")
            count += 1


