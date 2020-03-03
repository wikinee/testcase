#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import signal
import time
from threading import Thread

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")
gi.require_version("GLib", "2.0")

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import GLib as glib
from gi.repository import GObject as gobject


class Indicator:
    def __init__(self, name=None, icon=None):
        self.path = os.path.abspath(os.path.dirname(__file__))
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        if name is None:
            self.name = "MyApp"
        else:
            self.name = name

        if icon is None:
            self.icon = gtk.STOCK_INFO
        else:
            self.icon = icon

        self.indicator = appindicator.Indicator.new(self.name, self.icon, appindicator.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())
        self.running = True
        self.paused = False

        # Use thread set update function
        self.thread = Thread(target=self.thread_update)
        self.thread.setDaemon(True)
        self.thread.start()

        # Use timeout set update function
        glib.timeout_add_seconds(1, self.custom_update)

    def create_menu(self):
        menu = gtk.Menu()

        pause_entry = gtk.MenuItem("Pause")
        pause_entry.connect("activate", self.pause)
        menu.append(pause_entry)

        quit_entry = gtk.MenuItem("Quit")
        quit_entry.connect("activate", self.quit)
        menu.append(quit_entry)

        menu.show_all()
        return menu

    def thread_update(self):
        while self.running:
            time.sleep(1)
            if not self.paused:
                print("Update")

    def custom_update(self):
        if not self.paused:
            print("Update...")
            return True
        return False

    def start(self):
        # gobject.threads_init()
        gtk.main()

    def pause(self, menu):
        self.paused = not self.paused
        text = "Resume" if self.paused else "Pause"
        for widget in menu.get_children():
            print(widget.get_text())
            widget.set_text(text)

    def quit(self, menu=None):
        self.running = False
        gtk.main_quit()


if __name__ == "__main__":
    indicator = Indicator()
    indicator.start()