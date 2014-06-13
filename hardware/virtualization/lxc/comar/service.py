from comar.service import *

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "LXC Management Service",
                 "tr": "LXC Yönetim Hizmeti"})

pidfile="/run/lxc.pid"

@synchronized
def start():
    startService(command="/usr/bin/lxc-start",
                 args="-d -n",
                 pidfile=pidfile,
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/lxc-stop",
                args="-n",
                pidfile=pidfile,
                donotify=True)

def status():
    return isServiceRunning(pidfile)
