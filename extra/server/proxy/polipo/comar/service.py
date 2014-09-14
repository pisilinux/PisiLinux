from comar.service import *
import os

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "Polipo Proxy Server",
                 "tr": "Polipo Vekil Sunucusu"})

PIDFILE = "/run/polipo/polipo.pid"
LOGFILE = "/var/log/polipo"

@synchronized
def start():
    startService(command="/usr/bin/polipo",
                 args="-c /etc/polipo/config -- logFile=%s pidFile=%s daemonise=true" % (LOGFILE, PIDFILE),
                 chuid="polipo:polipo",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except OSError:
        pass

def restart():
    stop()
    start()

def reload():
    stopService(pidfile=PIDFILE,
                signalno=10,
                chuid="polipo:polipo",
                donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)
