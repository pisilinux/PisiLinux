#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Music Player Daemon",
                 "tr": "Müzik Çalıcı Sunucusu"})

from comar.service import *
import re
import os

PIDFILE = "/run/mpd/mpd.pid"

@synchronized
def start():
    startService(command="/usr/bin/mpd", 
                 args="/etc/mpd.conf",
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
