"""
随机生成五位数验证码
"""

import random

def get_vcode():
    tmp = []
    for i in range(5):
        l = chr(random.randint(97, 122))  # 生成随机的小写字母
        u = chr(random.randint(65, 90))  # 生成随机的大写字母
        n = str(random.randint(0, 9))  # 生成一个随机的数字
        # 从上面三个随机选一个
        r = random.choice([l, u, n])
        tmp.append(r)
    return "".join(tmp)


if __name__ == '__main__':
    ret = get_vcode()
    print(ret)
