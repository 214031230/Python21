#!/usr/bin/env python3
# 普通装饰器标准写法，可以满足传参和有返回值的情况
# def wrapper(f):
#     def inner(*args, **kwargs):
#         print("start_wrapper")
#         res = f(*args, **kwargs)
#         print("end_wrapper")
#         return res
#     return inner
# @wrapper  # func_test = wrapper(func_test)
# def func_test():
#     print("我是func_test")
# func_test() # func_test = inner

# 带参数的装饰器，假如有500个函数需要反复添加装饰器，可以通过装饰器传参来实现
# FLAG = True
# def outer(FLAG):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             if FLAG == True:
#                 print("start_wrapper")
#                 res = func(*args, **kwargs)
#                 print("end_wrapper")
#                 return res
#             else:
#                 res = func(*args, **kwargs)
#                 return res
#         return inner
#     return wrapper
#
# @outer(FLAG)  # @outer(FLAG)  = @wrapper
# def func1():
#     print("我是funcl!!!")
# func1()


#  多个装饰器装饰一个函数
def wrapper1(f):  # f = inner2
    def inner1():
        print("我是wrapper1")
        f()  # inner2()
        print("我是wrapper1")
    return inner1

def wrapper2(f): # f = func
    def inner2():
        print("我是wrapper2")
        f()  # func()
        print("我是wrapper2")
    return inner2

@wrapper1  # func = wrapper1(func)= wrapper1(inner2) = inner1
@wrapper2  # func = wrapper2(func) = inner2
def func():
    print("我是func")
func()  #  func = inner1 = inner1()

#  多个装饰器装饰一个函数，实现用户登录和性能测试
import time
user_status = {"alex": False}

# 登录装饰器
def login(f):  # f = inner2
    def inner1(name):
        if user_status[name] == False:
            user = input("请输入用户名：")
            pwd = input("请输入密码：")
            if user == "alex" and pwd == "123":
                print("登录成功")
                user_status[name] = True
                f(name)  # inner2(name)
        else:
            print("登录成功")
            f(name)   # inner2(name)
    return inner1

# 性能测试装饰器
def timmer(f): # f = func
    def inner2(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)  # f = func
        end_time = time.time()
        print(end_time - start_time)
        return res
    return inner2

@login  #  func = login(func) = login(inner2) = inner1
@timmer  # func = timer(func) = inner2  # 向上传完值以后销毁
def func(name):
    print("start_func")
    print("我是函数func")
    time.sleep(0.1)
    print("end_func")

func("alex")  # func = inner1

