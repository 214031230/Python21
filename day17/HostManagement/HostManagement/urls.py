"""HostManagement URL Configuration

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
from user import views as user_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', user_views.login),
    url(r'^platform/$', user_views.platform),
    url(r'^user_list/$', user_views.user_list),
    url(r'^add_user/$', user_views.add_user),
    url(r'^delete_user/$', user_views.delete_user),
    url(r'^edit_user/$', user_views.edit_user),
    url(r'^host_list/$', user_views.host_list),
    url(r'^bsline_list/$', user_views.BsLine.as_view()),
    url(r'^add_bsline/$', user_views.AddBsline.as_view()),
    url(r'^delete_bsline/$', user_views.DeleteBsline.as_view()),
    url(r'^edit_bsline/$', user_views.EditBsline.as_view()),
]
