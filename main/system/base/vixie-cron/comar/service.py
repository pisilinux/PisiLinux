from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Cron Task Scheduler",
                 "tr": "Cron Görev Zamanlayıcı"})
serviceDefault = "on"

@synchronized
def start():
    startService(command="/usr/sbin/cron",
                 pidfile="/var/run/cron.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/cron.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/cron.pid")
