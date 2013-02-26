# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "InfraRed Device Manager",
                 "tr": "Kızılötesi Aygıt Yöneticisi"})
serviceConf = "irda"

MSG_ERR_IRDACNFGNOTSET = {"en": "IRDA configuration is not set.",
                          "tr": "IRDA yapılandırılmamış.",
                          }
@synchronized
def start():
    if config.get("IRDA", "") != "yes" or config.get("IRDADEV", "") == "":
        fail(_(MSG_ERR_IRDACNFGNOTSET))
    else:
        args = []
        if "DONGLE" in config:
            args.append("-d %s" % config["DONGLE"])
        if config.get("DISCOVER", "no") == "yes":
            args.append("-s")
        if "IRDADEV" in config:
            args.append(config["IRDADEV"])

        startService(command="/usr/sbin/irattach",
                     args=" ".join(args),
                     pidfile="/var/run/irattach.pid",
                     donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/irattach.pid")

def status():
    return isServiceRunning("/var/run/irattach.pid")
