#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "FreeRadius Server",
                 "tr": "FreeRadius Sunucusu"})

ERR_CONFIG = _({"en": "Corrupted config file(s)",
                "tr": "Yapılandırma dosyası/dosyaları bozuk",
              })

serviceConf = "freeradius"

PIDFILE = "/run/radiusd/radiusd.pid"

def check_config():
    if run("/usr/sbin/radiusd", "-C"):
        fail(ERR_CONFIG)

@synchronized
def start():
    check_config()
    startService(command="/usr/sbin/radiusd",
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except OSError:
        pass

def reload():
    if os.path.exists(PIDFILE):
        os.kill(int(file(PIDFILE).read().strip()), signal.SIGHUP)

def status():
    return isServiceRunning(PIDFILE)
