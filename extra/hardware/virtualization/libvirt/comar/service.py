# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "libvirt virtualization API daemon",
                 "tr": "libvirt sanallaştırma hizmeti"})
serviceDefault = "on"

PIDFILE         = "/run/libvirt/libvirtd.pid"
KRB5_KTNAME     = "/etc/libvirt/krb5.tab"
LIBVIRTD_CONFIG = "/etc/libvirt/libvirtd.conf"

@synchronized
def start():
    os.environ["KRB5_KTNAME"] = config.get("KRB5_KTNAME", KRB5_KTNAME)
    os.environ["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/sbin:/usr/local/bin"

    if os.path.exists(PIDFILE):
        os.unlink(PIDFILE)

    startService(command="/usr/sbin/libvirtd",
                 args="--daemon --config %s %s --pid-file %s" % (
                     config.get("LIBVIRTD_ARGS", ""),
                     config.get("LIBVIRTD_CONFIG", LIBVIRTD_CONFIG),
                     PIDFILE,
                     ),
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/libvirt/libvirtd.pid",
                donotify=True)
    if os.path.exists(PIDFILE):
        os.unlink(PIDFILE)

@synchronized
def reload():
    if os.path.exists(PIDFILE):
        os.kill(int(open(PIDFILE, "r").read().strip()), 1)

def status():
    return isServiceRunning(pidfile=PIDFILE)
