#!/usr/bin/env python3
import socket
import time
sk = socket.socket()
sk.connect(("127.0.0.1", 9000))
time.sleep(10)
sk.close()