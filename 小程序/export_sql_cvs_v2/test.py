import paramiko
import zipfile
import os


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
        print(error)

    def run(self):
        self.zip()
        self.put()
        self.unzip()


obj = SftpClient("119.254.82.22")
obj.run()
# obj.zip()
# obj.put()
# obj.unzip()
