import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, Gdk

window = Gtk.Window(title="Hello World")
window.set_size_request(800, 600)
overlay = Gtk.Overlay()
pixbuf = GdkPixbuf.Pixbuf.new_from_file("/usr/share/backgrounds/nfs-backgrounds/nfs-1.jpg")
pixbuf = pixbuf.scale_simple(576, 324, GdkPixbuf.InterpType.BILINEAR)
image = Gtk.Image.new_from_pixbuf(pixbuf)
image_icon = Gtk.Image.new_from_icon_name("gtk-help", Gtk.IconSize.BUTTON)
overlay.add(image)
overlay.add_overlay(image_icon)
window.add(overlay)
window.show_all()
window.connect("destroy", Gtk.main_quit)
Gtk.main()