#需求：爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详情数据

import requests

url = 'https://movie.douban.com/j/chart/top_list?'

#针对get请求参数进行处理
param = {
    'type': '13',
    'interval_id': '100:90',
    'action':'' ,
    'start': '60',
    'limit': '20',
}

response = requests.get(url=url,params=param)

print(response.text)