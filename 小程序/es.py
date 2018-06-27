# -*- coding: utf-8 -*-
import sys
import requests
import time
import json
from elasticsearch import Elasticsearch
import certifi

ES = Elasticsearch(['https://vpc-rfinex-nxaxxpo3dm6fog2i7ltdsabkne.ap-northeast-2.es.amazonaws.com'],use_ssl=True, ca_certs=certifi.where())
def get_metrics_from_es(index,doc_type, query_para, start_time, end_time, time_field):
    query_body = {
        "from": "0",
            "size": "0",
                "query": {
                    "bool": {
                        "must": [
                    {
                    "range": {
                        "{0}".format(time_field): {
                            "gte": start_time,
                            "lte": end_time,
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
    return int(res)
def report_data(show_key, value,endpoint_host):
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

    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))    
if __name__ == '__main__':
    if len(sys.argv) == 9:
        index = sys.argv[1]
        doc_type = sys.argv[2]  # 文档类型
        query_para = sys.argv[3] # 查询语句
        start_time = sys.argv[4] # 开始时间
        end_time = sys.argv[5] # 结束时间
        time_field = sys.argv[6] #
        show_key = sys.argv[7] # 显示key数量
        endpoint_host = sys.argv[8]
        #print index, doc_type, query_para, start_time, end_time, time
    else:
        print("input error!")
        sys.exit(1)
    metrics_1m = get_metrics_from_es(index,doc_type,query_para,start_time,end_time, time_field)
    report_data(show_key, metrics_1m,endpoint_host)

