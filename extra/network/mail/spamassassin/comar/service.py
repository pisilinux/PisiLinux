# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Spam detection daemon",
                 "tr": "Spam algılama servisi"})

serviceConf = "spamd"

@synchronized
def start():
    startService(command="/usr/bin/spamd",
                 args="-d -r %s %s %s" % (config.get("PIDFILE", "/run/spamd.pid"), config.get("PARAMS",""), config.get("EXTRA","")),
                 nice = int(config.get("NICELEVEL","-0")),
                 donotify=True)

@synchronized
def stop():
    stopService(config.get("PIDFILE", "/run/spamd.pid"),
                donotify=True)

def status():
    return isServiceRunning(config.get("PIDFILE", "/run/spamd.pid"))
