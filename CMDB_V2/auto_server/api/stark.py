#!/usr/bin/env python3
from stark.service.stark import site
from api import models
from api.handler.idc import IDCConfig
from api.handler.server import ServerConfig

site.register(models.IDC, IDCConfig)
site.register(models.Server, ServerConfig)
