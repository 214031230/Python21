import requests

# 1.
url = 'https://www.sogou.com/web'

# 对url携带的参数进行字典形式的封装,封装好后，将字典赋值给get方法的params参数即可
param = {
    'query': '美女图片',
}
# 2
response = requests.get(url=url, params=param)
# 3

page_text = response.text

# 4
print(page_text)
