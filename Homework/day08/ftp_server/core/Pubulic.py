#!/usr/bin/env python3
import hashlib


class Public:
    @staticmethod
    def get_md5(file_path):
        """
        获取文件的md5值
        :param file_path: 文件路径
        :return:
        """
        with open(file_path) as f:
            md5obj = hashlib.md5()
            for line in f:
                md5obj.update(line)
            return md5obj.hexdigest()