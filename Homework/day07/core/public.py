#!/usr/bin/env python3
from conf.settings import userinfo
from conf.settings import logpath
import hashlib
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
        with open(filename, "rb") as f:
            return pickle.load(f)

    @staticmethod
    def dump(obj, filename):
        """
        序列化
        :param obj: 需要进行序列化的对象
        :param filename: 序列化后文件存储路径
        :return:
        """
        with open(filename, "wb") as f:
            pickle.dump(obj, f)


class Public:
    @staticmethod
    def print(meg, meg_type="info"):
        """
        打印带颜色的日志
        :param meg: 日志信息
        :param meg_type:  日志类型
        :return:
        """
        if meg_type == "info":
            print("\033[0;36;0mINFO：%s\033[0m" % meg)
        elif meg_type == "none":
            print("\033[0;36;0m%s\033[0m" % meg)
        elif meg_type is "menus":
            print("\033[0;35;0m%s\033[0m" % meg, end="")
        elif meg_type == "error":
            print("\033[0;31;0mERROR：%s\033[0m" % meg)
        else:
            return "Error：参数不正确"
        
    @staticmethod
    def log():
        """
        定义日志输出合格
        :return: 返回一个可以直接使用的logger对象
        """
        import logging
        logger = logging.getLogger()
        fh = logging.FileHandler(logpath, encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s  %(name)s   %(levelname)s  %(message)s File:<%(filename)s line %(lineno)d>')  # 定义文件日志格式
        logger.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    @staticmethod
    def check_show(file, name):
        """
        检测是否创建
        :param file:
        :param name:
        :return:
        """
        ret = MyPickle.load(file)
        if not ret:
            Public.print("还未创建%s" % name, "error")
        return ret


class MyLogin:
    """
    用户登录类
    包含登录和注册两个方法，密码进行md5加密
    """
    @staticmethod
    def __encryption_md5_salt1(username, password):  # 加密方式私有化
        """
        md5动态加盐
        :return: 加密后的字符串
        """
        md5obj = hashlib.md5(username.encode("utf-8"))   # 实例化一个md5摘要算法的对象
        md5obj.update(password.encode('utf-8'))  # 使用md5算法的对象来操作字符串
        return md5obj.hexdigest()

    @staticmethod
    def login():
        """
        用户登录
        :return: （用户名，用户权限）
        """
        Public.print("欢迎访问校园管理系统".center(50, "-"), "none")
        Public.print(">>>请登录:", "none")
        count = 0
        while count < 3:
            username = input(">>>请输入用户名：").strip()
            password = input(">>>请输入密码：").strip()
            if not username or not password:
                Public.print("用户名或密码不能为空", "error")
            password = MyLogin.__encryption_md5_salt1(username, password)
            user_info = MyPickle.load(userinfo)
            if username in user_info["name"]:
                pwd_index = user_info["name"].index(username)
                if password == user_info["password"][pwd_index]:
                    log = Public.log()
                    log.info("%s登录了系统" % username)
                    return username, user_info["type"][pwd_index]
                else:
                    Public.print("密码错误", "error")
            else:
                Public.print("用户名不存在", "error")
            count += 1

    @staticmethod
    def register(name, user_type):
        """
        创建用户登录权限
        :param name:  用户名
        :param user_type: 用户类型
        :return:
        """
        ret = MyPickle.load(userinfo)
        ret["name"].append(name)
        ret["password"].append("123456")
        ret["type"].append(user_type)
