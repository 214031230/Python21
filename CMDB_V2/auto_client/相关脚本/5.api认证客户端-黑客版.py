#!/usr/bin/env python3
import requests


response = requests.post(
    url="http://127.0.0.1:8000/api/test/?key=f7562c0027c39eba8c64d6ef22e56f50&ctime=1545299962.0844934",
    data={"data": "aaaa"}
)
print(response.text)