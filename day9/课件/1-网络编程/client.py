#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
sk = socket.socket()
sk.connect(('127.0.0.1',9999))
# while True:
#     print(sk.recv(1024))
#     sk.send(b'bye')
sk.close()