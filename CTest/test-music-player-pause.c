/* gcc test-pause.c -o test_pause `pkg-config --libs --cflags gio-2.0 glib-2.0` */
#include <stdlib.h>
#include <glib.h>
#include <gio/gio.h>

#define MEDIA_PLAYER_RHYTHMBOX "org.mpris.MediaPlayer2.rhythmbox"
#define MEDIA_PLAYER_SPOTIFY "org.mpris.MediaPlayer2.spotify"
#define MEDIA_PLAYER_OBJECT_PATH "/org/mpris/MediaPlayer2"
#define MEDIA_PLAYER_INTERFACE "org.mpris.MediaPlayer2.Player"

/* add by wikinee, pause media player before suspend */
static void
pause_play_switch (const gchar *media_player_name,
                   const gchar *media_player_bus_name,
                   const gchar *wanted_status,
                   const gchar *method_name) {
    GDBusProxy *proxy;
    GError *error = NULL;
    gchar *play_back_status = NULL;
    GVariant *status_variant = NULL;

    proxy = g_dbus_proxy_new_for_bus_sync (G_BUS_TYPE_SESSION,
                                           G_DBUS_PROXY_FLAGS_NONE,
                                           NULL,
                                           media_player_bus_name,
                                           MEDIA_PLAYER_OBJECT_PATH,
                                           MEDIA_PLAYER_INTERFACE,
                                           NULL,
                                           &error);
    if (error) {
        g_print ("Get MediaPlayer2 Proxy failed, because: %s\n", error->message);
        g_error_free (error);
    } else {
        status_variant = g_dbus_proxy_get_cached_property (proxy, "PlaybackStatus");
        if (status_variant != NULL) {
            play_back_status = (gchar *)g_variant_get_string (status_variant, NULL);

            g_print ("\nplay_back_status:%s\n", play_back_status);
            if (play_back_status == NULL || g_strcmp0 (play_back_status, wanted_status) != 0) {
                g_print ("%s PlaybackStatus is null or not %s, do nothing\n", media_player_name, wanted_status);
                return;
            }

            g_dbus_proxy_call_sync (proxy,
                                    method_name,
                                    NULL,
                                    G_DBUS_CALL_FLAGS_NONE,
                                    -1,
                                    NULL,
                                    &error);

            if (error) {
                g_print ("org.mpris.MediaPlayer2.Player method %s called failed\n", method_name);
                g_error_free (error);
            }
        } else {
            g_print ("%s cannot lookup property PlaybackStatus, maybe player not open\n", media_player_name);
        }
    }
}

int main(int argc, char const *argv[])
{
    /* code */
    pause_play_switch ("Rhythmbox", MEDIA_PLAYER_RHYTHMBOX, "Playing", "Pause");
    // pause_play_switch ("Spotify", MEDIA_PLAYER_SPOTIFY, "Playing", "Pause");
    // sleep(7);
    // pause_play_switch ("Rhythmbox", MEDIA_PLAYER_RHYTHMBOX, "Paused", "Play");
    return 0;
}
