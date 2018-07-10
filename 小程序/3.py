# -*- coding: utf-8 -*-
import random as r
import pymysql

first = ('张', '李', '牛', '赵', '金', '艾', '单', '龚', '钱', '周', '吴', '郑', '孔', '曺', '严', '华', '吕', '徐', '何')
middle = ('芳', '军', '建', '明', '辉', '芬', '红', '丽', '功')
last = ('明', '芳', '', '民', '敏', '丽', '辰', '楷', '龙', '雪', '凡', '锋', '芝', '')
name = []
passwd1 = ('1234', '5678', '147', '258')
for i in range(101):
    name1 = r.choice(first) + r.choice(middle) + r.choice(last)
    name2 = name1.rstrip()
    if name2 not in name:
        name.append(name2)
conn = pymysql.connect(host='192.168.10.219', port=3306, user='root', passwd='wanglei', db='store001')
cur = conn.cursor()
for i in range(len(name)):
    passwd = r.choice(passwd1)
    cur.execute("insert into wanglei(name,passwd) values(%s,%s)", (name[i], passwd))
cur.execute('select * from wanglei')
for s in cur.fetchall():
    print(s)
conn.commit()
cur.close()
conn.close()
