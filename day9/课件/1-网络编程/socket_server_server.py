#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import socketserver
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        print(conn)
        time.sleep(3)
        conn.send(b'hello')
        time.sleep(5)
        conn.send(b'hello2')
# socketserver
# socket

myserver = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
myserver.serve_forever()

# socketserver所启动的服务端是不能有input操作的
# server端一般都是根据client端的要求去执行固定的代码
# 20函数














