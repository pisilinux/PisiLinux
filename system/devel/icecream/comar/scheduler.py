serviceType = "server"
serviceDesc = _({"en": "Icecream Scheduler",
                 "tr": "Icecream Zamanlayıcı"})

from comar.service import *

@synchronized
def start():
    startService(command="/opt/icecream/sbin/icecc-scheduler",
                 args="-d > /dev/null",
                 pidfile="run/icecc-scheduler.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/icecc-scheduler.pid",
                donotify=True)

def status():
    return isServiceRunning("/run/icecc-scheduler.pid")