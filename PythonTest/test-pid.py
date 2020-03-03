#!/usr/bin/python3
# -*- coding:utf-8 -*-

import subprocess
import time
import os
import sys

def get_cmd_name(pid_str):
    cmd = "ps -o comm= {}".format(pid_str)
    # 在 Python3 是二进制字符串
    cmd_name = subprocess.check_output(cmd, stderr=subprocess.STDOUT, encoding='utf-8', shell=True)
    return cmd_name

def test_cmd_name():
    try:
        res = get_cmd_name('1000')
    except subprocess.CalledProcessError as e:
        print("Get ahead pid failed, because %s" % e.output)
        print("returncode: %d" % e.returncode)
    else:
        print("res: %s" % res)

def alive_check():
    """决定此函数进程是否停止的函数

    监听 DESKTOP_SESSION 的运行情况, 如果发现它停止, 就将 SyncGtk 也停止
    """
    DESKTOP_SESSION = 'gnome-session-binary'
    try:
        get_session_cmd = 'pgrep -U {} -f {}'.format(os.getuid(), DESKTOP_SESSION[0:15])
        if sys.version_info < (3, 6):
            session_pid = subprocess.check_output(get_session_cmd, shell=True).decode('utf-8').split()[0]
        else:
            session_pid = subprocess.check_output(get_session_cmd, encoding='utf-8', shell=True).split()[0]

        if not session_pid:
            raise OSError('session no exists')
    except subprocess.CalledProcessError as err:
        print('Called error, because {}'.format(err))
        return False
    except OSError as e:
        print('{}'.format(e))
        os.kill(os.getpid(), signal.SIGTERM)
        return False
    else:
        print("Wait session quit")
        return True

def test_alive_check():
    while True:
        time.sleep(65)
        if not alive_check():
            break

if __name__ == '__main__':
    # test_cmd_name()
    test_alive_check()
