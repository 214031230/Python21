import json
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from repository import models


@csrf_exempt
def server(request):
    """
    资产采集API
    POST：
        取到auto_client传递过来的数据
    GET:
        返回接口成功页面
    :param request:
    :return:
    """
    if request.method == "POST":
        client_info = json.loads(request.body.decode("utf-8"))

        if not client_info["basic"]["status"]:
            return HttpResponse("没有获取到主机名，无法进行下一步操作")
        else:
            """
            如果获取到主机名则执行创建和更新数据操作
            """
            hostname = client_info["basic"]["data"]["hostname"]
            print("32123423", hostname)
            server_obj = models.Server.objects.filter(hostname=hostname).first()
            if not server_obj:
                """
                如果没有hostname对象则进行添加操作
                """
                print("没有主机")
                # 增加server表开始
                tmp = {}
                tmp.update(client_info["basic"]["data"])
                tmp.update(client_info["board"]["data"])
                server_obj = models.Server.objects.create(**tmp)
                # 增加server表结束

                # 增加硬盘表数据开始
                for i in client_info["disk"]["data"].values():
                    i["server_obj"] = server_obj
                    models.Disk.objects.create(**i)
                # 增加硬盘表数据结束

                # 增加内存表数据开始
                for i in client_info["memory"]["data"].values():
                    i["server_obj"] = server_obj
                    models.Memory.objects.create(**i)
                # 增加内存表数据结束

                # 增加网卡表数据开始
                for k, v in client_info["nic"]["data"].items():
                    v["server_obj"] = server_obj
                    v["name"] = k
                    models.NIC.objects.create(**v)
                # 增加网卡表数据结束
                return HttpResponse("...")
            else:
                """
                如果有hostname对象则进行更新操作
                """
                print("已经有主机")

                # 更新主机表开始
                tmp = {}
                tmp.update(client_info["basic"]["data"])
                tmp.update(client_info["board"]["data"])

                tmp.pop("hostname")
                record_list = []
                for k, v in tmp.items():
                    old_val = getattr(server_obj, k)
                    new_val = v
                    if old_val != new_val:
                        record = "[%s]的[%s]由[%s]变更为[%s]" % (server_obj.hostname, k, old_val, new_val)
                        record_list.append(record)
                        setattr(server_obj, k, new_val)
                server_obj.save()
                if record_list:
                    models.ServerRecord.objects.create(server_obj=server_obj, content=";".join(record_list))
                # 更新主机表结束

                # 更新硬盘开始
                # 拿到新的硬盘信息
                new_disk_info_dict = client_info["disk"]["data"]
                """
                {
                '0': {'slot': '0', 'pd_type': 'SAS', 'capacity': '279.396',
                      'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'},
                '1': {'slot': '1', 'pd_type': 'SAS', 'capacity': '279.396',
                      'model': 'SEAGATE ST300MM0006     LS08S0K2B5AH'},
                '2': {'slot': '2', 'pd_type': 'SATA', 'capacity': '476.939',
                      'model': 'S1SZNSAFA01085L     Samsung SSD 850 PRO 512GB               EXM01B6Q'},
                '3': {'slot': '3', 'pd_type': 'SATA', 'capacity': '476.939',
                      'model': 'S1AXNSAF912433K     Samsung SSD 840 PRO Series              DXM06B0Q'},
                '4': {'slot': '4', 'pd_type': 'SATA', 'capacity': '476.939',
                      'model': 'S1AXNSAF303909M     Samsung SSD 840 PRO Series              DXM05B0Q'},
                '5': {'slot': '5', 'pd_type': 'SATA', 'capacity': '476.939',
                      'model': 'S1AXNSAFB00549A     Samsung SSD 840 PRO Series              DXM06B0Q'}
                """
                # 拿到旧的硬盘信息
                old_disk_info_dict = server_obj.disk.all()  # 等同于models.Disk.objects.filter(server_obj=server_obj)
                """
                <QuerySet [<Disk: 0>, <Disk: 1>, <Disk: 2>, <Disk: 3>, <Disk: 4>, <Disk: 5>]>
                """
                # 取到硬盘的槽位,通过集合筛选
                new_disk_slot_info = set(new_disk_info_dict.keys())
                old_disk_slot_info = {i.slot for i in old_disk_info_dict}
                # 拿到需要增加的硬盘信息
                add_slot_info = new_disk_slot_info - old_disk_slot_info
                # 拿到需要删除的硬盘信息
                del_slot_info = old_disk_slot_info - new_disk_slot_info
                # 拿到需要更新的硬盘信息
                update_slot_info = old_disk_slot_info & new_disk_slot_info

                # 执行增加操作
                disk_record_list = []
                for slot in add_slot_info:
                    val = new_disk_info_dict[slot]
                    val["server_obj"] = server_obj
                    disk_record_list.append("%s增加了硬盘%s" % (server_obj.hostname, val))
                    models.Disk.objects.create(**val)
                models.ServerRecord.objects.create(server_obj=server_obj, content=";".join(disk_record_list))

                # 执行删除操作
                models.Disk.objects.filter(server_obj=server_obj, slot__in=del_slot_info).delete()

                # 执行更新操作
                disk_update_record_list = []
                for slot in update_slot_info:
                    val = new_disk_info_dict[slot]
                    obj = models.Disk.objects.filter(server_obj=server_obj, slot=slot).first()
                    for k, new_val in val.items():
                        old_val = getattr(obj, k)
                        print("老的值：", old_val)
                        if new_val != old_val:
                            setattr(obj, k, new_val)
                            obj.save()
                            disk_update_record_list.append("%s的%s由%s变更为%s" % (hostname, k, old_val, new_val))
                if disk_update_record_list:
                    models.ServerRecord.objects.create(server_obj=server_obj, content=";".join(disk_update_record_list))
                # 更新硬盘结束

    return HttpResponse("Server Success!")
