#!/usr/bin/env python3
import os
import time
import paramiko
import zipfile
from concurrent.futures import ThreadPoolExecutor

user = "edu_platform"
password = "edu_platform"
db = "edu_platform"
output_dir = "./output"
sql_file_path = "./sql_file_list"
hostlist = "./hostlist"
log = "./log/error.log"
put_ip = "119.254.82.22"


class SftpClient:
    def __init__(self, host):
        self.host = host
        self.user = "edu-jcpt"
        self.password = "lanpa898989"
        self.port = 9917
        self.timeout = 2000
        self.d_path = "/home/edu-jcpt/sync/data/output.zip"
        self.s_path = "./output.zip"
        self.dirname = "./output"

    def put(self):
        """
        上传文件
        :return:
        """
        t = paramiko.Transport((self.host, self.port))
        t.connect(username=self.user, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(self.s_path, self.d_path)
        t.close()

    def zip(self):
        startdir = self.dirname  # 要压缩的文件夹路径
        file_news = startdir + '.zip'  # 压缩后文件夹的名字
        z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)  # 参数一：文件夹名
        for dirpath, dirnames, filenames in os.walk(startdir):
            fpath = dirpath.replace(startdir, '')  # 这一句很重要，不replace的话，就从根目录开始复制
            fpath = fpath and fpath + os.sep or ''  # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
        z.close()

    def unzip(self):
        cmd = "cd %s&&unzip -o %s" % (os.path.dirname(self.d_path), self.d_path,)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, port=self.port, username=self.user, password=self.password,
                       timeout=self.timeout)
        stdin, stdout, stderr = client.exec_command(cmd)
        error = stderr.read()
        client.close()

    def clear(self):
        rmcmd = "cd %s&&rm -rf output.zip" % (os.path.dirname(self.d_path))
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, port=self.port, username=self.user, password=self.password,
                       timeout=self.timeout)
        stdin, stdout, stderr = client.exec_command(rmcmd)
        error = stderr.read()
        client.close()

    def run(self):
        self.zip()
        self.put()
        self.unzip()
        self.clear()


def get_school_key(ip, school_name):
    """
    获取学校的key
    :param ip: 服务器IP
    :param school_name: 学校名称
    :return:
    """
    cmd = """mysql -u%s -p%s  -h%s -X --xml --database %s  --connect-timeout=2 -e"
        SELECT business_key FROM bd_school WHERE name='%s'"|grep field|awk -F">" '{print $2}'|awk -F"<" '{print $1}'
        """ % (user, password, ip, db, school_name)

    res = os.popen(cmd).read()
    return res.strip()


def get_data_to_csv(ip, school_name, school_key):
    """
    导出sql到csv
    :param ip: 服务器IP
    :param school_name: 学校名称
    :param school_key: 234s24s42sd42234
    :return:
    """
    for tname, tsql in get_sql().items():
        filedir = os.path.join(output_dir, tname)
        if not os.path.isdir(filedir):
            os.mkdir(filedir)
        sql = tsql.replace("e14059b54350457c8726cc99970d14ec", school_key)
        cmd = """mysql -u%s -p%s  -h%s  --database %s --connect-timeout=2 -e"%s" >%s/%s/%s_%s_%s.xls""" % (
            user, password, ip, db, sql, output_dir, tname, ip, school_name, tname)

        os.system(cmd)


def get_sql():
    """
    获取所有的sql语句
    :return: {t1:sql1, t2:sql2}
    """
    sql_dic = {}
    sql_file_list = os.listdir(sql_file_path)
    for file_name in sql_file_list:
        f = open("%s/%s" % (sql_file_path, file_name))
        sql = f.read()
        sql_dic[file_name.split(".")[0]] = sql
    return sql_dic


def run(school_name, ip):
    """
    主运行函数
    :param school_name:
    :param ip:
    :return:
    """
    t_date = time.strftime("%Y-%m-%d %H:%M:%S")
    key = get_school_key(ip, school_name)
    if key:
        get_data_to_csv(ip, school_name, key)
    else:
        with open(log, "a") as f:
            f.write("%s：%s_%s：网络不通\n" % (t_date, school_name, ip))


if __name__ == '__main__':
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    t = ThreadPoolExecutor(20)
    try:
        with open(hostlist) as f:
            for i in f.readlines():
                school_name, ip = i.split()
                t.submit(run, school_name, ip)
    except Exception as e:
        pass
    t.shutdown()
    os.system("./sed.sh")
    obj = SftpClient(put_ip)
    obj.run()
