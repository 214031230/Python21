# r = 只读模式，读的时候注意文件编码，如果被读文件是gbk编码，读的时候需指定encoding = "gbk"（在不知道文件编码的情况下，可以通过第三方模块chardet获取文件编码）
# rb = 以二进制方式读，一般操作图片、视频等非文字类文件。
# r+ = 以读写的方式读，先读在写入，顺序不能变！
# r+b = 以二进制的方式进行读写。
# read() 文件路径可以使用绝对路径和相对路径，如果文件和py在同一目录则使用相对路径
f1 = open('D:\logo.txt', encoding='utf-8', mode='r')
content = f1.read()
print(content)
f1.close()

# read 全部读出，mode默认是r
f1 = open('log1', encoding='utf-8')
content = f1.read()
print(content)
f1.close()

# read(n) 在mode=r的情况下按照字符读取
f1 = open('log1', encoding='utf-8')
content = f1.read(5)  # r 模式 按照字符读取。
print(content)
f1.close()

# read(n) 在mode=rb的情况下按照字节读取，注意编码中文占的位数，位数不对会乱码
f1 = open('log1', mode='rb')
content = f1.read(3)  # rb模式 按照字节读取。
print(content.decode('utf-8'))  # utf-8 一个中文占3个字节
f1.close()

# readline() 逐行读取，每次只读取一行
f1 = open('log1', encoding='utf-8')
print(f1.readline())  # 读取第一行
print(f1.readline())  # 读取第二行
print(f1.readline())  # 读取第三行
print(f1.readline())  # 读取第四行
f1.close()

# readlines() 将每一行作为列表的一个元素并返回这个列表
f1 = open('log1', encoding='utf-8')
print(f1.readlines())
f1.close()

# for循环 推荐这一种，只占用一行内存空间
f1 = open('log1', encoding='utf-8')
for i in f1:
    print(i)
f1.close()


# r+ 读写
f1 = open('log1', encoding='utf-8', mode='r+')
print(f1.read())
f1.write('666')
f1.close()

# seek 光标 按照字节去运转。
# 读写模式下，先写后读需要调整光标，不建议这样写
f1 = open('log1', encoding='utf-8', mode='r+')
f1.seek(0, 2)  # 调整光标到文件尾
f1.write('6666')
f1.seek(0)  # 调整光标到文件头
print(f1.read())
f1.close()

# rb 以二进制方式读
f2 = open('log1', mode='rb')
print(f2.read())
f2.close()

# 编码的补充：
s = "中国"  # 字符串在python3中为unicode编码 ,python2中为ascii编码
s1 = s.encode("gbk")   # s1是str（即unicode） 转换成 gbk编码的bytes类型
# s1 = b'\xd6\xd0\xb9\xfa'  # 以GBK编码存储的bytes类型
s2 = s1.decode('gbk')  # s2是由gbk编码的bytes类型 转换成str（即unicode）类型
# s2 = "中国"  #  s2 = s1
s3 = s2.encode('utf-8')  # s3 是str（即unicode） 转换成 utf-8编码的bytes类型，gbk不能直接转换成utf-8,需要先转成unicode类型
# s3 = b'\xe4\xb8\xad\xe5\x9b\xbd'

# 一行命令实现gbk（bytes）到utf-8（bytes）的转换
s4 = b'\xd6\xd0\xb9\xfa'.decode('gbk').encode('utf-8')
# s4 = b'\xe4\xb8\xad\xe5\x9b\xbd'


# 1、没有文件，则创建文件，写入内容
# 2、文件已经存在，则将原文件所有内容清空，写入新内容。
# w模式，
f1 = open('log2', encoding='utf-8', mode='w')
f1.write('alex是披着高富帅外衣的纯屌丝.....')
f1.close()
# wb模式，以bytes方式存储，需要指定编码类型
f1 = open('log2', mode='wb')
f1.write('alex是披着高富帅外衣的纯屌丝.....'.encode('utf-8'))
f1.close()

# w+ 写读模式，写入一行光标跑到尾部，读不到内容，需要移动光标到头部
f1 = open('log2', encoding='utf-8', mode='w+')
f1.write('666')
f1.seek(0)
print(f1.read())
f1.close()


# a 追加，不会删除原文件内容
f1 = open('log2', encoding='utf-8', mode='a')
f1.write('\n老男孩')
f1.close()

# ab 以二进制方式追加,需要指定编码格式
f1 = open('log3', mode='ab')
f1.write('\n老男孩'.encode("gbk"))
f1.close()

# a+ 追加写  和w+类似。同样需要调整光标位置
f1 = open('log2', encoding='utf-8', mode='a+')
f1.write('fdsafdsafdsagfdg')
f1.seek(0)
print(f1.read())
f1.close()


#其他操作方法：
#read read(n) readline() readlines() write() close

# readable writable 判断是否可以读和可写返回True或False
f1 = open('log2', encoding='utf-8', mode='w')
f1.write('fdsafdsafdsagfdg')
print(f1.readable())
print(f1.writable())
f1.close()

# tell 告诉指针的位置
f1 = open('log2', encoding='utf-8', mode='w')
f1.write('fdsafdsafdsagfdg')
print(f1.tell())
f1.close()

# seek(参数)，seek(0)调至文件最开始，seek(0,2)调至最后。按照字节去调整光标

# with open() as ，会自动关闭文件
with open('log1', encoding='utf-8') as f1:
    print(f1.read())

# 可以同时操作多个文件
with open('log1', encoding='utf-8') as f1,\
     open('log2', encoding='utf-8', mode='w')as f2:
    print(f1.read())
    f2.write('777')

# 文件的改
# 1，打开原文件，产生文件句柄。
# 2，创建新文件，产生文件句柄。
# 3，读取原文件，进行修改，写入新文件。
# 4，将原文件删除。
# 5，新文件重命名原文件。
import os
"""
log1的内容：
你好，我是坏人！
你好，我是坏人！
你好，我是坏人！
你好，我是坏人！
需求，把所有的坏人变成好人
"""
# 方法1  read会把文件的所有内容读取出来在进行修改，如果文件很大则会卡死
# readlines 同样是读取文件的所有内容，并按行为单个元素存在一个列表里。
with open("log1", encoding="utf-8") as f1,\
     open("log1.bak", encoding="utf-8", mode="a") as f2:
    f2.write(f1.read().replace("好人", "坏人"))
os.remove("log1")
os.rename("log1.bak", "log1")


# 方法2，不占用内存空间。处理大文件效果更好
with open("log1", encoding="utf-8") as f1,\
     open("log1.bak", encoding="utf-8", mode="a") as f2:
    for i in f1:
        f2.write(i.replace("坏人", "好人"))
os.remove("log1")
os.rename("log1.bak", "log1")






# import os
# with open('file_test', encoding='utf-8') as f1,\
#     open('file_test.bak', encoding='utf-8', mode='w') as f2:
#     old_content = f1.read()
#     new_content = old_content.replace('alex','SB')
#     f2.write(new_content)
# os.remove('file_test')
# os.rename('file_test.bak','file_test')

#
# import os
# with open('file_test', encoding='utf-8') as f1,\
#     open('file_test.bak', encoding='utf-8', mode='w') as f2:
#     for line in f1:
#         new_line = line.replace('SB','alex')
#         f2.write(new_line)
# os.remove('file_test')
# os.rename('file_test.bak','file_test')


