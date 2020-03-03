"""
test Pam check
"""
#!/usr/bin/python2

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk
import PAM


class MyPam(Gtk.Window):
    """pam test class"""

    def __init__(self):
        Gtk.Window.__init__(self, title="testPam")

        self.box = Gtk.Box(spacing=20)
        self.set_default_size(100, 100)
        self.add(self.box)

        self.entry = Gtk.Entry()
        self.entry.connect("focus-out-event", self._on_entry_focus_out)
        self.box.pack_start(self.entry, True, True, 0)

        self.button = Gtk.Button(label="OK")
        self.button.set_sensitive(False)
        self.box.pack_start(self.button, True, True, 0)

    def pam_conv(self, auth, query_list, user_data):
        resp = []
        for i in range(len(query_list)):
            query, typ = query_list[i]
            val = self.entry.get_text()
            if typ == PAM.PAM_PROMPT_ECHO_OFF: # pass
                resp.append((val, 0))
        return resp

    def _on_entry_focus_out(self, widget, event):
        if self.entry.get_text() != "":
            auth = PAM.pam()
            auth.start('passwd')
            auth.set_item(PAM.PAM_USER, GLib.get_user_name())
            auth.set_item(PAM.PAM_CONV, self.pam_conv)
            try:
                auth.authenticate()
                auth.acct_mgmt()
            except PAM.error, resp:
                self.button.set_sensitive(False)
                print "PAM.error:%s" % resp[0]
            except Exception:
                print "Internal error"
            else:
                print "Sucess!!"
                self.button.set_sensitive(True)
        print "return"
        return

def main():
    w = MyPam()
    w.connect("delete-event", Gtk.main_quit)
    w.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
