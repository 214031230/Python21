#!/usr/bin/env python3
import socket
import re
class MyServer:
    def __init__(self,ip,port):
        self.server = socket.socket()
        self.server.bind((ip, port))
        self.server.listen()
    def run(self):
        """
        启动服务
        :return:
        """
        print("server is running")
        while 1:
            self.conn, self.addr = self.server.accept()
            while True:
                try:
                    msg = self.conn.recv(1024).decode("utf-8")
                    ret = re.search("GET.*username.*password.*HTTP", msg).group()
                    username = re.search(r"username=.*&",ret).group().split("=")[1].split("&")[0]
                    password = ret.split("&")[1].split()[0].split("=")[1]
                    if self.login(username,password):
                        self.conn.send(b"HTTP/1.1 200 OK\r\n\r\n<html><body>OK</body></html>")
                        self.conn.close()
                    else:
                        self.conn.send(b"HTTP/1.1 200 OK\r\n\r\n<html><body>ERROR</body></html>")
                        self.conn.close()
                except Exception as e:
                    print(e)
                    break

    def login(self,username,password):
        print("地址:%s 用户名：%s 密码：%s" % (self.addr,username,password))
        if username == "spf" and password == "123":
            return True
        else:
            return False


server = MyServer("127.0.0.1",9000)
server.run()


