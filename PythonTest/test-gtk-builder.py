#!/usr/bin/python2
# *-* coding: utf-8 *-*

"""TestGlade
a example for *.glade in PyGObject
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def on_destroy_pressed(window):
    """destroy signal callback"""
    print("Destroy Window")


def on_button_pressed(button):
    """click signal callback"""
    print("Hello, World!")


builder = Gtk.Builder()
builder.add_from_file("builder_example.glade")

window = builder.get_object("window1")
window.connect("destroy", Gtk.main_quit)
builder.get_object("button1").connect("clicked", on_button_pressed)
window.show_all()

Gtk.main()
