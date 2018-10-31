#需求：爬取笑话网中的段子内容和作者https://www.xiaohua.com/duanzi/

import requests
from lxml import etree

url = 'https://www.xiaohua.com/duanzi/'

headers = {
    #对UA进行重写操作（伪装）
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
page_text = response.text

#实例化一个etree对象，并且将页面数据防止到etee对象中
tree = etree.HTML(page_text) #对象类型为Element类型
div_list = tree.xpath('//div[@class="content-left"]/div[@class="one-cont"]')
fp = open('./xiaohua.txt','w',encoding='utf-8')
#xpath函数返回值永远是一个列表
#Element类型的对象都可以调用xpath方法
for div in div_list:
    #针对div表示的局部页面内容进行指定内容的解析
    author = div.xpath('.//div[@class="one-cont-font clearfix"]/a/i/text()')[0]
    content = div.xpath('./p/a//text()')[0]
    fp.write(author+":"+content+"\n\n")
    
fp.close()

