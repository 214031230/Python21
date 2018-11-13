from django.shortcuts import render, HttpResponse
from repository import models
from django.http import JsonResponse
# Create your views here.


# def server(request):
#     return render(request, "server.html")


# def server_json(request):
#     table_config = [
#         {
#             'q': None,
#             'title': '选择',
#             'text': {'tpl':'<input type="checkbox" value="{nid}" />','kwargs':{'nid': '@id' }},
#         },
#         {
#             'q': 'id',
#             'title': 'ID',
#             'text': {'tpl': '{a1}', 'kwargs': {'a1': '@id'}},
#         },
#         {
#             'q': 'hostname',
#             'title': '主机名',
#             'text': {'tpl': '{a1}-{a2}','kwargs':{'a1': '@hostname','a2':'666'}},
#         },
#         {
#             'q': 'sn',
#             'title': '序列号',
#             'text': {'tpl': '{a1}','kwargs':{'a1': '@sn'}},
#         },
#         {
#             'q': 'os_platform',
#             'title': '系统',
#             'text': {'tpl': '{a1}','kwargs':{'a1': '@os_platform'}},
#         },
#         {
#             'q': 'os_version',
#             'title': '系统版本',
#             'text': {'tpl': '{a1}','kwargs':{'a1': '@os_version'}},
#         },
#         {
#             'q': 'business_unit__name',
#             'title': '业务线',
#             'text': {'tpl': '{a1}','kwargs':{'a1': '@business_unit__name'}},
#         },
#         {
#             'q': None,
#             'title': '操作',
#             'text': {'tpl': '<a href="/edit/{nid}/">编辑</a> | <a href="/del/{uid}/">删除</a> ', 'kwargs': {'nid': '@id','uid': '@id'}},
#         },
#     ]
# 
#     values = []  # ['hostname', 'sn', 'os_platform']
#     for item in table_config:
#         if item["q"]:
#             values.append(item["q"])
# 
#     server_list = models.Server.objects.values(*values)
#     print(server_list)
#     response = {
#         "data_list": list(server_list),
#         "table_config": table_config
#     }
#     """
#     {
#     "data_list": [
#         {
#             "hostname": "c1.com", 
#             "sn": "Parallels-1A 1B CB 3B 64 66 4B 13 86 B0 86 FF 7E 2B 20 30", 
#             "os_platform": "linux"
#         }
#     ], 
#     "table_config": [
#         {
#             "q": "hostname", 
#             "title": "主机名"
#         }, 
#         {
#             "q": "sn", 
#             "title": "序列号"
#         }, 
#         {
#             "q": "os_platform", 
#             "title": "系统"
#         }
#     ]
# }
#     """
#     return JsonResponse(response)























