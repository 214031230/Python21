#!/usr/bin/env python3
class Login:
    def __init__(self):
        self.__max_count = 3
        self.__count = 0
        self.__info = {"spf": "123", "wxx": "123"}

    def __login(self):
        """
        用户登录
        :return:
        """
        username = input("Please input username:")
        password = input("Please input password:")
        if self.__info.get(username) != password:
            return False
        return True

    def __logout(self):
        """
        用户注销
        :return:
        """
        pass

    def run(self):
        """
        主函数
        :return:
        """
        while self.__count < self.__max_count:
            if self.__login():
                print("登录成功")
                break
            self.__count += 1
            print("用户名或密码错误！还剩余%s机会！" % (self.__max_count - self.__count))


obj = Login()
obj.run()
