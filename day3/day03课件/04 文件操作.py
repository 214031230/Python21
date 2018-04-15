# f1 = open('D:\空姐护士老师主妇.txt', encoding='utf-8', mode='r')
# content = f1.read()
# print(content)
# f1.close()

# read 全部读出
# f1 = open('log1', encoding='utf-8')
# content = f1.read()  #
# print(content)
# f1.close()

#read(n)
# f1 = open('log1', encoding='utf-8')
# content = f1.read(5)  # r 模式 按照字符读取。
# print(content)
# f1.close()

# f1 = open('log1', mode='rb')
# content = f1.read(3)  # rb模式 按照字节读取。
# print(content.decode('utf-8'))
# f1.close()

#readline（）按行读取
# f1 = open('log1', encoding='utf-8')
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
# f1.close()

#readlines() 将每一行作为列表的一个元素并返回这个列表
# f1 = open('log1', encoding='utf-8')
# print(f1.readlines())
# f1.close()

#for循环
# f1 = open('log1', encoding='utf-8')
# for i in f1:
#     print(i)
# f1.close()


# f2 = open('log1',mode='rb')
# print(f2.read())
# f2.close()
#编码的补充：\
# s1 = b'\xd6\xd0\xb9\xfa'
# s2 = s1.decode('gbk')
# s3 = s2.encode('utf-8')
# print(s3)  # b'\xe4\xb8\xad\xe5\x9b\xbd'
# s1 = b'\xd6\xd0\xb9\xfa'.decode('gbk').encode('utf-8')
# print(s1)

#r+ 读写
# f1 = open('log1', encoding='utf-8', mode='r+')
# print(f1.read())
# f1.write('666')
# f1.close()

# f1 = open('log1', encoding='utf-8', mode='r+')
# f1.seek(0,2)
# f1.write('6666')
# f1.seek(0)#调整光标
# print(f1.read())
# #光标 按照字节去运转 seek
# f1.close()



# w模式
# f1 = open('log2', encoding='utf-8', mode='w')
# f1.write('alex是披着高富帅外衣的纯屌丝.....')
# f1.close()
# f1 = open('log2', mode='wb')
# f1.write('alex是披着高富帅外衣的纯屌丝.....'.encode('utf-8'))
# f1.close()

#w+ 写读模式
# f1 = open('log2', encoding='utf-8', mode='w+')
# print(f1.read())
# f1.write('666')
# f1.close()





#a ab
# f1 = open('log2', encoding='utf-8', mode='a')
# f1.write('\n老男孩')
# f1.close()

#a+
# f1 = open('log2', encoding='utf-8', mode='a+')
# f1.write('fdsafdsafdsagfdg')
# f1.seek(0)
# print(f1.read())
# f1.close()


#其他操作方法：
#read read(n) readline() readlines() write() close
#readable writable
#tell 告诉指针的位置
# f1 = open('log2', encoding='utf-8', mode='w')
# f1.write('fdsafdsafdsagfdg')
# print(f1.tell())
# f1.close()
#seek(参数)，seek(0,2) 调至最后 按照字节去调整光标

# with open() as：
# with open('log1', encoding='utf-8') as f1,\
#         open('log2', encoding='utf-8', mode='w')as f2:
#     print(f1.read())
#     f2.write('777')

#文件的改
#1,打开原文件，产生文件句柄。
#2，创建新文件，产生文件句柄。
#3，读取原文件，进行修改，写入新文件。
#4，将原文件删除。
#5，新文件重命名原文件。

# import os
# with open('file_test', encoding='utf-8') as f1,\
#     open('file_test.bak', encoding='utf-8', mode='w') as f2:
#     old_content = f1.read()
#     new_content = old_content.replace('alex','SB')
#     f2.write(new_content)
# os.remove('file_test')
# os.rename('file_test.bak','file_test')


import os
with open('file_test', encoding='utf-8') as f1,\
    open('file_test.bak', encoding='utf-8', mode='w') as f2:
    for line in f1:
        new_line = line.replace('SB','alex')
        f2.write(new_line)
os.remove('file_test')
os.rename('file_test.bak','file_test')


