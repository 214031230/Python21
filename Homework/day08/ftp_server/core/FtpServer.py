#!/usr/bin/env python3
import socket
import json
import os
import struct
from core.UserManager import User
from conf import settings
from core.Pubulic import Public


class FtpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket()
        self.server.bind((host, port))
        self.server.listen()
        self.home_dir = settings.home_dir
        self.status = False
        self.log = Public.log()

    def run(self):
        """启动server等待用户输入指令"""
        print("<---Server start---->")
        while True:
            self.conn, self.address = self.server.accept()
            print(self.address)
            if not self.status:
                try:
                    while True:
                        if self.login():
                            self.conn.send("True".encode("utf-8"))
                            self.log.info("%s登录成功" % self.username)
                            break
                        else:
                            self.conn.send("False".encode("utf-8"))
                            self.log.info("%s登录失败" % self.username)
                            continue
                    while self.status:
                            data = self.conn.recv(1024).decode("utf-8").split(" ", 1)
                            cmd = data[0]
                            if hasattr(self, cmd):
                                getattr(self, cmd)(data)
                            else:
                                print("命令不存在")
                except Exception as e:
                    print(e)
                    self.log.error(e)
                finally:
                    self.status = False
                    self.conn.close()

    def login(self):
        """用户登录，登录成功返回True,失败返回False，修改self.status为True或者False"""
        data = self.conn.recv(1024)
        self.username, password = json.loads(data.decode("utf-8"))
        user_obj = User(self.username, password)
        self.status = user_obj.login()
        return self.status

    def ls(self, data):
        """查看用户家目录下的文件列表，不同操作系统执行不同的系统命令"""
        if len(data) != 1:
            self.conn.send("False".encode("utf-8"))
            return
        else:
            self.conn.send("True".encode("utf-8"))
        if os.name == "nt":
            ret = os.popen("dir %s" % os.path.abspath(os.path.join(self.home_dir, self.username))).read()
            self.log.info("%s查看了家目录" % self.username)
        else:
            ret = os.popen("ls -l %s" % os.path.abspath(os.path.join(self.home_dir, self.username))).read()
            self.log.info("%s查看了家目录" % self.username)
        self.conn.send(ret.encode("utf-8"))
        print(ret)

    def get(self, data):
        """
         client下载文件操作
        :param data:
        :return:
        """
        file_path = os.path.join(os.path.join(self.home_dir, self.username), data[1].strip())
        if os.path.isfile(file_path):
            self.conn.send("True".encode("utf-8"))
            header_file = {"name": data[1].strip(),
                           "size": os.path.getsize(file_path),
                           "md5": Public.get_md5(file_path)}
            header_file_json = json.dumps(header_file)
            header_file_len = struct.pack("i", len(header_file_json))
            self.conn.send(header_file_len)
            self.conn.send(header_file_json.encode("utf-8"))
            with open(file_path, "rb") as f:
                for line in f:
                    self.conn.send(line)
            self.log.info("%s下载了%s文件" % (self.username, data[1].strip()))
        else:
            self.conn.send("False".encode("utf-8"))

    def put(self, data):
        """
        client上传文件操作
        :param data:
        :return:
        """
        header_len_bytes = self.conn.recv(4)
        header_len = struct.unpack("i", header_len_bytes)[0]
        header = self.conn.recv(header_len).decode("utf-8")
        header = json.loads(header)
        file_path = os.path.join(os.path.join(settings.home_dir, self.username), header["name"])
        user_home_dir = os.path.join(os.path.join(settings.home_dir, self.username))
        if self.check_home_size(user_home_dir, header["size"]):
            self.conn.send("True".encode("utf-8"))
            recv_size = 0
            with open(file_path, "wb") as f:
                while recv_size < header["size"]:
                    line = self.conn.recv(1024)
                    f.write(line)
                    recv_size += len(line)
        else:
            self.conn.send("False".encode("utf-8"))
        if Public.get_md5(file_path) == header["md5"]:
            self.conn.send("True".encode("utf-8"))
            self.log.info("%s上传了%s文件" % (self.username,  header["name"]))
        else:
            self.conn.send("False".encode("utf-8"))

    def check_home_size(self, home_path, recv_size):
        """
        检测用户剩余空间
        :param home_path: 用户家目录
        :param recv_size: 上传文件大小
        :return:
        """
        home_size = settings.home_size * 1024 * 1024
        user_size = Public.dir_size(home_path)
        surplus_size = home_size - user_size
        if surplus_size < recv_size:
            self.log.error("%s磁盘空间不足" % self.username)
            return False
        else:
            return True

    def du(self, data):
        """获取用户存储使用情况"""
        if len(data) != 1:
            self.conn.send("False".encode("utf-8"))
            return
        else:
            self.conn.send("True".encode("utf-8"))
        total = settings.home_size*1024*1024
        use = Public.dir_size(os.path.join(os.path.join(settings.home_dir, self.username)))
        residual = total - use
        status = {"User": self.username,
                  "Total_size": total,
                  "Use_size": use,
                  "Residual_size": residual}
        status_json_bytes = json.dumps(status).encode("utf-8")
        self.conn.send(status_json_bytes)

    def exit(self, data):
        if len(data) != 1:
            self.conn.send("False".encode("utf-8"))
            return
        else:
            self.conn.send("True".encode("utf-8"))
        self.conn.close()


