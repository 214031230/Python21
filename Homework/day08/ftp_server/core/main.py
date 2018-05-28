#!/usr/bin/env python3
import socket
import json
from conf import settings


def socket_server():
    sk = socket.socket()
    sk.bind((settings.bind_ip, settings.bind_port))
    sk.listen()

    while True:
        conn, address = sk.accept()
        msg = conn.recv(1024)
        username, password = json.loads(msg)
        with open(settings.user_info) as f:
            for i in f:
                i = i.strip()
                user, pwd = i.split("|")
                if username == user and password == pwd:
                    conn.send("Success".encode("utf-8"))
            else:
                conn.send("Fail".encode("utf-8"))
        conn.close()

