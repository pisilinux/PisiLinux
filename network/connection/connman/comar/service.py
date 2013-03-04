from comar.service import *
import os

serviceType = "local"
serviceDesc = _({
    "en": "connman Connection Manager",
    "pl": "connman Zarządca połączeń",
    "tr": "connman Ağ Yöneticisi"})

serviceDefault = "on"

@synchronized
def start():
    loadEnvironment()
    startService(command="/usr/sbin/connmand",
                 pidfile="/run/connman/connman.pid",
                 donotify=True)
    os.system("pidof -o %PPID /usr/sbin/connmand > /run/connman/connman.pid")

@synchronized
def stop():
    stopService(pidfile="/run/connman/connman.pid",
                donotify=True)

def status():
    return isServiceRunning("/run/connman/connman.pid")
