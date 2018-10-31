import requests

#1指定url
url = 'https://www.sogou.com/'
#2基于requests模块进行请求发送
#get方法最终会返回一个响应对象
response = requests.get(url=url) #根据指定url发起了一个get请求

#3.获取响应对象中存储的数据值
#text属性可以返回响应对象中字符串形式的数据值
#content属性返回的是响应对象中bytes类型的数据值
print(response.encoding)
#encoding表示的是响应对象中存储数据的编码格式
#response.encoding = 'gbk'
print(response.status_code)
response.url
print(response.headers)
#print(response.text)

#4持久化存储
#with open('./sogou.html','w',encoding='utf-8') as fp:
#    fp.write(response.text)