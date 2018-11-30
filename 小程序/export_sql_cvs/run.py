#!/usr/bin/env python3
import pymysql
import csv
import os

host_list_path = "./hostlist"
sql_file_list = "./sql_file_list"
output_path = "./output"


class SqlCvs:
    def __init__(self, sql, ip):
        self.sql = sql
        self.ip = ip
        self.conn = None
        self.cursor = None
        self.user = "edu_platform"
        self.password = "edu_platform"
        self.db = "edu_platform"
        self.charset = "utf8"
        self.port = 8306

    def get_conn(self):
        """
        拿到连接
        :return:
        """
        self.conn = pymysql.connect(host=self.ip,
                                    user=self.user,
                                    password=self.password,
                                    database=self.db,
                                    charset=self.charset,
                                    port=self.port)

    def get_cursor(self):
        """
        获取游标
        :return:
        """
        self.get_conn()
        self.cursor = self.conn.cursor()

    def execute(self, bus_key=None):
        """
        获取游标，执行SQL
        :param bus_key: 学校ID
        :return: 返回执行结果
        """
        self.get_cursor()
        if "e14059b54350457c8726cc99970d14ec" not in self.sql and bus_key is None:
            self.cursor.execute(self.sql)
            res = self.cursor.fetchall()
        else:
            self.sql = self.sql.replace("e14059b54350457c8726cc99970d14ec", bus_key)
            self.cursor.execute(self.sql)
            res = self.cursor.fetchall()
        self.close()
        return res

    def close(self):
        """
        关闭游标
        关闭连接
        :return:
        """
        self.cursor.close()
        self.conn.close()


def handel_sql(sql, file_name):
    """
    执行sql拿到返回结果
    :param sql: 从sql文件中读取的sql语句
    :param file_name: 文件名称
    :return:
    """
    # 读取所有的主机列表取到主机IP和学校名称
    with open(host_list_path, encoding="utf-8") as f1:
        for i in f1.readlines():
            if i.strip():
                school_name, ip = i.split()
                # 获取学校的key
                key = get_school_key(school_name, ip)
                if key: key = key[0][0]
                # 创建sql对象并获取sql执行结果
                obj = SqlCvs(sql, ip)
                res = obj.execute(key)
                # 获取表结构
                table_field = get_table_desc(file_name, ip)
                # 把sql结果写入到文件中
                write_csv(res, ip, file_name, table_field)


def write_csv(res, ip, file_name, table_field):
    """
    写入csv文件
    :param res:
    :param ip:
    :param file_name:
    :return:
    """
    with open("%s/%s_%s.csv" % (output_path, ip, file_name), mode="w", encoding="utf-8") as f2:
        write = csv.writer(f2, dialect="excel")
        write.writerow(table_field)
        for row in res:
            write.writerow(row)


def get_table_desc(table_name, ip):
    """
    获取表结构写入csv的时候使用
    :return:
    """
    obj = SqlCvs("select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s';" % (table_name,), ip)
    ret = obj.execute()
    ret_list = []
    for i in ret:
        ret_list.append(i[0])
    return ret_list


def get_school_key(name, ip):
    """
    获取学校ID
    :param name: 学校名称
    :param ip: 学校IP
    :return: 学校ID
    """
    obj = SqlCvs("SELECT business_key FROM bd_school WHERE name='%s'" % (name,), ip)
    key = obj.execute()
    return key


def run():
    # 取到所有sql文件列表
    sql_list = os.listdir(sql_file_list)
    # 循环所有的sql文件拿到sql语句，交个handel_sql函数进行查询操作
    for i in sql_list:
        with open("%s/%s" % (sql_file_list, i), encoding="utf-8") as f:
            sql = f.read()
            file_name = i.split(".")[0]
            handel_sql(sql, file_name)


if __name__ == '__main__':
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    run()
