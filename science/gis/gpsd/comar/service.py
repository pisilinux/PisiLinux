from comar.service import *

import os

serviceType = "local"
serviceDesc = _({"en": "GPS Daemon",
                 "tr": "GPS Hizmeti"})
serviceDefault = "off"

@synchronized
def start():
    startService(command="/usr/sbin/gpsd",
                 args="-P /var/run/gpsd.pid -F /var/run/gpsd.sock %s %s" %
                        (config.get("OPTIONS", "-n"), config.get("DEVICE", "/dev/ttyUSB0")))

@synchronized
def stop():
    stopService(pidfile="/var/run/gpsd.pid", donotify=True)
    if os.path.exists("/var/run/gpsd.pid"):
        os.unlink("/var/run/gpsd.pid")

def status():
    return isServiceRunning("/var/run/gpsd.pid")
