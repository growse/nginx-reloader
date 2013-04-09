#!/usr/bin/python

import pyinotify


class EventHandler(pyinotify.ProcessEvent):
    def process_default(self, event):
        if event.name.endswith(".conf"):
            print event

wm = pyinotify.WatchManager()
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_CLOSE_WRITE
wm.add_watch('/var/www', mask, rec=True)
notifier.loop()
