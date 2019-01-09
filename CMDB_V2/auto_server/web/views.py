from django.shortcuts import render


# Create your views here.
def test(request):
    """
    测试页面
    :param request:
    :return:
    """
    return render(request, "test.html")
