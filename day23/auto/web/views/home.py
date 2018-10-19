#!/usr/bin/env python3
from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings


def index(request):
    return render(request, "index.html", {"menus": settings.MENU_LIST})