from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Pyro Name Server Daemon"})
serviceConf = "pyro-nsd"

@synchronized
def start():
    startService(command="/usr/bin/pyro-nsd",
                 args="start",
                 pidfile="/var/run/pyro-nsd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/pyro-nsd",
                 args="stop",
                 pidfile="/var/run/pyro-nsd.pid",
                 donotify=True)

def status():
    return isServiceRunning("/var/run/pyro-nsd.pid")
