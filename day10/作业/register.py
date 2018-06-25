#!/usr/bin/env python3
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        addr = self.client_address
        print(conn)
        print(addr)


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(("127.0.0.1",9000),MyServer)
    server.serve_forever()