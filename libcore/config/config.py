#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import configparser, getpass , os, platform, shutil
from libcore.exception.config_key_not_exist_exception import ConfigKeyNotExistException
from libcore.exception.config_value_not_in_range_exception import ConfigValueNotInRangeException
from libcore.util.string_util import StringUtil
from libcore.exception.not_support_system_type_exception import NotSupportSystemTypeException
from libcore.exception.get_system_info_exception import GetSystemInfoException
from libcore.exception.config_file_parse_failed_exception import ConfigFileParseFailedException

class Config:
    """
    配置
    """
    """系统配置"""
    __config_file_windows_tpl = "{systemroot}\\Users\\{username}\\AppData\\Local\\jjvmm\\config\\.jvms-config.ini"
    __config_file_osx_tpl = "/Users/{username}/.jjvmm/Config/.jvms-config.ini"
    __config_file_linux_tpl = "/home/{username}/.jjvmm/config/.jvms-config.ini"

    __config_file_windows = None
    __config_file_osx = None
    __config_file_linux = None

    __curr_os_type = None
    __curr_username = None
    __curr_windows_system_root = None

    """文件配置"""
    __config = None
    __filename = None

    __allow_config_keys = (
        "publisher",
        "mirror",
        "lang"
    )

    __default_publisher = "Oracle"
    __default_mirror = ""
    __default_lang = "English"

    __allow_config_publishers = (
        "Oracle",
        "Amazon"
    )

    __allow_config_mirrors = (
        "url",
    )

    __allow_config_languages = (
        "English",
        "Chinese",
        "Japanese"
    )

    def __init_system_info(self):
        """
        初始化系统信息
        """
        os_type = platform.system()
        curr_username = getpass.getuser()
        if StringUtil.is_empty(curr_username):
            raise GetSystemInfoException("Failed to get current user name.")
        self.__curr_username = curr_username.strip()

        if os_type == "Darwin":
            self.__curr_os_type = "OSX"
        elif os_type == "Windows":
            system_root = os.getenv("SystemDrive", default="C:").strip()
            if StringUtil.is_empty(system_root):
                raise GetSystemInfoException("Inappropriate system root path: {}".format(system_root))
            self.__curr_windows_system_root = system_root
            self.__curr_os_type = "Windows"
        elif os_type == "Linux":
            self.__curr_os_type = "Linux"
        else:
            raise NotSupportSystemTypeException("Unrecognized operating system")

    def __init_config_file_location(self):
        """
        初始化配置文件位置
        """
        if self.__curr_os_type == "OSX":
            self.__config_file_osx = self.__config_file_osx_tpl.format(
                username=self.__curr_username)
        elif self.__curr_os_type == "Windows":
            self.__config_file_windows = self.__config_file_windows_tpl.format(
                systemroot=self.__curr_windows_system_root,
                username=self.__curr_username)
        elif self.__curr_os_type == "Linux":
            self.__config_file_linux = self.__config_file_linux_tpl.format(
                username=self.__curr_username)
        else:
            raise NotSupportSystemTypeException("Unrecognized operating system")

    def __load_config_file(self):
        """
        加载配置文件
        如果不存在此文件，那么不进行加载。
        如果第一次保存配置的时，文件不存在，则创建文件。
        如果文件存在，则加载且修改文件。
        """
        if self.__curr_os_type == "OSX":
            self.__filename = self.__config_file_osx
        elif self.__curr_os_type == "Windows":
            self.__filename = self.__config_file_windows
        elif self.__curr_os_type == "Linux":
            self.__filename = self.__config_file_linux
        else:
            raise NotSupportSystemTypeException("Unrecognized operating system")

        if os.path.exists(self.__filename):
            self.__config = configparser.ConfigParser()
            self.__config.read(self.__filename,encoding="UTF-8")
            if self.__config.has_section("app") == False:
                raise ConfigFileParseFailedException("{} parsing failed".format(self.__filename))

    def __init__(self):
        self.__init_system_info()
        self.__init_config_file_location()
        self.__load_config_file()

    def get(self,key:str) -> str:
        """
        获取配置项
        :param key: Key
        :return: Value
        """
        self.__key_check(key=key)
        if self.__config == None:
            return self.__match_key(key=key)
        else:
            self.__config.read(self.__filename, encoding="UTF-8")
            val = self.__config.get('app',key).strip()
            return self.__match_key(key=key) if StringUtil.is_empty(val) else val

    def set(self,key:str,value:str)-> bool:
        """
        设置配置项
        :param key: Key
        :param value: Value
        :return: 如果不存在这个配置项，那么返回 False
        """
        self.__key_check(key=key)
        if StringUtil.is_empty(s=value):
            raise ConfigValueNotInRangeException("{} is not in in range, the value is empty.".format(value))

        if key == self.__allow_config_keys[0]:
            if value not in self.__allow_config_publishers:
                raise ConfigValueNotInRangeException("{} is not in range, the value is irrational.".format(value))
            self.__modify_value(k=key, v=value)
        elif key == self.__allow_config_keys[1]:
            if value not in self.__allow_config_mirrors:
                raise ConfigValueNotInRangeException("{} is not in range, the value is irrational.".format(value))
            self.__modify_value(k=key, v=value)
        elif key == self.__allow_config_keys[2]:
            if value not in self.__allow_config_languages:
                raise ConfigValueNotInRangeException("{} is not in range, the value is irrational.".format(value))
            self.__modify_value(k=key, v=value)

        return True

    def get_with_default(self,key:str, defalut:str) ->str:
        """
        获取配置项，如果这个配置项的值为空，那么返回 default
        :param key: Key
        :param default: Default
        :return: value
        """
        self.__key_check(key=key)
        if self.__config == None:
            if key == "publisher":
                 return defalut if len(self.__default_publisher) == 0 else self.__match_key(key=key)
            elif key == "mirror":
                return defalut if len(self.__default_mirror) == 0 else self.__match_key(key=key)
            elif key == "lang":
                return defalut if len(self.__default_lang) == 0 else self.__match_key(key=key)
        else:
            self.__config.read(self.__filename, encoding="UTF-8")
            return defalut if len(self.__config.get('app', key)) == 0 else self.__config.get('app', key)

    def __key_check(self,key:str):
        """
        检查 Key 如果为空或不在配置项范围内，那么抛出异常
        :param key:
        """
        if StringUtil.is_empty(s=key):
            raise ConfigKeyNotExistException("{} is not in config file, the key is empty.".format(key))

        if key not in self.__allow_config_keys:
            raise ConfigKeyNotExistException("{} is not in config file, the key is irrational.".format(key))

    def __match_key(self,key:str)->str:
        """
        匹配默认配置项中的值
        :param key:
        :return:
        """
        if key == "publisher":
            return self.__default_publisher
        elif key == "mirror":
            return self.__default_mirror
        elif key == "lang":
            return self.__default_lang

    def __modify_value(self,k:str,v:str):
        """
        修改选定配置项的值
        :param k: key
        :param v: value
        """
        if self.__config == None:
            work_dir = os.getcwd()
            if self.__curr_os_type == "Windows":
                config_tpl = work_dir+ "\\" +"assets\.jvms-config.ini.template"
            else:
                config_tpl = work_dir + "/" + "assets/.jvms-config.ini.template"
            if os.path.exists(config_tpl):
                config_dir = self.__filename.split(".jvms-config.ini")
                os.makedirs(r'{}'.format(config_dir[0]))
                shutil.copy(config_tpl, self.__filename)
                self.__config = configparser.ConfigParser()
                self.__config.read(self.__filename, encoding="UTF-8")
                self.__config.set('app', k, v)
                self.__config.write(open(self.__filename, "r+", encoding="UTF-8"))
            else:
                raise GetSystemInfoException("Config template is missing: {}".format(config_tpl))
        else:
            self.__config.read(self.__filename,encoding="UTF-8")
            self.__config.set('app', k, v)
            self.__config.write(open(self.__filename,"r+",encoding="UTF-8"))

            
if __name__ == '__main__':
    pass

