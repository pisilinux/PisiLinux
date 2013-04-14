# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Hardware Abstraction Layer",
                 "tr": "Donanım Soyutlama Katmanı (HAL)"})
serviceDefault = "on"
serviceConf = "hal"

MSG_ERR_DBUS = _({"en": "Couldn't start HAL, please ensure DBus is running.",
                  "tr": "HAL başlatılamadı, lütfen DBus'un çalışıp çalışmadığını kontrol edin",
                  })

@synchronized
def start():
    # Check DBus socket
    if not os.path.exists("/var/run/dbus/system_bus_socket"):
        fail(MSG_ERR_DBUS)

    # Ensure that acpid is launched before HAL for avoiding /proc/acpi/event
    # race conditions.
    startDependencies("acpid")

    # Some dummy hack to avoid gparted to do some stupid things
    if os.path.exists("/usr/share/hal/fdi/policy/gparted-disable-automount.fdi"):
        os.remove("/usr/share/hal/fdi/policy/gparted-disable-automount.fdi")

    startService(command="/usr/sbin/hald",
                 args=config.get("DAEMON_OPTS", "--daemon=yes --use-syslog"),
                 pidfile="/var/run/hald/pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/hald/pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/hald/pid")
