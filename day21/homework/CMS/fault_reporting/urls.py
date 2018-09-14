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
    url(r'(class|tag|archive|search)/(.*)/$', views.index),
    # 后台首页 显示当前用户发布的报障
    url(r'info/$', views.info),
    # 故障详情页面,需要(\d+)传参，参数=故障ID
    url(r'report_detail/(\d+)/$', views.report_detail),
    # 点赞、反对
    url(r'up_down/$', views.up_down),
    # 评论
    url(r'comment/$', views.comment),
    # 新增报障
    url(r'add_report/$', views.add_report),
    # 富文本展示图片
    url(r'upload_img/$', views.upload_img),
    # 编辑故障详情
    url(r'edit_report/(\d+)$', views.edit_report),
    # 删除故障
    url(r'delete_report/$', views.delete_report),
    # 用户访问fault-report 跳转到index页面
    url('^$', views.index),  # index(request)
]
