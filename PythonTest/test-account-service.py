"""
Test libAccountsService
"""
#!/usr/bin/python3
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AccountsService', '1.0')
from gi.repository import Gtk, AccountsService


class MyWindow(Gtk.Window):
    """a simple GtkWindow instance"""

    def __init__(self):
        Gtk.Window.__init__(self, title="testAccountsService")

        self.box = Gtk.Box(spacing=20)
        self.set_default_size(100, 100)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Run")
        self.button1.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.account_service = AccountsService.UserManager.get_default()

    def on_button_clicked(self, widget):
        """Callback
        callback for button click
        """
        users = self.account_service.list_users()
        for user in users:
            if user.get_automatic_login():
                print("%s is automatic login in" % user.get_real_name())
            else:
                print("%s not automatic login." % user.get_real_name())


W = MyWindow()
W.connect("delete-event", Gtk.main_quit)
W.show_all()
Gtk.main()
