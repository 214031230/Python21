#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENGINE_HANDLERS = {
    'agent': 'src.engine.agent.AgentHandler',
    'ssh': 'src.engine.ssh.SSHHandler',
    'salt': 'src.engine.salt.SaltHandler',
}
ENGINE = 'ssh'

# ########### SSH模式 ###########
# 私钥地址
SSH_PRIVATE_KEY = '/xxx/xx/xx'
SSH_PORT = 22
SSH_USER = 'cmdb'

# ############################## 插件 ################################
PLUGIN_DICT = {
    'disk': 'src.plugins.disk.Disk',
    'memory': 'src.plugins.memory.Memory',
    'network': 'src.plugins.network.Network',
}

DEBUG = False

ASSET_API = "http://192.168.17.58:8000/api/asset/"
