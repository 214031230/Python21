# -*- coding: utf-8 -*-
from os import path
from sys import path as sys_path
import json
import time
import io
import logging
from concurrent.futures import ThreadPoolExecutor
sys_path.insert(0, path.dirname(path.dirname(path.abspath(__file__))))
import requests
from elasticsearch import Elasticsearch
import certifi

# 2分钟前时间从59结束
# end_time = time.strftime("%Y-%m-%d %H:%M:59", time.localtime(time.time() - 120))
# # 2分钟前时间从00开始
# start_time = time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time() - 120))
end_time = "2018-07-05 00:00:00"
# 2分钟前时间从00开始
start_time = "2018-07-06 11:00:00"
# 数据文件
data_file = r"./data.txt"
log_file_path = r"./run.log"
ES = Elasticsearch(['https://vpc-rfinex-nxaxxpo3dm6fog2i7ltdsabkne.ap-northeast-2.es.amazonaws.com'], use_ssl=True, ca_certs=certifi.where())


def my_logger(log_file):
    """
    定义日志输出合格
    :return: 返回一个可以直接使用的logger对象
    """
    logger = logging.getLogger()
    fh = logging.FileHandler(log_file, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s  %(name)s   %(levelname)s  %(message)s File:<%(filename)s line %(lineno)d>')
    logger.setLevel(logging.DEBUG)  # 定义文件日志级别
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def get_metrics_from_es(index, doc_type, query_para, s_time, e_time, time_field):
    """
    从elasticsearch获取信息
    :param index:
    :param doc_type:
    :param query_para:
    :param s_time:
    :param e_time:
    :param time_field:
    :return:
    """
    query_body = {
        "from": "0",
        "size": "0",
        "query": {
            "bool": {
                "must": [
                    {
                        "range": {
                            "{0}".format(time_field): {
                                "gte": s_time,
                                "lte": e_time,
                                "format": "yyyy-MM-dd HH:mm:ss"
                            }
                        }
                    },
                    {
                        "query_string": {
                            "query": query_para
                        }
                    }
                ]
            }
        }
    }
    response = ES.search(
        index="{0}".format(index),
        doc_type="{0}".format(doc_type),
        body=query_body
    )

    res = response['hits']['total']
    print("命中数量：%s" % res)
    return int(res)


def report_data(show_key, value, endpoint_host):
    """
    上传信elasticsearch结果到127.0.0.1:198
    :param show_key:
    :param value:
    :param endpoint_host:
    :return:
    """
    ts = int(time.time())
    payload = [
          {
              "endpoint": endpoint_host,
              "metric": show_key,
              "timestamp": ts,
              "step": 60,
              "value": value,
              "counterType": "GAUGE",
              "tags": "idc=lg,loc=beijing",
          }
      ] 

    print("payload:" % payload)
    # r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))


def get_argv():
    """
    把文本转换成参数一次只取一行
    :return:
    """
    with io.open(data_file, encoding="utf-8") as f:
        for i in f:
            i = i.strip()
            if i:
                ret = i.split("|")
                yield ret


def run(endpoint_host, show_key, index, doc_type, query_para, time_field, s_time, e_time):
    """
    多线程执行代码
    :param endpoint_host:
    :param show_key:
    :param index:
    :param doc_type:
    :param query_para:
    :param time_field:
    :param s_time:
    :param e_time:
    :return:
    """
    metrics_1m = get_metrics_from_es(index, doc_type, query_para, s_time, e_time, time_field)
    report_data(show_key, metrics_1m, endpoint_host)


if __name__ == '__main__':
    log = my_logger(log_file_path)
    t = ThreadPoolExecutor(50)
    try:
        g = get_argv()
        while True:
            try:
                a1, a2, a3, a4, a5, a6 = next(g)
                t.submit(run(a1, a2, a3, a4, a5, a6, start_time, end_time))
                # t.submit(run(*next(g), start_time, end_time))
            except StopIteration:
                break
            except Exception as e:
                log.debug(e)
    except Exception as e:
        log.debug(e)


