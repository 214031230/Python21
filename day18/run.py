#!/usr/bin/env python3
import importlib


if __name__ == '__main__':
    choice = input(">>>:")
    func = importlib.import_module("{}".format(choice))

    print(func.msg)
    print(func.tall())