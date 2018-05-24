#!/usr/bin/env python3
from conf import settings
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
        :return: 返回文件内容
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
        fh = logging.FileHandler(settings.logpath, encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s  %(name)s   %(levelname)s  %(message)s File:<%(filename)s line %(lineno)d>')
        logger.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    @staticmethod
    def helper():
        """
        帮助文档
        :return:
        """
        with open(settings.help_file, encoding="utf-8") as f:
            for i in f:
                print(i.rstrip())

    @staticmethod
    def check_show(file, name):
        """
        检测是否创建
        :param file: 表文件
        :param name: 学校、课程、班级、老师、学生
        :return: 返回反序列化后的表内容
        """
        ret = MyPickle.load(file)
        if not ret:
            Public.print("请先创建%s" % name, "error")
            return None
        return ret

    @staticmethod
    def m_create_info(self, s_class, file, types="", u_types=""):
        """
        创建班级、课程、老师、学生
        :param self: 班级、课程、老师、学生对象
        :param s_class: 班级、课程、老师、学生类
        :param file: 班级、课程、老师、学生表
        :param types: 班级、课程、老师、学生属性
        :param u_types: 老师、学生类型
        :return:  0 = 返回
                   1 = 创建成功
                   2 = 老师或者学生已经存在
        """
        while 1:
            name = input(">>>请输入%s名称(B/b返回)：" % types).strip()
            if not name:continue
            if name.upper() == "B":break
            if self.show_school():
                if types:
                    ret = Public.m_create(name, s_class, file, types, u_types)
                else:
                    ret = Public.m_create(name, s_class, file, types)
                if ret == 0:break
                if ret == 2:continue
                if ret == 1:
                    self.log.info("%s创建了%s:%s" % (self.name, types, name))
                    return 1

    @staticmethod
    def m_create(name, str_class, file, types, name_types=""):
        """
        创建班级、课程、老师、学生
        :param name: 创建班级、课程、老师、学生名称
        :param str_class: 创建班级、课程、老师、学生类
        :param file: 创建班级、课程、老师、学生表
        :param types: 创建班级、课程、老师、学生属性
        :param name_types：用户权限
        :return: 0=返回
                  1=成功
                  2=班级已经存在，返回上一层
        """

        while 1:
            school_num = input(">>>请选择学校(输入学校ID)(B/b返回)：").strip()
            if not school_num: continue
            if school_num.upper() == "B": return 0
            try:
                school_num = int(school_num)
                school_ret = MyPickle.load(settings.schoolinfo)
                obj = str_class(name)
                ret = obj.create(school_ret[school_num], file, types)
                if name_types:
                    MyLogin.register(name, name_types)
                if ret == 0: return 2
                if ret == 1: return 1
            except Exception:
                Public.print("ID不存在，请重试！", "error")

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
            if ret:
                for i in ret.values():
                    Public.print("学校名称：%s" % i .name, "none")
                    Public.print("%s列表：" % s_types, "none")
                    for x in getattr(i, types).values():
                        Public.print("          %s.%s" % (x.num, x.name), "none")
        else:
            if ret:
                Public.print("学校名称：%s" % ret[school_num].name, "none")
                Public.print("%s列表：" % s_types, "none")
                for i in getattr(ret[school_num], types).values():
                    Public.print("          %s.%s" % (i.num, i.name), "none")

    @staticmethod
    def m_show_teacher_student(user_name, types, s_types, user_file):
        """
        查看老师或者学生
        :param user_name: 老师、学生账号名称
        :param types: 属性 classes course
        :param s_types: 老师或者学生
        :param user_file: studentinfo 或者teacherinfo
        :return:
        """
        ret = Public.check_show(user_file, s_types)
        if ret:
            for i in ret.values():
                if not user_name:
                    Public.print("%s.name：<%s> school：<%s> course：<%s> classes:<%s>"
                                % (i.num, i.name, i.school.name, [i.course[x].name for x in i.course], [i.classes[x].name for x in i.classes]))
                else:
                    if user_name == i.name:
                        Public.print("%s: <%s>"
                                     % (types, [getattr(i, types)[x].name for x in getattr(i, types)]))

    @staticmethod
    def choice_classes_course(name, s_class, st_file, c_file, types, show):
        """
        :param name: 老师或者学生账号
        :param s_class: Manager类
        :param st_file: 老师或者学生表
        :param c_file: 课程或者班级表
        :param types: 课程或者班级属性
        :param show :
        :return:
        """
        ret1 = MyPickle.load(st_file)
        for i in ret1:
            if name == ret1[i].name:
                MyPickle.load(settings.schoolinfo)
                obj = s_class(name)
                getattr(obj, show)(ret1[i].school.num)
                choice = input(">>>请选择(输入数字ID):")
                ret2 = MyPickle.load(c_file)
                obj1 = ret2[int(choice)]
                getattr(ret1[i], types)[obj1.num] = obj1
                MyPickle.dump(ret1, st_file)
                return 1

    @staticmethod
    def choice_info(obj, s_types):
        """
        创建老师和学生的时候选择相关信息
        :param obj: 老师或者学生对象
        :param s_types: 老师或者学生
        :return:
        """
        while True:
            try:
                name = input(">>>请输入%s名称(B/b返回)：" % s_types).strip()
                if not name: continue
                if name.upper() == "B": return 0
                obj.show_school()
                school_num = input(">>>请选择学校(输入学校ID)(B/b返回)：").strip()
                if school_num.upper() == "B": return 0
                school_num = int(school_num)
                return name, school_num
            except Exception:
                Public.print("请输入正确的ID！！！", "error")


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
            password = MyLogin.__encryption_md5_salt1(username, password)
            user_info = MyPickle.load(settings.userinfo)
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
        ret = MyPickle.load(settings.userinfo)
        ret["name"].append(name)
        ret["password"].append(password)
        ret["type"].append(user_type)
        MyPickle.dump(ret, settings.userinfo)
