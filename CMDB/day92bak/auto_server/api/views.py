import json
import hashlib
import time
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from api.plugins import PluginsManage
from django.db.models import Q
from datetime import date
from repository import models
from django.views import View
from django.conf import settings
from django.utils.decorators import method_decorator


def md5_code(arg):
    """
    MD5加密
    :param arg:
    :return:
    """
    hs = hashlib.md5()
    hs.update(arg.encode("utf-8"))
    return hs.hexdigest()


visited_keys = {

}


def api_auth(func):
    """
    API验证装饰器
    :param func:
    :return:
    """

    def inner(request, *args, **kwargs):
        # 拿到服务器的当前时间，时间戳格式
        server_float_c_time = float(time.time())
        # 拿到客户端传递过来的验证数据
        client_auth_api_info = request.META.get("HTTP_AUTH_API")
        client_md5_str, client_c_time = client_auth_api_info.rsplit("|", maxsplit=1)
        client_c_time = float(client_c_time)

        # 判断密钥是否超时(5秒内有效)
        if (client_c_time + 20) < server_float_c_time:
            return HttpResponse("密钥超时")

        # 判断加密是否正常
        server_md5_str = md5_code("%s|%s" % (settings.KEY, client_c_time))
        if server_md5_str != client_md5_str:
            return HttpResponse("无权限，密钥不正确")

        # 判断key是否已经被使用
        if visited_keys.get("client_md5_str"):
            return HttpResponse("密钥已经被使用")

        visited_keys[client_md5_str] = client_c_time
        return func(request, *args, **kwargs)
    return inner


@csrf_exempt
@api_auth
def server(request):
    """
    资产采集API
    POST：
        取到auto_client传递过来的数据
    GET:
        返回未采集的主机列表
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
        print("执行了POST请求")
        return HttpResponse(response)

    # 获取当前时间(年月日)
    current_date = date.today()
    # 获取未采集的主机列表(最后一次采集时间为None或采集时间小于当前时间，并且服务器状态为在线状态),每次处理200台机器
    host_list = models.Server.objects.filter(
        (Q(latest_date=None) | Q(latest_date__date__lt=current_date)) & Q(server_status_id=2)
    ).values("hostname")[0:200]

    # 把QuerySet 对象转到成 列表
    host_list = list(host_list)
    print("执行了GET请求")
    # 返回一个JSON格式的数据
    return HttpResponse(json.dumps(host_list))


# class Server(View):
#     """
#     CBV方式处理，不对get请求添加装饰器
#     """
#     def get(self, request):
#         print("执行了GET请求")
#         # 获取当前时间(年月日)
#         current_date = date.today()
#         # 获取未采集的主机列表(最后一次采集时间为None或采集时间小于当前时间，并且服务器状态为在线状态),每次处理200台机器
#         host_list = models.Server.objects.filter(
#             (Q(latest_date=None) | Q(latest_date__date__lt=current_date)) & Q(server_status_id=2)
#         ).values("hostname")[0:200]
#         # 把QuerySet 对象转到成 列表
#         host_list = list(host_list)
#         # 返回一个JSON格式的数据
#         return HttpResponse(json.dumps(host_list))
#
#     @method_decorator(api_auth)
#     @method_decorator(csrf_exempt)
#     def post(self, request):
#         print("执行了POST请求")
#         client_info = json.loads(request.body.decode("utf-8"))
#         # 检查是否采集到主机信息
#         if not client_info["basic"]["status"]:
#             return HttpResponse("未采集到主机信息，不进行其他操作")
#         obj = PluginsManage(client_info)
#         response = obj.exec()
#         return HttpResponse(response)
