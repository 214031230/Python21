#!/usr/bin/env python3
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        print(conn)


my_server = socketserver.ThreadingTCPServer(("127.0.0.1", 9000), MyServer)
my_server.serve_forever()