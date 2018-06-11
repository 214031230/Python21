#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor
import time
import random
# concurrent.futures callback是由子线程做的
# callback回调函数

urls=[
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/',
        'http://www.cnblogs.com/',
        'http://www.sogou.com/',
        'http://www.sohu.com/'
    ]


def get_url(url):
    time.sleep(random.randint(1,3))
    return url


def fx_url(res):
    print(res.result())


if __name__ == '__main__':
    t = ThreadPoolExecutor(2)
    for url in urls:
        t.submit(get_url, url).add_done_callback(fx_url)