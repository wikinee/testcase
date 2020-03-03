"""Test Encoding
Test encoding transfer in Python3
"""
#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class TestEncoding(Gtk.Window):
    """TestEncoding
    This test case will translate gb18030 to human readings
    """
    def __init__(self):
        """construct"""
        Gtk.Window.__init__(self, title="Test Encoding")
        self.set_border_width(9)
        self.set_default_size(600, 200)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.add(vbox)
        vbox.add(hbox)

        self.entry1_label = Gtk.Label("Label1")
        self.entry1 = Gtk.Entry()
        self.entry1.set_max_length(2)
        hbox.pack_start(self.entry1_label, False, False, 2)
        hbox.pack_start(self.entry1, False, False, 2)

        self.entry2_label = Gtk.Label("Label2")
        self.entry2 = Gtk.Entry()
        self.entry2.set_max_length(2)
        hbox.pack_start(self.entry2_label, False, False, 2)
        hbox.pack_start(self.entry2, False, False, 2)

        self.entry3_label = Gtk.Label("Label3")
        self.entry3 = Gtk.Entry()
        self.entry3.set_max_length(2)
        hbox.pack_start(self.entry3_label, False, False, 2)
        hbox.pack_start(self.entry3, False, False, 2)

        self.entry4_label = Gtk.Label("Label4")
        self.entry4 = Gtk.Entry()
        self.entry4.set_max_length(2)
        hbox.pack_start(self.entry4_label, False, False, 2)
        hbox.pack_start(self.entry4, False, False, 2)

        self.btn = Gtk.Button("OK")
        hbox.pack_start(self.btn, False, False, 2)
        self.btn.connect("clicked", self.update_gb18030_label)

        self.gb18030_label = Gtk.Label()
        vbox.pack_start(self.gb18030_label, False, False, 0)
        self.list = []

    def update_gb18030_label(self, widget):
        """Button Clicked callback"""
        text1 = self.entry1.get_text()
        text2 = self.entry2.get_text()
        text3 = self.entry3.get_text()
        text4 = self.entry4.get_text()
        is_four = True

        if text1 is None:
            self.gb18030_label.set_text("First Entry Empty")
            return

        if (text3 is '') and text4:
            self.gb18030_label.set_text("Entry3 is None, but Entry4 is not.")
            return

        if text3 and (text4 == ''):
            self.gb18030_label.set_text("Entry3 is not None, and Entry4 is.")
            return

        if (text3 == '') and (text4 == ''):
            is_four = False

        self.list = []
        try:
            a = int(text1, 16)
            if (text2 == '') and (a > 127):
                self.gb18030_label.set_text("Sigle byte word in 0x00~0x7f")
                return
            self.list.append(a)
            b = int(text2, 16)
            self.list.append(b)
            if is_four:
                c = int(text3, 16)
                self.list.append(c)
                d = int(text4, 16)
                self.list.append(d)
        except ValueError as e:
            self.gb18030_label.set_text(str(e))
            return
        except Exception as e:
            self.gb18030_label.set_text(str(e))
            return

        # print(self.list)
        sss = bytes(self.list)
        msg = sss.decode(encoding='gb18030', errors='strict')
        self.gb18030_label.set_text(msg)


# main func
def main():
    win = TestEncoding()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()


# test run
if __name__ == '__main__':
    main()
