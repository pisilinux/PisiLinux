from comar.service import *

serviceType="server"
serviceDesc = _({"en": "Avahi Server",
                 "tr": "Avahi Hizmeti"})

@synchronized
def start():
    startService(command="/usr/sbin/avahi-daemon",
                 args="-D",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/avahi-daemon",
                args="-k",
                donotify=True)

def reload():
    stopService(command="/usr/sbin/avahi-daemon",
                args="-r",
                donotify=True)

def status():
    return isServiceRunning("/run/avahi-daemon/pid")
