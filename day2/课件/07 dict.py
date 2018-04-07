'''
字典的key是唯一的。key 必须是不可变的数据类型。
    key:不可变的数据类型(可哈希)：str，bool，tuple，int。
    value：任意数据类型。
        数据类型分类：
            不可变的数据类型(可哈希)：str，bool，tuple，int
            可变的数据类型：dict，list，set。
            容器类数据类型：list，tuple，dict，set.
字典：存储数据多，关系型数据，查询速度快（二分查找）。
3.6版本之前，字典是无序的，3.6之后字典是有序的。
'''
# dic = {'name':'taibai','age':21,'hobby':'girl',}
# print(dic)
dic = {'name': 'taibai', 'age': 21, 'hobby': 'girl', }
#增
#  dic['high'] 有则覆盖，无则添加
# dic['high'] = 180
# dic['name'] = 'ritian'
# print(dic)
# dic.setdefault() 有则不变，无则添加
# dic.setdefault('high')
# dic.setdefault('high',180)
# dic.setdefault('name','日天')
# print(dic)
# 删
# print(dic.pop('name'))  # 返回值 对应的值
# print(dic.pop('name1','没有此key sb'))
# print(dic)
# print(dic)
# dic.clear()  # 清空
# print(dic)
# print(dic.popitem())  #随机删除，返回值
# print(dic)
# del dic
# print(dic)
# del dic['age']
# print(dic)
# 改
# dic['name'] = '老男孩'
# print(dic)

# dic = {"name":"jin","age":18,"sex":"male"}
# dic2 = {"name":"alex","weight":75}
# dic2.update(dic)  # 将dic的键值对覆盖添加到dic2中，dic不变。
# print(dic)
# print(dic2)
#查
# print(dic['name2'])
# print(dic.get('name'))
# print(dic.get('name1'))
# print(dic.get('name1','没有此key，sb'))

#keys() values() items()
# print(list(dic.keys()))
# for i in dic.keys():
#     print(i)

# print(dic.values())
# for i in dic.values():
#     print(i)

# print(list(dic.items()))
# for i in dic.items():
#     print(i)

#分别赋值
# a,b = 1,2
# a,b,c = ['alex', 'wusir', 'ritain']
# print(a,b,c)
# a = 1
# b = 5
# a,b = b,a
# print(a,b)
# for i in dic.items():
#     print(i)
#
# for k,v in dic.items():
#     print(k,v)

#len
# print(len(dic))

#fromkeys
# dic1 = dict.fromkeys('abc','张三')
# dic2= dict.fromkeys([1,2,3],'李四')
# print(dic2)

# dic3 = dict.fromkeys('abc',[])
# # print(dic3)
# dic3['a'].append('老男孩')
# print(dic3)

#字典的嵌套

dic = {
    'name_list':['b哥', '张帝', '人帅', 'kitty'],
    '老男孩':{
        'name':'老男孩',
        'age': 46,
        'sex': 'ladyboy',
    },
}
#1,['b哥', '张帝', '人帅', 'kitty']追加一个元素，'骑兵'
# dic['name_list'].append('骑兵')
# print(dic)
#2，将kitty全部变成大写。
# l1 = dic['name_list']
# print(l1[-1].upper())
# l1[-1] = l1[-1].upper()
# print(dic)
# dic['name_list'][-1] = dic['name_list'][-1].upper()
# print(dic)

#3，将老男孩 改成oldboy。
# dic['老男孩']['name'] = 'oldboy'
# print(dic)
#，将ladyboy首字母大写。
# dic['老男孩']['sex'] = dic['老男孩']['sex'].capitalize()
# print(dic)

