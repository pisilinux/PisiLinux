from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Distributed IRC Core",
                 "tr": "Dağıtımlı IRC Çekirdeği"})
serviceDefault = "off"

pidfile = "/run/quasselcore.pid"
datadir = "/var/cache/quassel"

@synchronized
def start():
    startService(command="/usr/bin/quasselcore",
                 args="--datadir=%s" % datadir,
                 chuid="quasselcore:quassel",
                 makepid=True,
                 detach=True,
                 pidfile=pidfile,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidfile,
                donotify=True)

def status():
    return isServiceRunning(pidfile)
