from django.shortcuts import render

# Create your views here.


def index(request):
    alex = "hehe"
    return render(request, "index.html", {"alex": alex})
