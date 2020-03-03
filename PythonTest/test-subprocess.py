#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import subprocess
import signal
import time

def test_popen():
    proc = subprocess.Popen("ping www.bing.com", shell=True)
    print("proc: {}".format(proc.pid))
    try:
        outs, errs = proc.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        outs, errs = proc.communicate()
        print("proc: {}".format(proc.pid))

def test_pgid():
    proc1 = subprocess.Popen("ping www.baidu.com", shell=True, start_new_session=True)
    proc2 = subprocess.Popen("ping www.sogou.com", shell=True, start_new_session=True)
    proc3 = subprocess.Popen("ping www.bing.com", shell=True, start_new_session=True)
    os.killpg(os.getpgid(proc1.pid), signal.SIGTERM)
    os.killpg(os.getpgid(proc2.pid), signal.SIGTERM)
    os.killpg(os.getpgid(proc3.pid), signal.SIGTERM)
    i = 1
    while True:
        time.sleep(1)


if __name__ == '__main__':
    # test_popen()
    test_pgid()