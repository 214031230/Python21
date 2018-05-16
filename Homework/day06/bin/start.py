#!/usr/bin/env python3
from os import path, getcwd
from sys import path as sys_path
from core import main
sys_path.insert(0, path.dirname(getcwd()))  # 配置syspath加载目录顺序

if __name__ == "__main__":
    main.main()
