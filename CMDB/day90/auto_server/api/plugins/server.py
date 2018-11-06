#!/usr/bin/env python3
from repository import models


class Server:
    def __init__(self, server_obj, basic_dict, board_dict):
        self.server_obj = server_obj
        self.basic_dict = basic_dict
        self.board_dict = board_dict

    def process(self):
        """
        更新主机表
        :return:
        """
        tmp = {}
        tmp.update(self.basic_dict["data"])
        tmp.update(self.board_dict["data"])
        tmp.pop("hostname")
        record_list = []
        for k, v in tmp.items():
            old_val = getattr(self.server_obj, k)
            new_val = v
            if old_val != new_val:
                record = "[%s]的[%s]由[%s]变更为[%s]" % (self.server_obj.hostname, k, old_val, new_val)
                record_list.append(record)
                setattr(self.server_obj, k, new_val)
        self.server_obj.save()
        if record_list:
            models.ServerRecord.objects.create(server_obj=self.server_obj, content=";".join(record_list))
