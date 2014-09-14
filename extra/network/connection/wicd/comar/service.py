from comar.service import *

serviceType = "local"
serviceDesc = _({
    "en": "Wicd Connection Manager",
    "tr": "Wicd Ağ Yöneticisi"})

serviceDefault = "on"

@synchronized
def start():
    loadEnvironment()
    startService(command="/usr/sbin/wicd",
                 pidfile="/run/wicd/wicd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/wicd/wicd.pid",
                donotify=True)

def status():
    return isServiceRunning("/run/wicd/wicd.pid")
