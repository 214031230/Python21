#!/usr/bin/env python3
from django.conf.urls import url
from app01.views import user

urlpatterns = [
    url(r'login/$', user.login),
]