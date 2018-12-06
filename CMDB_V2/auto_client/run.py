#!/usr/bin/env python3
import requests
import json


def agent():
    """
    采集器发生数据到api
    :return: 
    """
    
    info = {"hostname": "c1.com", "cpu": "xxx"}

    response = requests.post(
        url="http://127.0.0.1:8000/api/asset/",
        data=json.dumps(info).encode("utf-8")
    )
    
    print(response.text)
    
    
agent()
