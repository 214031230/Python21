#!/usr/bin/env python3
from sys import path as sys_path
from os import path
sys_path.insert(0, path.dirname(path.dirname(path.abspath(__file__))))
from conf import settings
from core.FtpClient import FtpClient

if __name__ == "__main__":
    func = FtpClient(settings.server_ip, settings.server_port)
    func.run()
