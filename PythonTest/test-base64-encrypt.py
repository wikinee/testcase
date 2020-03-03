"""myPasswd
my passwd encrypt by base64
"""
#! /usr/bin/python3
# *-* coding: utf-8 *-*

import base64
import sys
encry = base64.b64encode(sys.argv[1]).decode('utf-8')
print(encry[:10])
