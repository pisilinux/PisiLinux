from comar.service import *
import os

serviceType = "server"
serviceDefault = "on"
serviceDesc = _({"en": "CUPS Printer Server",
                 "tr": "CUPS Yazıcı Sunucusu"})
serviceConf = "cups"

PIDFILE = "/run/cups/cupsd.pid"

@synchronized
def start():
    # FIXME: After avahi before hal
    startDependencies("avahi")

    # Load ppdev and lp drivers if wanted
    if config.get("LOAD_LP_MODULE") == "yes":
        os.system("/sbin/modprobe -q lp")
        os.system("/sbin/modprobe -q ppdev")

    startService(command="/usr/sbin/cupsd",
                 donotify=True)
    os.system("pidof -o %PPID /usr/sbin/cupsd > " + PIDFILE)

    # Tell udevd to replay printer events
    # One for low-level usb
    os.system("udevadm trigger --subsystem-match=usb \
                               --attr-match=bInterfaceClass=07 \
                               --attr-match=bInterfaceSubClass=01 \
                               --action=add")
    # One for usblp backend
    os.system("udevadm trigger --subsystem-match=usb \
                               --property-match=DEVNAME=\"/dev/usb/lp*\" \
                               --action=add")


@synchronized
def reload():
    if os.path.exists(PIDFILE):
        # 1 is SIGHUP
        os.kill(int(open(PIDFILE, "r").read().strip()), 1)

@synchronized
def stop():
    stopService(pidfile=PIDFILE, donotify=True)
    if os.path.isfile(PIDFILE): os.unlink(PIDFILE)

def status():
    return isServiceRunning(pidfile=PIDFILE)
