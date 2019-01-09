#!/usr/bin/env python3
import os
from concurrent.futures import ThreadPoolExecutor


class UpdateJCDIR:
    def __init__(self):
        self.sql_list_path = "./sql_list"
        self.ip_list_path = "./ip_list"
        self.user = "edu_platform"
        self.password = "edu_platform"
        self.port = 3306
        self.db = "edu_platform"
        self.thread_count = 20

    def __get_sql_list(self):
        """
        获取sql文件路径列表
        :return: ["path1", "path2", ...]
        """
        res = os.listdir(self.sql_list_path)
        return [os.path.join(self.sql_list_path, i) for i in res]

    def __get_sql_content(self):
        """
        获取sql列表
        :return: ["sql1", "sql2", ...]
        """
        sql_list = []
        for i in self.__get_sql_list():
            with open(i, "r", encoding="utf-8") as f:
                for sql in f.readlines():
                    sql_list.append(sql.strip())
        return sql_list

    def __run_sql(self, ip):
        """
        执行sql
        :param ip: ip
        :return:
        """
        for i in self.__get_sql_content():
            sql = """
            mysql -u%s -p%s  -h%s -X --xml --database %s  --connect-timeout=2 -e"%s"
            """ % (self.user, self.password, ip, self.db, i)
            os.popen(sql)

    def run(self):
        t = ThreadPoolExecutor(self.thread_count)
        with open(self.ip_list_path, "r", encoding="utf-8") as f:
            for i in f.readlines():
                t.submit(self.__run_sql, i)


if __name__ == '__main__':
    obj = UpdateJCDIR()
    obj.run()
