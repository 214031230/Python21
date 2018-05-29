#!/usr/bin/env python3
import json


class MyJson:
    @staticmethod
    def load(file_path):
        with open(file_path, "r") as f:
            return json.load(f)

    @staticmethod
    def dump(obj, file_path):
        with open(file_path, "w") as f:
            json.dump(obj, f)
