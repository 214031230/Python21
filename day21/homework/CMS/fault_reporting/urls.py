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
from django.conf.urls import url
from fault_reporting import views


urlpatterns = [
    # 根据产品线，标签，日期归档分类 ()在正则是分组的意思，这里分2个组传了2个参数
    url(r'(class|tag|archive)/(.*)/$', views.index),
    # 后台首页 显示当前用户发布的报障
    url(r'info/$', views.info)
]
