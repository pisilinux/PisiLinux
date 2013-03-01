# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "DHCP Daemon",
                 "tr": "DHCP Servisi"})

serviceConf = "dhcpd"

MSG_NM_NOT_RUNNING = _({"en": "NetworkManager service is not running",
                        "tr": "NetworkManager hizmeti çalışmıyor",
                       })

PIDFILE = "/run/dhcpd.pid"
TIMEOUT = config.get("TIMEOUT", 10)

@synchronized
def start():
    try:
        startDependencies("NetworkManager")
        # Prevent race condition between NM and dhcpd
        if run("/usr/bin/nm-online -q -t %s" % TIMEOUT) != 0:
            # NM is not running
            fail(MSG_NM_NOT_RUNNING)
    except:
        pass

    startService(command="/usr/sbin/dhcpd",
                 args="-cf %s %s %s" % (config.get("DHCPD_CONF", "/etc/dhcp/dhcpd.conf"), config.get("DHCPD_ARGS", ""), config.get("INTERFACES", "")),
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
