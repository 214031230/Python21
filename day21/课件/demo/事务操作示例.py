import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
    import django
    django.setup()

    from app01 import models

    # 不用事务操作，出现两个数据库操作：一个成功，一个失败
    # models.Publisher.objects.create(name="沙河出版社")
    # models.Book.objects.create(title="跟老男孩学Linux", isher_id=10000)



    # 事务操作
    # from django.db import transaction
    # with transaction.atomic():
    #     models.Publisher.objects.create(name="沙河出版社")
    #     models.Book.objects.create(title="跟老男孩学Linux", isher_id=10000)



    # 如何在字段原来值的基础上+1
    # book_obj = models.Book.objects.create(
    #     title="跟老男孩学Linux",
    #     publisher_id=1,
    #     num=100
    # )

    # 基于对象的更新
    # 基于对象的更新SQL语句是所有字段都更新一边
    # book_obj = models.Book.objects.first()
    # book_obj.num = book_obj.num + 1
    # book_obj.save()

    # 基于queryset的更新
    # update只会更新指定的那个字段，其他的字段不更新

    # from django.db.models import F
    # query_set = models.Book.objects.filter(id=1)
    # query_set.update(num=F("num")+1)


    # 查询收藏数大于1000的书
    # ret = models.Book.objects.filter(keep_num__gt=1000)
    # print(ret)

    # 查询收藏数大于评论数的书
    from django.db.models import F
    # ret = models.Book.objects.filter(keep_num__gt=F("comment_num"))
    # print(ret)

    # 查询收藏数等于100 或 书名是跟Alex学熬鸡汤 的书
    # from django.db.models import Q
    # ret = models.Book.objects.filter(keep_num=100, title="跟Alex学熬鸡汤")
    # print(ret)
    # print("=" * 120)
    # ret = models.Book.objects.filter(Q(keep_num=100) | Q(title="跟Alex学熬鸡汤"))
    # print(ret)


    # 执行原生的SQL语句
    # from django.db import connection
    # cursor = connection.cursor()
    # cursor.execute("select * from app01_book;")
    # ret = cursor.fetchone()
    # print(ret)














