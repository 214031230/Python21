#!/usr/bin/env python3
import pymysql
from conf import setting as sett


class Mysql:
    def __init__(self, sql, argv):
        self.host = sett.host
        self.port = sett.port
        self.user = sett.user
        self.password = sett.password
        self.database = sett.database
        self.charset = sett.charset
        self.sql = sql
        self.argv = argv

    def cursor(self):
        """
        创建mysql连接
        :return: 返回连接
        """
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset
        )
        return self.conn.cursor()

    def select(self):
        """
        执行sql查询语句返回结果
        :return: 返回执行结果
        """
        ret = self.cursor().execute(self.sql, self.argv)
        self.close()
        return ret

    def insert(self):
        """
        执行sql插入语句
        :return: 返回成功的行
        """
        ret = self.cursor().execute(self.sql, self.argv)
        self.conn.commit()
        self.close()
        return ret

    def close(self):
        """
        关闭连接
        :return:
        """
        self.cursor().close()
        self.conn.close()
