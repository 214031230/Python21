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
from web.views import business
from web.views import idc
from web.views import server
from web.views import tag
from web.views import disk
from web.views import nic
from web.views import memory
from web.views import server_record

urlpatterns = [
    url(r'^index/$', basic.index, name="index"),
    url(r'^login/$', basic.login, name="login"),
    
    
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
    url(r'^business/list/$', business.business_list, name="business_list"),
    url(r'^business/add/$', business.business_add, name="business_add"),
    url(r'^business/edit/(\d+)$', business.business_edit, name="business_edit"),
    url(r'^business/del/(\d+)$', business.business_del, name="business_del"),

    # IDC机房管理
    url(r'^idc/list/$', idc.idc_list, name="idc_list"),
    url(r'^idc/add/$', idc.idc_add, name="idc_add"),
    url(r'^idc/edit/(\d+)$', idc.idc_edit, name="idc_edit"),
    url(r'^idc/del/(\d+)$', idc.idc_del, name="idc_del"),

    # 标签管理
    url(r'^tag/list/$', tag.tag_list, name="tag_list"),
    url(r'^tag/add/$', tag.tag_add, name="tag_add"),
    url(r'^tag/edit/(\d+)$', tag.tag_edit, name="tag_edit"),
    url(r'^tag/del/(\d+)$', tag.tag_del, name="tag_del"),

    # 服务器管理
    url(r'^server/list/$', server.server_list, name="server_list"),
    url(r'^server/add/$', server.server_add, name="server_add"),
    url(r'^server/edit/(\d+)$', server.server_edit, name="server_edit"),
    url(r'^server/del/(\d+)$', server.server_del, name="server_del"),

    # 硬盘管理
    url(r'^disk/list/$', disk.disk_list, name="disk_list"),
    url(r'^disk/add/$', disk.disk_add, name="disk_add"),
    url(r'^disk/edit/(\d+)$', disk.disk_edit, name="disk_edit"),
    url(r'^disk/del/(\d+)$', disk.disk_del, name="disk_del"),

    # 网卡管理
    url(r'^nic/list/$', nic.nic_list, name="nic_list"),
    url(r'^nic/add/$', nic.nic_add, name="nic_add"),
    url(r'^nic/edit/(\d+)$', nic.nic_edit, name="nic_edit"),
    url(r'^nic/del/(\d+)$', nic.nic_del, name="nic_del"),

    # 内存管理
    url(r'^memory/list/$', memory.memory_list, name="memory_list"),
    url(r'^memory/add/$', memory.memory_add, name="memory_add"),
    url(r'^memory/edit/(\d+)$', memory.memory_edit, name="memory_edit"),
    url(r'^memory/del/(\d+)$', memory.memory_del, name="memory_del"),

    # 服务器更新记录表
    url(r'^server_record/list/$', server_record.server_record_list, name="server_record_list"),
    # url(r'^server_record/add/$', server_record.server_record_add, name="server_record_add"),
    # url(r'^server_record/edit/(\d+)$', server_record.server_record_edit, name="server_record_edit"),
    # url(r'^server_record/del/(\d+)$', server_record.server_record_del, name="server_record_del"),



]

