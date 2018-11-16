"""auto_server URL Configuration

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
from web.views import basic
from web.views import user
from web.views import admin_user
from web.views import group

urlpatterns = [
    url(r'^index/$', basic.index, name="index"),
    
    # 所有用户管理
    url(r'^user/list/$', user.user_list, name="user_list"),
    url(r'^user/add/$', user.user_add, name="user_add"),
    url(r'^user/edit/(\d+)$', user.user_edit, name="user_edit"),
    url(r'^user/del/(\d+)$', user.user_del, name="user_del"),

    # 可登陆用户管理
    url(r'^admin_user/list/$', admin_user.admin_user_list, name="admin_user_list"),
    url(r'^admin_user/add/$', admin_user.admin_user_add, name="admin_user_add"),
    url(r'^admin_user/edit/(\d+)$', admin_user.admin_user_edit, name="admin_user_edit"),
    url(r'^admin_user/del/(\d+)$', admin_user.admin_user_del, name="admin_user_del"),

    # 用户组管理
    url(r'^group/list/$', group.group_list, name="group_list"),
    url(r'^group/add/$', group.group_add, name="group_add"),
    url(r'^group/edit/(\d+)$', group.group_edit, name="group_edit"),
    url(r'^group/del/(\d+)$', group.group_del, name="group_del"),

    # 业务线管理
    url(r'^group/list/$', group.group_list, name="group_list"),
    url(r'^group/add/$', group.group_add, name="group_add"),
    url(r'^group/edit/(\d+)$', group.group_edit, name="group_edit"),
    url(r'^group/del/(\d+)$', group.group_del, name="group_del"),


]

