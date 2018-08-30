from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
import random


# Create your views here.


def register(request):
    """
    用户注册
    :param request:
    :return:
    """
    if request.method == "POST":
        pass

    return render(request, "register.html")


def login(request):
    """
    用户登录页面
    :param request: 
    :return: 
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next = request.GET.get("next", "/index/")
        v_code = request.POST.get("v_code")
        if v_code.upper() == request.session.get("v_code"):
            user = auth.authenticate(request, username=username, password=password)
            if user:
                return redirect(next)
            else:
                return render(request, "login.html", {"error_msg": "*用户或者密码错误！"})
        else:
            return render(request, "login.html", {"code_msg": "*验证码有误！"})

    return render(request, "login.html")


def v_code(request):
    """
     随机验证码
    :param request:
    :return:
    """
    from PIL import Image, ImageDraw, ImageFont
    # 定义一个生成随机颜色代码的函数

    def random_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    # 创建一个随机颜色的图片对象
    image_obj = Image.new(
        "RGB",
        (100, 33),
        (255, 255, 140)
        # random_color()
    )
    # 在该图片对象上生成一个画笔对象
    draw_obj = ImageDraw.Draw(image_obj)
    # 加载一个字体对象
    font_obj = ImageFont.truetype('static/fonts/kumo.ttf', 28)
    tmp = []
    for i in range(5):
        l = chr(random.randint(97, 122))  # 生成随机的小写字母
        u = chr(random.randint(65, 90))  # 生成随机的大写字母
        n = str(random.randint(0, 9))  # 生成一个随机的数字
        # 从上面三个随机选一个
        r = random.choice([l, u, n])
        # 将选中过的那个字符写到图片上
        draw_obj.text((15 * i + 10, 0), r, fill=random_color(), font=font_obj)
        tmp.append(r)

    # 加干扰线
    width = 250  # 图片宽度（防止越界）
    height = 35
    for i in range(3):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw_obj.line((x1, y1, x2, y2), fill=random_color())

    # 加干扰点
    for i in range(20):
        draw_obj.point([random.randint(0, width), random.randint(0, height)], fill=random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw_obj.arc((x, y, x+4, y+4), 0, 90, fill=random_color())
    v_code = "".join(tmp).upper()
    # 将生成的验证码保存
    request.session["v_code"] = v_code
    # 直接在内存中保存图片替代io操作
    from io import BytesIO
    f1 = BytesIO()
    image_obj.save(f1, format="PNG")
    img_data = f1.getvalue()
    return HttpResponse(img_data, content_type="image/png")
