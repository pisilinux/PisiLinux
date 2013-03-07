from comar.service import *

import os

serviceType = "local"
serviceDesc = _({"en": "GPS Daemon",
                 "tr": "GPS Hizmeti"})
serviceDefault = "off"

@synchronized
def start():
    startService(command="/usr/sbin/gpsd",
                 args="-P /run/gpsd.pid -F /run/gpsd.sock %s %s" %
                        (config.get("OPTIONS", "-n"), config.get("DEVICE", "/dev/ttyUSB0")))

@synchronized
def stop():
    stopService(pidfile="/run/gpsd.pid", donotify=True)
    if os.path.exists("/run/gpsd.pid"):
        os.unlink("/run/gpsd.pid")

def status():
    return isServiceRunning("/run/gpsd.pid")
