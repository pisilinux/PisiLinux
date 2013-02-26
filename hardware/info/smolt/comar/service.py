#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *
import os

serviceType = "script"
serviceDesc = _({"en": "Smolt Monthly Checkin",
                 "tr": "Smolt Aylık Kontrol"})

LOCKFILE = "/var/lock/subsys/smolt"

def start():
    startDependencies("vixie_cron")

    startService(command="/bin/touch",
                 args="%s" % LOCKFILE,
                 donotify=True)

def stop():
    if os.path.exists(LOCKFILE):
        stopService(command="/bin/rm",
                    args="%s" % LOCKFILE,
                    donotify=True)

def status():
    return os.path.exists(LOCKFILE)
