from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Image, Coord, UserInfo
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
from django.contrib import auth
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = auth.authenticate(username=username, password=password)
#         print(user)
#         if user is not None and user.is_active:
#             auth.login(request, user)
#             return redirect('/tagPage/', {'user': user})
#         else:
#             error = '用户名或者密码错误!!!'
#             return render(request, 'login.html', {'error': error})
#     elif request.method == 'GET':
#
#         return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        # uf = UserForm(request.POST)
        # if uf.is_valid():
        #     username = uf.cleaned_data['username']
        #     password = uf.cleaned_data['password']
        #     user_obj = User.objects.filter(username=username, password=password).first()
        #     if user_obj:
        #         auth.login(request, user_obj)
        #         return redirect('/tagPage/')
        # user_obj = auth.authenticate(username=username, password=pwd)
        # if user_obj is not None:
        #     auth.login(request, user_obj)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = UserInfo.objects.filter(username=username, password=password).first()
        # user_obj = auth.authenticate(username=username, password=password)
        if user_obj:
            # auth.login(request, user_obj)
            # auth.authenticate(user_obj)

            return redirect('/tagPage/', {'user': user_obj})
        else:
            error = '用户名或者密码错误!!!'
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


def tag_page(request):
    # res = {"code": 0}
    # res1 = {'code': 0}
    if request.method == 'POST':
        # print(request.POST.get("id"))
        # prev_id = request.POST.get("id") - 1
        # if prev_id >= 36:
        #     prev_obj = Image.objects.filter(id=prev_id).first()
        #     if not prev_obj:
        #         return JsonResponse(res1)
        #     res1["code"] = 1
        #     res1["data"] = {
        #         "id": prev_obj.id,
        #         "image_url": str(prev_obj.image_url)
        #     }
        #     return JsonResponse(res1)

        # print(request.POST.get("id"))
        # next_id = int(request.POST.get("id")) + 1
        # next_id = int(request.POST.get("id"))
        # next_obj = Image.objects.filter(id=next_id).first()
        # if not next_obj:
        #     return JsonResponse(res)
        # res["code"] = 1
        # res["data"] = {
        #     "id": next_obj.id,
        #     "image_url": str(next_obj.image_url)
        # }
        # return JsonResponse(res)

        print(request.POST.get('res'))
        result = request.POST.get('res')
        # img = request.POST.get('img')
        result = json.loads(result)
        print(result[0])
        print(result[0]['x'])
        print(result[0]['y'])
        print(result[0]['w'])
        print(result[0]['h'])
        coord = Coord()
        coord.x = result[0]['x']
        coord.y = result[0]['y']
        coord.w = result[0]['w']
        coord.h = result[0]['h']
        if not coord.x and coord.y:
            coord.save()

    return render(request, 'tagPage.html')


def faceShow(request):
    images = Image.objects.all()
    # limit = 5
    p = Paginator(images, 5)
    # p.count
    # p.num_pages
    # p.page_range
    page_num = request.GET.get('page')

    try:
        image_list = p.page(page_num)
    except PageNotAnInteger:
        image_list = p.page(1)
    except EmptyPage:
        image_list = p.page(page_num)

    return render(request, 'faceCluster.html', locals())
