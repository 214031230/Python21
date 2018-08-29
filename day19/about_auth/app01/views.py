from django.shortcuts import render, redirect
from app01 import models
from django import forms
from django.contrib import auth

def login(request):
    if request.method == "POST":
        next_url = request.GET.get("next")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user_obj = auth.authenticate(request,
                                     username=username,
                                     password=password)

    return render(request, "login.html")
