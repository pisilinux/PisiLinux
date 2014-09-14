# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Simple Network Management Protocol (SNMP) Daemon",
                 "tr": "Simple Network Management Protocol (SNMP) Servisi"})
serviceConf = "snmpd"

pidfile = "/run/snmpd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/snmpd",
                args="-p %s %s"  % (pidfile, config.get("SNMPD_FLAGS", "")),
                pidfile=pidfile,
                donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidfile, donotify=True)

def status():
    return isServiceRunning(pidfile)
