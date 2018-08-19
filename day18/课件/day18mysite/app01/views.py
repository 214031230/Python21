from django.shortcuts import render
from app01 import models
from utils import mypage

# Create your views here.


def book_list(request):
    # 查找到所有的书籍
    books = models.Book.objects.all()
    # 拿到总数据量
    total_count = books.count()
    # 从url拿到page参数
    current_page = request.GET.get("page", None)

    page_obj = mypage.MyPage(current_page, total_count, url_prefix="book_list", max_show=7)
    # 对总数据进行切片，拿到页面显示需要的数据
    data = books[page_obj.start:page_obj.end]
    page_html = page_obj.page_html()

    return render(request, "book_list.html", {"books": data, "page_html": page_html})


def publisher_list(request):
    publishers = models.Publisher.objects.all()
    total_count = publishers.count()
    current_page = request.GET.get("page")

    # 三行完成分页功能
    page_obj = mypage.MyPage(current_page, total_count, url_prefix='publisher_list')
    data = publishers[page_obj.start:page_obj.end]
    page_html = page_obj.page_html()

    return render(request, "publisher_list.html", {"publishers": data, "page_html": page_html})
