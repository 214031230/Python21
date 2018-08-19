
"""
自定义中间件
"""
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


# class MD1(MiddlewareMixin):
#
#     def process_request(self, request):
#         print("这是MD1中的process_request方法！")
#         print(id(request))
#         request.s21 = "好"
#         # return HttpResponse("呵呵")
#
#     def process_response(self, request, response):
#         print("这是MD1中的process_response方法！")
#         return response
#         # return HttpResponse("哈哈")
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         # print("=" * 120)
#         # print(view_func.__name__)
#         # print(view_func.__doc__)
#         # view_func(request)
#         # print("-" * 120)
#         print("这是MD1中的process_view方法！")
#         # return HttpResponse("嘻嘻")
#
#     def process_template_response(self,request,response):
#         print("这是MD1中的process_template_response方法！")
#         return response
#
#     def process_exception(self, request, exception):
#         print("这是MD1中的process_exception方法！")
#
#
#
# class MD2(MiddlewareMixin):
#
#     def process_request(self, request):
#         print("这是MD2中的process_request方法！")
#
#     def process_response(self, request, response):
#         print("这是MD2中的process_response方法！")
#         return response
#         # return HttpResponse("嘿嘿")
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         print("这是MD2中的process_view方法！")
#
#     def process_template_response(self,request,response):
#         print("这是MD2中的process_template_response方法！")
#         return response
#
#     def process_exception(self, request, exception):
#         print("这是MD2中的process_exception方法！")
#         print(exception)
#         return HttpResponse("视图函数报错啦！！！")

D = {}
# WHITE_LIST = ['/test/']

import time
class XianZhi(MiddlewareMixin):

    def process_request(self, request):
        # 限制访问频率
        # 当前请求的IP
        # print(request.META)
        ip = request.META.get("REMOTE_ADDR")
        now = time.time()
        # print(ip)

        # if request.path_info in WHITE_LIST:
        #     return None

        if ip not in D:
            D[ip] = []
        # 拿到当前ip的访问历史记录
        history = D[ip]
        # 不能遍历列表的同时又操作列表的元素个数
        # for record in history:
        #     if now - record > 60:

        while history and now - history[-1] > 10:
            history.pop()

        if len(history) >= 3:
            return HttpResponse("滚~")
        else:
            history.insert(0, now)




