from django.shortcuts import render, HttpResponse
from app01 import models


# Create your views here.
def reg(request):
    if request.method == "GET":
        return render(request, "reg.html")
    
    
def check(request):
    username = request.POST.get("username")
    obj = models.User.objects.filter(username=username)
    if not obj.exists():
        return HttpResponse("1")
    else:
        return HttpResponse("0")
    