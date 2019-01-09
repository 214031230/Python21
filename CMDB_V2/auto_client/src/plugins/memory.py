#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import traceback
from .base import BasePlugin
from lib import convert
from lib.response import BaseResponse
from lib.log import log


class Memory(BasePlugin):
    def win(self, handler, hostname):
        """
        获取windows内存信息
        :param handler: 采集器引擎
        :param hostname: 需要采集的主机
        :return: result
        """
        result = handler.cmd('wmic memorychip', hostname)
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
        result = BaseResponse()
        try:
            if self.debug:
                output = open(os.path.join(self.base_dir, 'files/memory.out'), 'r').read()
            else:
                shell_command = "dmidecode  -q -t 17 2>/dev/null"
                output = handler.cmd(shell_command, hostname)
            result.data = self.parse(output)
        except Exception as e:
            msg = traceback.format_exc()
            result.status = False
            result.error = msg
            log.error(msg)

        return result.dict

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        ram_dict = {}
        key_map = {
            'Size': 'capacity',
            'Locator': 'slot',
            'Type': 'model',
            'Speed': 'speed',
            'Manufacturer': 'manufacturer',
            'Serial Number': 'sn',

        }
        if type(content) != str:
            content = content.decode("utf-8")
        devices = content.split('Memory Device')
        for item in devices:
            item = item.strip()
            if not item:
                continue
            if item.startswith('#'):
                continue
            segment = {}
            lines = item.split('\n\t')
            for line in lines:
                if len(line.split(':')) > 1:
                    key, value = line.split(':')
                else:
                    key = line.split(':')[0]
                    value = ""
                if key in key_map:
                    if key == 'Size':
                        segment[key_map['Size']] = convert.convert_mb_to_gb(value, 0)
                    else:
                        segment[key_map[key.strip()]] = value.strip()
            ram_dict[segment['slot']] = segment

        return ram_dict
