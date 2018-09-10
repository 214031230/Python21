#!/usr/bin/env python3
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
    import django

    django.setup()

    from app01 import models

    obj1 = models.Book.objects.all()
    obj2 = models.Book.objects.first()

    for i in obj1:
        print(i.name)
    print(obj2.name)
