#!/usr/bin/env python3
import os
# 项目路径
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 监控插件配置
PLUGINS_ITEMS = {
    "board": "src.plugins.board.Board",
    "disk": "src.plugins.disk.Disk",
    "nic": "src.plugins.nic.Nic",
    "memory": "src.plugins.memory.Memory",
}

# API 接口
API = "http://127.0.0.1:8000/api/server.html"

# 采集器模式支持 AGENT、SALT、SSH
MODE = "SALT"

# 当MODE = "SSH" 需要配置下面的内容
USER = "root"
PASSWORD = "123456"
PORT = 22
