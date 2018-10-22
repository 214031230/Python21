import requests



response = requests.get(url='http://www.baidu.com')

print(response.status_code)