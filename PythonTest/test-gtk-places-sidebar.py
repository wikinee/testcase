#!/usr/bin/env python3
#
# created: 18/11/22
# author: wikinee
# first relase: 16/7/11
TITLE = "PlacesSidebar"
DESCRIPTION = """
A Gtk widget used in GtkFileChooser
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class PlacesSidebarWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Test PlaceSidebarWindow")
        self.set_size_request(200, 200)
        widget = Gtk.PlacesSidebar()
        widget.props.show_enter_location = True
        widget.props.show_other_locations = True
        widget.props.populate_all = True
        widget.connect("show-other-locations-with-flags",
            self.on_open_location)
        self.add(widget)

    def on_open_location(self, placesidebar, flags):
        print("hello")
        location = placesidebar.get_location()


def main():
    win = PlacesSidebarWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
