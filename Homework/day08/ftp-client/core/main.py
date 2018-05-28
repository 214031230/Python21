#!/usr/bin/env python3
import socket
import json
from conf import settings


def socket_client():
    sk = socket.socket()
    sk.connect((settings.server_ip, settings.server_port))
    
    username = input(">>>User:").strip()
    password = input(">>>Password").strip()
    
    user_info = (username, password)
    sk.send(json.dumps(user_info).encode("utf-8"))
    ret = sk.recv(1024)
    print(ret.decode("utf-8"))
    
    sk.close()