from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def server(request):
    """
    资产采集API
    POST：
        取到auto_client传递过来的数据
    GET:
        返回接口成功页面
    :param request:
    :return:
    """
    if request.method == "POST":
        print(request.POST)
    return HttpResponse("Server Success!")