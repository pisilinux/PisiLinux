# -*- coding: utf-8 -*-
serviceType = "server"
serviceDesc = _({"en": "RSync Daemon",
                 "tr": "RSync Servisi"})
serviceConf = "rsyncd"

from comar.service import *

@synchronized
def start():
    startService(command="/usr/bin/rsync",
                 args="--daemon %s" % config.get("RSYNC_OPTS", ""),
                 pidfile="/var/run/rsyncd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/rsyncd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/rsyncd.pid")
