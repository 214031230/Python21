#!/usr/bin/env python3
import socket
from threading import Thread
sk = socket.socket()
sk.bind(("127.0.0.1", 9000))
sk.listen()


def run():
    conn, address = sk.accept()
    while 1:
        msg = conn.recv(1024).decode("utf-8")
        if msg.lower() == "q":break
        print("%s:%s" % (address, msg))
    conn.close()


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=run)
        t.start()


