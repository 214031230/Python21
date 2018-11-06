#!/usr/bin/env python3
import sys
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
os.environ["auto_client_settings"] = "conf.settings"
from lib.config import settings

print(settings.DEBUG)
print(settings.API)