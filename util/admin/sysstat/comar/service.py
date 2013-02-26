# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "System activity data collector",
                 "tr": "Sistem etkinliği veri toplayıcısı"})

MSG_ERR_FAILSYST = _({"en": "Sysstat failed.",
                      "tr": "Sysstat başarısız oldu."})

CRON_FILE = '/etc/cron.d/sysstat'

def check_log():
    if not os.path.exists("/var/log/sa/sa21"):
        run("/usr/lib/sa/sadc -F -L -")

@synchronized
def start():
    check_log()
    startDependencies("vixie_cron")
    if run("/usr/lib/sa/sa1 --boot -S DISK") == 0:
        if not os.path.lexists(CRON_FILE):
            os.symlink("/etc/sysstat/sysstat.crond", CRON_FILE)
        notify("System.Service", "Changed", (script(), "started"))
    else:
        fail(MSG_ERR_FAILSYST)

@synchronized
def stop():
    if run("rm -f /etc/cron.d/sysstat") == 0:
        notify("System.Service", "Changed", (script(), "stopped"))
    else:
        fail(MSG_ERR_FAILSYST)

@synchronized
def status():
    return os.access(CRON_FILE, os.F_OK)
