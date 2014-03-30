# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "System Message Logger",
                 "tr": "Sistem Günlükleme Hizmeti"})
serviceDefault = "on"

PIDFILE = "/run/syslogd.pid"

@synchronized
def start():
    startService(command="/usr/bin/rsyslogd",
                 args=config.get("SYSLOGD_OPTIONS", "-c 4"),
                 pidfile=PIDFILE,
                 detach=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)
