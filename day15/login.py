#!/usr/bin/env python3
import pymysql
username = input("user:").strip()
password = input("password:").strip()
conn = pymysql.connect(
    host="127.0.01",
    port=3306,
    database="test",
    user="root",
    password="@@spf"
)

cursor = conn.cursor()


sql = "select id from user where username=%s and password=%s"


ret = cursor.execute(sql, (username, password))

if ret:
    print("登录成功！")
else:
    print("用户名密码错误！")