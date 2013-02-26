# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"

serviceDesc = _({"en": "vsFTP Server",
                 "tr": "vsFTP Sunucusu"})

@synchronized
def start():
    startService(command="/usr/sbin/vsftpd",
                 args="/etc/vsftpd/vsftpd.conf",
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/vsftpd",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/sbin/vsftpd")
