#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Ntop web service daemon",
                 "tr": "Ntop web servisi"})

from comar.service import *

@synchronized
def start():
    startService("/usr/bin/ntop",
                 args="@/etc/conf.d/ntop",
                 donotify=True
                 )

@synchronized
def stop():
    stopService(pidfile="/var/run/ntop.pid")

def status():
    return isServiceRunning("/var/run/ntop.pid")
