import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(sys.path)
from core import core2
# # 所有的模块就是一个py文件的名字
# # 所有的模块导入都需要精确到具体的模块
if __name__ == '__main__':
    core2.main()
