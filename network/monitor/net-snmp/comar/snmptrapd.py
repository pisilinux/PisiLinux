# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Simple Network Management Protocol (SNMP) Trap Daemon",
                 "tr": "Simple Network Management Protocol (SNMP) Trap Servisi"})
serviceConf = "snmptrapd"

pidfile = "/run/snmptrapd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/snmptrapd",
                args="-p %s %s"  % (pidfile, config.get("SNMPTRAPD_FLAGS", "")),
                pidfile=pidfile,
                donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidfile, donotify=True)

def status():
    return isServiceRunning(pidfile)
