from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
import random
import os
from django.contrib.auth.decorators import login_required
from fault_reporting.forms import UserUpdateForm
from fault_reporting.forms import RegisterForm
from fault_reporting import models
from django.http import JsonResponse
from django.forms import model_to_dict
from django.db.models import Count
from django.db import transaction
from django.db.models import F
from bs4 import BeautifulSoup
from public.paging import Paging


# Create your views here.


def register(request):
    """
    用户注册
        1. 前端使用ajax提交
        2. res 返回给前端js的字典，前端用过判断code值来返回对应的页面。
    :param request:
    :return:
            1. get 请求，返回form_obj对象，在页面展示
            2. post 请求,
                1. 生成一个res字典用于返回给前端页面
                2. 拿到request.POST中的数据去form_obj中校验
                3. form_obj.is_valid 如果校验通过，开始创建数据
                    1. 由于RegisterForm 中没有re_password字段，需要先删除cleaned_data中删除
                    2. 头像（avatar）无法从cleaned_data中获取，需要从request.FILES.get中获取时刻
                    3. 拿到数据开始创建，由于密码是加密的，所以需要使用create_user创建，而不是直接
                        使用orm 的 create创建，**form_obj.cleaned_data 是打散字典的操作，头像赋值给
                        avatar
                    4. 创建成功给用户返回一个url
                4. 校验失败
                    1. 把校验状态改成1， 并返回错误信息
                5. 通过JsonResponse返回字典给JS，这里返回的是json字典对象。前端可以做响应的处理
    """
    form_obj = RegisterForm()
    if request.method == "POST":
        res = {"code": 0}
        form_obj = RegisterForm(request.POST)
        if form_obj.is_valid():
            form_obj.cleaned_data.pop("re_password")
            avatar_obj = request.FILES.get("avatar")
            models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_obj)
            res["url"] = "/login/"
        else:
            res["code"] = 1
            res["error"] = form_obj.errors
        return JsonResponse(res)

    return render(request, "register.html", locals())


def login(request):
    """
    用户登录页面
        1. get 请求： 返回用户登录页面，用户登录的时候不需要显示用户名，user = ""
        2. post 请求：
                    1. 取到用户名，密码，请求的页面，验证码
                    2. 忽略验证码大写小，判断验证码和session中存的是否一致
                        1. 验证码一致，
                        2. 使用auth组件的authenticate方法校验用户
                            1. 校验通过
                            2. 使用auth组件login方法创建session
                            3. 并返回用户请求页面，如果没有默认请求页面则跳转到/index/页面
                                next = request.GET.get("next", "/index/") 如果取不到next的值，默认值是/index/
                        3. 校验失败 返回错误信息给页面，并返回用户名给input的value，不需要用户在填用户名
                    3. 验证码不一致，则返回错误页面，并返回用户给input的value，不要用户在填写用户名
    :param request:
    :return:
    """

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password")
        next = request.GET.get("next", "/index/")
        v_code = request.POST.get("v_code")
        # if v_code.upper() == request.session.get("v_code"):
        if True:
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(next)
            else:
                return render(request, "login.html", {"error_msg": "*用户或者密码错误！", "user": username})
        else:
            return render(request, "login.html", {"code_msg": "*验证码有误！", "user": username})

    return render(request, "login.html", {"user": ""})


