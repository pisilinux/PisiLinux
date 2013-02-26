# -*- coding: utf-8 -*-
import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "RPCbind Daemon",
                 "tr": "RPCbind Servisi"})

serviceConf = "rpcbind"

PIDFILE = "/var/run/rpcbind.pid"

@synchronized
def start():
    startService(command="/sbin/rpcbind",
                 args="-f %s" % config.get("RPCBIND_OPTS"),
                 makepid=True,
                 detach=True,
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except OSError:
        pass

def status():
    return isServiceRunning(PIDFILE)
