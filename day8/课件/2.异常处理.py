# inp = int(input('num : '))   # 逻辑错误  ValueError
# name   # NameError
# l = []   # IndexError
# l[2]
# try:
#     l = []
#     num = int(input('num ： '))
#     l[num]
# except ValueError:print('请输入一个数字')
# except IndexError:print('您要找的项目不存在')
# except Exception as e:print(e)
# except IndexError:print('您要找的索引不存在')

# try
# excpet
# except as
# 找到一个满足条件的其他分支都不走了
# 预料不到的错误 —— 万能异常
    # except
    # except Exception:
    # except Exception as e:  ---推荐
# 所有的异常处理都用万能异常好不好？
# 具体的异常处理+万能异常：
    # 能够提前预料到的异常都应该用具体的异常去处理，剩下其他的异常用万能异常控制
    # 万能异常应该写在最后

# try:
#     f = open('a','w')
#     l = [1]
#     num = int(input('num ： '))
#     l[num]
# except ValueError:print('请输入一个数字')
# except IndexError:print('您要找的项目不存在')
# except Exception as e:print(e)
# else:print('执行else了')     # 如果try语句中的代码都顺利的执行了，没有报错，那么执行else中的代码
# finally:
#     print('执行finally了') # 无论如何都会执行
#     f.close()


# def func():
#     try:
#         f = open('aaa','w')
#         ret = f.read()
#         return ret
#     # except:
#     #     print('error')
#     finally:f.close()


# try:
#     pass #可能有问题的代码
# except ValueError:  # 能预料到的错误
#     pass
# except Exception as e:print(e) # 能处理错有的异常
# else:pass          # try中的代码没有错误的时候执行
# finally:pass       # 无论如何都会执行的

# try:
#     main()
# except Exception as e:
#     print(e)

# raise ValueError

# class EvaException(BaseException):
#     def __init__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg
# obj = EvaException('类型错误')
# print(obj)

# assert 1==2   # if条件判断


# try except else finally
# raise 错误类型
# 自定义异常 自定义一个类继承BaseException
# 断言 assert

