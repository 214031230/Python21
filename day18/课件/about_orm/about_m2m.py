import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_orm.settings")

    import django
    django.setup()

    from app01 import models

    # author_obj = models.Author.objects.first()
    # # 多对多的正向查询
    # ret = author_obj.books.all()
    # print(ret)
    # 多对多的反向查询
    # book_obj = models.Book.objects.last()
    # # 默认按照表名（全小写）_set.all()
    # # ret = book_obj.author_set.all()
    # # 如果多对多字段设置了related_name属性，反向查询的时候就按该属性值来查询
    # ret = book_obj.authors.all()
    # print(ret)

    # add方法
    # author_obj = models.Author.objects.first()
    # ret = author_obj.books.all()
    # print(ret)
    # # 给作者加一本关联的书籍
    # # author_obj.books.set([2, 3])
    # author_obj.books.add(2)
    # ret = author_obj.books.all()
    # print(ret)

    # 查询第一个作者写过的书的名字
    # 1. 基于对象的查询
    # ret = models.Author.objects.first().books.all().values("title")
    # print(ret)
    # 基于QuerySet的双下划线查询
    # ret = models.Author.objects.filter(id=2).values("books__title")
    # print(ret)

    # 基于QuerySet的双下划线的反向查询
    # 由书找作者
    # ret = models.Book.objects.filter(id=2).values("authors__name")
    # print(ret)





