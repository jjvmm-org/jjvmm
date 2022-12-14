#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import typing as t

import click
from click import Context


class InstallCommand(click.Command):

    def invoke(self, ctx: Context) -> t.Any:
        """
        在这里调用其他模块的方法，然后执行。
        如果失败，那么调用 ctx 对象的 exit() 或者 fail() 或者 abort() 方法退出
        通过 ctx 对象的 params 属性获取用户传过来的值
        """
        return None


class InstallCommandDownloadOnlyOption(click.Option):
    pass


class InstallCommandPublisherArgument(click.Argument):
    pass


class InstallCommandVersionArgument(click.Argument):
    pass


if __name__ == '__main__':
    pass
