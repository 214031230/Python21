from django.shortcuts import render, redirect, HttpResponse
from django import views
from django.contrib import auth
import random
from fault_reporting import forms
from django.http import JsonResponse
from fault_reporting import models
from django.db.models import F
from django.db import transaction
from django.contrib.auth.decorators import login_required
import os
from bs4 import BeautifulSoup
# Create your views here.

from utils.geetest import GeetestLib

#请在官网申请ID使用，示例ID不可使用
pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"


# 这就是人家文档中提到的 初始化（API1）
def pcgetcaptcha(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)


class LoginView(views.View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        next_url = request.GET.get("next", "/index/")
        username = request.POST.get("username")
        pwd = request.POST.get("password")

        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)

        # 先判断验证码正不正确
        if result:
            user_obj = auth.authenticate(username=username, password=pwd)
            if user_obj:
                auth.login(request, user_obj)  # request.user
                return redirect(next_url)
            else:
                return render(request, "login.html", {"error_msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"error_msg": "验证码错误！"})


def index(request, *args):
    # 拿到当前登陆的用户
    # request.user
    # 拿到所有的业务线
    from django.db.models import Count
    lob_list = models.LOB.objects.all().annotate(num=Count("faultreport")).values("title", "num")
    # ORM 分组查询和聚合查询
    # 拿到所有的标签
    tag_list = models.Tag.objects.all().annotate(num=Count("faultreport")).values("title", "num")
    # 拿到一个日期归档的数据
    archive_list = models.FaultReport.objects.all().extra(
        # select={"ym": "date_format(create_time, '%%Y-%%m')"}  # MySQL日期格式化的写法
        select={"ym": "strftime('%%Y-%%m', create_time)"}  # sqlite数据库日期格式化的写法
    ).values("ym").annotate(num=Count("id")).values("ym", "num")

    # 取到所有的故障总结
    report_list = models.FaultReport.objects.all()

    if args and len(args) == 2:
        # 进入细分查询
        if args[0] == "lob":
            # 如果是按业务线查询
            report_list = report_list.filter(lob__title=args[1])
        elif args[0] == "tag":
            # 是按照标签查询
            report_list = report_list.filter(tags__title=args[1])
        else:
            # 按照日期（年月）来查询
            try:
                year, month = args[1].split("-")
                report_list = report_list.filter(create_time__year=year, create_time__month=month)
            except Exception:
                report_list = []

    return render(request, "index.html", locals())


# day20 ↓
class RegisterView(views.View):
    def get(self, request):
        # 实例化一个form对象
        form_obj = forms.RegisterForm()
        return render(request, "register.html", locals())

    def post(self, request):
        res = {"code": 0}
        print(request.POST)
        # 对用户提交过来的数据做有效性校验
        form_obj = forms.RegisterForm(request.POST)
        if form_obj.is_valid():
            # 数据没问题
            # 去数据库创建一条用户记录
            # form_obj.cleaned_data    --> 所有经过校验的数据
            # 创建用户
            # 先从form表单的cleaned_data里把确认密码字段的数据移除， 因为UserInfo表里不需要这个字段
            form_obj.cleaned_data.pop("re_password")
            # 头像数据 ，文件对象
            avatar_obj = request.FILES.get("avatar")
            # 头像文件可以自己写代码保存在服务端，然后将保存文件的路径传到数据库中保存
            models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_obj)
            res["url"] = "/login/"
        else:
            # 数据有问题
            res["code"] = 1
            res["error"] = form_obj.errors

        return JsonResponse(res)


def logout(request):
    auth.logout(request)  # request.session.flush()
    return redirect("/login/")


# 课件↓
# 个人中心视图
@login_required
def info(request):
    # 把当前这个用户发布的所有故障总结展示出来
    report_list = models.FaultReport.objects.filter(user=request.user)  # requesr.user.username
    return render(request, "info.html", locals())


# 故障总结详情页
def report_detail(request, report_id):
    # 根据id值去数据库中找到对应的那个故障总结
    report = models.FaultReport.objects.filter(id=report_id).first()
    if not report:
        return HttpResponse("404")

    return render(request, "report_detail.html", {"report": report})


# 点赞的视图函数
def updown(request):
    print(request.user)
    res = {"code": 0}
    print(request.POST)
    user_id = request.POST.get("user_id")  # request.user.id  --> 其实 谁发的请求就是谁点赞，没有必要前端传值
    report_id = request.POST.get("report_id")
    # is_up = request.POST.get("is_up")  # is_up永远是字符串  'true'或'false'
    is_up = True if request.POST.get("is_up") == "true" else False

    # 2. 每个人只能给一篇文章点一次推荐或者点一次反对
    is_exist = models.UpDown.objects.filter(user_id=user_id, fault_report_id=report_id).first()

    # 1. 不能推荐/反对 自己的文章
    if models.FaultReport.objects.filter(user_id=user_id, id=report_id):
        # 说明是给自己点赞/反对
        res["code"] = 1
        res["msg"] = "不能支持自己的文章" if is_up else "不能反对自己的文章"

    elif is_exist:
        # 如果有记录就说明已经点过了
        res["code"] = 1
        res["msg"] = "你已经推荐过" if is_exist.is_up else "你已经反对过"
    # 去创建点赞记录
    else:
        # 因为点赞表创建了新纪录同时还要更新故障总结表的点赞字段，涉及到事务操作
        # Django  ORM如何实现事务操作

        with transaction.atomic():
            # 1. 创建点赞记录
            models.UpDown.objects.create(
                user_id=user_id,
                fault_report_id=report_id,
                is_up=is_up
            )
            # 2. 更新对应故障总结的点赞数
            # 3. 如何在某个字段的值基础上+1
            if is_up:
                models.FaultReport.objects.filter(id=report_id).update(up_count=F("up_count")+1)
            else:
                models.FaultReport.objects.filter(id=report_id).update(down_count=F("down_count")+1)
        # 事务操作结束
        res["msg"] = "支持成功" if is_up else "反对成功"

    return JsonResponse(res)


# 评论
def comment(request):
    res = {"code": 0}
    print(request.POST)
    print("=" * 120)
    # 取到用户发送的评论数据
    report_id = request.POST.get("report_id")
    content = request.POST.get("content")
    parent_id = request.POST.get("parent_id", None)

    with transaction.atomic():
        if not parent_id:
            # 去数据库创建一条新评论
            comment_obj = models.Comment.objects.create(
                fault_report_id=report_id,
                user=request.user,
                content=content,
            )
        else:
            # 去数据库创建一条新的子评论
            comment_obj = models.Comment.objects.create(
                fault_report_id=report_id,
                user=request.user,
                content=content,
                parent_comment_id=parent_id
            )
        models.FaultReport.objects.filter(id=report_id).update(comment_count=F("comment_count")+1)

    res["data"] = {
        "id": comment_obj.id,
        "n": models.Comment.objects.count(),
        "create_time": comment_obj.create_time.strftime("%Y-%m-%d %H:%M:%S"),
        "user": comment_obj.user.username,
        "content": comment_obj.content
    }
    return JsonResponse(res)


# 发布新的故障总结
def add_report(request):
    if request.method == "POST":
        print(request.POST)
        content = request.POST.get("content")
        soup = BeautifulSoup(content, "html.parser")
        # 把script清洗掉
        for i in soup.find_all("script"):
            # 遍历所有的script标签，删除掉
            i.decompose()

        with transaction.atomic():
            # 先创建一条故障总结记录
            report_obj = models.FaultReport.objects.create(
                title=request.POST.get("title"),
                # 简介
                desc=soup.text[0:150],   # 只取HTML代码的文本内容
                lob_id=request.POST.get("lob"),
                user=request.user
            )
            # 创建一条故障总结详情记录
            models.FaultDetail.objects.create(
                content=soup.prettify(),  # 格式化完整的HTML内容
                fault_id=report_obj.id
            )
        return redirect("/fault-report/info/")

    lobs = models.LOB.objects.all()
    return render(request, "add_report.html", locals())


# 富文本编辑器上传图片的视图
def upload_img(request):
    print(request.FILES)
    res = {"error": 0}
    file_obj = request.FILES.get("imgFile")
    file_path = os.path.join("upload", "report_images", file_obj.name)
    # 将文件保存在本地
    with open(file_path, "wb") as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    # 将上传文件的url返回给富文本编辑器
    res["url"] = "/media/report_images/{}".format(file_obj.name)
    return JsonResponse(res)


def edit_report(request, report_id):
    # 编辑之后的更新





    report_obj = models.FaultReport.objects.filter(id=report_id).first()
    lobs = models.LOB.objects.all()
    return render(request, "edit_report.html", locals())


