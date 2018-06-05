#!/usr/bin/env python3
import socket
import json
import os
import struct
from core.UserManager import User
from conf import settings
from core.Pubulic import Public
from core.MyJson import MyJson


class FtpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket()
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.home_dir = settings.home_dir
        self.status = False
        self.log = Public.log()
        self.user_size = settings.user_size
        self.user_size_dic = MyJson.load(self.user_size)

    def run(self):
        """启动server等待用户输入指令"""
        print("<---Server start---->")
        while True:
            self.conn, self.address = self.server.accept()
            self.log.info("Run %s:%s" % (self.host, self.port))
            print(self.address)
            if not self.status:
                try:
                    while True:
                        if self.login():
                            self.conn.send("True".encode(settings.code))
                            self.log.info("%s登录成功" % self.username)
                            self.home_path = os.path.abspath(os.path.join(self.home_dir, self.username))
                            break
                        else:
                            self.conn.send("False".encode(settings.code))
                            self.log.info("%s登录失败" % self.username)
                            continue
                    while self.status:
                            data = self.conn.recv(settings.buffer_size).decode(settings.code).split(" ", 1)
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
        data = self.conn.recv(settings.buffer_size)
        self.username, password = json.loads(data.decode(settings.code))
        user_obj = User(self.username, password)
        self.status = user_obj.login()
        return self.status

    def ls(self, data):
        """查看用户家目录下的文件列表，不同操作系统执行不同的系统命令"""
        if len(data) != 1:
            self.conn.send("False".encode(settings.code))
            return
        else:
            self.conn.send("True".encode(settings.code))
        if os.name == "nt":
            ret = os.popen("dir %s" % os.path.abspath(self.home_path)).read()
            self.log.info("%s查看了家目录" % self.username)
        else:
            ret = os.popen("ls -l %s" % os.path.abspath(os.path.join(self.home_dir, self.username))).read()
            self.log.info("%s查看了家目录" % self.username)
        self.conn.send(ret.encode(settings.code))
        print(ret)

    def get(self, data):
        """
         client下载文件操作
        :param data:
        :return:
        """
        file_path = os.path.join(self.home_path, data[1].strip())
        if os.path.isfile(file_path):
            self.conn.send("True".encode(settings.code))
            header_file = {"name": data[1].strip(),
                           "size": os.path.getsize(file_path),
                           "md5": Public.get_md5(file_path)}
            header_file_json = json.dumps(header_file)
            header_file_len = struct.pack("i", len(header_file_json))
            self.conn.send(header_file_len)
            self.conn.send(header_file_json.encode(settings.code))
            with open(file_path, "rb") as f:
                for line in f:
                    self.conn.send(line)
            self.log.info("%s下载了%s文件" % (self.username, data[1].strip()))
        else:
            self.conn.send("False".encode(settings.code))

    def put(self, data):
        """
        client上传文件操作
        :param data:
        :return:
        """
        header_len_bytes = self.conn.recv(4)
        header_len = struct.unpack("i", header_len_bytes)[0]
        header = self.conn.recv(header_len).decode(settings.code)
        header = json.loads(header)
        file_path = os.path.join(self.home_path, header["name"])
        user_home_dir = os.path.join(os.path.join(settings.home_dir, self.username))
        if self.check_home_size(user_home_dir, header["size"]):
            self.conn.send("True".encode(settings.code))
            recv_size = 0
            with open(file_path, "wb") as f:
                while recv_size < header["size"]:
                    line = self.conn.recv(settings.buffer_size)
                    f.write(line)
                    recv_size += len(line)
        else:
            self.conn.send("False".encode(settings.code))
            return
        if Public.get_md5(file_path) == header["md5"]:
            self.conn.send("True".encode(settings.code))
            self.log.info("%s上传了%s文件" % (self.username,  header["name"]))
        else:
            self.conn.send("False".encode(settings.code))

    def check_home_size(self, home_path, recv_size):
        """
        检测用户剩余空间
        :param home_path: 用户家目录
        :param recv_size: 上传文件大小
        :return:
        """
        Public.sum_size = 0
        home_size = self.user_size_dic[self.username] * 1024 * 1024
        user_size = Public.dir_size(home_path)
        surplus_size = home_size - user_size
        if surplus_size < recv_size:
            self.log.error("%s磁盘空间不足" % self.username)
            return False
        else:
            return True

    def du(self, data):
        """获取用户存储使用情况"""
        Public.sum_size = 0
        if len(data) != 1:
            self.conn.send("False".encode(settings.code))
            return
        else:
            self.conn.send("True".encode(settings.code))
        total = self.user_size_dic[self.username] * 1024 * 1024
        use = Public.dir_size(os.path.abspath(os.path.join(os.path.join(settings.home_dir, self.username))))
        residual = total - use
        status = {"User": self.username,
                  "Total_size": "%s M" % (total/1024/1024),
                  "Use_size": "%s M" % (use/1024/1024),
                  "Residual_size": "%s M" % (residual/1024/1024)}
        print(status)
        status_json_bytes = json.dumps(status).encode(settings.code)
        self.conn.send(status_json_bytes)

    def cd(self, data):
        """切换目录"""
        if data[1] == "..":
            if os.path.basename(self.home_path) == self.username:
                print("已经到最顶层")
                self.conn.send("False".encode(settings.code))
            else:
                self.home_path = os.path.dirname(self.home_path)
                print(self.home_path)
                self.conn.send("True".encode(settings.code))
        else:
            if os.path.exists(os.path.join(self.home_path, data[1])):
                self.home_path = os.path.join(self.home_path, data[1])
                self.conn.send("True".encode(settings.code))
            else:
                self.conn.send("False".encode(settings.code))

    def mkdir(self, data):
        """创建目录"""
        home_path = os.path.join(os.path.abspath(self.home_path))
        mk_path = os.path.join(home_path, data[1])
        if not os.path.exists(mk_path):
            os.makedirs(mk_path)
            self.conn.send("True".encode(settings.code))
            self.log.info("%s创建了%s目录" % (self.username, data[1]))
        else:
            self.conn.send("False".encode(settings.code))

    def rm(self, data):
        """删除文件或者目录"""
        desdir = os.path.join(self.home_path, data[1])
        if os.path.exists(desdir):
            try:
                print(desdir)
                if os.path.isfile(desdir):
                    os.remove(desdir)
                else:
                    os.rmdir(desdir)
            except Exception as e:
                self.log.error("%s" % e)
                print(e)
                self.conn.send("False".encode(settings.code))
            else:
                self.conn.send("True".encode(settings.code))

    def exit(self, data):
        if len(data) != 1:
            self.conn.send("False".encode(settings.code))
            return
        else:
            self.conn.send("True".encode(settings.code))
        self.conn.close()