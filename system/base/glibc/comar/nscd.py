# -*- coding: utf-8 -*-
from comar.service import *

import os

serviceType = "local"
serviceDesc = _({"en": "Name Service Caching Daemon",
                 "tr": "İsim Hizmeti Önbellek Sunucusu"})
serviceDefault = "on"


MSG_ERR_STRTSRVC = {"en": "Unable to start service.",
                    "tr": "Servis başlatılamadı.",
                    }

RUNDIR = "/var/run/nscd"
DBDIR = "/var/db/nscd"

CONFFILE = "/etc/nscd.conf"
PIDFILE = "%s/nscd.pid" % RUNDIR
SOCKETFILE = "%s/socket" % RUNDIR


@synchronized
def start():
    if not os.path.exists(CONFFILE):
        fail(_(MSG_ERR_STRTSRVC))

    for i in [RUNDIR, DBDIR]:
        if not os.path.exists(i):
            os.makedirs(i, mode=0755)

    startService(command="/usr/sbin/nscd",
                 pidfile=PIDFILE,
                 detach=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    # if nscd drops priviledges it can't delete these
    for i in [PIDFILE, SOCKETFILE]:
        if os.path.exists(i):
            os.unlink(i)

def status():
    return isServiceRunning(pidfile=PIDFILE)

