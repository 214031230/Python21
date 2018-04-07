'''
集合：
    无序，不重复的数据类型。它里面的元素必须是可哈希的。但是集合本身是不可哈希的。
    1：关系测试。交集并集，子集，差集....
    2,去重。（列表的去重）
'''
# set1 = {1,'alex',False,(1,2,3)}
# l1 = [1,1,2,2,3,3,4,5,6,6]
# l2 = list(set(l1))
# print(l2)

# set1 = {'alex','wusir','ritian','egon','barry'}
# 增
# set1.add('666')
# print(set1)

# update
# set1.update('abc')
# print(set1)

#删
# set1 = {'alex','wusir','ritian','egon','barry'}

# set1.remove('alex')  # 删除一个元素
# print(set1)

# set1.pop()  # 随机删除一个元素
# print(set1)
#
# set1.clear()  # 清空集合
# print(set1)
#
# del set1  # 删除集合
# print(set1)


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

#交集 &  intersectio
# print(set1 & set2)
# print(set1.intersection(set2))

#并集 |   union
# print(set1 | set2)
# print(set1.union(set2))

#差集  -  difference
# print(set1 - set2)
# print(set1.difference(set2))

#反交集 ^ symmetric_difference
# print(set1 ^ set2)
# print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}
# set1 = {1,2,3}
# set2 = {1,2,3,4,5,6}

# print(set1 < set2)
# print(set1.issubset(set2))  # 这两个相同，都是说明set1是set2子集。

# print(set2 > set1)
# print(set2.issuperset(set1))

# s = frozenset('barry')
# s1 = frozenset({4,5,6,7,8})
# print(s,type(s))
# print(s1,type(s1))