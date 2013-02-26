# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "TFTP Daemon",
                 "tr": "TFTP Servisi"})

@synchronized
def start():
    startService(command="/usr/sbin/in.tftpd",
                 args="-u nobody -s -l /tftpboot",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/in.tftpd",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/sbin/in.tftpd")
