#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import salt.client
local = salt.client.LocalClient()
result = local.cmd('pengfei', 'cmd.run', ['df -h'])
#print(result[hostname])
print(local.get_cache_returns(result))
