#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Nginx Web Server",
                 "tr": "Nginx Web Sunucusu"})

from comar.service import *

@synchronized
def start():
    startService(command="/usr/sbin/nginx",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/nginx.pid",
                donotify=True)

def status():
    return isServiceRunning("/run/nginx.pid")
