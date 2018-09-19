#!/usr/bin/env python3
from django.shortcuts import render


def login(request):
    """
    用户登录
    :param request: 
    :return: 
    """
    return render(request, "login1.html")
