#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from libcore.config.config import Config
from libcore.repository.index import Index
from libcore.repository.local_repository import LocalRepository
from libcore.repository.remote_repository import RemoteRepository
from libcore.exception.not_support_repository_indexer_exception import NotSupportRepositoryIndexerException


def jjvmm():
    app_config = Config()
    app_indexer = Index(config=app_config)
    try:
        app_local_repository = LocalRepository(indexer=app_indexer)
        app_remote_repository = RemoteRepository(indexer=app_indexer)
    except NotSupportRepositoryIndexerException as e:
        print(e)


if __name__ == '__main__':
    jjvmm()
