# -*- coding: utf-8 -*-
from comar.service import *

import os

serviceType = "server"
serviceDesc = _({"en": "NTP Daemon",
                 "tr": "NTP Hizmeti"})
serviceConf = "ntpd"

PIDFILE = "/run/ntpd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/ntpd",
                 args=config.get("OPTIONS", "-u ntp:ntp -p %s -g" % PIDFILE),
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    if os.path.exists(PIDFILE):
        os.unlink(PIDFILE)

def status():
    return isServiceRunning(pidfile=PIDFILE)
