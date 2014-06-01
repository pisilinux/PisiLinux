#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Ntop web service daemon",
                 "tr": "Ntop web servisi"})

from comar.service import *
import os

os.system("ln -s /var/lib/ntop/ntop.pid /run/ntop.pid")

@synchronized
def start():
    startService("/usr/bin/ntop",
                 args="-w 3000 -d",
                 donotify=True
                 )

@synchronized
def stop():
    stopService(pidfile="/run/ntop.pid")

def status():
    return isServiceRunning("/run/ntop.pid")
