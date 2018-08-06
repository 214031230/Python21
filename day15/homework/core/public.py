#!/usr/bin/env python3
import logging
from conf import setting


class Public:
    @staticmethod
    def log():
        """
        定义日志输出合格
        :return: 返回一个可以直接使用的logger对象
        """
        logger = logging.getLogger()
        fh = logging.FileHandler(setting.logdir, encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s  %(name)s   %(levelname)s  %(message)s File:<%(filename)s line %(lineno)d>')
        logger.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

