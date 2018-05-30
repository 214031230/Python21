#!/usr/bin/env python3
import hashlib
from conf import settings

class Public:
    @staticmethod
    def get_md5(file_path):
        """
        获取文件的md5值
        :param file_path: 文件路径
        :return:
        """
        with open(file_path, "rb") as f:
            md5obj = hashlib.md5()
            for line in f:
                md5obj.update(line)
            return md5obj.hexdigest()

    @staticmethod
    def helper():
        with open(settings.help_file, encoding="utf-8") as f:
            for i in f:
                i = i.rstrip()
                print(i)