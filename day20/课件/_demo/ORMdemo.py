import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_demo.settings")
    import django
    django.setup()

    from app01 import models
    # ret = models.Employee1.objects.all()  # select * from employee1;
    # print(ret)

    # ret = models.Employee1.objects.values()  # [{}, {}]
    # ret = models.Employee1.objects.values_list()  # [(), ()]
    # ret = models.Employee1.objects.values("dept")  # select dept from employee1;
    # print(ret)
    from django.db.models import Avg, Max, Min, Count, Sum
    # ret = models.Employee1.objects.values("dept").annotate(avg_salary=Avg("salary")).values("dept", "avg_salary")
    # print(ret)

    ret = models.Employee2.objects.values("dept_id").annotate(avg_salary=Avg("salary")).values("dept__name", "avg_salary")
    print(ret)