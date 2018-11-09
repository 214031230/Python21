#!/usr/bin/env python3
from repository import models


class Memory:
    def __init__(self, server_obj, info):
        self.server_obj = server_obj
        self.client_info = info

    def process(self):
        """
        更新内存开始
        :return: 
        """
        # 拿到新的内存信息
        new_memory_info_dict = self.client_info["data"]
        """
           { 'DIMM #0': {'capacity': 1024, 'slot': 'DIMM #0', 'model': 'DRAM', 'speed': '667 MHz',
                        'manufacturer': 'Not Specified', 'sn': 'Not Specified'},
            'DIMM #1': {'capacity': 0, 'slot': 'DIMM #1', 'model': 'DRAM', 'speed': '667 MHz',
                        'manufacturer': 'Not Specified',
                        'sn': 'Not Specified'},
            'DIMM #2': {'capacity': 0, 'slot': 'DIMM #2', 'model': 'DRAM', 'speed': '667 MHz',
                        'manufacturer': 'Not Specified',
                        'sn': 'Not Specified'},
            'DIMM #3': {'capacity': 0, 'slot': 'DIMM #3', 'model': 'DRAM', 'speed': '667 MHz',
                        'manufacturer': 'Not Specified',
                        'sn': 'Not Specified'},
            'DIMM #4': {'capacity': 0, 'slot': 'DIMM #4', 'model': 'DRAM', 'speed': '667 MHz',
                        'manufacturer': 'Not Specified',
                        'sn': 'Not Specified'},
            'DIMM #5': {'capacity': 0, 'slot': 'DIMM #5', 'model': 'DRAM', 'speed': '667 MHz',
                        'manufacturer': 'Not Specified',
                        'sn': 'Not Specified'},
            'DIMM #6': {'capacity': 0, 'slot': 'DIMM #6', 'model': 'DRAM', 'speed': '667 MHz',
                        'manufacturer': 'Not Specified',
                        'sn': 'Not Specified'},
            'DIMM #7': {'capacity': 0, 'slot': 'DIMM #7', 'model': 'DRAM', 'speed': '667 MHz',
                        'manufacturer': 'Not Specified',
                        'sn': 'Not Specified'}
        """
        # 拿到旧的内存信息
        old_memory_info_dict = self.server_obj.memory.all()  # 等同于models.memory.objects.filter(server_obj=server_obj)
        """
        <QuerySet [<memory: 0>, <memory: 1>, <memory: 2>, <memory: 3>, <memory: 4>, <memory: 5>]>
        """
        # 取到内存的槽位,通过集合筛选
        new_memory_slot_info = set(new_memory_info_dict.keys())
        old_memory_slot_info = {i.slot for i in old_memory_info_dict}
        # 拿到需要增加的内存信息
        add_slot_info = new_memory_slot_info - old_memory_slot_info
        # 拿到需要删除的内存信息
        del_slot_info = old_memory_slot_info - new_memory_slot_info
        # 拿到需要更新的内存信息
        update_slot_info = old_memory_slot_info & new_memory_slot_info

        # 执行增加操作
        memory_record_list = []
        for slot in add_slot_info:
            val = new_memory_info_dict[slot]
            val["server_obj"] = self.server_obj
            memory_record_list.append("%s增加了内存%s" % (self.server_obj.hostname, val))
            models.Memory.objects.create(**val)
        models.ServerRecord.objects.create(server_obj=self.server_obj, content=";".join(memory_record_list))

        # 执行删除操作
        models.Memory.objects.filter(server_obj=self.server_obj, slot__in=del_slot_info).delete()

        # 执行更新操作
        memory_update_record_list = []
        for slot in update_slot_info:
            val = new_memory_info_dict[slot]
            obj = models.Memory.objects.filter(server_obj=self.server_obj, slot=slot).first()
            for k, new_val in val.items():
                old_val = getattr(obj, k)
                if new_val != old_val:
                    setattr(obj, k, new_val)
                    obj.save()
                    memory_update_record_list.append("%s的%s由%s变更为%s" % (self.server_obj.hostname, k, old_val, new_val))
        if memory_update_record_list:
            models.ServerRecord.objects.create(server_obj=self.server_obj, content=";".join(memory_update_record_list))