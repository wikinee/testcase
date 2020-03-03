#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import time
import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super(MyHandler, self).__init__()

    def on_created(self, event):
        print("Started: %s" % event.src_path)
        if event.src_path[-4:] == '.iso':
            print("1==>> %f" % os.path.getsize(event.src_path))
            time.sleep(2)
            print("2==>> %f" % os.path.getsize(event.src_path))

    def on_modified(self, event):
        print("Finished")


if __name__ == "__main__":
    path = '/home/yongliang/Backup'
    event_handler = MyHandler()
    observer = Observer()
    try:
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
    except OSError:
        print('Path is not a directory')
    else:
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()