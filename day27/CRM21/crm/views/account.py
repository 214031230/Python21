import random
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from crm import models
from crm.utils.md5 import md5
from rbac.service.permission import init_permission


def login(request):
    """
    用户登录
        post请求：
            1. 获取用户名和密码进行ORM校验（校验前需要先对密码进行MD5加密（加盐））
            2. 如果校验失败，则返回登录页面，并返回错误提示
            3. 校验成功，则创建session用来存储用户ID和用户名
            4. 进行RBAC登录初始化操作（初始化操作需要传递2个参数，用户对象和request）
            5. 登录成功跳转到欢迎页面
        get请求：
            1. 返回登录页面
    :param request:
    :return:
    """
    if request.method == 'POST':
        msg = {
            "error": "",
            "v_code": "",
        }
        session_v_code = request.session.get("v_code")
        v_code = request.POST.get("v_code")
        if v_code.upper() != session_v_code:
            msg["v_code"] = "验证码错误！"
            return render(request, 'login.html', msg)
        user = request.POST.get('username')
        pwd = md5(request.POST.get('password'))
        user_object = models.UserInfo.objects.filter(username=user, password=pwd).first()
        if not user_object:
            msg["error"] = "用户名或密码错误！"
            return render(request, 'login.html', msg)
        request.session['user_info'] = {'id': user_object.id, 'name': user_object.username}
        init_permission(user_object, request)
        return redirect(reverse('index'))

    return render(request, 'login.html')


def logout(request):
    """
    注销
        1. 删除用户session
        2. 跳转到登录页面
    :param request:
    :return:
    """
    request.session.delete()
    return redirect(reverse("login"))


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
    font_obj = ImageFont.truetype('crm/static/crm/fonts/kumo.ttf', 28)
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


def index(request):
    msg = {"username": request.session.get("user_info").get("name")}
    return render(request, 'index.html', msg)
