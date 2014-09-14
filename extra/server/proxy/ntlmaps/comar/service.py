# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "NTLM Proxy Daemon",
                 "tr": "NTLM Vekil Servisi"})

PIDFILE = "/run/ntlmaps.pid"

@synchronized
def start():
    startService(command="/usr/bin/python",
                 args="/usr/bin/ntlmaps",
                 pidfile=PIDFILE,
                 makepid=True,
                 chuid="ntlmaps",
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
