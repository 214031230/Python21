#!/usr/bin/env python3
import os
from lib.config import settings


class Board:
    """
    主板监控
    """
    @classmethod
    def initial(cls):
        """
        在执行process之前自定义一些操作
        :return:
        """
        return cls()

    def process(self, exec_cmd, debug):
        if debug:
            output = open(os.path.join(settings.BASEDIR, 'files/board.out'), mode="r", encoding="utf-8").read()
        else:
            output = exec_cmd("sudo dmidecode -t1")
        return output

    def parse(self, content):
        result = {}
        key_map = {
            'Manufacturer': 'manufacturer',
            'Product Name': 'model',
            'Serial Number': 'sn',
        }

        for item in content.split('\n'):
            row_data = item.strip().split(':')
            if len(row_data) == 2:
                if row_data[0] in key_map:
                    result[key_map[row_data[0]]] = row_data[1].strip() if row_data[1] else row_data[1]

        return result
