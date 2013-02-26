# -*- coding: utf-8 -*-
serviceType = "server"
serviceDesc = _({"en": "Icecream Daemon",
                 "tr": "Icecream Servisi"})

from comar.service import *

@synchronized
def start():
    startService(command="/opt/icecream/sbin/iceccd",
                 args="-d -m 5 > /dev/null",
                 pidfile="/var/run/iceccd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/iceccd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/iceccd.pid")