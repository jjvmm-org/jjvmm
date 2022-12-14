#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import typing as t

import click
from click import Context


class UseCommand(click.Command):

    def invoke(self, ctx: Context) -> t.Any:
        return None


class UseCommandPublisherArgument(click.Argument):
    pass


class UseCommandVersionArgument(click.Argument):
    pass


if __name__ == '__main__':
    pass
