# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "USB over IP daemon",
                 "tr": "IP üzerinden USB hizmeti"})
serviceDefault = "off"

PIDFILE = "/var/run/usbipd.pid"

MSG_MODULE_ERROR = _({
        "en" : "The kernel module usbip.ko can not be loaded.",
        "tr" : "usbip.ko çekirdek sürücüsü yüklenemedi.",
        })


@synchronized
def start():
    # Check for kernel modules
    if not os.path.exists("/sys/modules/usbip"):
        retval = os.system("/sbin/modprobe -q usbip")
        if retval > 0:
            fail(MSG_MODULE_ERROR)

    try:
        os.unlink(PIDFILE)
    except OSError:
        pass

    startService(command="/usr/bin/usbipd",
                 pidfile=PIDFILE,
                 detach=True,
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except OSError:
        pass

def status():
    return isServiceRunning(PIDFILE)
