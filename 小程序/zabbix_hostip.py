#!/usr/bin/python 
# coding:utf-8

import json
import urllib2
from urllib2 import URLError
import sys, argparse


class zabbix_api:
    def __init__(self):
        self.url = 'http://zbx01.6.cn:18080/zabbix/api_jsonrpc.php'
        self.header = {"Content-Type": "application/json"}

    def user_login(self):
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": "yunwei",  # 修改用户名
                "password": "password"  # 修改密码
            },
            "id": 0
        })

        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            print "\033[041m 用户认证失败，请检查 !\033[0m", e.code
        else:
            response = json.loads(result.read())
            result.close()
            self.authID = response['result']
            return self.authID

    def host_get(self, hostName=''):
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": "extend",
                "filter": {"host": hostName}
            },
            "auth": self.user_login(),
            "id": 1
        })
        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])

        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            # print response
            result.close()
            print
            "主机数量: \033[31m%s\033[0m" % (len(response['result']))
            for host in response['result']:
                status = {"0": "OK", "1": "Disabled"}
                available = {"0": "Unknown", "1": "available", "2": "Unavailable"}
                # print host
                if len(hostName) == 0:
                    print
                    "HostID : %s\t HostName : %s\t Status :\033[32m%s\033[0m " % (
                        host['hostid'], host['name'], status[host['status']])
                else:
                    print
                    "HostID : %s\t HostName : %s\t Status :\033[32m%s\033[0m " % (
                        host['hostid'], host['name'], status[host['status']])
                    return host['hostid']

    def host_ip(self):
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "hostinterface.get",
            "params": {
                "output": ["hostid", "ip"],
                #                              "hostids": ['hostid']
            },
            "auth": self.user_login(),
            "id": 1
        })
        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])

        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            # print response
            hostid_list = {}
            for host in response['result']:
                print "HostID: %s\t IP: %s\t" % (host['hostid'], host['ip'])
                hostid_list[host['hostid']] = host['ip']
            result.close()
            print
            "主机数量: \033[31m%s\033[0m" % (len(response['result']))
            return hostid_list


    def host_delete(self, hostid):
        """
        删除hostid
        :param hostid:  "2343,3344,333"
        :return:
        """
        hostid_list = []
        for i in hostid.split(','):
            var = {}
            var['hostid'] = self.host_get(i)
            hostid_list.append(var)
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "host.delete",
            "params": hostid_list,  # [{"hostid": v1},{"hostid": v2},{"hostid": v3}]
            "auth": self.user_login(),
            "id": 1
        })

        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])

        try:
            result = urllib2.urlopen(request)
        except Exception, e:
            print e
        else:

            result.close()
            print "主机 \033[041m %s\033[0m  已经删除 !" % hostid


def filter_hostid(val):
    """
    过滤重复项并删除重复的，只保留一个
    :param val:
    :return: 字符串格式类型，需要删除的所有ID "id1,id2,id3"
    """
    l1 = []
    l2 = []
    for k, v in val.items():
        if v in l1:
            l2.append(k)
        l1.append(v)
    return ",".join(l2)


if __name__ == "__main__":
    zabbix = zabbix_api()
    zabbix.host_get()
    # {"1": "123", "2": "123", "3": "456", "4": "456", "5": "123"}
    ret = zabbix.host_ip()
    zabbix.host_delete(filter_hostid(ret))
