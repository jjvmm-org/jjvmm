#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Cache:
    """
    缓存
    """

    __file_ext = ".store"
    # __cache_name_tpl = "{fileid}####{year}#{month}#{day}{file_ext}"

    @staticmethod
    def get_file_by_app(file_id: str):
        pass

    @staticmethod
    def get_store_time(name: str) -> str:
        """
        根据缓存文件名获取存储时间
        """
        pass

    @staticmethod
    def get_file_id(name: str) -> str:
        """
        根据缓存文件名获取到文件ID
        :param name:
        :return:
        """
        pass

    @staticmethod
    def scan_caches(path: str) -> tuple:
        """
        跨平台的方式扫描缓存列表
        :param path:
        :return:
        """
        pass

    @staticmethod
    def remove_cache_name(name: str) -> bool:
        """
        删除指定的缓存
        :param name:
        :return:
        """
        pass

    @staticmethod
    def auto_remove_cache() -> int:
        """
        删除最近30天的缓存文件
        :return:
        """

    @staticmethod
    def remove_all_caches() -> bool:
        """
        删除全部的缓存
        :return:
        """
        pass


if __name__ == '__main__':
    pass
