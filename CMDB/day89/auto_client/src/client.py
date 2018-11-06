#!/usr/bin/env python3
import requests
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
        # 使用requests 发送post请求。把采集到客户端信息发送给api
        requests.post(
            url=settings.API,
            json=dict_info,
        )


class AgentClient(BaseClient):
    def exec(self):
        """
        AGENT模式不需要获取主机列表，安装过采集器的服务器都可以直接采集数据
        :return:
        """
        obj = PluginsManager()
        dict_info = obj.exec_plugins()
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
        return ["c1.com", "c2.com"]
    
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
            pool.submit(self.task, host)


    

    