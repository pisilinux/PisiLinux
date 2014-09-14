from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Bluetooth Service",
                 "tr": "Bluetooth Hizmeti"})
serviceDefault = "on"

PIDFILE="/run/bluez.pid"
DAEMON = "/usr/libexec/bluetooth/bluetoothd"

@synchronized
def start():
    # Work-around udev bug, bluetoothd wasn't getting enabled on coldplug
    #run("/sbin/udevadm trigger --subsystem-match=bluetooth")
    startService(command=DAEMON,
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
