from django.shortcuts import render
from app01 import models
from public.paging import Paging


# Create your views here.


def user_list(request):
    """
    显示用户列表
    :param request:
    :return:
    """
    if request.method == "GET":
        # 查找到所有的用户
        books = models.User.objects.all()
        # 拿到总数据量
        total_count = books.count()
        # 从url拿到page参数
        current_page = request.GET.get("page", None)
        page_obj = Paging(current_page, total_count, url_prefix="user_list", max_show=7)
        # 对总数据进行切片，拿到页面显示需要的数据
        data = books[page_obj.start:page_obj.end]
        page_html = page_obj.page_html()
        return render(request, "user_list.html", {"data": data, "num": page_obj.num, "page_html": page_html})
