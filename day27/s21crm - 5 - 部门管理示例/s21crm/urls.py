"""s21crm URL Configuration

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
from crm.views import depart
from crm.views import user

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^depart/list/', depart.depart_list, name='depart_list'),
    url(r'^depart/add/', depart.depart_add, name='depart_add'),
    url(r'^depart/edit/(\d+)/', depart.depart_edit, name='depart_edit'),
    url(r'^depart/del/(\d+)/', depart.depart_del, name='depart_del'),
    url(r'^user/list/', user.user_list, name='user_list'),
    url(r'^user/add/', user.user_add, name='user_add'),
    url(r'^user/edit/(\d+)/', user.user_edit, name='user_edit'),
    url(r'^user/del/(\d+)/', user.user_del, name='user_del'),
]
