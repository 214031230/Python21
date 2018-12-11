from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.views import Response

# Create your views here.

# @csrf_exempt
# def api(request):
#     if request.method == "GET":
#         info = {"k1": "v1"}
#         return JsonResponse(info)
#     else:
#         print(request.body)
#         return HttpResponse("收到数据")

# @method_decorator(csrf_exempt, name='dispatch')
# class Api(View):
#     def get(self, request):
#         info = {"k1": "v1"}
#         return JsonResponse(info)
# 
#     def post(self, request):
#         print(request.body)
#         return HttpResponse("收到数据")


class Api(APIView):
    """
    GET:

    POST:

    """
    def get(self, request):
        info = {"k1": "v1"}
        return Response(info)

    def post(self, request):
        print(request.body)
        return HttpResponse("收到数据")
