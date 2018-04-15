import time
# def wrapper():
#     def inner():
#         name1 = 'alex'
#         print(name1)
#     inner()
# wrapper()

# def wrapper():
#     def inner():
#         name1 = 'alex'
#         print(name1)
#     return inner
# ret = wrapper()  # inner
# ret()
def func1():
    print('晚上回去吃烧烤....')
    time.sleep(0.3)

def func2():
    print('晚上回去喝啤酒....')
    time.sleep(0.3)

# 最简单版的装饰器
# def timer(f1):  # f1 = func1
#     def inner():
#         start_time = time.time()
#         f1()
#         end_time = time.time()
#         print('此函数的执行效率%s' %(end_time-start_time))
#     return inner
'''
# f = func1
# func1 = timer
#
# func1(f)  # timmer(func1)
'''
# func1 = timer(func1)  # inner
# func1()  # inner()


# @
def timer(f1):  # f1 = func1
    def inner():
        start_time = time.time()
        f1()
        end_time = time.time()
        print('此函数的执行效率%s' %(end_time-start_time))
    return inner

@timer  # func1 = timer(func1)
def func1():
    print('晚上回去吃烧烤....')
    time.sleep(0.3)
@timer # func2 = timer(func2)
def func2():
    print('晚上回去喝啤酒....')
    time.sleep(0.3)
func1()  # inner()
#装饰器：在不改变原函数即原函数的调用的情况下，
# 为原函数增加一些额外的功能，打印日志，执行时间，登录认证等等。

#被装饰函数带参数
# def timer(f1):  # f1 = func1
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         f1(*args,**kwargs)  # func1()
#         end_time = time.time()
#         print('此函数的执行效率%s' %(end_time-start_time))
#     return inner
#
# @timer  # func1 = timer(func1)  inner
# def func1(a,b):
#     print(a,b)
#     print('晚上回去吃烧烤....')
#     time.sleep(0.3)
# func1(111,222)  # inner(111,222)

#被装饰函数带参数
# def timer(f1):  # f1 = func1
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         ret = f1(*args,**kwargs)  # func1()
#         end_time = time.time()
#         print('此函数的执行效率%s' %(end_time-start_time))
#         return ret
#     return inner
#
# @timer  # func1 = timer(func1)  inner
# def func1(a,b):
#     print(a,b)
#     print('晚上回去吃烧烤....')
#     time.sleep(0.3)
#     return 666
# ret2 = func1(111,222)  # inner(111,222)
# print(ret2)

def wrapper(f1):
    def inner(*args,**kwargs):
        '''执行函数之前的操作'''
        ret = f1(*args,**kwargs)
        '''执行函数之后的操作'''
        return ret
    return f1

# @wrapper
# def func1():
#     print(222)
#     return 333
# print(func1())
user_status= {
    'username':None,
    'status':False,
}

def login():
    pass

def register():
    pass

def wrapper(f1):
    def inner(*args,**kwargs):
        if user_status.get('status'):
            ret = f1(*args,**kwargs)
            return ret
        else:
            login()
    return f1

@wrapper
def article():
    print('欢迎%s来到文章页面')

dic = {
    1:login,
    2:register,
    3:article,
}
while True:
    pass
'''
1)，启动程序，首页面应该显示成如下格式：
    欢迎来到博客园首页
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序
2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，没成功则结束整个程	序运行，成功之后，
可以选择访问3~6项.
4)，如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选择。
5)，注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
6)，退出程序为结束整个程序运行。

'''