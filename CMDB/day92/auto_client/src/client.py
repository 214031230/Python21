#!/usr/bin/env python3
import requests
import json
import time
import hashlib
from os import path as os_path
from lib.config import settings
from src.plugins import PluginsManager
from abc import abstractmethod, ABCMeta
from concurrent.futures import ThreadPoolExecutor


class BaseClient(metaclass=ABCMeta):
    """
    实现接口类（接口约束）：
        抽象类：ABCMeta
        抽象方法：abstractmethod
        继承接口类的类都必须实现抽象方法
    """

    @abstractmethod
    def exec(self):
        pass

    def post_server_info(self, dict_info):
        # 取到当前时间
        c_time = str(time.time())
        # 当前时间和key结合生成动态key
        new_key = "%s|%s" % (settings.KEY, c_time)
        # 对动态key进行加密
        ret = self.md5(new_key)
        # 生成头信息
        auth_header_val = "%s|%s" % (ret, c_time)
        # 发送key信息进行验证
        response = requests.post(url=settings.API, json=dict_info, headers={"auth-api": auth_header_val})
        # 使用requests 发送post请求。把采集到客户端信息发送给api
        print("发送成功并收到响应：", response.text)
        # requests.post(
        #     url=settings.API,
        #     json=dict_info,
        # )

    def md5(self, arg):
        """
        MD5加密
        :param arg:
        :return:
        """
        hs = hashlib.md5()
        hs.update(arg.encode("utf-8"))
        return hs.hexdigest()


class AgentClient(BaseClient):
    def exec(self):
        """
        AGENT模式不需要获取主机列表，安装过采集器的服务器都可以直接采集数据
        update:
            约束条件：主机名唯一
            问题：如果用户临时更改了主机名，就会出现重复汇报的问题。1个固定资产变成2个
            解决方法：
                1. 在客户端生成一个文件./conf/cref
                2. 判断cref是否为空，如果为空则程序第一次运行：
                       则汇报新的主机名给API,并把主机名写入到cref
                3. 如果不为空
                        则修改需要汇报的主机名为cref文件中的主机名 并发送给API进行汇报
                注释：
                    如果需要修改主机名， 需要同时修改cref和后台管理中的主机名
        :return:
        """
        obj = PluginsManager()
        dict_info = obj.exec_plugins()
        # 获取新的主机名
        new_hostname = dict_info["basic"]["data"]["hostname"]
        # 获取cref文件路径
        cref_path = os_path.join(settings.BASEDIR, "conf/cref")
        # 获取旧的主机名
        f = open(cref_path, mode="r")
        old_hostname = f.read()
        f.close()
        # 如果文件为空
        if not old_hostname:
            with open(cref_path, "w") as f:
                f.write(new_hostname)
            print("用户未修改主机名")
        else:
            # 如果不为空
            dict_info["basic"]["data"]["hostname"] = old_hostname
            print("用户修改了主机名")
        print(dict_info)
        self.post_server_info(dict_info)


class SaltSshClient(BaseClient):
    def task(self, host):
        """
        1. 拿到插件管理对象
        2. 执行插件方法获取采集信息
        3. 发送采集信息到API
        :param host:
        :return:
        """
        obj = PluginsManager(host)
        dict_info = obj.exec_plugins()
        print(dict_info)
        self.post_server_info(dict_info)

    def get_hosts_lists(self):
        """
        从API获取未采集过的服务器列表
        :return:
        """
        # 取到当前时间
        c_time = str(time.time())
        # 当前时间和key结合生成动态key
        new_key = "%s|%s" % ("324SD2342SD242FSFS2", c_time)
        # 对动态key进行加密
        ret = self.md5(new_key)
        # 生成头信息
        auth_header_val = "%s|%s" % (ret, c_time)
        # 发送key信息进行验证
        response = requests.get(url=settings.API, headers={"auth-api": auth_header_val})
        # response = requests.get(settings.API)
        # host_list = json.loads(response.text)  # [{"hostname": "c1.com"}]
        # print(host_list)
        # return host_list
        if response:
            host_list = json.loads(response.text)
            print(host_list)
            return host_list

    def exec(self):
        """
        1. 生成线程池
        2. 获取需要采集的服务器列表
        3. 循环提交采集任务（线程池方式）
        更新：使用线程池代替循环提高代码执行效率
        :return:
        """
        pool = ThreadPoolExecutor(settings.THREAD)
        for host in self.get_hosts_lists():
            pool.submit(self.task, host["hostname"])