def index(request, *args):
    """
    首页
        1. 在前端页面需要显示的分类（两种方法：1、反向查询（一次查询操作2张表） 2、聚合分组查询（效率高））
                1. class_list 通过分组聚合取到所有的产品线名称，只取name和num字段
                2. tag_list 通过分组聚合取所有的表标签名称,只取name和num字段
                3. archive_list 由于orm没有时间格式化的功能，需要通过orm执行原生sql，时间格式化只取年-月(2018-9)，
                    只取日期和num字段，当使用mysql的时候需要这样写：
                    select={"ym": "date_format(create_time, '%%Y-%%m')"}  # MySQL日期格式化的写法
        2. user = 通过auth取到用户名
        3. 如果args没有值，返回index页面，并返回所有的报障信息 
            fault_list = 默认显示所有的报障内容
        4. 如果args有值，并且是2个值
            1. 如果args[0] == "class"  fault_list  = 对应产品线的名称
            2. 如果args[0] == "tag":   fault_list  = 对应标签的名称
            3. 如果args[0] == "archive":  fault_list  =  对应月份的时间
                注意：  year, month = args[1].split("-") 只能切割 2018-9类似这样格式的日期，如果是其他格式则会报错，这里
                        使用try捕捉异常，如果捕捉到 fault_list = []
    :param request:
    :param args  args[0] = class|tag|archive
                 args[1] = classify__name|tags__name|时间（2018-9）
    :return:
    """
    # user = auth.get_user(request).username
    # class_list = models.Classify.objects.all().annotate(num=Count("fault")).values("name", "num")
    # tag_list = models.Tag.objects.all().annotate(num=Count("fault")).values("name", "num")
    # archive_list = models.Fault.objects.all().extra(select={
    #     "ym": "strftime('%%Y-%%m', create_time)"}).values("ym").annotate(num=Count("id")).values("ym", "num")
    # fault_list = models.Fault.objects.all()
    # if args and len(args) == 2:
    #     if args[0] == "class":
    #         fault_list = fault_list.filter(classify__name=args[1])
    #     elif args[0] == "tag":
    #         fault_list = fault_list.filter(tags__name=args[1])
    #     else:
    #         try:
    #             year, month = args[1].split("-")
    #             fault_list = fault_list.filter(create_time__year=year, create_time__month=month)
    #         except Exception:
    #             fault_list = []
    #
    # return render(request, "index.html", locals())
    user = auth.get_user(request).username
    class_list = models.Classify.objects.all().annotate(num=Count("fault")).values("name", "num")
    tag_list = models.Tag.objects.all().annotate(num=Count("fault")).values("name", "num")
    archive_list = models.Fault.objects.all().extra(select={
        "ym": "strftime('%%Y-%%m', create_time)"}).values("ym").annotate(num=Count("id")).values("ym", "num")
    fault_list = models.Fault.objects.all()
    total_count = fault_list.count()
    current_page = request.GET.get("page", None)
    page_obj = Paging(current_page, total_count, url_prefix="index", max_show=5)
    if args and len(args) == 2:
        if args[0] == "class":
            fault_list = fault_list.filter(classify__name=args[1])
        elif args[0] == "tag":
            fault_list = fault_list.filter(tags__name=args[1])
        else:
            try:
                year, month = args[1].split("-")
                fault_list = fault_list.filter(create_time__year=year, create_time__month=month)
            except Exception:
                return HttpResponse("404页面不存在")
        total_count = fault_list.count()
        current_page = request.GET.get("page", None)
        page_obj = Paging(current_page, total_count, url_prefix="fault-report/{}/{}".format(args[0], args[1]), max_show=5)
    try:
        data = fault_list[page_obj.start:page_obj.end]
    except Exception:
        data = []
    page_html = page_obj.page_html()
    return render(request, "index.html", locals())


@login_required
def logout(request):
    """
    注销用户
         auth.logout 删除session并返回到登录页面
    :param request:
    :return:
    """
    auth.logout(request)
    return redirect("/login/")


@login_required
def p_center(request):
    """
    编辑中心
        1. 取到当前用户名
        2. 根据用户名取到用户对象（即orm对象）
        3. 请求是get :
            1. 把用户对象转成字典 model_to_dict（）
            2. 把用户对象传值给form并返回给页面
        4. 请求是post ：
            1. 拿到request.POST中数据到form进行校验
            2. 如果校验通过
                1. 更新cleaned_data中的数据到orm对象中
                2. 文件格式的数据需要request.FILES.get("avatar")取值，
                    1. 用户编辑头像的时候没有修改头像，则使用原来的头像，如果传值了则使用新值
                3. 保存对象
                4. 并返回到个人中心页面
    :param request:
    :return:
    """
    user = auth.get_user(request)
    user_obj = models.UserInfo.objects.filter(username=user).first()
    user_dict = model_to_dict(user_obj)
    form_obj = UserUpdateForm(user_dict)
    if request.method == "POST":
        form_obj = UserUpdateForm(request.POST)
        if form_obj.is_valid():
            user_obj.phone = form_obj.cleaned_data.get("phone")
            user_obj.email = form_obj.cleaned_data.get("email")
            user_obj.avatar = request.FILES.get("avatar") if request.FILES.get("avatar") else user_obj.avatar
            user_obj.save()
            return redirect("/p_center/")

    return render(request, "p_center.html", locals())


