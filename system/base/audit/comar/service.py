# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "AUDIT Daemon",
                 "tr": "AUDIT Servisi"})
serviceDefault = "on"

@synchronized
def start():
    reply = startService(command="/usr/sbin/auditd",
                         pidfile="/run/auditd.pid",
                         donotify=True)
    if reply == 0:
        run("/usr/sbin/auditctl -R /etc/audit/rules.d/audit.rules")

@synchronized
def stop():
    stopService(pidfile="/run/auditd.pid",
                        donotify=True)
    run("/usr/sbin/auditctl -D")

def status():
    return isServiceRunning("/run/auditd.pid")
