from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Task Scheduler",
                 "tr": "Görev Zamanlayıcı"})
serviceDefault = "on"
serviceConf="atd"

PIDFILE = "/var/run/atd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/atd",
                 args=config.get("OPTS", ""),
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
