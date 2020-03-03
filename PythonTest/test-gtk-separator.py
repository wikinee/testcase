#!/usr/bin/env python3
#
# created: 19/01/15
# author: wikinee
# first relase: 19/01/15
TITLE = "Separator"
DESCRIPTION = """
A Gtk widget used in separator widgets
"""

import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

CSS_PATH = os.getcwd() + "/test.css"

class SeparatorWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Test SeparatorWindow")
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(box)
        self.set_size_request(200, 200)
        button1 = Gtk.Button()
        button1.set_label("Button1")
        button1.set_name("hehehe")
        box.add(button1)
        widget = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        widget.set_name ("hahaha")
        box.add(widget)
        button2 = Gtk.Button()
        button2.set_label("Button2")
        box.add(button2)
        button3 = Gtk.Button()
        button3.set_label("Button3")
        box.add(button3)
        provider = Gtk.CssProvider()
        provider.load_from_path(CSS_PATH)
        Gtk.StyleContext.add_provider_for_screen (
            Gdk.Screen.get_default(),
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)



def main():
    win = SeparatorWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
