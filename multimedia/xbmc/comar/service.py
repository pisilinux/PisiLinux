# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "XBMC Daemon",
                 "tr": "XBMC Hizmeti"})

pidfile = "/var/run/xbmc.pid"

@synchronized
def start():
    startService(command="/usr/bin/xinit",
                 args="/usr/bin/xbmc",
                 pidfile=pidfile,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidfile,
                donotify=True)

def status():
    return isServiceRunning(pidfile)
