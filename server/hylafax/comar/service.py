# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "HylaFax Daemon",
                 "tr": "HylaFax Servisi"})

@synchronized
def start():
    reply = startService(command="/usr/sbin/faxq",
                         pidfile="/var/run/faxq.pid",
                         makepid=True,
                         donotify=True)
    if reply == 0:
        startService(command="/usr/sbin/hfaxd",
                     args="-i hylafax")

@synchronized
def stop():
    stopService(pidfile="/var/run/faxq.pid",
                donotify=True)
    stopService(command="/usr/sbin/hfaxd")

def status():
    return isServiceRunning(command="/usr/sbin/hfaxd")
