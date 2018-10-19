from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def user(request):
    return render(request, 'user.html')

def order(request):
    return render(request, 'order.html')

def center(request):
    return render(request, 'center.html')