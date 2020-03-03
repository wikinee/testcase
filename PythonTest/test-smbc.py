#!/usr/bin/python3
# -*- coding:utf-8 -*-

import smbc
import os
import stat
from pprint import pprint
import time
import shutil

WORKGROUP = "WORKGROUP"
SERVER = "172.30.13.105"
SHARE = "share02"
DESTDIR = "test"
USERNAME = "nsy"
PASSWORD = "nsy123"

BASE_URI = "smb://" + SERVER + '/' + SHARE
DEST_URI = BASE_URI + '/' + "ubuntu-18.04.1-desktop-amd64.iso"
FILE_URI = '/home/apple/ubuntu-18.04.1-desktop-amd64.iso'

# print(DEST_URI)

def my_auth_callback_fn(wg, se, sh, u, p):
    return (WORKGROUP, USERNAME, PASSWORD)

def test_opendir(dest_dir):
    ctx = smbc.Context(auth_fn=my_auth_callback_fn)
    try:
        open_obj = ctx.opendir(dest_dir)
    except smbc.TimedOutError:
        print("Connection failed, server path maybe error")
    except smbc.NoEntryError:
        print("Connection failed, share path or destination path maybe error")
    except smbc.PermissionError as e:
        print("Permission failed, username or password error")
    except Exception as e:
        print("333 {}".format(e))

def test_write():
    ctx = smbc.Context(auth_fn=my_auth_callback_fn)
    file_obj = ctx.open(DEST_URI, os.O_CREAT | os.O_WRONLY)
    file_obj.write("YOYOYOYOYOYO")
    file_obj.close()

    st = ctx.stat(DEST_URI)
    # print(st)
    print(st[stat.ST_SIZE])
    # mode = st[stat.ST_MODE]
    # print(mode)
    print(os.path.getsize('/home/apple/MyTest/ubuntu-18.04.1-desktop-amd64.iso'))

def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

def test_shutil():
    print(get_time_stamp())
    ctx = smbc.Context(auth_fn=my_auth_callback_fn)
    with open(FILE_URI, 'rb') as source_file_obj:
        dest_file_obj = ctx.open(DEST_URI, os.O_CREAT | os.O_WRONLY)
        shutil.copyfileobj(source_file_obj, dest_file_obj, 3 * 1024 * 1024)
    print(get_time_stamp())

def test_write():
    print(get_time_stamp())
    ctx = smbc.Context(auth_fn=my_auth_callback_fn)
    with open(FILE_URI, 'rb') as source_file_obj:
        dest_file_obj = ctx.open(DEST_URI, os.O_CREAT | os.O_WRONLY)
        while True:
            slice_data = source_file_obj.read(3 * 1024 * 1024)
            if not slice_data:
                break
            ret = dest_file_obj.write(slice_data)
    print(get_time_stamp())


if __name__ == '__main__':
    test_opendir(BASE_URI + '/' + DESTDIR)