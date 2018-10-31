import requests
#session也可以发起请求。
session = requests.session()
url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018901717882'
data = {
    'rkey':'1ad002b47d8446d446f8d76f5bb5ff66',
    'password':	'75c6acde54f800fecf07577d3332ae275354b40d0a84ebfa35c9cecdde6a50f1',
    'origURL':'http://www.renren.com/home',
    'key_id':'1',
    'icode'	:'',
    'f':	'http%3A%2F%2Fwww.renren.com%2F289676607%2Fprofile',
    'email'	:'www.zhangbowudi@qq.com',
    'domain':	'renren.com',
    'captcha_type'	:'web_login',
}
headers = {
    #对UA进行重写操作（伪装）
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
#使用session发起登录请求，请求成功后可以将cookie自动存储到session
response = session.post(url=url,data=data,headers=headers)

url = 'http://www.renren.com/289676607/profile'
response = session.get(url=url,headers=headers)#该次请求一定会携带cookie

with open('./renren.html','w',encoding='utf-8') as fp:
    fp.write(response.text)
