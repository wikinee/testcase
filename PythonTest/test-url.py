#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

TEST_URL = "https://www.baidu.com"
TEST_ERROR_URL = "https://www.bbbaidu.com"

def try_url_open(URL):
    try:
        print("Test %s" % URL)
        request.urlopen(URL)
    except Exception as e:
        print("Test failed: %s" % e)
    else:
        print("Test ok!")

try_url_open(TEST_URL)
try_url_open(TEST_ERROR_URL)
