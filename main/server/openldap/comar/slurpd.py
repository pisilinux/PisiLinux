# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Slurpd Daemon",
                 "tr": "Slurpd Servisi"})

def start():
    startService(command="/usr/libexec/slurpd",
                 donotify=True)

def stop():
    stopService(command="/usr/libexec/slurpd",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/libexec/slurpd")
