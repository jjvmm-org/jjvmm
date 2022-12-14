#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import click


# from libcore.config.config import Config
# from libcore.repository.index import Index
# from libcore.repository.local_repository import LocalRepository
# from libcore.repository.remote_repository import RemoteRepository
# from libcore.exception.not_support_repository_indexer_exception import NotSupportRepositoryIndexerException
# from libcore.exception.indexer_init_failed_exception import IndexerInitFailedException
# from libcore.cache.cache import Cache


def jjvmm():
    # app_config = Config()
    #
    # try:
    #     app_indexer = Index(config=app_config)
    # except IndexerInitFailedException as e:
    #     print(e)
    #     return
    #
    # try:
    #     app_local_repository = LocalRepository(indexer=app_indexer)
    #     app_remote_repository = RemoteRepository(indexer=app_indexer)
    # except NotSupportRepositoryIndexerException as e:
    #     print(e)
    #     return
    #
    # auto_remove_num = Cache.auto_remove_cache()
    # if auto_remove_num > 0:
    #     print("Auto task: {} cache files are cleared.".format(auto_remove_num))
    pass


@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)


if __name__ == '__main__':
    hello()
