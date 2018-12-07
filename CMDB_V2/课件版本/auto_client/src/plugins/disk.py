#!/usr/bin/python
# -*- coding:utf-8 -*-
import re
import os
from .base import BasePlugin


class Disk(BasePlugin):
    def win(self, handler, hostname):
        """
        获取windows硬盘信息
        :param handler: 采集器引擎
        :param hostname: 需要采集的主机
        :return: result
        """
        result = handler.cmd('dir', hostname)
        return result

    def linux(self, handler, hostname):
        """
        获取linux内存信息
        1. 如果是debug模式，则读取本地文件处理
        2. 如果是不是debug模式，则执行对象的命令
            1. 拿到采集结果交给parse进行格式化处理
        :param handler: 采集器引擎
        :param hostname: 需要采集的主机
        :return: self.parse(output)
        """
        if self.debug:
            output = open(os.path.join(self.base_dir, 'files/disk.out'), 'r').read()
        else:
            print("执行了disk")
            shell_command = "sudo MegaCli  -PDList -aALL"
            output = handler.cmd(shell_command, hostname)
        return self.parse(output)

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        response = {}
        result = []
        for row_line in content.split("\n\n\n\n"):
            result.append(row_line)
        for item in result:
            temp_dict = {}
            for row in item.split('\n'):
                if not row.strip():
                    continue
                if len(row.split(':')) != 2:
                    continue
                key, value = row.split(':')
                name = self.mega_patter_match(key)
                if name:
                    if key == 'Raw Size':
                        raw_size = re.search('(\d+\.\d+)', value.strip())
                        if raw_size:
                            temp_dict[name] = raw_size.group()
                        else:
                            raw_size = '0'
                    else:
                        temp_dict[name] = value.strip()
            if temp_dict:
                response[temp_dict['slot']] = temp_dict
        return response

    @staticmethod
    def mega_patter_match(needle):
        grep_pattern = {'Slot': 'slot', 'Raw Size': 'capacity', 'Inquiry': 'model', 'PD Type': 'pd_type'}
        for key, value in grep_pattern.items():
            if needle.startswith(key):
                return value
        return False
