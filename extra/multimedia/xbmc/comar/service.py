# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "XBMC Daemon",
                 "tr": "XBMC Hizmeti"})

pidfile = "/run/xbmc.pid"

@synchronized
def start():
    startService(command="/usr/bin/xinit",
                 args="/usr/bin/dbus/launch --exit-with-session /usr/bin/xbmc-standalone -- :0 -nolisten tcp vt7",
                 pidfile=pidfile,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidfile,
                donotify=True)

def status():
    return isServiceRunning(pidfile)
