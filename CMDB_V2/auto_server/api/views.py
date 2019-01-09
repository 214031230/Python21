import time
import hashlib
from rest_framework.views import APIView
from rest_framework.views import Response
from django.http import JsonResponse
from api import models
from api.lib import service
from django.conf import settings
key_dict = {}


def get_key(ctime):
    key = "%s|%s" % (settings.AUTH_KEY, ctime)
    md5 = hashlib.md5()
    md5.update(key.encode("utf-8"))
    return md5.hexdigest()


class ApiAuthView(APIView):
    class TestApi(APIView):
        def dispatch(self, request, *args, **kwargs):
            info = {
                "status": True,
                "msg": None
            }
            # api认证开始
            server_ctime = time.time()
            client_ctime = request.GET.get("ctime")
            client_key = request.GET.get("key")
            # 1. 判断key的时间是否超时
            if int(server_ctime) - int(float(client_ctime)) > 5:
                info["status"] = False
                info["msg"] = "key已经超时"
                return Response(info)

            # 2. 判断key存不存在
            if client_key in key_dict:
                info["status"] = False
                info["msg"] = "key已经被使用"
                return Response(info)

            # 3. 判断key是否正确
            server_key = get_key(client_ctime)
            if client_key != server_key:
                info["status"] = False
                info["msg"] = "key错误"
                return Response(info)
            # 保存使用过的key
            key_dict[client_key] = client_ctime
            return super().dispatch(request, *args, **kwargs)


class AssetAPI(ApiAuthView):
    """
    采集器API
    GET:
        返回需要采集的主机列表
    POST：
        接受主机汇报过来的资产信息
    """

    def get(self, request):
        host_list = ["192.168.186.133"]
        return Response(host_list)

    def post(self, request):
        print(request.data)
        info = {
            "status": True,
            "error": None,
            "hostname": None,
        }
        data_type = request.data.get("type")
        if data_type == "create":
            """
            创建主机: 主机第一次汇报
            """
            # 1. 基本信息：在server表中添加数据
            server_dict = {}
            server_dict.update(request.data["basic"]["data"])
            server_dict.update(request.data["cpu"]["data"])
            server_dict.update(request.data["main_board"]["data"])

            server = models.Server.objects.create(**server_dict)

            # 2. 硬盘
            disk_info = request.data["disk"]["data"]
            for k, v in disk_info.items():
                v["server"] = server
                models.Disk.objects.create(**v)

            # 3. 网卡
            nic_info = request.data["network"]["data"]
            for k, v in nic_info.items():
                v["server"] = server
                v["name"] = k
                models.NIC.objects.create(**v)

            # 4.内存
            memory_info = request.data["memory"]["data"]
            for k, v in memory_info.items():
                v["server"] = server
                models.Memory.objects.create(**v)
        elif data_type == "update":
            """
            更新主机： 主机名不变，其他信息变化
            """
            hostname = request.data["basic"]["data"]["hostname"]
            server = models.Server.objects.filter(hostname=hostname).first()
            # 1. 基本信息
            service.basic(request, hostname)
            # 2. 硬盘
            service.disk(request, server)
            # 3. 网卡
            service.nic(request, server)
            # 4. 内存
            service.memory(request, server)
        else:
            """
            更新主机和主机名： 主机名变化，其他信息变化
            """
            hostname = request.data["cert"]
            server = models.Server.objects.filter(hostname=hostname).first()
            # 1. 基本信息
            service.basic(request, hostname)
            # 2. 硬盘
            service.disk(request, server)
            # 3. 网卡
            service.nic(request, server)
            # 4. 内存
            service.memory(request, server)
        info["hostname"] = request.data.get("basic").get("data").get("hostname")
        return JsonResponse(info)

