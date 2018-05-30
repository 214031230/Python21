#!/usr/bin/env python3
import socket
import json
import struct
import os
from conf import settings
from core.Pubulic import Public


class FtpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket()
        self.client.connect((host, port))
        
    def run(self):
        """启动client，用户输入指令"""
        Public.helper()
        if self.login():
            print("INFO：登录成功，请输入指令")
            while True:
                data = input(">>>:").strip()
                if not data:continue
                if data.upper() == "EXIT":break
                cmd = data.split()[0]
                if hasattr(self, cmd):
                    self.client.send(data.encode("utf-8"))
                    getattr(self, cmd)(data)
                else:
                    print("Error：命令不存在")

    def login(self):
        """客户端登录"""
        count = 0
        while count < 3:
            self.username = input(">>>User:").strip()
            self.password = input(">>>Password:").strip()
            if not self.username or not self.password:continue
            user_info = (self.username, self.password)
            user_info_json = json.dumps(user_info)
            self.client.send(user_info_json.encode("utf-8"))
            if self.client.recv(1024).decode("utf-8") == "True":
                return True
            else:
                print("Error：用户或密码错误")
            count += 1
        else:
            return False

    def ls(self, data):
        """客户端接受ls执行返回的结果并打印"""
        ret = self.client.recv(1024).decode("utf-8")
        if ret != "False":
            ret = self.client.recv(1024).decode("utf-8")
            print(ret)
        else:
            print("Error：ls不需要带参数")

    def get(self, data):
        """下载文件"""
        ret = self.client.recv(1024).decode("utf-8")
        if ret != "False":
            check_file = self.client.recv(1024).decode("utf-8")
            if check_file == "True":
                header_len_bytes = self.client.recv(4)
                header_len = struct.unpack("i", header_len_bytes)[0]
                header = self.client.recv(header_len).decode("utf-8")
                header = json.loads(header)
                file_path = os.path.join(settings.download, header["name"])
                recv_size = 0
                with open(file_path, "wb") as f:
                    while recv_size < header["size"]:
                        line = self.client.recv(1024)
                        f.write(line)
                        recv_size += len(line)
                if Public.get_md5(file_path) == header["md5"]:
                    print("INFO：下载成功")
                else:
                    print("ERROR：下载失败")

            else:
                print("Error：文件不存在")
        else:
            print("Error：请输入正确的指令")

    def put(self, data):
        """上传文件"""
        ret = self.client.recv(1024).decode("utf-8")
        if ret != "False":
            data = data.split()
            file_path = data[1]
            file_name = os.path.basename(file_path)
            if os.path.exists(file_path):
                header_file = {"name": file_name,
                               "size": os.path.getsize(file_path),
                               "md5": Public.get_md5(file_path)}

                header_file_json = json.dumps(header_file)
                header_file_len = struct.pack("i", len(header_file_json))
                self.client.send(header_file_len)

                self.client.send(header_file_json.encode("utf-8"))

                with open(file_path, "rb") as f:
                    for line in f:
                        self.client.send(line)
                if self.client.recv(1024).decode("utf-8") == "True":
                    print("INFO：上传成功")
                else:
                    print("ERROR：上传失败")

            else:
                print("Error：文件不存在")
        else:
            print("Error：请输入正确的指令")
