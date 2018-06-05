#!/usr/bin/env python3
import socket
import struct
import os
import json
import hashlib
IP = "127.0.0.1"
PORT = 9999


class FtpServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = socket.socket()
        self.server.bind((ip, port))
        self.server.listen()
        self.code = "utf-8"
        self.buffer_size = 8192
        self.upload = "./server"

    def file(self):
        flag = True
        while flag:
            try:
                self.conn, self.address = self.server.accept()
                while flag:
                    header_len = struct.unpack("i", self.conn.recv(4))[0]
                    print("header_len:", header_len)
                    header = self.conn.recv(header_len).decode(self.code)
                    header = json.loads(header)
                    print("header:", header)
                    filepath = os.path.join(self.upload, header["name"])
                    print("filepath:", filepath)
                    with open(filepath, "wb") as f:
                        recv_size = 0
                        while recv_size < header["size"]:
                            line = self.conn.recv(self.buffer_size)
                            f.write(line)
                            recv_size += len(line)

            except Exception as e:
                print(e)

    @staticmethod
    def check_file(header_md5, file_path):
        if FtpServer.file_md5(file_path) == header_md5:
            return True
        else:
            return False

    @staticmethod
    def file_md5(file_path):
        with open(file_path, "rb") as f:
            md5obj = hashlib.md5()
            for i in f:
                md5obj.update(i)
            return md5obj.hexdigest()


obj = FtpServer(IP, PORT)
obj.file()