#!/usr/bin/env python3
# try excpet
# try:
#     choice = int(input(">>>"))
#     print(choice)
# except ValueError:
#     print("您输入的不是数字")


# 万能异常
# 所有的异常处理都用万能异常好不好？
# 具体的异常处理+万能异常：
    # 能够提前预料到的异常都应该用具体的异常去处理，剩下其他的异常用万能异常控制
    # 万能异常应该写在最后
# try:
#     choice = int(input(">>>"))
#     print(choice)
# except Exception:   # 不写Exception也是万能异常
#     print("您输入的不是数字")


# try excpet as
# 可以显示具体的错误
# try:
#     choice = int(input(">>>"))
#     print(choice)
# except ValueError as e:
#     print(e)
# except Exception as e:  # 如果使用万能异常，一定要用as显示错误
#     print(e)
#


# try excpet else
# try:
#     choice = int(input(">>>"))
#     print(choice)
# except ValueError: print('请输入一个数字')
# except Exception as e: # 处理未知异常的所有异常
#     print(e)
# else:
#     print('执行else了')     # 如果try语句中的代码都顺利的执行了，没有报错，那么执行else中的代码
# finally:
#     print('执行finally了')  # 无论如何都会执行


# try标准写法
# try:
#     pass  # 可能有问题的代码
# except ValueError:  # 能预料到的错误
#     pass
# except Exception as e:print(e)  # 能处理所有的异常
# else:pass          # try中的代码没有错误的时候执行
# finally:pass       # 无论如何都会执行的

# 断言
# 如果断言失败则不执行断言下面的代码
# assert 1==2

