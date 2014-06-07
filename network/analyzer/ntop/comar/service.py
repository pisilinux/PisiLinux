#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Ntop web service daemon",
                 "tr": "Ntop web servisi"})

from comar.service import *
import os

PIDFILE="/run/ntop.pid"

@synchronized
def start():
    os.system("ln -s /var/lib/ntop/ntop.pid /run/ntop.pid")
    startService("/usr/bin/ntop",
                 args="-w 3000 -d",
                 pidfile=PIDFILE,       
                 donotify=True
                 )

@synchronized
def stop():
    os.system("killall ntop")
    stopService(pidfile="/var/lib/ntop/ntop.pid")

def status():
    return isServiceRunning("/run/ntop.pid")
