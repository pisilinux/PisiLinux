# -*- coding: utf-8 -*-
serviceType = "local"
serviceDesc = _({"en": "Console Mouse Daemon",
                 "tr": "Konsol Fare Servisi"})

from comar.service import *

@synchronized
def start():
    args = []
    args.append("-m %s" % config.get("MOUSEDEV", "/dev/input/mice"))
    args.append("-t %s" % config.get("MOUSE", "imps2"))
    if "RESPONSIVENESS" in config:
        args.append("-r %s " % config.get("RESPONSIVENESS"))
    if "REPEAT_TYPE" in config:
        args.append("-R%s " % config.get("REPEAT_TYPE"))
    args.append(config.get("APPEND", ""))

    startService(command="/usr/sbin/gpm",
                 args=" ".join(args),
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/gpm.pid",
                donotify=True)

def status():
    return isServiceRunning("/run/gpm.pid")
