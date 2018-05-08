#!/usr/bin/env python3
# os模块是与操作系统交互的一个接口
import os
# os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
print(os.getcwd())
# os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
# os.chdir(r'F:')
# os.chdir(r"F:\3.4")
print(os.getcwd())
# os.curdir  返回当前目录: ('.')  基本无用
# os.pardir  获取当前目录的父目录字符串名：('..')  基本无用

# os.makedirs('dirname1/dirname2')    可生成多层递归目录
# os.makedirs(r"c:\a\b\c")
os.makedirs(r"c:\a\b\c", exist_ok=True)
# os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove()  删除一个文件
# os.rename("oldname","newname")  重命名文件/目录
# os.stat('path/filename')  获取文件/目录信息
print(os.stat(r"C:\Users\lanpa\Desktop\蓝帕（北京）科技股份有限公司\172.3.0.23.pdf"))
# os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print(os.sep)
# os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
print(os.linesep)
# os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
print(os.pathsep)
# os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
print(os.name)
# os.system("bash command")  运行shell命令，直接显示
os.system("dir")
# os.popen("bash command).read()  运行shell命令，获取执行结果
res = os.popen("dir").read()
print(res)
# os.environ  获取系统环境变量
print(os.environ)
#
# os.path
# os.path.abspath(path) 返回path规范化的绝对路径 os.path.split(path) 将path分割成目录和.文件名二元组返回 os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素 os.path.basename(path) 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。
#                         即os.path.split(path)的第二个元素
print(os.path.abspath("__init__.py"))
# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
print(os.path.exists(r"d:"))
print(os.path.exists(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\day"))
# os.path.isabs(path)  如果path是绝对路径，返回True
print(os.path.isabs(r"../day5"))
# os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
print(os.path.isfile(r"../day5/__init__.py"))
# os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
print(os.path.isdir(r"../day5"))
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.join(r"C:\Users\lanpa", r"day3", r"day2"))
# os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时
import time
print(os.path.getatime(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\day5\__init__.py"))
print(time.strftime("%x %X", time.gmtime(os.path.getatime(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\day5\__init__.py"))))

# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
print(os.path.getmtime(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\day5\__init__.py"))
print(time.strftime("%x %X", time.gmtime(os.path.getmtime(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\day5\__init__.py"))))

# os.path.getsize(path) 返回path的大小
print(os.path.getsize(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\day5\__init__.py"))
print(os.path.getsize(r"C:\Users\lanpa\Desktop\Python自动化21期\Python21\day5"))

# 练习 计算目录大小
# lst = [1, [2, [3, [4]]],"a"]
#
# def func(lst):
#     for i in lst:
#         if type(i) == list:
#             func(i)
#         else:
#             print(i)
# func(lst)
print("*" * 50)
sums = 0
def func(dirs):
    if os.path.exists(dirs):
        dir_list = os.listdir(dirs)
        global sums
        for i in dir_list:
            if os.path.isdir(os.path.join(dirs, i)):
                func(os.path.join(dirs, i))
            else:
                sums += os.path.getsize(os.path.join(dirs, i))
        return sums
    else:
        return None
print(func("../day5"))

