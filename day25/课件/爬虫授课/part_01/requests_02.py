# 需求：登录豆瓣电影，爬取登录成功后的页面数据

import requests

# 进行登录操作
# 1.指定url
url = 'https://accounts.douban.com/login'

# 进行post请求的参数处理
data = {
    'ck': 'TNmg',
    'source': 'movie',
    'redir': 'https://www.douban.com',
    'form_email': '15027900535',
    'form_password': 'bobo@15027900535',
    'login': '登录',
}
# 2请求发送（post）
# headers表示的就是自制定的请求头信息
headers = {
    # 对UA进行重写操作（伪装）
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
response = requests.post(url=url, data=data, headers=headers, proxies={"https": '183.111.235.198:8080'})
# 3.
page_text = response.text

# 4
fp = open('./douban.html', 'w', encoding='utf-8')
fp.write(page_text)
fp.close()

# 补充：自制定请求头信息
# User-Agent:请求载体的身份标识
