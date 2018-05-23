#!/usr/bin/env python3
from sys import modules
from core.manager import Manager
from core.student_manager import StudentManager
from core.teacher_manager import TeacherManager
from core.public import Public
from core.public import MyLogin


def main():
    """
    选择视图
    通过对象角色去调用对应的方法，根据用户选择跳转到对应的方法中
    :return:
    """
    ret = MyLogin.login()
    while True:
        if ret:
            role_class = getattr(modules[__name__], ret[1])
            obj = role_class(ret[0])
            print("-"*136)
            for i in obj.menus:
                Public.print("%s" % i[0], "menus")
            print()
            print("-"*136)
            choice = input(">>>请选择菜单功能(输入数字ID)：").strip()
            if choice.upper() == "Q":choice = "12"
            try:
                func = obj.menus[int(choice) - 1][1]
                getattr(obj, func)()
            except IndexError:
                Public.print("请输入正确的ID！！！", "error")
            except ValueError:
                Public.print("请输入正确的ID！！！", "error")




