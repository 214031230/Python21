"""mysite URL Configuration

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
from django.contrib import admin
from app01 import views

# from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^publisher_list/$', views.publisher_list, name="alex"),
    url(r'^edit_publisher/(?P<edit_id>\d+)/$', views.EditPublisher.as_view(), name="wusir"),
    # 测试上传你文件
    url(r'^upload/$', views.Upload.as_view()),
    # 测试返回Json格式数据
    url(r'^json_test/$', views.JsonTest.as_view()),
    # 测试模板语法
    url(r'^template_test/$', views.template_test),
    # 测试跨站请求伪造 （CSRF）
    url(r'^csrf_test/$', views.csrf_test),

    url(r'^book_list/$', views.book_list),
    url(r'^add_book/$', views.AddBook.as_view()),
    url(r'^delete_book/(?P<pk>\d+)/$', views.DeleteBook.as_view()),
    url(r'^edit_book/(?P<pk>\d+)/$', views.EditBook.as_view()),
    url(r'^login/$', views.login),


]
