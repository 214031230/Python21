# 如何在一个py文件中 使用Django项目的相关配置或内容
import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    import django
    django.setup()

    from app01 import models

    # 查询age=18的第一个人
    # ret = models.Person.objects.get(age=18)  # pk unique
    # print(ret)
    # 查询age=18的所有人
    # ret = models.Person.objects.filter(age=18)
    # print(ret[0])

    # ret = models.Person.objects.filter(age=18).values("age", "phone")
    # print(ret)

    # ret = models.Person.objects.filter(age=18).values_list("age", "phone")
    # print(ret)

    # 排序
    # ret = models.Person.objects.all().order_by("age")
    # print(ret)

    # 查询年龄大于18岁的
    # ret = models.Person.objects.filter(age__gt=18, id__gt=1)
    # print(ret)

    # 查询id值在 [1, 2]的人
    # ret = models.Person.objects.filter(id__in=[1, 2, 20000])
    # print(ret)
    #
    # 查询id值不在[1,2]的人
    # ret = models.Person.objects.exclude(id__in=[1,2])
    # print(ret)

    # 查询名字中包含 JJ 的那个人
    # ret = models.Person.objects.filter(name__contains="JJ")
    # print(ret)
    # 不区分大小写查询
    # ret = models.Person.objects.filter(name__icontains="jj")
    # print(ret)

    # 查询id在1-3区间内的数据
    # ret = models.Person.objects.filter(id__range=[1, 3])
    # print(ret)

    # 查询以JJ结尾的人
    # ret = models.Person.objects.filter(name__endswith='JJ')
    # print(ret)
    # print(models.Person.objects.first().birthday)
    # 查询 生日 是 2018年的所有人
    # ret = models.Person.objects.filter(birthday__year=2018)
    # print(ret)

    # 查询第一本书关联的出版社的名字
    # 1. 基于对象的查询
    # book_obj = models.Book.objects.first()
    # ret = book_obj.publisher.name
    # print(ret)
    # 2. 基于queryset的双下划线查询，双下划线表示跨表
    # ret = models.Book.objects.all().values_list("publisher__name").distinct()
    # print(ret)

    # 反向查询
    # 1. 由出版社反向查询书籍(基于对象的查询)
    # publisher_obj = models.Publisher.objects.get(id=2)  # 找到张江出版社
    # 张江出版社出版的所有书籍
    # ret = publisher_obj.book_set.all()
    # print(ret)

    # 2. 基于queryset的双下划线
    # 江出版社出版的所有书籍的书名
    ret = models.Publisher.objects.filter(id=2).values_list("book__title")
    print(ret)



