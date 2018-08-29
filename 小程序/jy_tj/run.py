#!/usr/bin/env python3
import os
import pymysql
from concurrent.futures import ThreadPoolExecutor


def run(s_name, host_ip):
    """
    导出SQL操作
    :param host_ip: 服务器IP
    :param s_name: 学校名称
    :return:
    """
    conn = pymysql.connect(host='{}'.format(host_ip),
                           user='edu_platform',
                           password='edu_platform',
                           database='edu_platform',
                           charset='utf8'
                           )
    cursor = conn.cursor()
    sql = "SELECT business_key FROM bd_school WHERE name={}".format(s_name)
    res = cursor.execute(sql)
    cursor.close()
    conn.close()
    print("--->", res)
    # com = """
    # mysql -uedu_platform -pedu_platform  -h%s  --database edu_platform -e"
    # SELECT b.id as id,b.business_key as business_key,b.user_code as '用户名',b.name,b.pass_word,b.sex,b.device_number as '设备号',
    # s.name as '学校',s.business_key as '学校id',g.name as '年级',g.business_key as '年级id',c.name as '班级',c.business_key as '班级id'
    # from
    # base_user b ,bd_student t,bd_school s,bd_grade g,bd_edu_class c
    # where b.id = t.id
    # and t.school_business_key = s.business_key
    # and t.grade_business_key = g.business_key
    # and t.class_business_key = c.business_key
    # and s.business_key = '%s'" >%s_%s.xls
    # """ % (host_ip, res, host_ip, s_name)
    # os.system(com)


if __name__ == '__main__':
    t = ThreadPoolExecutor(20)
    with open("host_list", "r", encoding="utf-8") as f:
        for i in f:
            school_name, ip = i.strip().split()
            t.submit(run, school_name, ip)
        t.shutdown()