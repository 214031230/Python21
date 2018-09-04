from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
import random
from django.contrib.auth.decorators import login_required
from fault_reporting.forms import UserUpdate
from fault_reporting.forms import RegisterForm
from fault_reporting import models
from django.http import JsonResponse
from django.forms import model_to_dict
from django.db.models import Count


# Create your views here.


def register(request):
    """
    用户注册
    :param request:
    :return:
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


def index(request):
    """
    首页
    :param request:
    :return:
    """
    user = auth.get_user(request).username
    fault_list = models.Fault.objects.all()
    # class_list = models.Classify.objects.all()  # 反向查询取值
    class_list = models.Classify.objects.all().annotate(num=Count("fault")).values("name", "num")  # 反向查询取值
    # tag_list = models.Tag.objects.all()  # 反向查询取值
    tag_list = models.Tag.objects.all().annotate(num=Count("fault")).values("name", "num")  # 反向查询取值
    archive_list = models.Fault.objects.all().extra(
        # select={"ym": "date_format(create_time, '%%Y-%%m')"}  # MySQL日期格式化的写法
        select={"ym": "strftime('%%Y-%%m', create_time)"}  # sqlite数据库日期格式化的写法
    ).values("ym").annotate(num=Count("id")).values("ym", "num")
    return render(request, "index.html", locals())


@login_required
def logout(request):
    """
    注销用户
    :param request:
    :return:
    """
    auth.logout(request)
    return redirect("/login/")


@login_required
def p_center(request):
    """
    编辑中心
    :param request:
    :return:
    """
    user = auth.get_user(request)
    obj = models.UserInfo.objects.filter(username=user).first()
    user_dict = model_to_dict(obj)
    form_obj = UserUpdate(user_dict)
    if request.method == "POST":
        form_obj = UserUpdate(request.POST, instance=obj)
        if form_obj.is_valid():
            obj.save()
            return redirect("/index/")
    return render(request, "p_center.html", locals())


@login_required
def set_password(request):
    """
    修改密码
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
    :param request:
    :return:
    """
    from PIL import Image, ImageDraw, ImageFont

    def random_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    image_obj = Image.new(
        "RGB",
        (100, 33),
        (255, 255, 140)
        # random_color()
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

    width = 250
    height = 35
    for i in range(3):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw_obj.line((x1, y1, x2, y2), fill=random_color())

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
