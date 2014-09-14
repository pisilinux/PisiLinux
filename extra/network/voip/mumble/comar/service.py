# -*- coding: utf-8 -*-
from comar.service import *

serviceType="server"

serviceDesc = _({"en": "Mumble VoIP Server",
                 "tr": "Mumble VoIP Sunucusu"})

PIDFILE = "/run/murmurd.pid"
INIFILE = "/etc/mumble-server.ini"

@synchronized
def start():
    startService(command="/usr/sbin/murmurd",
                 args="-ini %s" % INIFILE,
                 pidfile=PIDFILE,
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/murmurd",
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except:
        pass

def status():
    return isServiceRunning(command="/usr/sbin/murmurd")
