from django.shortcuts import render, redirect, HttpResponse
from django import views
from django.contrib import auth
import random
from fault_reporting import forms
from django.http import JsonResponse
from fault_reporting import models
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


# 课件 ↓
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
