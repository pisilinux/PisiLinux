# -*- coding: utf-8 -*-
from comar.service import *

import os

serviceType = "server"
serviceDesc = _({"en": "Network Block Device (NBD) Server",
                 "tr": "Ağ Blok Aygıtı (NBD) Sunucusu"})
serviceDefault = "off"


NBDBIN = "/usr/bin/nbd-server"
NBDCONF = "/etc/nbd-server/config"
PIDFILE = "/run/nbd-server.pid"

@synchronized
def start():
    startService(command=NBDBIN,
                 pidfile=PIDFILE,
                 detach=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)

