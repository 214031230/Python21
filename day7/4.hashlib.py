#!/usr/bin/env python3
import hashlib
# hashlib特性:
# 1、单向不可逆 （采用摘要算法）
# 2、将一个字符串进行摘要运算 拿到不变的 固定长度的值
# 用途：
# 1、存储用户密码的时候 ： 不要存储明文
#       # 注册 ：alex3714  ->  摘要-> 文件里
#       # 登录 ：alex3714  ->  摘要-> 和文件里比对

# md5加密
# 普通版本
md5obj = hashlib.md5()   # 实例化一个md5摘要算法的对象
md5obj.update("123".encode("utf-8"))    # 使用md5算法的对象来操作字符串
print(md5obj.hexdigest())   # 获取算法的结果

# # 升级版本加盐
md5obj = hashlib.md5("sunpengfei".encode("utf-8"))
md5obj.update("123".encode("utf-8"))
print(md5obj.hexdigest())

# 动态加盐
username = "sunpengfei"  # 动态加盐可以把用户名当做盐
md5obj = hashlib.md5(username.encode("utf-8"))
md5obj.update("123".encode("utf-8"))
print(md5obj.hexdigest())

# sha1加密
# sha1 用法和md5一模一样
sha1obj = hashlib.sha1()
sha1obj.update("123".encode("utf-8"))
print(sha1obj.hexdigest())


# 校验文件一致性，当文件很大的时候，可以对文件进行一部分一部分验证。最后得到的结果还是一样的
md5obj = hashlib.md5()   # 实例化一个md5摘要算法的对象
md5obj.update('alex'.encode('utf-8'))  # 使用md5算法的对象来操作字符串
md5obj.update('3714'.encode('utf-8'))  # 使用md5算法的对象来操作字符串
print(md5obj.hexdigest())

md5obj = hashlib.md5()   # 实例化一个md5摘要算法的对象
md5obj.update('alex3714'.encode('utf-8'))  # 使用md5算法的对象来操作字符串
print(md5obj.hexdigest())

# 练习题：对比两个文件


def check_file(src_file, dest_file):
    """
    对比两个文件是否一致
    :param src_file: 源文件
    :param dest_file: 目标文件
    :return: True/False
    """
    ret = []
    for file in [src_file, dest_file]:
        md5obj = hashlib.md5()
        with open(file, encoding="utf-8") as f1:
            for i in f1:
                md5obj.update(i.encode('utf-8'))
            ret.append(md5obj.hexdigest())
    return True if ret[0] == ret[1] else False


print(check_file("./test.py", "test.py"))

