#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name='jjvmm',
    version='1.0.0',
    py_modules=['app.py'],
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        jjvmm=jjvmm:jjvmm
    '''
)

if __name__ == '__main__':
    pass
