# -*- coding: utf-8 -*-
serviceType = "local"
serviceDesc = _({"en": "ATI Events Daemon",
                 "tr": "ATI Olay Servisi"})
serviceConf = "atieventsd"

from comar.service import *

@synchronized
def start():
    startService(command="/usr/sbin/atieventsd",
                 args=config.get("ATIEVENTSDOPTS", ""),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/atieventsd",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/sbin/atieventsd")
