#!/usr/bin/env python3
import socketserver
# socketserver所启动的服务端是不能有input操作的
# server端一般都是根据client端的要求去执行固定的代码


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            msg = conn.recv(1024).decode("utf-8")
            address = self.client_address
            if hasattr(self, msg):
                print("%s:%s" % (address, msg))
                getattr(self, msg)()

    def ls(self):
        print("%s:in ls" % self.client_address[1])

    def du(self):
        print("%s:in du" % self.client_address[1])


my_server = socketserver.ThreadingTCPServer(("127.0.0.1", 9000), MyServer)
my_server.serve_forever()