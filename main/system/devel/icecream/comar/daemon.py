# -*- coding: utf-8 -*-
serviceType = "server"
serviceDesc = _({"en": "Icecream Daemon",
                 "tr": "Icecream Servisi"})

from comar.service import *

@synchronized
def start():
    startService(command="/opt/icecream/sbin/iceccd",
                 args="-d -m 5 > /dev/null",
                 pidfile="/run/iceccd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/iceccd.pid",
                donotify=True)

def status():
    return isServiceRunning("/run/iceccd.pid")