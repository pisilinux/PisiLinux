#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Icecast Daemon",
                 "tr": "Icecast Servisi"})

@synchronized
def start():
    startService(command="/usr/bin/icecast",
                 args="-c /etc/icecast/icecast.xml",
                 pidfile="/run/icecast/icecast.pid",
                 donotify=True,
                 detach=True)
@synchronized
def stop():
    stopService(pidfile="/run/icecast/icecast.pid",
                donotify=True)

def status():
    return isServiceRunning("/run/icecast/icecast.pid")

def reload():
    stopService(command="/usr/bin/icecast",
                args="reload")
