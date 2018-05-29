#!/usr/bin/env python3
from conf import settings
from core.FtpServer import FtpServer


def run():
    func = FtpServer(settings.bind_ip, settings.bind_port)
    func.run()
