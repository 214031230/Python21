from django.shortcuts import render


def index(request):
    """
    首页
    :param request: 
    :return: 
    """
    return render(request, "web/index.html")
