import json
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
@csrf_exempt
def asset(request):
    """
    获取采集器发送过来的数据
    request.body 和 request.POST区别：
        POST: 获取请求体中的所有数据
        body: 获取请求体中的原生数据
        
        如果http发送的请求体格式是：
                "hostname=123&cpu=xxxx"
        则request.POST才能进行解析
    :param request: 
    :return: 
    """
    if request.method == "GET":
        return JsonResponse(["192.168.186.133"], safe=False)
    info = json.loads(request.body)
    print(info)
    print(info.keys())
    return HttpResponse("收到数据！")
