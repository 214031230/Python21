#!/usr/bin/env python3
from os import path, getcwd
from sys import path as sys_path
sys_path.insert(0, path.dirname(getcwd()))  # 配置sys.path加载顺序
from core import main

if __name__ == "__main__":
    print("---")
    main.main()
