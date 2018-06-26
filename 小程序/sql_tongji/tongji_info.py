#!/usr/bin/env python3
import os
import re
from concurrent.futures import ThreadPoolExecutor
school_list = "./school_list"
error_file = "./ip_error_list"
sql_file = "./sql"
school_list_dir = "./tongji"


def sql(school_name, school_ip):
    """
    导出统计数据到xls
    :param school_name: 学校名称
    :param school_ip: 学校IP
    :return:
    """
    with open(sql_file, encoding="utf-8") as f:
        ret = f.read()
        sql_cmd = ret.replace("北京研发", school_name)
    cmd = """
    mysql -uedu_platform -pedu_platform  -h%s  --database edu_apps -e"%s" >%s/%s_%s.xls
    """ % (school_ip,sql_cmd,school_list_dir,school_name, school_ip)

    check_network = """ ssh root@%s -p8997  -o ConnectTimeout=2  "w" """ % school_ip
    ret = os.popen(check_network).read()
    if ret:
        os.system(cmd)
    else:
        with open(error_file,mode="a",encoding="utf-8") as f:
            f.write("ERROR:%s 网络不可达\n" % school_ip)
        print("\ERROR:%s 网络不可达" % school_ip)


def fx():
    """
    对统计数据进行合并处理
    :return: 合并后的数据
    """
    lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for name in os.listdir(school_list_dir):
        with open("%s/%s" % (school_list_dir, name), encoding="utf-8") as f:
            for i in f:
                if re.match(r"\d", i):
                    ret = i.split()
                    lst[0] += int(ret[0])
                    lst[1] += int(ret[1])
                    lst[2] += int(ret[2])
                    lst[5] += int(ret[5])
                    lst[6] += int(ret[6])
                    lst[7] += int(ret[7])
                    lst[10] += int(ret[10])
                    lst[11] += int(ret[11])
                    lst[12] += int(ret[12])
                    lst[15] += int(ret[15])
                    lst[16] += int(ret[16])
                    lst[17] += int(ret[17])
                    lst[20] += int(ret[20])
                    lst[21] += int(ret[21])
                    lst[22] += int(ret[22])
    return lst


if __name__ == '__main__':
    if os.path.exists(error_file):
        os.remove(error_file)
    t = ThreadPoolExecutor(50)
    with open(school_list, encoding="utf-8") as f:
        for i in f:
            if i.strip():
                school_name, school_ip = i.split()
                t.submit(sql,school_name,school_ip)
    t.shutdown()
    print("合并数据结果：", *fx())
    print("INFO:统计完毕")