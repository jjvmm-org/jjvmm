#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import getpass
import platform
import configparser

from libcore.util.string_util import StringUtil
from libcore.exception.config_key_not_exist_exception import ConfigKeyNotExistException
from libcore.exception.not_support_system_type_exception import NotSupportSystemTypeException
from libcore.exception.get_system_info_exception import GetSystemInfoException
from libcore.exception.config_file_parse_failed_exception import ConfigFileParseFailedException


class Config:
    """
    配置
    """

    __default_mirror = None
    __default_lang = "en_US"
    __default_publisher = "Oracle"

    __config = None

    __config_file_windows_tpl = "{system_root}\\Users\\{username}\\AppData\\Local\\jjvmm\\config\\.jjvmm-config.ini"
    __config_file_osx_tpl = "/Users/{username}/.jjvmm/Config/.jjvmm-config.ini"
    __config_file_linux_tpl = "/home/{username}/.jjvmm/config/.jjvmm-config.ini"

    __config_file_windows = None
    __config_file_osx = None
    __config_file_linux = None

    __curr_system_type = None
    __curr_windows_system_root = "C:"
    __curr_username = None

    __allow_config_keys = (
        'mirror',
        'lang',
        'publisher'
    )

    def __init_system_info(self):
        """
        获取操作系统各种信息
        :return:
        """
        system_type = platform.system()
        curr_username = getpass.getpass()

        if StringUtil.is_empty(curr_username):
            raise GetSystemInfoException("Failed to get current user name.")

        self.__curr_username = curr_username.strip()

        if system_type == "Darwin":
            self.__curr_system_type = "OSX"
        elif system_type == "Windows":
            system_root = os.getenv("SystemDrive", default="C:")
            if StringUtil.is_empty(system_root):
                raise GetSystemInfoException("Illegal system root path: {}".format(system_root))

            self.__curr_windows_system_root = system_root.strip()
        elif system_type == "Linux":
            self.__curr_system_type = "Linux"
        else:
            raise NotSupportSystemTypeException("Unrecognized operating system.")

    def __init_config_file_location(self):
        """
        初始化配置文件位置
        :return:
        """
        if self.__curr_system_type == "OSX":
            self.__config_file_osx = self.__config_file_osx_tpl.format(username=self.__curr_username)
        elif self.__curr_system_type == "Windows":
            self.__config_file_windows = self.__config_file_windows_tpl.format(
                system_root=self.__curr_windows_system_root,
                username=self.__curr_username)
        elif self.__curr_system_type == "Linux":
            self.__config_file_linux = self.__config_file_linux_tpl.format(username=self.__curr_username)
        else:
            pass

    def __load_config_file(self):
        """
        加载配置文件
        如果文件不存在，那么不加载。
        如果第一次保存配置的时候，文件不存在，直接创建。
        如果文件存在，加载，修改。
        :return:
        """

        # TODO 通过操作系统路径加载 .jjvmm-config.ini

        filename = ""
        if os.path.exists(filename):
            self.__config = configparser.ConfigParser()
            self.__config.read(filename, encoding="UTF-8")

            sections = self.__config.sections()

            if "app" not in sections:
                raise ConfigFileParseFailedException(filename)

    def __init__(self):
        self.__init_system_info()
        self.__init_config_file_location()
        self.__load_config_file()

    def get(self, key: str) -> str:
        """
        获取配置项
        :param key: Key
        :return: Value
        """

        if StringUtil.is_empty(key):
            raise ConfigKeyNotExistException("{} is not in config file, because key is empty.".format(key))

        if key not in self.__allow_config_keys:
            raise ConfigKeyNotExistException("{} is not in config file, the specified key is illegal.".format(key))

        key = key.strip()

        if self.__config is None:
            return self.__match_config_key()
        else:
            val = self.__config.get("app", key).strip()
            return self.__match_config_key(key=key) if StringUtil.is_empty(val) else val

    def __match_config_key(self, key: str) -> str:
        if key == "mirror":
            return self.__default_mirror
        elif key == "lang":
            return self.__default_lang
        elif key == "publisher":
            return self.__default_publisher

    def set(self, key: str, value: str) -> bool:
        """
        设置配置项
        :param key: Key
        :param value: Value
        :return: 如果不存在这个配置项，那么返回 False
        """
        pass

    def get_with_default(self, key: str, default: str):
        """
        获取配置项, 如果这个配置项的值为空，那么返回用户指定的 default
        :param key: Key
        :return: Value
        :param default: 默认值
        :return: Value
        """
        pass


if __name__ == '__main__':
    pass
