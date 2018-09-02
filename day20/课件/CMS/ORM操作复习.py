import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CMS.settings")
    import django
    django.setup()

    from fault_reporting import models
    # 找到第一个故障总结对象
    # report = models.FaultReport.objects.first()
    # # 找该故障总结关联的所有评论
    # # 基于对象的反向查询
    # ret = report.comment_set.all().count()
    # print(ret)
    #
    # # 找该故障总结关联的支持数
    # ret = report.updown_set.all().filter(is_up=True).count()
    # print(ret)
    from django.db.models import Count
    lob_list = models.LOB.objects.all().annotate(num=Count("faultreport")).values("title", "num")
    print(lob_list)

    archive_list = models.FaultReport.objects.all().extra(
        # select={"ym": "date_format(create_time, '%%Y-%%m')"}  # MySQL日期格式化的写法
        select={"ym": "strftime('%%Y-%%m', create_time)"}  # sqlite数据库日期格式化的写法
    ).values("ym").annotate(num=Count("id")).values("ym", "num")
    print(archive_list)
