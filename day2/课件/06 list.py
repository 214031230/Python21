# li = [111,'alex',222,'wusir']
# print(li[1])  # alex
# print(li[-1])  # wusir
# print(li[:2])  # [111, 'alex']
# print(li[:3:2]) # [111, 222]
l = ['老男孩', 'alex', 'wusir', 'taibai', 'ritian']
#增
# append 在最后追加
# l.append('葫芦')
# l.append([1,2,3])
# print(l)
#
# insert 插入
# l.insert(1,'景nvshen')
# print(l)
#
# 迭代着添加
# l.extend('alex')
# l.extend(['111',222,333])
# print(l)

# 删
#pop 有返回值  按照索引删除
# print(l.pop(0))
# print(l)

#remove
# l.remove('alex')
# print(l)

#clear 清空列表
# l.clear()
# print(l)

#del 内存级别删除列表
# del l
# print(l)
#按索引删除
# del l[1]
# print(l)

#切片删除
# del l[:3]
# print(l)

# 改
# 按照索引改
# print(l[2])
# l[2] = '武藤兰'
# print(l)
#
# 按照切片去改
# l[:2] = 'abc'
# print(l)
# l[1:3] = [111,222,333,444]
# print(l)

# 查
#按照索引去查询，按照切片去查询
# for i in l:
#     print(i)

# l1 = [1,2,1,2,1,1,3,4]

# 其他方法：
#count 计数
# print(l1.count(1))

#len
# print(len(l1))

#通过元素找索引
# print(l1.index(2))

# l2 = [3,2,4,6,9,8,7,1]

#sort
# l2.sort()  从小到大
# print(l2)
# l2.sort(reverse=True)  #从大到小排序
# print(l2)

#reverse
# l2.reverse()
# print(l2)


# #列表的嵌套
# l1 = [1, 2, 'alfdsafex', 'wusir',['oldboy', 'ritian', 99], 'taibai']
# l2 = [1, 2, 'alfdsafex', 'wusir',['oldboy', 'ritian', 10], 'taibai']
#
# # 1,将'alex'全部变成大写，放回原处。
# # 方法1
# l1[2] = 'ALEX'
# # 方法2
# l1[2] = l1[2].upper()
# print(l1)
#
# # 2，给['oldboy', 'ritian', 99] 追加一个元素‘女神’。 一个方法
# l1[-2].append('女神')
# print(l1)
#
# # 3，将'ritian'首字母大写，放回原处。
# l1[-2][1] = l1[-2][1].capitalize()
# print(l1)
#
# # 4，将99通过数字相加，或者字符串相加或者等等，变成'100'
# l1[-2][-1] = str(l1[-2][-1] + 1)
# print(l1)
#
# l2[-2][-1] = str(l1[-2][-1]) + '0'
# print(l2)

# a = 2 ** 8
# print(a)