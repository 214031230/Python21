# 登录 —— hashilib
# 数据库泄露
# 存储用户密码的时候 ： 不要存储明文
# 对用户输入的密码进行一种计算 计算之后 会得到一个新的 固定的 字符串

# hashlib模块  摘要算法  --->  单向不可逆
# 包含了多种算法
# 将一个字符串进行摘要运算 拿到不变的 固定长度的值
# import hashlib
# md5obj = hashlib.md5()   # 实例化一个md5摘要算法的对象
# md5obj.update('alex3714'.encode('utf-8')) # 使用md5算法的对象来操作字符串
# ret = md5obj.hexdigest() # 获取算法的结果 hex+digest 16进制+消化
# print(ret,type(ret),len(ret))
# 注册 ：alex3714  -摘要-> 文件里
# 登录 ：alex3714  -摘要-> 和文件里比对
# md5obj = hashlib.sha1()   # 实例化一个md5摘要算法的对象
# md5obj.update('alex3714'.encode('utf-8')) # 使用md5算法的对象来操作字符串
# ret = md5obj.hexdigest() # 获取算法的结果 hex+digest 16进制+消化
# print(ret,type(ret),len(ret))

# 撞库
# 别人有一个庞大的库 ：字符串 --> md5值的关系
# 加盐
# md5obj = hashlib.md5('tesla'.encode('utf-8'))   # 实例化一个md5摘要算法的对象，加盐
# md5obj.update('alex3714'.encode('utf-8')) # 使用md5算法的对象来操作字符串
# ret = md5obj.hexdigest() # 获取算法的结果 hex+digest 16进制+消化
# #aee949757a2e698417463d47acac93df
# print(ret)

# 动态加盐
# userinfo表
# username = 'alex'
# md5obj = hashlib.md5(username.encode('utf-8'))   # 实例化一个md5摘要算法的对象，加盐
# md5obj.update('alex3714'.encode('utf-8')) # 使用md5算法的对象来操作字符串
# ret = md5obj.hexdigest() # 获取算法的结果 hex+digest 16进制+消化
# #aee949757a2e698417463d47acac93df
# print(ret)

# 校验文件一致性
# 自动化 —— python代码来做验证
# import hashlib
# md5obj = hashlib.md5()   # 实例化一个md5摘要算法的对象
# md5obj.update('alex'.encode('utf-8')) # 使用md5算法的对象来操作字符串
# md5obj.update('3714'.encode('utf-8')) # 使用md5算法的对象来操作字符串
# print(md5obj.hexdigest())

# aee949757a2e698417463d47acac93df
# aee949757a2e698417463d47acac93df

# 写一个函数 接收两个文件的地址 返回T/F
