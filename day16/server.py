#!/usr/bin/env python3
import socket

server = socket.socket()
server.bind(("127.0.0.1", 8000))
server.listen()

while 1:
    conn, address = server.accept()
    data = conn.recv(8096)
    print(data)
    conn.send("你好".encode("utf-8"))
    conn.close()
    server.close()
    break
"""
    GET / HTTP/1.1\r\n
    Host: 127.0.0.1:8000\r\n
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:40.0) Gecko/20100101 Firefox/40.0\r\n
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n
    Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3\r\n
    Accept-Encoding: gzip, deflate\r\n
    Connection: keep-alive\r\n\r\n

"""
