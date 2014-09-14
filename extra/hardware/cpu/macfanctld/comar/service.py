from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "macfanctld Service",
                 "tr": "macfanctld Hizmeti"})
serviceDefault = "on"

PIDFILE="/run/macfanctld.pid"
DAEMON = "/usr/bin/macfanctld"

@synchronized
def start():
    startService(command=DAEMON,
                 args=" -f",
                 donotify=True)
    os.system("pidof -o %PPID " + "%s > %s" % (DAEMON, PIDFILE))

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except:
        pass

def status():
    return isServiceRunning(pidfile=PIDFILE)
