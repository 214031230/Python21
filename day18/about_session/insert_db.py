#!/usr/bin/env python3
import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_session.settings")
    import django
    django.setup()
    from app01 import models

    # 批量导入500条数据
    data = [models.User(username="user{}".format(i), password="123") for i in
            range(1, 501)]
    models.User.objects.bulk_create(data)

