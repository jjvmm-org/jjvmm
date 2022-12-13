#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from libcore.repository.index import Index, App
from libcore.cache.cache import Cache
from libcore.util.string_util import StringUtil
from libcore.exception.not_support_repository_indexer_exception import NotSupportRepositoryIndexerException


class LocalRepository:
    __indexer = None

    __file_id_tpl = "{publisher}::{version}::{os}::{arch}::{dist}"

    def __init__(self, indexer: Index):
        if indexer is None:
            raise NotSupportRepositoryIndexerException("Local Repository indexer is null.")
        self.__indexer = indexer

    def get_file_by_app(self, app: App) -> str:
        """
        FileID: Publisher::Version::OS::Arch::Dist
        :param app:
        :return:
        """
        file = Cache.get_file_by_app(self.__file_id_tpl.format(
            # TODO 传入文件ID
        ))

        if StringUtil.is_empty(file):
            return ""

        return file


if __name__ == '__main__':
    pass
