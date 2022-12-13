#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from libcore.repository.index import Index
from libcore.repository.index import App
from libcore.exception.not_support_repository_indexer_exception import NotSupportRepositoryIndexerException


class RemoteRepository:
    __indexer = None

    def __init__(self, indexer: Index):
        if indexer is None:
            raise NotSupportRepositoryIndexerException("Remote Repository indexer is null.")
        self.__indexer = indexer

    def get_file_by_app(self, app: App):
        return app.get_file()


if __name__ == '__main__':
    pass
