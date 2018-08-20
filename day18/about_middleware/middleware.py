#!/usr/bin/env python3
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render


class Mid1(MiddlewareMixin):
    def process_request(self, request):
        print("这是Mid1中的process_request方法")
        # return render(request, "wh.html")

    def process_response(self, request, response):
        print("这是Mid1中的process_response方法")
        return response


class Mid2(MiddlewareMixin):
    def process_request(self, request):
        print("这是Mid2中的process_request方法")

    def process_response(self, request, response):
        print("这是Mid2中的process_response方法")
        return response
