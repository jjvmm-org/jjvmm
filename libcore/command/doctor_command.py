#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import typing as t

import click
from click import Context


class DoctorCommand(click.Command):
    """
    安装 Java 的时候，需要修改 CLASSPATH、PATH、JAVA_HOME，我们认为 JAVA_HOME 和 CLASSPATH 可以通过 use 命令实现。
    PATH 的设置，在 doctor 命令中实现
    doctor 只是实现了检查，需要通过 jjvmmm doctor --fix 参数或者 -f 参数进行修复
    """

    def invoke(self, ctx: Context) -> t.Any:
        return None


class DoctorCommandFixOption(click.Option):
    pass


if __name__ == '__main__':
    pass
