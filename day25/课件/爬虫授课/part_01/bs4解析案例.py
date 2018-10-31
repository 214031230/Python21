import requests
from bs4 import BeautifulSoup

url = 'http://www.shicimingju.com/book/sanguoyanyi.html'

headers = {
    #对UA进行重写操作（伪装）
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

response = requests.get(url=url,headers=headers)

page_text = response.text

#进行章节标题和内容的解析
#实例化一个bs对象
soup = BeautifulSoup(page_text,'lxml')

#解析章节标题
li_list = soup.select(".book-mulu > ul > li")
fp = open('./sanguo.txt','w',encoding="utf-8")
for li in li_list:
    title = li.a.string
    content_url = "http://www.shicimingju.com"+li.a["href"]
    content_page_text = requests.get(url=content_url,headers=headers).text
    soup = BeautifulSoup(content_page_text,"lxml")
    #章节对应的小说内容
    content = soup.find("div",class_="chapter_content").text
    fp.write(title+":"+content)
fp.close()
    
    