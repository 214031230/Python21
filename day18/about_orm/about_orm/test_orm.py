#!/usr/bin/env python3
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")
    import django
    django.setup()
    
    from app01 import models
    
    # 单表增删改查

    # 增
    # models.Book.objects.create(name="跟老男孩学py", publisher_id=2)
    # 删
    # models.Book.objects.filter(id=3).delete()
    # 改
    # models.Book.objects.filter(id=1).update(name="运维自动化01")
    # obj = models.Book.objects.filter(id=1).first()
    # obj.name = "运维自动化02"
    # obj.save()
    # 查
    # ret = models.Book.objects.all()
    # print(ret)
    #
    # # 1.
    # # all() --> 查询所有结果
    # print(models.Book.objects.all())
    # # 2.
    # # filter() --> 根据查询条件查询数据库的
    # print(models.Book.objects.filter(id=1))
    # # 3.
    # # get() --> 获取一个唯一的值
    # print(models.Book.objects.get(id=1))
    # # 4.
    # # exclude() --> 将符合条件的都剔除掉，留下不符合条件的
    # print(models.Book.objects.exclude(id=1))
    # # 5.
    # # values('字段名', ...) --> 返回一个QuerySet, 里面是字典
    # print(models.Book.objects.values())
    # # 6.
    # # values_list(字段名
    # # ', ...)          --> 返回一个QuerySet,里面是元祖
    # print(models.Book.objects.values_list())
    # # 7.
    # # order_by() --> 对查询结果排序
    # print(models.Book.objects.all().order_by("id"))
    # # 8.
    # # reverse() --> 对一个有序的查询结果集做反转
    # print(models.Book.objects.all().order_by("id").reverse())
    # # 9.
    # # distinct() --> 去重，跨表查询时去掉重复的记录
    # print("-"*20)
    # print(models.Book.objects.all().values("name").distinct())
    # # 10.
    # # count() --> 返回数据条数
    # print(models.Book.objects.all().count())
    # # 11.
    # # first() --> 取第一个数据
    # print(models.Book.objects.first())
    # # 12.
    # # last() --> 取最后一条数据
    # print(models.Book.objects.last())
    # # 13.
    # # exists() --> 判断表里有没有数据
    # print(models.Book.objects.filter(id=10).exists())

    # print(models.Book.objects.filter(id__lt=3, id__gt=1))
    # print(models.Book.objects.filter(id__in=[1, 2, 3]))
    # print(models.Book.objects.exclude(id__in=[1, 2]))
    # print(models.Book.objects.filter(name__contains="03"))
    # print(models.Book.objects.filter(id__range=[1, 3]))
    # print(models.Book.objects.filter(name__startswith="运"))

    # 跨表查询
    # 基于对象的查询
    # 正向查询
    # print(models.Book.objects.first().publisher.name)
    # print(models.Book.objects.last().publisher.name)
    # print(models.Book.objects.filter(id=1).first().publisher.id)
    # 反向查询
    # print(models.Publisher.objects.first().book_set.all())

    # 基于queryset的查询
    # 正向查询
    # print(models.Book.objects.values_list("publisher__name"))
    # # 反向查询
    # print(models.Publisher.objects.values_list("book__name"))

    # 多对多正向查询
    #
    # print(models.Author.objects.last().books.all())
    # print(models.Book.objects.last().authors.all())
    # models.Author.objects.last().books.set([1, 2])
    # print(models.Author.objects.last().books.all())
    # models.Author.objects.last().books.add(7)
    # print(models.Author.objects.last().books.all())
    # print(models.Author.objects.last().books.all().values("name"))
    # print(models.Author.objects.filter(id=1).values("books__name"))
    # print(models.Book.objects.filter(id=1).values("authors__name"))




