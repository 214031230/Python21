#需求：爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数据

import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {
    #对UA进行重写操作（伪装）
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
data = {
    'cname':'',
    'pid':'',
    'keyword':	'上海',
    'pageIndex':'3',
    'pageSize':	'10',
}

response = requests.post(url=url,data=data,headers=headers)

print(response.text)