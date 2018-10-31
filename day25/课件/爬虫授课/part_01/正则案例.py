#项目需求：爬取糗事百科指定页面的糗图，并将其保存到指定文件夹中

import requests
import re
import os

if not os.path.exists('qiutu'):
    os.mkdir('qiutu')


#1.
url = 'https://www.qiushibaike.com/pic/'

#2
headers = {
    #对UA进行重写操作（伪装）
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
response = requests.get(url=url,headers=headers)

#3
page_text = response.text

#4数据解析：将页面中所有的图片数据进行爬取
#根据正则获取的页面源码中所有的图片链接
img_url = re.findall('<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>',page_text,re.S)
#根据图片链接发起请求，获取图片二进制数据
for url in img_url:
    url = "https:" + url
    img_response = requests.get(url=url,headers=headers)
    img_data = img_response.content #bytes
    imgName = url.split('/')[-1]
    imgPath = "qiutu/"+imgName
    with open(imgPath,'wb') as fp:
        print(imgPath+"savaed success!!!!!")
        fp.write(img_data)
    



