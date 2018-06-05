#!/usr/bin/env python3
import socket
import struct
import os
import hashlib
import json
IP = "127.0.0.1"
PORT = 9999


class FtpClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client = socket.socket()
        self.client.connect((ip, port))
        self.code = "utf-8"
        self.buffer_size = 8192
        self.upload = "./client"

    def file(self):
        flag = True
        while flag:
            file = input(">>>:")
            header = {"name": os.path.basename(file),
                      "size": os.path.getsize(file),
                      "md5": FtpClient.file_md5(file)}
            header_json = json.dumps(header)
            self.client.send(struct.pack("i", len(header_json)))
            self.client.send(header_json.encode(self.code))
            with open(file, "rb") as f:
                for i in f:
                    self.client.send(i)

    @staticmethod
    def file_md5(file_path):
        with open(file_path, "rb") as f:
            md5obj = hashlib.md5()
            for i in f:
                md5obj.update(i)
            return md5obj.hexdigest()


obj = FtpClient(IP, PORT)
obj.file()