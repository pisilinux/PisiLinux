serviceType = "local"
serviceDesc = _({"en": "Connection Tracking Daemon",
                 "tr": "Bağlantı İzleme Sunucusu"})

import os
from comar.service import *

@synchronized
def start():
    os.system("modprobe -q nf_conntrack")
    os.system("modprobe -q nf_conntrack_ipv4")
    os.system("modprobe -q nf_conntrack_netlink")

    startService(command="/usr/sbin/conntrackd",
                 args="-d",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/conntrackd",
                args="-k",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/sbin/conntrackd")
