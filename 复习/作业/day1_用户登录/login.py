#!/usr/bin/env python3
import hashlib
import json
userinfo_path = "./userinfo"


class MyJson:
    """自定义json"""
    @staticmethod
    def load(file_path):
        """自定义的json load"""
        with open(file_path) as f:
            return json.load(f)

    @staticmethod
    def dump(obj, file_path):
        """自定义json dump"""
        with open(file_path, "w") as f:
            json.dump(obj, f)


class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.__code = "utf-8"
        self.__load = MyJson.load(userinfo_path)

    def __md5(self):
        """加密：动态加盐"""
        md5obj = hashlib.md5(self.username.encode(self.__code))
        md5obj.update(self.__password.encode(self.__code))
        return md5obj.hexdigest()

    def __check(self):
        """用户检测"""
        return self.__load.get(self.username)

    def login(self):
        """用户登录"""
        for i in self.__load:
            if self.username == i and self.__md5() == self.__load[i]:
                return True

    def register(self):
        """用户注册"""
        if not self.__check():
            self.__load[self.username] = self.__md5()
            MyJson.dump(self.__load, userinfo_path)
            return True


def run(msg,func):
    max_count = 0
    while max_count < 3:
        username = input(">>>Input Username：")
        password = input(">>>Input Password：")
        if not username or not password:continue
        obj = User(username,password)
        max_count += 1
        if getattr(obj, func)():
            return True
        else:
            print(msg)
    else:
        return False


def main():
    menus = ["1.登录","2.注册","q.退出"]
    while True:
        for i in menus:
            print("%s " % i, end="")
        while 1:
            choice = input("\n>>>请选择：").strip()
            if not choice:continue
            if choice.lower() == "q":exit()
            try:
                choice = int(choice)
                if choice == 1:
                    if run("Error:用户名或者密码错误","login"):print("INFO:注册成功")
                    else:print("Error:注册失败")
                elif choice == 2:
                    if run("Error:用户名已经存在","register"):print("INFO:注册成功")
                    else:print("Error:注册失败")
                else:
                    print("Error:你输入的ID不存在")
            except ValueError:
                print("Error:你输入的ID不正确")


if __name__ == '__main__':
    main()