from django.shortcuts import render, HttpResponse

# Create your views here.


def test(request):
    """
    将要执行的视图函数的注释...
    :param request:
    :return:
    """
    print("这是test视图函数")
    print(id(request))
    # print(request.s21)
    # raise ValueError('s21')
    return HttpResponse("o98k")
    # rep = HttpResponse("o98k")
    # def func():
    #     return HttpResponse('霍霍')
    # rep.render = func
    # return rep

