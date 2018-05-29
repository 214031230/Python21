#!/usr/bin/env python3
import socket
import json


class FtpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket()
        self.client.connect((host, port))
        
    def run(self):
        if self.login():
            while True:
                data = input(">>>:").strip()
                if not data:break
                self.client.send(data.encode("utf-8"))

    def login(self):
        count = 0
        while count < 3:
            username = input(">>>User:").strip()
            password = input(">>>Password:").strip()
            if not username or not password:continue
            user_info = (username, password)
            user_info_json = json.dumps(user_info)
            self.client.send(user_info_json.encode("utf-8"))
            if self.client.recv(1024).decode("utf-8") == "True":
                return True
            else:
                print("用户或密码错误")
            count += 1
        else:
            return False

    def ls(self, data):
        print("in ls")
        pass

    def get(self, data):
        print("in get")
        pass

    def put(self, data):
        print("in put")
        pass
