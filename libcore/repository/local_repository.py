#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from libcore.repository.index import Index, App
from libcore.exception.not_support_repository_indexer_exception import NotSupportRepositoryIndexerException


class LocalRepository:
    __indexer = None

    def __init__(self, indexer: Index):
        if indexer is None:
            raise NotSupportRepositoryIndexerException("Local Repository indexer is null.")
        self.__indexer = indexer

    def file_by_app(self, app: App) -> str:
        pass


if __name__ == '__main__':
    pass
