#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import glob
from libcore.util.archive_util import ArchiveUtil


class OSX:
    """
    1. 通过绝对路径解析出版本号
    2. 校验 checksum - sha256
    3. 解压文件到规定的目录:
    """

    @staticmethod
    def __checksum(self, file: str, target_checksum: str) -> bool:
        """
        计算文件的 checksum 与 target_checksum 进行对比，
        如果不一样，那么不能安装
        :param file:
        :param target_checksum:
        :return:
        """
        pass

    @staticmethod
    def __install_zip(self, file: str) -> bool:
        pass

    @staticmethod
    def __install_tar_gz(self, file: str) -> bool:
        pass

    @staticmethod
    def __install_dmg(self, file: str) -> bool:
        raise NotImplementedError("Can not support dmg file format")

    @staticmethod
    def __install_pkg(self, file: str) -> bool:
        raise NotImplementedError("Can not support pkg file format")

    @staticmethod
    def install(self, file: str) -> bool:
        pass


if __name__ == '__main__':
    pass
