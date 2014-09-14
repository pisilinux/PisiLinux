from comar.service import *
import os

serviceType = "local"
serviceDesc = _({
    "en": "Color Management Daemon",
    "tr": "Renk Yönetimi Servisi",
})
serviceDefault = "on"

pidFile = "/run/colord.pid"

@synchronized
def start():
    startService(command="/usr/libexec/colord",
                 pidfile=pidFile,
                 makepid=True,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidFile,
                donotify=True)
    os.unlink(pidFile)

def status():
    return isServiceRunning(pidFile)
 
