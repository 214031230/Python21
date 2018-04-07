#对于英文
# s = 'laonanhai'
# print(s,type(s))
#
# s1 = b'laonanhai'
# print(s1,type(s1))

#对于中文：
# s = '中国'
# print(s,type(s))
#
# s1 = b'\xe4\xb8\xad\xe5\x9b\xbd'
# print(s1,type(s1))

#转化
# s = 'laonanhai'
# s2 = s.encode('utf-8')  #str -->bytes encode 编码
# s3 = s.encode('gbk')
# print(s2,s3)
# s = '中国'
# s2 = s.encode('utf-8')  #str -->bytes encode 编码
# # s3 = s.encode('gbk')
# # print(s2)
# # print(s3)
# ss = s2.decode('utf-8')  # bytes ---> str decode 解码
# print(ss)