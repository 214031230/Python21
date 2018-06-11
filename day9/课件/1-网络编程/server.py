#!/usr/bin/env python
# -*- coding:utf-8 -*-
# tcp协议的socket

import socket
sk = socket.socket()
sk.bind(('127.0.0.1',9999))
sk.listen()   # 允许最大的等待链接数

conn,addr = sk.accept()  # 获取到一个连接
print(conn)
while True:
    conn.send(b'hello')
    msg = conn.recv(1024)
    print(msg)
conn.close()
sk.close()


# server socket  client
#