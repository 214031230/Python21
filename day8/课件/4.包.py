# 一组py文件组成的文件夹，在这个文件夹里有一个__init__.py，包


# 如何从一个包里import模块
# import glance.api.policy as policy
# policy.get()
# import glance.api.policy
# glance.api.policy.get()

# from...import
# from glance.api import policy
# policy.get()

# 为什么模块的导入要从glance开始？
# 精确到一个模块

# import glance
# glance.api.policy.get()  # 不行
# 导入一个文件相当于执行了这个文件中的代码
# __init__文件有什么用？
# 但是导入一个包相当于执行这个包中的init文件
# import后面的这个名字 永远会出现在全局的命名空间里

# import glance       # 绝对导入
# glance.api.policy.get()

# import glance       #相对导入
# # D:\myproject\PY21\day8
# glance.api.policy.get()

# 相对导入
# 带有先对导入路径的文件不能直接执行—— 会报错