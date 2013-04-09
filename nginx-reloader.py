#!/usr/bin/python

import pyinotify

wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm)
wm.add_watch('/var/www', pyinotify.ALL_EVENTS)
notifier.loop()
