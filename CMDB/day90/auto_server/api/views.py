import json
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api.plugins import PluginsManage


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
        client_info = json.loads(request.body.decode("utf-8"))

        # 检查是否采集到主机信息
        if not client_info["basic"]["status"]:
            return HttpResponse("未采集到主机信息，不进行其他操作")

        obj = PluginsManage(client_info)
        response = obj.exec()
        return HttpResponse(response)
    return HttpResponse("Server Success!")
