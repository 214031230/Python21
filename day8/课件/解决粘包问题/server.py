import socket
import struct
sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()

conn,addr = sk.accept()
inp = input('>>>').encode('utf-8')
inp_len = len(inp)
bytes_msg = struct.pack('i',inp_len)
conn.send(bytes_msg)
conn.send(inp)
conn.send(b'alex sb')

conn.close()
sk.close()
