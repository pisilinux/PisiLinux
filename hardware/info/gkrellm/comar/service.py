# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "GNU Krell Monitor Daemon",
                 "tr": "GNU Krell Sistem Takip Servisi"})

@synchronized
def start():
    startService(command="/usr/bin/gkrellmd",
                 pidfile="/var/run/gkrellmd.pid",
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/gkrellmd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/gkrellmd.pid")
