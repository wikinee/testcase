#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

def get_filter_files(local_new_folder, filter_list):
    """ 获取本地支持上传的文件 """
    file_list = []
    if not os.path.isdir(local_new_folder):
        return file_list
    print("Get Local Filter Files!")
    for top_dir, dirs, files in os.walk(local_new_folder):
        for item in files:
            if item[0] == '.':
                print("Get Local Filter Files: file is hidden file")
                continue
            file_suffix = os.path.splitext(item)[1]
            if not file_suffix:
                continue

            if file_suffix[1:] in filter_list:
                single_file = os.path.join(top_dir, item)
                file_list.append(single_file)

    return file_list


if __name__ == '__main__':
    res = get_filter_files('/home/user/Documents', ['txt', 'doc', 'docx', 'pdf'])
    print(res)