#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# import salt.client
# local = salt.client.LocalClient()
# result = local.cmd('pengfei', 'cmd.run', ['df -h'])
# #print(result[hostname])
# print(local.get_cache_returns(result))
信用卡欠 = -44967
卡内余额 = +12000
媳妇公积金 = +9000
车贷 = -3750
本月工资 = +13000

下个月工资 = + 13000
下个月车贷 = - 3750
下个月公积金 = +4500
print("本月负债：", 信用卡欠 + 卡内余额 + 媳妇公积金 + 车贷 + 本月工资)
print("下个月负债：", 信用卡欠 + 卡内余额 + 媳妇公积金 + 车贷 + 本月工资 + 下个月工资 + 下个月车贷 + 下个月公积金)
