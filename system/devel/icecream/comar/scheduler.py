serviceType = "server"
serviceDesc = _({"en": "Icecream Scheduler",
                 "tr": "Icecream Zamanlayıcı"})

from comar.service import *

@synchronized
def start():
    startService(command="/opt/icecream/sbin/scheduler",
                 args="-d > /dev/null",
                 pidfile="/var/run/scheduler.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/scheduler.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/scheduler.pid")