#!/usr/bin/env python3
import os
from concurrent.futures import ThreadPoolExecutor
school_list = "./school_list"
error_file = "./ip_error_list"
sql_file = "./sql"
def sql(school_name, school_ip):
    with open(sql_file, encoding="utf-8") as f:
        ret = f.read()
        sql_cmd = ret.replace("北京研发", school_name)
    cmd = """
    mysql -uedu_platform -pedu_platform  -h%s  --database edu_apps -e"%s" >%s_%s.xls
    """ % (school_ip,sql_cmd, school_name, school_ip)

    check_network = """ ssh root@%s -p8997  -o ConnectTimeout=2  "w" """ % school_ip
    ret = os.popen(check_network).read()
    if ret:
        os.system(cmd)
    else:
        with open(error_file,mode="a",encoding="utf-8") as f:
            f.write("ERROR:%s 网络不可达\n" % school_ip)
        print("\033[0;31;0mERROR:%s 网络不可达\033[0m" % school_ip)


if __name__ == '__main__':
    t = ThreadPoolExecutor(50)
    with open(school_list, encoding="utf-8") as f:
        for i in f:
            if i.strip():
                school_name, school_ip = i.split()
                t.submit(sql,school_name,school_ip)
    t.shutdown()
    print("\033[0;36;0mINFO:统计完毕\033[0m")