#!/usr/bin/env python3
# with open("a.txt", mode="a") as f:
#     f.write("aaaa")
# with open("a.txt", mode="r") as f:
#     for i in f:
#         print(i.strip())

# with open("a.txt", mode="wb") as f:
#     f.write("adfa".encode("utf-8"))

def wrapper(f):
    """
    装饰器
    :param f:
    :return:
    """
    def inner(*args, **kwargs):
        print("执行函数之前")
        ret = f(*args, **kwargs)
        print("执行函数之后")
        return ret

    return inner

@wrapper
def fun():
    print("我是fun")
fun()
