#!/usr/bin/env python3
from conf import settings
from core.FtpClient import FtpClient


def run():
    func = FtpClient(settings.server_ip, settings.server_port)
    func.run()
