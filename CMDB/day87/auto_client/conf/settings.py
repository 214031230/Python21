#!/usr/bin/env python3
# 监控插件配置
PLUGINS_ITEMS = {
    "board": "src.plugins.board.Board",
    "disk": "src.plugins.disk.Disk",
    "nic": "src.plugins.nic.Nic",
    "memory": "src.plugins.memory.Memory",
}

API = "http://127.0.0.1:8000/api/server.html"
