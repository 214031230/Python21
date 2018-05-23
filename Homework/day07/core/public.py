#!/usr/bin/env python3
from conf.settings import userinfo
from conf import settings
from sys import modules
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
    def helper():
        with open(settings.help_file, encoding="utf-8") as f:
            for i in f:
                print(i.rstrip())

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
            Public.print("请先创建%s" % name, "error")
        return ret

    @staticmethod
    def m_create_course_class(name, str_class, file, types):
        """
        创建班级和课程
        :param name: 班级名称
        :param str_class: 班级类
        :param file: 班级表或者课程表
        :param types: 属性classes 或者 course
        :return: 0=返回
                  1=成功
                  2=班级已经存在，返回上一层
        """
        while 1:
            school_num = input(">>>请选择学校(输入学校ID)(B/b返回)：").strip()
            if not school_num:continue
            if school_num.upper() == "B": return 0
            try:
                school_num = int(school_num)
                ret = MyPickle.load(settings.schoolinfo)
                obj = str_class(name)
                ret = obj.create(ret[school_num], file, types)
                if ret == 0:return 2
                if ret == 1:return 1
            except ValueError:
                Public.print("ID不存在，请重试！", "error")
            except KeyError:
                Public.print("ID不存在，请重试！", "error")

    @staticmethod
    def m_create_student_teacher(name, name_types, str_class, school_num, classes_num, course_num, file, types):
        """
        创建老师和学生
        :param name: 账号名称
        :param name_types: 账号类型
        :param str_class: 老师或者学生类
        :param school_num: 学校ID
        :param classes_num: 班级ID
        :param course_num: 课程ID
        :param file:老师表或者学生表
        :param types 属性 student 或者 teacher
        :return: 0 = 已经存在
                  1 = 成功
        """
        school_ret = MyPickle.load(settings.schoolinfo)
        classes_ret = MyPickle.load(settings.classinfo)
        course_ret = MyPickle.load(settings.courseinfo)
        obj = str_class(name)
        ret = obj.create(school_ret[school_num], classes_ret[classes_num], course_ret[course_num], file, types)
        if ret == 0:return 0
        if ret == 1:return 1
        MyLogin.register(name, name_types)

    @staticmethod
    def m_show_course_class(school_num, types, s_types):
        """
        查看班级和课程
        :param school_num: 学校ID
        :param types: 属性名称：classes 或者 course
        :param s_types: 班级或者课程
        :return:
        """
        ret = Public.check_show(settings.schoolinfo, s_types)
        if not school_num:
            for i in ret.values():
                Public.print("学校名称：%s" % i .name, "none")
                Public.print("%s列表：" % s_types, "none")
                for x in getattr(i, types).values():
                    Public.print("          %s.%s" % (x.num, x.name), "none")
        else:
            Public.print("学校名称：%s" % ret[school_num].name, "none")
            Public.print("%s列表：" % s_types, "none")
            for i in getattr(ret[school_num], types).values():
                Public.print("          %s.%s" % (i.num, i.name), "none")

    @staticmethod
    def m_show_teacher_student(user_name, types, s_types, user_file):
        """
        查看老师或者学生
        :param user_name: 账号名称
        :param types: 属性 classes course
        :param s_types: 老师或者学生
        :param user_file: studentinfo 或者teacherinfo
        :return:
        """
        ret = Public.check_show(user_file, s_types)
        for i in ret.values():
            if not user_name:
                Public.print("%s.name：<%s> school：<%s> course：<%s> classes:<%s>"
                            % (i.num, i.name, i.school.name, [i.course[x].name for x in i.course], [i.classes[x].name for x in i.classes]))
            else:
                if user_name == i.name:
                    Public.print("%s: <%s>"
                                 % (types, [getattr(i, types)[x].name for x in getattr(i, types)]))


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
        password = MyLogin.__encryption_md5_salt1(name, "123")
        ret = MyPickle.load(userinfo)
        ret["name"].append(name)
        ret["password"].append(password)
        ret["type"].append(user_type)
        MyPickle.dump(ret, userinfo)
