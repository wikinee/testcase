"""Test Encoding
Test encoding transfer in Python3
"""
#!/usr/bin/python3
# -*- coding:utf-8 -*-

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class TestEncoding(Gtk.Window):
    """Test Encoding
    This Test Case will encoding human readings to GB18030
    """
    def __init__(self):
        Gtk.Window.__init__(self, title="Test Encoding")
        self.set_border_width(9)
        self.set_default_size(600, 200)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_max_length(10)
        vbox.pack_start(self.entry, False, True, 0)
        self.encoding_label = Gtk.Label("TEST ENCDOE")
        self.encoding_label.set_width_chars(10)
        self.encoding_label.set_line_wrap(True)
        self.entry.connect("changed", self.update_gb18030_label)

        self.gb18030_label = Gtk.Label()
        vbox.pack_start(self.gb18030_label, True, True, 0)

    def update_gb18030_label(self, widget):
        """GtkEntry changed callback"""
        text = widget.get_text()
        encodes_bytes = text.encode(encoding='gb18030', errors='strict')
        encodes = str(encodes_bytes)
        print(encodes.split('\\x'))
        self.gb18030_label.set_text(encodes)


def main():
    """main func"""
    win = TestEncoding()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


# test
if __name__ == '__main__':
    main()
