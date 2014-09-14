from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Network Information Server",
                 "tr": "Ağ Bilgi Sunucusu (NIS)"})

PIDFILE = "/run/ypserv.pid"

@synchronized
def start():
    startDependencies("rpcbind")
    startService(command="/usr/sbin/ypserv",
                 args=config.get("YPSERV_OPTS", ""),
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
