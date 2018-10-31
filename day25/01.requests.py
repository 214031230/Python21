#!/usr/bin/env python3
# 基于requests模块的get请求
#   需求：爬取搜狗指定词条搜索后的页面数据
import requests

if __name__ == '__main__':
    # 爬取的URL
    url = "https://www.sogou.com/web?"

    # 爬取的参数，这里是Get请求
    params = {
        "query": "美女图片"
    }

    # 开始爬取页面，拿到响应
    response = requests.get(url=url, params=params)

    # 打印响应页面
    print(response.text)
