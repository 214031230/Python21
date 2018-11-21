#!/usr/bin/env python3
import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings


class LoginCheckMiddleware(MiddlewareMixin):
    """
    用户登录检测，如果用户没有登录则跳转到登录页面
    """

    def process_request(self, request):
        """
        在方式视图函数前检测
        :param request: 
        :return: 
        """
        path_info = request.path_info
        for i in settings.VALID_LIST:
            if re.match(i, path_info):
                return None

        if request.session.get("user"):
            return None
        return redirect(reverse("login"))
