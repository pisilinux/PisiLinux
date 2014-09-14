# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "InfraRed Controller Manager",
                 "tr": "Kızılötesi Denetleyici Yöneticisi"})

lircdpid = "/var/run/lirc/lircd.pid"

@synchronized
def start():
    lircmodule = config.get("LIRC_MODULE", "")
    if lircmodule != "":
        run("modprobe %s" % lircmodule)

    reply = startService(command="/usr/sbin/lircd",
                         args=config.get("LIRCD_OPTS", ""),
                         pidfile=lircdpid,
                         donotify=True)

    if reply == 0 and config.get("USE_LIRCMD", "no") == "yes":
        startService(command="/usr/sbin/lircmd")

@synchronized
def stop():
    reply = stopService(pidfile=lircdpid,
                        donotify=True)

    if config.get("USE_LIRCMD", "no") == "yes":
        stopService(command="/usr/sbin/lircmd")

def status():
    return isServiceRunning(lircdpid)
