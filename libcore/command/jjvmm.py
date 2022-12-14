#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import click

from libcore.command.list_command import *
from libcore.command.install_command import *
from libcore.command.use_command import *
from libcore.command.help_command import *
from libcore.command.doctor_command import *
from libcore.command.remove_command import *


class JJVMM:

    @staticmethod
    @click.group
    def jjvmm():
        pass

    @staticmethod
    def run():
        JJVMM.jjvmm.add_command(cmd=ListCommand(name="list",
                                                help="""List local and remote Java environment.
\nFor example: 
\n  jjvmm list
\n  jjvmm list Oracle
\n  jjvmm list oracle
\n
\n[PUBLISHER]: Default: Oracle;
\n    Optional Publishers: 
\n      - Amazon(Amazon Corretto)
\n      - Azul(Azul Zulu Community)
\n      - BellSoft(BellSoft Liberica JDK)
\n      - Eclipse(Eclipse Temurin - AdoptOpenJDK HotSpot)
\n      - GraalVM(GraalVM Community Edition)
\n      - Oracle(Oracle OpenJDK)
\n      - SAP(SAP SapMachine)
\n      - IBM(IBM Semmeru - AdoptOpenJDK OpenJ9)
        """,
                                                short_help="List local and remote Java environment.",
                                                params=[
                                                    ListCommandPublisherArgument(param_decls=["publisher"],
                                                                                 required=False)
                                                ]))
        JJVMM.jjvmm.add_command(cmd=InstallCommand(name="install",
                                                   help="""Download and install a Java environment to this machine.
\nFor example:
\n  jjvmm install 19.0.1
\n  jjvmm install Oracle 19.0.1
\n  jjvmm install --download-only 19.0.1
\n  jjvmm install --download-only oracle 19.0.1
\n  jjvmm install -o 19.0.1
\n
\n[PUBLISHER]: Default: Oracle;
\n    Optional Publishers: 
\n      - Amazon(Amazon Corretto)
\n      - Azul(Azul Zulu Community)
\n      - BellSoft(BellSoft Liberica JDK)
\n      - Eclipse(Eclipse Temurin - AdoptOpenJDK HotSpot)
\n      - GraalVM(GraalVM Community Edition)
\n      - Oracle(Oracle OpenJDK)
\n      - SAP(SAP SapMachine)
\n      - IBM(IBM Semmeru - AdoptOpenJDK OpenJ9)
\n
\n[VERSION]: Default: latest.
        """,
                                                   short_help="Download and install a Java environment to this machine.",
                                                   params=[
                                                       InstallCommandDownloadOnlyOption(
                                                           param_decls=("--download-only", "-o"),
                                                           is_flag=True,
                                                           help="Only download Java environment."),
                                                       InstallCommandPublisherArgument(param_decls=["publisher"],
                                                                                       required=False),
                                                       InstallCommandVersionArgument(param_decls=["version"],
                                                                                     required=False)
                                                   ]))
        JJVMM.jjvmm.add_command(cmd=UseCommand(
            name="use",
            help="""""",
            short_help="Set a Java environment to current.",
            params=[
                UseCommandPublisherArgument(),
                UseCommandVersionArgument()
            ]
        ))
        JJVMM.jjvmm.add_command(cmd=DoctorCommand(
            name="doctor",
            help="""""",
            short_help="Diagnose the JJVMM and try to repair it.",
            params=[
                DoctorCommandFixOption()
            ]
        ))
        JJVMM.jjvmm.add_command(cmd=RemoveCommand(
            name="remove",
            help="""
\n1. Delete the installed Java (delete the files and environment variables in the installation directory), but do not delete the cache. (--install | -i)
\n2. Delete the installed Java (delete the files and environment variables in the installation directory), but delete the cache. (--cache --install | -c -i)
\n3. Do not delete the installed Java, but delete the cache of the specified Java. (--cache | -c)
\n4. Do not delete the installed Java, but delete all caches.(--cache --all | -c -a)
\n5. --install | -i is default.
\n
\n For example:
\n  jjvmm remove Oracle
\n  jjvmm remove oracle
\n  jjvmm remove Oracle 19.0.1
\n  jjvmm remove --install Oracle
\n  jjvmm remove --install oracle 19.0.1
\n  jjvmm remove --cache --all
\n  jjvmm remove --cache Oracle
\n  jjvmm remove --cache Oracle 19.0.1
\n  jjvmm remove --cache --install Oracle
\n  jjvmm remove --cache --install Oracle 19.0.1
\n  jjvmm remove -i Oracle
\n  jjvmm remove -i oracle 19.0.1
\n  jjvmm remove -c -a
\n  jjvmm remove -c Oracle
\n  jjvmm remove -c Oracle 19.0.1
\n  jjvmm remove -c -i Oracle
\n  jjvmm remove -c -i Oracle 19.0.1
""",
            short_help="Remove cached or installed Java environment.",
            params=[
                RemoveCommandAllOption(),
                RemoveCommandCacheOption(),
                RemoveCommandInstallOption(),
                RemoveCommandPublisherArgument(),
                RemoveCommandVersionArgument()
            ]
        ))


if __name__ == '__main__':
    pass
