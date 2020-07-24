#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

Author: wikinee
Command: python3 setup.py build_ext --inplace
Dependency: cpython3
Description: 将 python 源码文件编译成 so 文件
Filename: setup.py
First Release: 2020.07.22

"""

import os
import sysconfig
from setuptools import setup
from setuptools.extension import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext

cur_dir = os.path.abspath(os.path.dirname(__file__))
build_tmp_dir = os.path.join(cur_dir, 'temp')

def get_ext_filename_without_platform_suffix(filename):
    """ 去除文件多余扩展名的函数

    :param: filename: 文件名
    :return: 不包含平台信息的文件名
    """
    name, ext = os.path.splitext(filename)
    ext_suffix = sysconfig.get_config_var('EXT_SUFFIX')

    if ext_suffix == ext:
     return filename

    ext_suffix = ext_suffix.replace(ext, '')
    idx = name.find(ext_suffix)

    if idx == -1:
     return filename
    else:
     return name[:idx] + ext


class BuildExtWithoutPlatformSuffix(build_ext):
    """ 重写生成 so 文件的命名机制

    原生函数生成的 so 命名机制是: 原文件名.平台信息.so，例如：
    cpython-35m-x86_64-linux-gnu.so
    """
    def get_ext_filename(self, ext_name):

        filename = super().get_ext_filename(ext_name)
        return get_ext_filename_without_platform_suffix(filename)

# will generate build/aaa.so, build/bbb.so
setup(
    name="cythontest",
    ext_modules=cythonize(
        [
            Extension('build/aaa', ["source/aaa.py"]),
            Extension('build/bbb', ["source/bbb.py"]),
        ],
        build_dir="build",
        compiler_directives=dict(
            always_allow_keywords=True,
            c_string_encoding='utf-8',
            language_level=3
        )
    ),
    cmdclass=dict(
        build_ext=BuildExtWithoutPlatformSuffix
    ),
    packages=["cythontest"]
)
