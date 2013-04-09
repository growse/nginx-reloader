#!/usr/bin/python

import psutil
import pyinotify
import os
import signal

class EventHandler(pyinotify.ProcessEvent):
    def process_default(self, event):
        if event.name.endswith(".conf"):
            pid = get_nginx_pid()
            os.kill(pid, signal.SIGHUP)
            print 'Sent HUP to {}'.format(pid)


def get_nginx_pid():
    return [p.pid for p in psutil.process_iter() if "nginx: master process" in str(p.cmdline)][0]

wm = pyinotify.WatchManager()
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
mask = pyinotify.IN_DELETE | pyinotify.IN_CLOSE_WRITE
wm.add_watch('/var/www', mask, rec=True)
notifier.loop()
