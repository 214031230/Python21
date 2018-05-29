#!/usr/bin/env python3
import socket
import json
from core.UserManager import User


class FtpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket()
        self.server.bind((host, port))
        self.server.listen()

    def run(self):
        print("Server start")
        while True:
            self.conn, self.address = self.server.accept()
            print(self.address)
            while True:
                if self.login():
                    self.conn.send("True".encode("utf-8"))
                    data = self.conn.recv(1024).decode("utf-8").split()
                    cmd = data[0]
                    if hasattr(self, cmd):
                        func = getattr(self, cmd)
                        func(data)
                    else:
                        print("命令不存在")
                else:
                    self.conn.send("False".encode("utf-8"))
            self.conn.close()

    def login(self):
        data = self.conn.recv(1024)
        username, password = json.loads(data.decode("utf-8"))
        user_obj = User(username, password)
        return user_obj.login()

    def ls(self, data):
        print("in ls")
        pass

    def get(self, data):
        print("in get")
        pass

    def put(self, data):
        print("in put")
        pass

