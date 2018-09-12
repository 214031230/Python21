from django.conf.urls import url
from fault_reporting import views

urlpatterns = [

    # 第一版， 特别low版
    # url('^lob/(.*)/$', views.lob),
    # url('^tag/(.*)/$', views.tag),
    # url('^archive/(.*)/$', views.archive),
    #
    # # 第二版： 三合一
    # url(r'(lob|tag|archive)/(.*)/$', views.sanhe1),  # sanhe1(request, *args)  args[0]=="lob"

    # 第三版： 四合一
    url(r'(lob|tag|archive)/(.*)/$', views.index),  # index(request, "lob", "游戏")

    # 课件
    url(r'^info/$', views.info),
    # 故障总结详情页面
    url(r'^report/(\d+)/$', views.report_detail),  # report_detail(request, report_id)
    url(r'^updown/$', views.updown),  # 点赞
    url(r'^comment/$', views.comment),  # 评论

    url(r'^add-report/$', views.add_report),  # 发布新的故障总结
    url(r'^edit-report/(\d+)/$', views.edit_report),  # 编辑故障总结
    url(r'^upload-img/$', views.upload_img),  # 富文本编辑器用到的上传图片的接口


    url('^$', views.index),  # index(request)
]