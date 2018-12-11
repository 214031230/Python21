#!/usr/bin/env python3
import requests

response = requests.post(
    url="http://127.0.0.1:8000/api/",
    data={"k2": "v2"},
    headers={
        'Content-Type': 'application/json'
    }
)
print(response.text)