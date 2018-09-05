"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from fault_reporting import views
from django.views.static import serve
from django.conf import settings
from fault_reporting import urls as fault_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 用户注册
    url(r'^register/$', views.register),
    # 用户登录
    url(r'^login/$', views.login),
    # 验证码
    url(r'^v_code/$', views.v_code),
    # 报障系统首页
    url(r'^index/$', views.index),
    # 用户注销
    url(r'^logout/$', views.logout),
    # 个人中心-编辑用户信息
    url(r'^p_center/$', views.p_center),
    # 修改密码
    url(r'^set_password/$', views.set_password),
    # 用户上传文件展示路径
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    # 报障分类二级路由
    url(r'^fault-report/', include(fault_urls))
]
