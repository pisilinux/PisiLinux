# -*- coding: utf-8 -*-
from comar.service import *

serviceType="server"
serviceDesc = _({"en": "Mediatomb uPnP Media Server",
                 "tr": "Mediatomb Tak-kullan (uPnP) Ortam Sunucusu"})

@synchronized
def start():
    startService(command="/usr/bin/mediatomb",
                 args=config.get("MEDIATOMB_OPTS", ""),
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/mediatomb/mediatomb.pid",
                donotify=True)

    try:
        os.unlink("/run/mediatomb/mediatomb.pid")
    except:
        pass

def status():
    return isServiceRunning("/run/mediatomb/mediatomb.pid")

