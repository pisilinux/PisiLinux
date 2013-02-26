# -*- coding: utf-8 -*-
from comar.service import *
import signal

serviceType = "server"
serviceDesc = _({"en": "eXtended InterNET Services Daemon",
                 "tr": "Genişletilmiş İnternet Hizmetleri Servisi (xinetd)"
                 })
serviceDefault = "off"

@synchronized
def start():
    startService(command="/usr/sbin/xinetd",
                 args="-pidfile /var/run/xinetd.pid -stayalive -reuse",
                 pidfile="/var/run/xinetd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/xinetd.pid",
                donotify=True)

def reload():
    stopService(command="/usr/sbin/xinetd",
                signal=signal.SIGHUP)

def status():
    return isServiceRunning("/var/run/xinetd.pid")
