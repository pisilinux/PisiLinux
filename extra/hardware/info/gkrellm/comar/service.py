# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "GNU Krell Monitor Daemon",
                 "tr": "GNU Krell Sistem Takip Servisi"})

PIDFILE = "/run/gkrellmd.pid"

@synchronized
def start():
    startService(command="/usr/bin/gkrellmd",
                 pidfile=PIDFILE,
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    if os.path.exists(PIDFILE):
        os.unlink(PIDFILE)

def status():
    return isServiceRunning(PIDFILE)
