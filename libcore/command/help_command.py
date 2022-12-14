#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import typing as t

import click
from click import Context


class HelpCommand(click.Command):

    def invoke(self, ctx: Context) -> t.Any:
        return None


if __name__ == '__main__':
    pass
