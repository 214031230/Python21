#!/usr/bin/env python3
from django.shortcuts import render


def index(request):
    """
    欢迎页面
    :param request:
    :return:
    """
    return render(request, "web/index.html")