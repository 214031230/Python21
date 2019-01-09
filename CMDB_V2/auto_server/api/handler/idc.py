#!/usr/bin/env python3
from stark.service.stark import StarkConfig


class IDCConfig(StarkConfig):
    list_display = ["name", "floor"]
