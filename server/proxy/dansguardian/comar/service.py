# -*- coding: utf-8 -*-
import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Dansguardian Daemon",
                 "tr": "Dansguardian Servisi"})

PIDFILE = "/run/dansguardian.pid"

@synchronized
def start():
    startDependencies("clamav")
    startService(command="/usr/sbin/dansguardian",
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/dansguardian",
                pidfile=PIDFILE,
                donotify=True)

def reload():
    stopService(command="/usr/sbin/dansguardian",
                args="-g")

def status():
    return isServiceRunning(PIDFILE)
