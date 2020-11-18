#include <stdio.h>
#include <glib.h>

// gcc test-time.c -o testtime `pkg-config --libs --cflags glib-2.0`

void get_time_now () {
    GDateTime *utc = g_date_time_new_now_local ();
    gint m = g_date_time_get_microsecond (utc);
    g_print ("microsecond:%s.%d\n", g_date_time_format (utc, "%Y-%m-%d %H:%M:%S"), m);
}

int main() {
    get_time_now();
    return 0;
}
