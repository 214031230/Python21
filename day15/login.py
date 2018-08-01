#!/usr/bin/env python3
import pymysql
username = input("user:").strip()
password = input("password:").strip()
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    database="test",
    user="root",
    password="@@spf"
)

cursor = conn.cursor()


# sql = "select id from user where username=%s and password=%s"
sql = "insert into user(username,password) values(%s,%s)"


ret = cursor.execute(sql, (username, password))
conn.commit()
cursor.close()
conn.close()