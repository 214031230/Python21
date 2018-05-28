#!/usr/bin/env python3
# 模块总结
# 能不能导入模块 ： sys.path
# 导入模块的顺序 ： 内置模块 扩展模块 自定义模块
# 导入模块 ： 相当于执行了这个模块，文件中的名字会被存储在一块独立的内存空间中
# 一个模块如果执行多次import，只会执行一次
# 模块之间不能发生循环引用。

# import
# 在全局创建了一个模块名，指向属于这个模块的命名空间
# 空间里存储了所有文件中的名字
# 起别名 import ... as ..
# 不推荐一行导入多个模块

# from import
# import后面的名字会出现在全局 ，相当于对独立命名空间中的一个引用
# from import 也支持 as语句 也支持 导入多个名字
# from import * 相当于导入所有名字,*和被导入模块__all__是互相影响的

# 包
# 定义:一组py文件组成的文件夹，在这个文件夹里有一个__init__.py 叫做包
# 导入一个模块相当于执行了模块中的代码
# 导入一个包相当于执行了__init__.py的代码
# 相对导入:以glance作为起始
# from ..cmd import manage
# manage.main()
# 绝对导入:用.或者..的方式最为起始（只能在一个包中使用，不能用于不同目录内）
# from glance.cmd import manage
# manage.main()















