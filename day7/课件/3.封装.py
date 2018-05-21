# 广义上的封装 :把变量和函数都放在类中
# 狭义上的封装 :把一些变量 或者 方法 隐藏起来，不对外公开
    # 公有的 :
    # 私有的 : __名字
# class Person:
#     __country = '中国'    # 私有的静态属性

# print(Person.__country)   # AttributeError: type object 'Person' has no attribute '__country'
# 私有的名字 只能在类的内部使用 不能在类的外部使用
# print(Person.__dict__)
# _Person__country
# print(Person._Person__country)  # 不能使用上面这种方式去调用私有的变量
# 如果非要在类的外部调用一个私有的名字，name必须是在私有的名字前面加 _类名__私有的名字
# Person.__name = 'XXX'
# print(Person.__name)   # 在类的外部不能第一一个私有变量
# print(Person.__dict__)

# 私有的变量 ：
    # 在类的内部 如果使用__变量的形式会发生变形，python会自动的为你加上_类名

# class Person:
#     __country = '中国'
#     def __init__(self,name,pwd):
#         self.name = name
#         self.__pwd = pwd      # 私有的对象属性
#     def login(self):
#         print(self.__dict__)
#         if self.name == 'alex' and self.__pwd == 'alex3714':
#             print('登录成功')
#
# alex = Person('alex','alex3714')
# alex.login()
# print(alex.__dict__)
# print(alex.__pwd)

# class Person:
#     def __init__(self):pass
#     def __制造密码转换(self,inp):
#         print('eating')
#     def 注册(self):
#         inp = input('pwd>>>')
#         加密之后的密码 = self.__制造密码转换(inp)

# alex3714 --->

# 静态属性 、 对象属性、 方法（动态属性） 前面加上双下划綫都会变成私有的
# 私有的特点就是只能在类的内部调用，不能在类的外部使用

# class Foo:
#     def __init__(self):
#         self.func()
#     def func(self):
#         print('in Foo')

# class Son(Foo):
#     def func(self):
#         print('in son')
#
# s = Son()


# class Foo:
#     def __init__(self):
#         self.__func()    # self._Foo__func
#     def __func(self):
#         print('in Foo')
#
# class Son(Foo):
#     def __func(self):    # _Son__func
#         print('in son')
#
# s = Son()