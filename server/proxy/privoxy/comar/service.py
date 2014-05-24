from comar.service import *
import os

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "Privoxy Proxy Server",
                 "tr": "Privoxy Vekil Sunucusu"})

PIDFILE = "/run/privoxy.pid"

@synchronized
def start():
    startService(command="/usr/sbin/privoxy",
                 args="--pidfile %s --user privoxy /etc/privoxy/" % PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except OSError:
        pass

def status():
    return isServiceRunning(PIDFILE)