@login_required
def set_password(request):
    """
    修改密码
        1. get 请求 返回修改密码页面
        2. post 请求 
            1. 用户POST中取到 原始密码，新密码，确认密码
            2. 使用auth组件对原始密码进行校验
                1. 校验通过
                    1. 对比新密码和确认密码是否一致，如果不一致则返回错误页面
                    2. 如果一致，则使用auth修改密码，并保存
                    3. 跳转到 index 页面
                2. 校验不通过
                    返回错误信息
    :param request:
    :return:
    """
    user = auth.get_user(request)
    if request.method == "POST":
        password_old = request.POST.get("password_old")
        password_new_1 = request.POST.get("password_new_1")
        password_new_2 = request.POST.get("password_new_2")

        if user.check_password(password_old):
            if password_new_1 == password_new_2:
                user.set_password(password_new_2)
                user.save()
                return redirect("/index/")
            else:
                return render(request, "set_password.html", {"user": user, "error_msg_pwd": "*两次密码不一致"})
        else:
            return render(request, "set_password.html", {"user": user, "error_msg": "*原始密码不正确"})

    return render(request, "set_password.html", {"user": user})


def v_code(request):
    """
     随机验证码
        1. ImageDraw.Draw 创建一个随机颜色的图片对象
        2. ImageFont.truetype 加载一个字体对象
        3. for i in range(5) 生成随机5位验证码
            1. 包含大小写字母，数字
            2. 每生成一个写到图片上，draw_obj.text((15 * i + 10, 0), r, fill=random_color(), font=font_obj)
        4. 将验证码保存到session中
        5. from io import BytesIO 直接在内存中保存图片替代io操作
    :param request:
    :return:
    """
    from PIL import Image, ImageDraw, ImageFont

    def random_color():
        """
        定义一个生成随机颜色代码的函数
        :return: 返回一个随机颜色，元组格式的rgb
        """
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    image_obj = Image.new(
        "RGB",
        (100, 33),
        (255, 255, 140)
    )
    draw_obj = ImageDraw.Draw(image_obj)
    font_obj = ImageFont.truetype('static/fonts/kumo.ttf', 28)
    tmp = []
    for i in range(5):
        l = chr(random.randint(97, 122))
        u = chr(random.randint(65, 90))
        n = str(random.randint(0, 9))
        r = random.choice([l, u, n])
        draw_obj.text((15 * i + 10, 0), r, fill=random_color(), font=font_obj)
        tmp.append(r)

    # 添加干扰线
    width = 250  # 图片宽度（防止越界）
    height = 35
    for i in range(3):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw_obj.line((x1, y1, x2, y2), fill=random_color())

    # 添加噪点
    for i in range(20):
        draw_obj.point([random.randint(0, width), random.randint(0, height)], fill=random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw_obj.arc((x, y, x + 4, y + 4), 0, 90, fill=random_color())
    v_code = "".join(tmp).upper()
    request.session["v_code"] = v_code
    from io import BytesIO
    f1 = BytesIO()
    image_obj.save(f1, format="PNG")
    img_data = f1.getvalue()
    return HttpResponse(img_data, content_type="image/png")


@login_required
def info(request):
    """
    用户个人中心首页，显示用户发布的故障
        1. 取到当前用户
        2. 使用数据库中取当前用户的发布的所有报障
        3. 返回给页面，交给html显示处理
    新增功能：分页功能
    :param request:
    :return:
    """
    # user = request.user
    # fault_list_user = models.Fault.objects.filter(user=user)
    # return render(request, "info.html", locals())
    user = request.user
    fault_list_user = models.Fault.objects.filter(user=user)
    total_count = fault_list_user.count()
    current_page = request.GET.get("page", None)
    page_obj = Paging(current_page, total_count, url_prefix="fault-report/info", max_show=5)
    data = fault_list_user[page_obj.start:page_obj.end]
    page_html = page_obj.page_html()
    return render(request, "info.html", locals())


def report_detail(request, detail_id):
    """
    用户详情页面
    1. 根据用户传过来的故障ID值，取故障对象返回给页面展示处理
    2. ID取不到对象，则返回404
    3. 导航条需要接受一个user参数，
    :param request: 
    :param detail_id: 
    :return: 
    """
    report = models.Fault.objects.filter(id=detail_id).first()
    print(report.comment_set.all())
    user = request.user.username
    if not report:
        return HttpResponse("404页面")
    return render(request, "report_detail.html", locals())


def up_down(request):
    """
    点赞或者反对
        1. 取到点赞用户的ID
        2. 取到被点赞的文章
        3. 取到用户是点赞还是反对
        4. 用户不能对自己的文章进行点赞，判断用户是不是对自己的文章进行点赞
            1. is_me 判断文章作者和点赞用户是不是同一个人
            2. 如果is_me是有值说明是给自己点赞
            3. 修改res["code"]等于1，增加res["mes"]等于 "不能支持自己的文章" if is_up else "不能反对自己的文章"
        5. 用户只能对一篇文章进行一次点赞或者反对，判断用户是否是第一次点赞
            1. is_exist 判断用户是否已经点过赞或者反对
            2. 如果is_exist有值说明用户已经点过赞
            3. 修改res["code]等于1，增加res["meg"]等于 "你已经推荐过" if is_exist.is_up else "你已经反对过"
        6. 开始在数据库中增加增加点赞或反对数据
            1. 用户点赞需要操作两张表，Fault 和UpDown表，这里用到了事务操作
            2. 创建成功以后，增加 res["msg"] = "点赞成功" if is_up else "反对成功"
        7. 返回JsonResponse(res)
    :param request:
    :return:
    """
    res = {"code": 0}
    user = models.UserInfo.objects.filter(username=request.user.username).first()
    report_id = request.POST.get("report_id")
    is_up = True if request.POST.get("is_up") == "true" else False
    is_exist = models.UpDown.objects.filter(user_id=user.id, fault_id=report_id).first()
    is_me = models.Fault.objects.filter(id=report_id, user_id=user.id).first()
    if is_me:
        res["code"] = 1
        res["msg"] = "不能支持自己的文章" if is_up else "不能反对自己的文章"
    elif is_exist:
        res["code"] = 1
        res["msg"] = "你已经推荐过" if is_exist.is_up else "你已经反对过"
    else:
        with transaction.atomic():
            models.UpDown.objects.create(
                user_id=user.id,
                fault_id=report_id,
                is_up=is_up
            )

            if is_up:
                models.Fault.objects.filter(id=report_id).update(up_count=F("up_count") + 1)
            else:
                models.Fault.objects.filter(id=report_id).update(up_count=F("down_count") + 1)
        res["msg"] = "点赞成功" if is_up else "反对成功"

    return JsonResponse(res)


@login_required
def comment(request):
    """
    用户评论
    1. 取到页面传递的参数
        1. 取到文章ID
        2. 取到评论内容
        3. 取到评论的父评论ID
    2. 往数据库中写评论，需要操作2张表（Comment和Fault），这里又用到了事务操作，要成功都成功，有一个失败则都失败
    3. 操作Comment表判断是否有父评论
        1. 如果没有父评论
            1. 去ORM创建评论，只需要传递3个字段，评论内容，被评论的文章ID，评论用户
        2. 如果有父评论
            1. 去ORM创建评论，只需要传递3个字段，评论内容，被评论的文章ID，评论用户, 父评论ID
    4. 操作Fault表，增加评论数 
    5. 返回评论内容到前端页面进行展示
          
    :param request:
    :return:
    """
    res = {"code": 0}
    report_id = request.POST.get("report_id")
    content = request.POST.get("content")
    parent_id = request.POST.get("parent_id", None)
    user = request.user

    with transaction.atomic():
        if not parent_id:
            comment_obj = models.Comment.objects.create(
                content=content,
                fault_id=report_id,
                user=user,
            )
        else:
            comment_obj = models.Comment.objects.create(
                content=content,
                fault_id=report_id,
                user=user,
                parent_comment_id=parent_id
            )
        models.Fault.objects.filter(id=report_id).update(comment_count=F("comment_count") + 1)

    res["data"] = {
        "id": comment_obj.id,
        "n": models.Comment.objects.filter(fault_id=report_id).count(),
        "create_time": comment_obj.comment_date,
        "user": comment_obj.user.username,
        "content": comment_obj.content,
    }
    return JsonResponse(res)


@login_required
def add_report(request):
    """
    新增报障
        1. get请求：
            1. 取到所有的业务线
            2. 返回发布页面，并返回业务线
        2. post请求
            1. 取到故障标题
            2. 取到故障内容
            3. 取到所属业务线
            4. 在发布故障之前，先清除script代码，防止跨站攻击.使用bs4模块
            5. 发布故障需要同时操作两种表，又用到了事务操作, FaultDetail 和 Fault
            6. 创建数据需要注意：
                1. 由于用户内容是html文件，直接字符串切割简介是包含html内容的，需要使用BeautifulSoup
                    切割
                2. 同样保障详情也需要使用需要使用BeautifulSoup格式化
            7. 发布成功以后跳转到故障详情页面
    :param request:
    :return:
    """
    class_obj = models.Classify.objects.all()
    if request.method == "POST":
        report_title = request.POST.get("report_title")
        report_content = request.POST.get("report_content")
        report_class = request.POST.get("report_class")

        soup = BeautifulSoup(report_content, "html.parser")
        for i in soup.find_all("script"):
            i.decompose()

        with transaction.atomic():
            obj = models.Fault.objects.create(
                title=report_title,
                summary=soup.text[0:150],
                classify_id=report_class,
                user=request.user
            )
            models.FaultDetail.objects.create(
                content=soup.prettify(),
                fault_id=obj.id
            )
        return redirect("/fault-report/report_detail/%s/" % (obj.id,))
    return render(request, "add_report.html", locals())


def upload_img(request):
    """
    富文本框图片显示
        1. 取到富文本框上传的图片
        2. 保存文件
        3. 将上传文件的url返回给富文本编辑器
    :param request:
    :return:
    """
    res = {"error": 0}
    file_obj = request.FILES.get("imgFile")
    file_path = os.path.join("media", "report_images", file_obj.name)
    with open(file_path, "wb") as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    res["url"] = "/media/report_images/{}".format(file_obj.name)
    return JsonResponse(res)


@login_required
def edit_report(request, report_id):
    """
    编辑故障
        1. get请求
    :param request:
    :return:
    """
    if request.method == "POST":
        report_title = request.POST.get("report_title")
        report_content = request.POST.get("report_content")
        report_class = request.POST.get("report_class")
        report = models.Fault.objects.filter(id=report_id).first()

        soup = BeautifulSoup(report_content, "html.parser")
        for i in soup.find_all("script"):
            i.decompose()

        with transaction.atomic():
            obj = models.Fault.objects.filter(id=report_id).update(
                title=report_title,
                summary=soup.text[0:150],
                classify_id=report_class,
            )
            models.FaultDetail.objects.filter(fault_id=report.id).update(
                content=soup.prettify(),
            )
        return redirect("/fault-report/report_detail/%s/" % (report.id,))

    report_obj = models.Fault.objects.filter(id=report_id).first()
    class_obj = models.Classify.objects.all()
    return render(request, "edit_report.html", locals())


@login_required
def delete_report(request):
    """
    删除故障
    :param request:
    :return:
    """
    report_id = request.GET.get("id")
    obj_id = models.Fault.objects.filter(id=report_id).first()
    with transaction.atomic():
        models.Fault.objects.filter(id=report_id).delete()
        models.FaultDetail.objects.filter(fault_id=obj_id).delete()

    return HttpResponse("1")
    # return redirect("/fault-report/info/")


@login_required
def my_comment(request):
    """
    查看我评论的
    :param request:
    :return:
    """
    user = request.user
    obj = models.Comment.objects.filter(user=user)
    fault_list_user = obj.values("fault__title")
    return render(request, "my_comment.html", locals())
