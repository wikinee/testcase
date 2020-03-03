#!/usr/bin/env python3
# Created by xiaosanyu at 16/6/16
# section 088
TITLE = "IconView"
DESCRIPTION = """
Gtk.IconView provides an alternative view on a Gtk.TreeModel.
It displays the model as a grid of icons with labels. Like Gtk.TreeView
"""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf

icons = ["edit-cut", "edit-paste", "edit-copy"]


class IconViewWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)

        liststore = Gtk.ListStore(Pixbuf, str)
        iconview = Gtk.IconView.new()
        iconview.set_model(liststore)
        iconview.set_pixbuf_column(0)
        iconview.set_text_column(1)
        iconview.set_item_padding(0)

        theme = Gtk.IconTheme.get_default()
        # print(theme.get_search_path())
        for icon in icons:
            if theme.has_icon(icon):
                pixbuf = theme.load_icon(icon, 48, 0)
            liststore.append([pixbuf, "Label"])

        self.add(iconview)


def main():
    win = IconViewWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()