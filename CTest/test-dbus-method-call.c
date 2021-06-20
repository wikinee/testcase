#include <glib-object.h>
#include <glib.h>
#include <gio/gio.h>

int main (void)
{
    GDBusConnection *connection = NULL;
    GError *error = NULL;

    connection = g_bus_get_sync (G_BUS_TYPE_SESSION, NULL, &error);

    GDBusProxy* proxy = g_dbus_proxy_new_sync(connection, 0, NULL,
                                              "org.freedesktop.Notifications",
                                              "/org/freedesktop/Notifications",
                                              "org.freedesktop.Notifications", NULL, NULL);

    GVariant *value = g_dbus_proxy_call_sync(proxy, "GetCapabilities", NULL, 0, -1, NULL, &error);

    if (value == NULL) {
        g_print ("\n FALSE! \n");
        return 0;
    }

    g_print ("\n OK(%s)! \n", g_variant_print(value, TRUE));
    return 1;
}