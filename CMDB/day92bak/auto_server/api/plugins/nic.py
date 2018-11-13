#!/usr/bin/env python3
from repository import models


class Nic:
    def __init__(self, server_obj, info):
        self.server_obj = server_obj
        self.client_info = info

    def process(self):
        """
        更新网卡开始
        :return: 
        """
        # 拿到新的网卡信息
        new_nic_info_dict = self.client_info["data"]
        """        
        {
            'eth0': {
                'up': True,
                'hwaddr': '00:1c:42:a5:57:7a',
                'ipaddrs': '10.211.55.4',
                'netmask': '255.255.255.0'}
        },
        """

        # 拿到旧的网卡信息
        old_nic_info_dict = self.server_obj.nic.all()  # 等同于models.nic.objects.filter(server_obj=server_obj)
        """
        <QuerySet [<nic: 0>, <nic: 1>, <nic: 2>, <nic: 3>, <nic: 4>, <nic: 5>]>
        """
        # 取到网卡的槽位,通过集合筛选
        new_nic_slot_info = set(new_nic_info_dict.keys())
        old_nic_slot_info = {i.name for i in old_nic_info_dict}
        # 拿到需要增加的网卡信息
        add_slot_info = new_nic_slot_info - old_nic_slot_info
        # 拿到需要删除的网卡信息
        del_slot_info = old_nic_slot_info - new_nic_slot_info
        # 拿到需要更新的网卡信息
        update_slot_info = old_nic_slot_info & new_nic_slot_info

        # 执行增加操作
        nic_record_list = []
        for slot in add_slot_info:
            val = new_nic_info_dict[slot]
            val["server_obj"] = self.server_obj
            val["name"] = slot
            nic_record_list.append("%s增加了网卡%s" % (self.server_obj.hostname, val))
            models.NIC.objects.create(**val)
        models.ServerRecord.objects.create(server_obj=self.server_obj, content=";".join(nic_record_list))

        # 执行删除操作
        models.NIC.objects.filter(server_obj=self.server_obj, name__in=del_slot_info).delete()

        # 执行更新操作
        nic_update_record_list = []
        for slot in update_slot_info:
            val = new_nic_info_dict[slot]
            obj = models.NIC.objects.filter(server_obj=self.server_obj, name=slot).first()
            for k, new_val in val.items():
                old_val = getattr(obj, k)
                if new_val != old_val:
                    setattr(obj, k, new_val)
                    obj.save()
                    nic_update_record_list.append("%s的%s由%s变更为%s" % (self.server_obj.hostname, k, old_val, new_val))
        if nic_update_record_list:
            models.ServerRecord.objects.create(server_obj=self.server_obj, content=";".join(nic_update_record_list))