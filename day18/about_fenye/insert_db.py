#!/usr/bin/env python3
"""
批量向数据库插入用户
"""
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "about_fenye.settings")
    import django
    django.setup()
    from app01 import models

    # 低效写法
    # for i in range(500):
    #     models.User.objects.create(name="user{}".format(i))

    # 高效写法
    data = [models.User(name="user{}".format(i)) for i in range(403)]
    models.User.objects.bulk_create(data)
    
    

