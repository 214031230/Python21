#!/usr/bin/env python3
import sys
import os

# 配置模块的加载路径
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

# 把用户可以更改的配置文件路径加载到环境变量中,在lib/config/__init__.py中使用
os.environ["auto_client_settings"] = "conf.settings"

from src import script

if __name__ == '__main__':
    """
    执行主函数
    """
    script.start()
