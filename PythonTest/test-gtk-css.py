#!/usr/bin/python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

CLASS_FILE_PATH = "xxx.css"

def set_theme(self, file_theme):
    screen = Gdk.Screen.get_default()
    provider = Gtk.CssProvider()
    provider.load_from_path(file_theme)
    context = Gtk.StyleContext()
    context.add_provider_for_screen(screen,
                                provider,
                                Gtk.STYLE_PROVIDER_PRIORITY_USER)


# xxx_widget.set_theme(CLASS_FILE_PATH)
