#!/usr/bin/env python3
import httplib2
from urllib.parse import urlencode  # python3
import requests
import json

# params = urlencode({'ip': '114.114.114.114', 'datatype': 'jsonp', 'callback': 'find'})
# url = 'http://api.ip138.com/query/?' + params
# headers = {"token": "4229f3e83aa32a755898c7654bfae0ed"}
# http = httplib2.Http()
# response, content = http.request(url, 'GET', headers=headers)
# print(content.decode("utf-8"))
payload = {"ip": "8.8.8.8",
           "datatype": "txt",
           "callback": "find",
           "token": "4229f3e83aa32a755898c7654bfae0ed"
           }
response = requests.get(
    url="http://api.ip138.com/query/?",
    params=payload
)
print(response.text)
