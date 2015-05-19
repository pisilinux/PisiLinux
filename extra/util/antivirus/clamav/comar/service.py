# -*- coding: utf-8 -*-
import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Clam Anti-Virus Daemon",
                 "tr": "Clam Antivirüs Servisi"})

@synchronized
def start():
    #if config.get("DAZUKO_SUPPORT", "no") == "yes":
    #            call("System.Service.start", "dazuko")

    startService(command="/usr/sbin/clamd",
            chuid="clamav",
            pidfile="/run/clamav/clamd.pid",
            donotify=False)
    time.sleep(3)
    startService(command="/usr/bin/freshclam",
            args="-d -p /run/clamav/freshclam.pid",
            chuid="clamav",
            pidfile="/run/clamav/freshclam.pid",
            donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/clamd",
                        donotify=True)
    time.sleep(4)
    stopService(command="/usr/bin/freshclam",
                        donotify=True)
    #if config.get("DAZUKO_SUPPORT", "no") == "yes":
    #    call("System.Service.stop", "dazuko")

def status():
    return isServiceRunning("/run/clamav/clamd.pid") and isServiceRunning("/run/clamav/freshclam.pid")
