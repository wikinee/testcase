#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
import time
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk

class TestGdk(object):
    def __init__(self):
        self.screen = Gdk.Screen().get_default()
        self.display = Gdk.Display().get_default()
        print(self.screen.get_n_monitors())
        self.screen.connect("monitors-changed", self.on_monitors_changed)
        self.display.connect("monitor-added", self.on_monitor_added)

    def on_monitors_changed(self, screen):
        print("=============================")
        # display = screen.get_display()
        # print(display.get_name())

    def on_monitor_added(self, display, monitor):
        print("+++++++++++++++++++++++++++++")

if __name__ == '__main__':
    td = TestGdk()
    while True:
        time.sleep(1)
