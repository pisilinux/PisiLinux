# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "ACPI Daemon",
                 "tr": "ACPI Hizmeti"})
serviceDefault = "on"

PIDFILE = "/run/acpid.pid"

MSG_NO_PIDFILE = _({
                    "en" : "Could not reload acpid daemon as the PID file %s does not exist." % PIDFILE,
                    "tr" : "%s PID dosyası mevcut olmadığından acpid hizmeti yeniden yüklenemiyor." % PIDFILE,
                   })

@synchronized
def start():
    startService(command="/usr/sbin/acpid",
                 args=config.get("OPTIONS", ""),
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def reload():
    import signal
    import os
    try:
        os.kill(int(open(PIDFILE, "r").read().strip()), signal.SIGHUP)
    except:
        fail(MSG_NO_PIDFILE)

def status():
    return isServiceRunning(pidfile=PIDFILE)
