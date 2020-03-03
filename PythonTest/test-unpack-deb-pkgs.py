#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys

def get_deb_files(deb_path):
    deb_files = []
    for root, dirs, files in os.walk(deb_path, topdown=False):
        for name in files:
            # print(os.path.join(root, name))
            deb_files.append(os.path.join(root, name))
        # for name in dirs:
        #     print(os.path.join(root, name))
    return deb_files

def unpack_deb(deb_path):
    deb_files = get_deb_files(deb_path)
    for deb_file in deb_files:
        try:
            if deb_file == __file__:
                continue
            # if len(deb_file) < 4:
            #     continue
            # if deb_file[-4:] != ".deb" or deb_file[-5:0] != ".udeb":
            if deb_file[-4:] != ".deb":
                continue
            basename = os.path.basename(deb_file)
            subprocess.call(["dpkg-deb", "-R", deb_file, os.path.splitext(basename)[0]])
        except Exception as e:
            print("Unpack {} error, because {}".format(deb_file, e))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        pkg_path = os.path.dirname(os.path.realpath(__file__))
    else:
        pkg_path = sys.argv[1]
    unpack_deb(pkg_path)

