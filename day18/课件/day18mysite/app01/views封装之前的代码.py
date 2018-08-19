from django.shortcuts import render
from app01 import models

# Create your views here.


def book_list(request):
    # 查找到所有的书籍
    books = models.Book.objects.all()
    # 拿到总数据量
    total_count = books.count()
    # 每一页显示多少条数据
    per_page = 10
    # 页面最多显示多少页码
    max_show = 7
    # 最多显示页码数的一半
    half_show = max_show//2

    # 从url拿到page参数
    current_page = request.GET.get("page")
    #    因为URL取到的参数是字符串格式，需要转换成int类型
    try:
        current_page = int(current_page)
    except Exception as e:
        # 如果输入的页码不是正经页码，默认展示第一页
        current_page = 1

    # 求总共需要多少页显示
    total_page, more = divmod(total_count, per_page)
    if more:
        total_page += 1
    # 如果输入的当前页码数大于总数据的页码数，默认显示最后一页
    if current_page > total_page:
        current_page = total_page
    # 计算一下显示页码的起点和终点
    show_page_start = current_page - half_show
    show_page_end = current_page + half_show
    # 特殊情况特殊处理
    # 1. 当前页码 - half_show <= 0
    if current_page - half_show <= 0:
        show_page_start = 1
        show_page_end = max_show
    # 2. 当前页码数 + hale_show >= total_page
    if current_page + half_show >= total_page:
        show_page_end = total_page
        show_page_start = total_page - max_show+1
    # 3. 总共需要的页码数 < max_show
    if total_page < max_show:
        show_page_start = 1
        show_page_end = total_page



    # 数据切片的起点
    data_start = (current_page-1) * per_page
    # 数据切片的终点
    data_end = current_page * per_page
    # 对总数据进行切片，拿到页面显示需要的数据
    data = books[data_start:data_end]

    # 生成分页的html代码
    """
    <nav aria-label="Page navigation" class="text-center">
    <ul class="pagination">
        <li>
            <a href="#" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
            </a>
        </li>
        <li><a href="/book_list?page=1">1</a></li>
        <li>
            <a href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
            </a>
        </li>
    </ul>
</nav>
    """
    tmp = []
    page_html_start = '<nav aria-label="Page navigation" class="text-center"><ul class="pagination">'
    page_html_end = '</ul></nav>'
    tmp.append(page_html_start)
    # 添加一个首页
    tmp.append('<li><a href="/book_list?page=1">首页</a></li>')
    # 添加一个上一页
    # 当当前页是第一页的时候不能再点击上一页
    if current_page -1 <= 0:
        tmp.append('<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
    else:
        tmp.append('<li><a href="/book_list?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(current_page-1))
    # for循环添加要展示的页码
    for i in range(show_page_start, show_page_end+1):
        # 如果for循环的页码等于当前页码，给li标签加一个active的样式
        if current_page == i:
            tmp.append('<li class="active"><a href="/book_list?page={0}">{0}</a></li>'.format(i))
        else:
            tmp.append('<li><a href="/book_list?page={0}">{0}</a></li>'.format(i))
    # 添加一个下一页
    # 当前 当前页已经是最后一页，应该不让下一页按钮能点击
    if current_page + 1 > total_page:
        tmp.append('<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">&raquo;</span></a></li>')
    else:
        tmp.append('<li><a href="/book_list?page={}" aria-label="Previous"><span aria-hidden="true">&raquo;</span></a></li>'.format(current_page+1))
    # 添加一个尾页
    tmp.append('<li><a href="/book_list?page={}">尾页</a></li>'.format(total_page))
    tmp.append(page_html_end)

    page_html = "".join(tmp)

    return render(request, "book_list.html", {"books": data, "page_html": page_html})
