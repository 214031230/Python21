import socket
import struct
sk = socket.socket()
sk.connect(('127.0.0.1',8080))
num = sk.recv(4)
num = struct.unpack('i',num)[0]
print(sk.recv(num))
print(sk.recv(10))
# dic = {'filename':'client','filesize':'os.path.getsize('路径')'}
# str_dic = json.dumps(dic).encode('utf-8')
# len(str_dic)
# struct.pack()
# dic_len = send(dic_len)
# send(str_dic)
sk.close()

# 通读网络编程的博客
# 登录 ——上传下载功能，解决粘包
# 进阶需求
