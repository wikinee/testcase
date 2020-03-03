#!/usr/bin/python
#-*- coding:utf-8 -*-

from Xlib import X, display
from Xlib.ext import randr

from Xlib.ext.randr import PROPERTY_RANDR_EDID

import Xlib

import pdb

d = display.Display()
s = d.screen()
window = s.root.create_window(0, 0, 1, 1, 1, s.root_depth)

res = randr.get_screen_resources(window)


for mode in res.modes:
    w, h = mode.width, mode.height
    # print("Width: {}, height: {}".format(w, h))

outputs = randr.get_screen_resources(window).outputs

for output in outputs:
    outInfo = randr.get_output_info(window, output, 0)

    if outInfo.connection == 0:
        print(outInfo)
        # print("{} connected==>".format(outInfo.name))
        print(outInfo.name.encode('utf-8'))
    else:
    	print("WOOO: {}".format(outInfo))