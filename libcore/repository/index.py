#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import json
import requests

from libcore.config.config import Config


class App:
    __publisher = None
    __version = None
    __os = None
    __arch = None
    __dist = None
    __checksum_algo = None
    __checksum_content = None
    __file = None

    # TODO Getter/Setter


class Index:
    """
    用于访问 GitHub 存储库或者镜像源的 Index 文件（JSON）。
    """

    def __init__(self, config: Config = None):
        # TODO 根据环境变量和配置文件读取镜像源
        pass

    def get_version(self) -> str:
        pass

    def get_name(self) -> str:
        pass

    def get_publisher(self) -> str:
        pass

    def get_update_time(self) -> str:
        pass

    def get_app_versions_by_publisher(self, publisher: str) -> tuple:
        pass

    def get_app(self, publisher: str, version: str) -> tuple:
        pass


if __name__ == '__main__':
    pass
