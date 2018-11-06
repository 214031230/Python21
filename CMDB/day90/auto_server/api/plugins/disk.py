#!/usr/bin/env python3
from repository import models


class Disk:
    def __init__(self, server_obj, info):
        self.server_obj = server_obj
        self.client_info = info

    def process(self):
        """
        更新硬盘信息开始
        :return:
        """
        # 拿到新的硬盘信息
        new_disk_info_dict = self.client_info["data"]
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
        old_disk_info_dict = self.server_obj.disk.all()  # 等同于models.Disk.objects.filter(server_obj=server_obj)
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
            val["server_obj"] = self.server_obj
            disk_record_list.append("%s增加了硬盘%s" % (self.server_obj.hostname, val))
            models.Disk.objects.create(**val)
        models.ServerRecord.objects.create(server_obj=self.server_obj, content=";".join(disk_record_list))

        # 执行删除操作
        models.Disk.objects.filter(server_obj=self.server_obj, slot__in=del_slot_info).delete()

        # 执行更新操作
        disk_update_record_list = []
        for slot in update_slot_info:
            val = new_disk_info_dict[slot]
            obj = models.Disk.objects.filter(server_obj=self.server_obj, slot=slot).first()
            for k, new_val in val.items():
                old_val = getattr(obj, k)
                if new_val != old_val:
                    setattr(obj, k, new_val)
                    obj.save()
                    disk_update_record_list.append("%s的%s由%s变更为%s" % (self.server_obj.hostname, k, old_val, new_val))
        if disk_update_record_list:
            models.ServerRecord.objects.create(server_obj=self.server_obj, content=";".join(disk_update_record_list))


