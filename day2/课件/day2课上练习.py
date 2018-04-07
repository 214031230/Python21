l1 = [1, 2, 'alex', 'wusir',['oldboy', 'ritian', 10], 'taibai']
#1.将'alex'全部变成大写,放回原处
#2.给['oldboy', 'ritian', 99]追加一个元素'女神'
#3.将'ritian'首字母大写,放回原处
#4.将10通过数字相加,或者字符串相加变成100

l1 = [1, 2, 'alex', 'wusir',['oldboy', 'ritian', 10], 'taibai']
l1[2]=l1[2].upper()
l1[4].append('女神')
l1[4][1]=l1[4][1].capitalize()
l1[4][2]=str(l1[4][2]+90)
print(l1)
l1[4][2]=int(l1[4][2])-90
l1[4][2]=str(l1[4][2])+'0'
print(l1)

#######练习2###########
dic = {
    'name_list':['b哥', '张帝', '人帅', 'kitty'],
    '老男孩':{
        'name':'老男孩',
        'age': 46,
        'sex': 'ladyboy',
    },
}
#1,['b哥', '张帝', '人帅', 'kitty']追加一个元素，'骑兵'
#2，将kitty全部变成大写。
#3，将老男孩 改成oldboy。
#，将ladyboy首字母大写。
dic['name_list'].append('骑兵')
dic['name_list'][-2]=dic['name_list'][-2].upper()
dic['老男孩']['name']='oldboy'
dic['老男孩']['sex']=dic['老男孩']['sex'].capitalize()
print(dic)