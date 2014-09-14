# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Gnokii SMS daemon",
                 "tr": "Gnokii Kısa Mesaj servisi"})
serviceDefault = "off"
serviceConf = "gnokii-smsd"

@synchronized
def start():
    startService(command="/usr/bin/smsd",
                 args="%s --logfile %s" % (config.get("SMSD_OPTS", ""),
                                           config.get("SMSD_LOG", "/var/log/smsd.log")),
                 pidfile="/run/smsd.pid",
                 detach=True)

@synchronized
def stop():
    stopService(command="/usr/bin/smsd",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/bin/smsd")
