#!/usr/bin/env python3
from os import path
from sys import path as sys_path
sys_path.insert(0, path.dirname(path.dirname(path.abspath(__file__))))  # 配置sys.path(模块)加载顺序
from core import main

if __name__ == "__main__":
    main.main()
