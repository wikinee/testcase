#include <stdio.h>
#include <sys/statvfs.h>

int main(int argc, char **argv){

    struct statvfs fs_usage;
    statvfs(argv[1],&fs_usage);
    printf("%s:%f MageBytes available, %f bytes used, %f MageBytes free\n",argv[1],
                fs_usage.f_frsize * (double)fs_usage.f_bavail / 1024 / 1024,
                fs_usage.f_frsize * (double)(fs_usage.f_blocks - fs_usage.f_bfree),
                fs_usage.f_frsize * (double)fs_usage.f_bfree  / 1024 / 1024);
    return 0;
}