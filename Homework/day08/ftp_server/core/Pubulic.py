#!/usr/bin/env python3
import hashlib
import logging
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
    def log():
        """
        定义日志输出合格
        :return: 返回一个可以直接使用的logger对象
        """

        logger = logging.getLogger()
        fh = logging.FileHandler(settings.log_dir, encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s  %(name)s   %(levelname)s  %(message)s File:<%(filename)s line %(lineno)d>')
        logger.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
