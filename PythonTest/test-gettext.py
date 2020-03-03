#!/usr/bin/python3
# -*- coding: utf-8 -*-

import locale
PACKAGE_NAME = 'hello'
LOCAL_DIR = '/usr/share/locale'
locale.bindtextdomain(PACKAGE_NAME, LOCAL_DIR)
locale.textdomain(PACKAGE_NAME)
_ = locale.gettext
