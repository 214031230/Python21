#!/usr/bin/env python3
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HostManagement.settings")
    import django

    django.setup()
    from user import models
    from user.public import Public

    # 批量导入用户
    data = [models.UserInfo(username="user{}".format(i), password=Public.md5("user{}".format(i), "123")) for i in
            range(100)]
    models.UserInfo.objects.bulk_create(data)
