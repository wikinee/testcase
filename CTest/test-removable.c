// gcc -o test-removable test-removable.c `pkg-config --libs --cflags gio-2.0` 

#include<stdio.h>
#include<gio/gio.h>

// Check uuid in linux, following two methods:
// 1. ls -l /dev/disk/by-uuid
// 2. sudo blkid

int main(int argc, char const *argv[])
{
	GVolumeMonitor *monitor;
	GList *volumes, *l;
	GDrive *drive;
	gchar *name, *uuid;

	monitor = g_volume_monitor_get();
	volumes = g_volume_monitor_get_mounts(monitor);
	g_print("volumes length %d\n", g_list_length(volumes));
	for (l = volumes; l; l = l->next) {
		GMount *volume = l->data;
		name = g_mount_get_name(volume);
		drive = g_mount_get_drive(volume);
		gboolean is_removable = g_drive_is_removable(drive);
		gboolean is_media_removable = g_drive_is_media_removable(drive);
		g_print ("%s is removable? %d, is media removable? %d\n", name, is_removable, is_media_removable);
	}

	return 0;
}