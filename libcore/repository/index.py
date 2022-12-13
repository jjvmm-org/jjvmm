#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import json
import requests

from libcore.config.config import Config
from libcore.util.string_util import StringUtil
from libcore.exception.config_key_not_exist_exception import ConfigKeyNotExistException
from libcore.exception.indexer_init_failed_exception import IndexerInitFailedException


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

    def get_file(self) -> str:
        return self.__file

class Index:
    """
    用于访问 GitHub 存储库或者镜像源的 Index 文件（JSON）。
    """

    __index_json = "index.json"
    __mirror_url = ""

    def __init__(self, config: Config = None):
        # TODO 根据环境变量和配置文件读取镜像源
        try:
            mirror = config.get("mirror")
            # TODO 处理兼容 http://mirrors.xlab.io 和 http://mirrors.xlab.io/
            self.__mirror_url = mirror + self.__index_json
        except ConfigKeyNotExistException as e:
            raise IndexerInitFailedException("Can not read mirror from config file, because: {}".format(e))

    def get_version(self) -> str | None:
        response = requests.get(self.__mirror_url)
        if response.status_code != 200:
            return None

        json_response = response.json()
        index_version = json_response["version"]

        if StringUtil.is_empty(index_version):
            return None

        return index_version.strip()

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
