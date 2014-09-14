# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Cyrus-SASL Daemon",
                 "tr": "Cyrus-SASL Servisi"})
serviceConf = "saslauthd"

SOCKETDIR = "/run/saslauthd"
PIDFILE = "/run/saslauthd/saslauthd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/saslauthd",
                 args="-m %s %s" % (SOCKETDIR, config.get("SASLAUTHD_OPTS", "")),
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
