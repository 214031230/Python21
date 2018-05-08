#!/usr/bin/env python3
import sys
# sys模块是与python解释器交互的一个接口
# sys.argv           命令行参数List，第一个元素是程序本身路径
print(sys.argv)
# sys.exit(n)        退出程序，正常退出时exit(0),错误退出sys.exit(1)
# sys.version        获取Python解释程序的版本信息
print(sys.version)
# sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.path)
# sys.platform       返回操作系统平台名称
print(sys.platform)
# sys.modules        放了所有在解释器运行的过程中导入的模块名
print(sys.modules)
