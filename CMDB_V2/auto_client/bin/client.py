#!/usr/bin/env python3
import os
import sys

# 添加auto_client为模块加载路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == '__main__':
    from src.script import run
    run()
