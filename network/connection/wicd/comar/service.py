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
                 pidfile="/var/run/wicd/wicd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/wicd/wicd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/wicd/wicd.pid")
