#!/usr/bin/env python3
from api import models


def basic(request, hostname):
    """
     数据库录入基本信息
    :param request:
    :param hostname:
    :return:
    """
    server_dict = {}
    server_dict.update(request.data["basic"]["data"])
    server_dict.update(request.data["cpu"]["data"])
    server_dict.update(request.data["main_board"]["data"])

    models.Server.objects.filter(hostname=hostname).update(**server_dict)


def disk(request, server):
    """
     数据库录入硬盘信息
    :param request:
    :param server:
    :return:
    """
    # 2.1 取到数据库中的硬盘信息
    disk_queryset = models.Disk.objects.filter(server=server)

    # 2.2 取到采集传递过来的硬盘信息
    disk_info = request.data["disk"]["data"]

    # 2.3 根据槽位转成集合，判断哪些槽位进行了更新，删除，增加
    disk_queryset_set = {i.slot for i in disk_queryset}
    disk_info_set = set(disk_info)

    # 2.3.1 需要增加的
    add_slot_list = disk_info_set - disk_queryset_set
    # 2.3.2 需要删除的
    del_slot_list = disk_queryset_set - disk_info_set
    # 2.3.3 需要更新的
    update_slot_list = disk_queryset_set & disk_info_set

    # 2.4 增加硬盘
    for slot in add_slot_list:
        row_dict = disk_info[slot]
        record_list = []
        for name, new_value in row_dict.items():
            verbose_name = models.Disk._meta.get_field(name)
            tpl = "%s: %s" % (verbose_name, new_value)
            record_list.append(tpl)
        if record_list:
            msg = "【新增硬盘】 槽位%s新增硬盘，硬盘信息：%s" % (slot, ";".join(record_list))
            models.AssetRecord.objects.create(server=server, content=msg)
        row_dict["server"] = server
        # models.Disk.objects.create(**row_dict)
    # 2.5 删除硬盘
    models.Disk.objects.filter(server=server, slot__in=del_slot_list).delete()
    if del_slot_list:
        msg = "【硬盘删除】 移除槽位%s的硬盘" % (";".join(del_slot_list),)
        models.AssetRecord.objects.create(server=server, content=msg)
    # 2.6 更新硬盘
    for slot in update_slot_list:
        # models.Disk.objects.filter(server=server, slot=slot).update(**disk_info[slot])
        # 取到硬盘对象
        obj = models.Disk.objects.filter(server=server, slot=slot).first()
        # 取到采集传递过来的硬盘槽位信息
        row_dict = disk_info[slot]
        record_list = []
        for name, new_value in row_dict.items():
            old_value = str(getattr(obj, name))
            if old_value != new_value:
                setattr(obj, name, new_value)
                verbose_name = models.Disk._meta.get_field(name).verbose_name
                msg = "【硬盘变更】槽位%s: %s由%s更新为%s" % (slot, verbose_name, old_value, new_value)
                record_list.append(msg)
        obj.save()
        if record_list:
            models.AssetRecord.objects.create(server=server, content=";".join(record_list))


def nic(request, server):
    """
     数据库录入网卡信息
    :param request:
    :param server:
    :return:
    """
    # 3.1 取到数据库中的网卡信息
    nic_queryset = models.NIC.objects.filter(server=server)

    # 3.2 取到采集传递过来的网卡信息
    nic_info = request.data["network"]["data"]

    # 3.3 根据槽位转成集合，判断哪些槽位进行了更新，删除，增加
    nic_queryset_set = {i.name for i in nic_queryset}
    nic_info_set = set(nic_info)

    # 3.3.1 需要增加的
    add_name_list = nic_info_set - nic_queryset_set
    # 3.3.2 需要删除的
    del_name_list = nic_queryset_set - nic_info_set
    # 3.3.3 需要更新的
    update_name_list = nic_queryset_set & nic_info_set

    # 3.4 增加网卡
    for name in add_name_list:
        row_dict = nic_info[name]
        row_dict["server"] = server
        row_dict["name"] = name
        models.NIC.objects.create(**row_dict)
    # 3.5 删除网卡
    models.NIC.objects.filter(server=server, name__in=del_name_list).delete()
    # 3.6 更新网卡
    for name in update_name_list:
        models.NIC.objects.filter(server=server, name=name).update(**nic_info[name])


def memory(request, server):
    """
     数据库录入内存信息
    :param request:
    :param server:
    :return:
    """
    # 4.1 取到数据库中的内存信息
    memory_queryset = models.Memory.objects.filter(server=server)

    # 4.2 取到采集传递过来的内存信息
    memory_info = request.data["memory"]["data"]

    # 4.3 根据槽位转成集合，判断哪些槽位进行了更新，删除，增加
    memory_queryset_set = {i.slot for i in memory_queryset}
    memory_info_set = set(memory_info)

    # 4.4.1 需要增加的
    add_slot_list = memory_info_set - memory_queryset_set
    # 4.4.2 需要删除的
    del_slot_list = memory_queryset_set - memory_info_set
    # 4.4.3 需要更新的
    update_slot_list = memory_queryset_set & memory_info_set

    # 4.4 增加内存
    for slot in add_slot_list:
        row_dict = memory_info[slot]
        row_dict["server"] = server
        models.Memory.objects.create(**row_dict)
    # 4.5 删除内存
    models.Memory.objects.filter(server=server, slot__in=del_slot_list).delete()
    # 4.6 更新内存
    for slot in update_slot_list:
        models.Memory.objects.filter(server=server, slot=slot).update(**memory_info[slot])
