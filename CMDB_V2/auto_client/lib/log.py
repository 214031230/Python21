#!/usr/bin/env python3
import logging
from config import settings


def my_logger():
    """
    定义日志输出合格
    :return: 返回一个可以直接使用的logger对象
    """
    logger = logging.getLogger()  # 实例化一个logger对象
    fh = logging.FileHandler(settings.LOG_FILE_PATH, encoding='utf-8')  # 创建一个文件handler，用于写入日志文件
    formatter = logging.Formatter(
        '%(asctime)s  %(name)s   %(levelname)s  %(message)s File:<%(filename)s line %(lineno)d>')  # 定义文件日志格式
    logger.setLevel(logging.INFO)  # 定义文件日志级别
    fh.setFormatter(formatter)  # 设置文件日志格式
    logger.addHandler(fh)  # logger对象fh对象
    return logger


log = my_logger()
