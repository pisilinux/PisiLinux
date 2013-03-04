# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDefault = "off" #NM starts wpa_supp automatically. Use at your own risk if you start manually
serviceDesc = _({"en": "WPA Daemon",
                 "tr": "WPA Hizmeti"})

PIDFILE = "/run/wpa_supplicant.pid"

@synchronized
def start():
    startService(command="/usr/sbin/wpa_supplicant",
                 args="-WuB -P%s %s" % (PIDFILE, config.get("OPTS", "")),
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
