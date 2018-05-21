#!/usr/bin/env python3
# 广义上的封装 :把变量和函数都放在类中
# 狭义上的封装 :把一些变量 或者 方法 隐藏起来，不对外公开
    # 公有的 :
    # 私有的 : __名字

# 静态属性 、 对象属性、 方法（动态属性） 前面加上双下划綫都会变成私有的
# 私有的特点就是只能在类的内部调用，不能在类的外部使用
# 私有的变量 ：在类的内部 如果使用__变量的形式会发生变形，python会自动的为你加上_类名


# class Person:
#     __country = '中国'    # 私有静态属性
#
#     def __init__(self,name,pwd):
#         self.name = name
#         self.__pwd = pwd      # 私有的对象属性
#
#     def login(self):
#         print(self.__dict__)
#         if self.name == 'alex' and self.__pwd == 'alex3714':
#             print('登录成功')
#
#
# alex = Person('alex','alex3714')
# alex.login()
# print(alex.__dict__)

# 私有的名字 只能在类的内部使用 不能在类的外部使用：AttributeError: type object 'Person' has no attribute '__country'
# print(Person.__country)

# python中不并能真正的隐藏属性，是通过变形的方式实现。_Person__country
# 如果非要在类的外部调用一个私有的名字，name必须是在私有的名字前面加 _类名__私有的名字
# print(Person._Person__country)

# Person.__name = 'XXX'
# print(Person.__name)   # 在类的外部不能第一一个私有变量，只有在类定义的时候__名称才叫做私有属性


# 类内方法的调用过程
# class Foo:
#     def __init__(self):  # 第二步 找到父类的__init__ 这时候self = s 即 Son类的对象
#         self.func()   # 第三步执行父类s.func()
#
#     def func(self):
#         print('in Foo')
#
#
# class Son(Foo):
#     def func(self):  # 第四步 执行func方法
#         print('in son')
#
#
# s = Son()  # 实例化类，第一步去执行__init__函数由于Son没有__init,会去父类找__init__


# 类内私有方法的调用过程
# class Foo:
#     def __init__(self):  # 第二步 找到父类的__init__ 这时候self = s 即 Son类的对象
#         self.__func()    # 第三步 类在定义的过程中已经把私有属性变形为 self._Foo__func
#                          # 第四步 执行self._Foo__func
#
#     def __func(self):   # 类在定义的时候变形为 _Foo__func
#         print('in Foo')
#
#
# class Son(Foo):
#     def __func(self):    # _Son__func
#         print('in son')
#
#     def start(self):
#         self.__func()
#
#
# s = Son()  # 实例化类，第一步去执行__init__函数由于Son没有__init,会去父类找__init__

# 练习题：登录增加mad5校验,用户不可以访问你的加密方式
import hashlib


class MyLogin:
    def __init__(self, name, password):
        self.name = name
        self.__password = password  # 密码私有化

    def __encryption_md5(self):  # 加密方式私有化
        """
        普通md5密码
        :return: 加密后的字符串
        """
        md5obj = hashlib.md5()   # 实例化一个md5摘要算法的对象
        md5obj.update(self.__password.encode('utf-8'))  # 使用md5算法的对象来操作字符串
        return md5obj.hexdigest()

    def __encryption_md5_salt(self):  # 加密方式私有化
        """
        md5加盐
        :return: 加密后的字符串
        """
        md5obj = hashlib.md5("sunpengfei".encode("utf-8"))   # 实例化一个md5摘要算法的对象
        md5obj.update(self.__password.encode('utf-8'))  # 使用md5算法的对象来操作字符串
        return md5obj.hexdigest()

    def __encryption_md5_salt1(self):  # 加密方式私有化
        """
        md5动态加盐
        :return: 加密后的字符串
        """
        md5obj = hashlib.md5(self.name.encode("utf-8"))   # 实例化一个md5摘要算法的对象
        md5obj.update(self.__password.encode('utf-8'))  # 使用md5算法的对象来操作字符串
        return md5obj.hexdigest()

    def login(self):
        """
        202cb962ac59075b964b07152d234b70
        5dfb835be352750bb15045eae941b8c7
        6b783000a3177ac09ae3706a077d6d80
        :return:
        """
        self.__password = self.__encryption_md5_salt1()
        if self.name == "spf" and self.__password == "202cb962ac59075b964b07152d234b70":
            return "Success"
        if self.name == "spf" and self.__password == "5dfb835be352750bb15045eae941b8c7":
            return "Success"
        if self.name == "spf" and self.__password == "6b783000a3177ac09ae3706a077d6d80":
            return "Success"


spf = MyLogin("spf", "1235")
print(spf.login())
