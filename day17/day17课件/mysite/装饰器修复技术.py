from functools import wraps


def wrapper(func):
    @wraps(func)  # 借助内置的工具修复被装饰的函数
    def inner(*args, **kwargs):
        print("呵呵")
        func(*args, **kwargs)
    return inner


@wrapper
def foo(arg):
    """
    这是一个测试装饰器的函数
    :param arg: int 必须是int类型
    :return: None
    """
    print("嘿嘿嘿" * arg)


foo(10)
print(foo.__doc__)

