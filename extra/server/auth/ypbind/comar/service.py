# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "NIS Bind Service",
                 "tr": "Ağ Bilgi Sunucusu Bağlantı Servisi"})

MSG_ERR_NONISDOMAIN = _({"en": 'NISDOMAIN is not set. You can set it via "domainname NISDOMAIN".',
                         "tr": 'NISDOMAIN atanmamış. "domainname NISDOMAIN" komutuyla atayabilirsiniz.',
                         })

PIDFILE = "/run/ypbind.pid"

@synchronized
def start():
    startDependencies("rpcbind")

    # Search for domainname
    DOMAINNAME = subprocess.Popen("domainname", stdout=subprocess.PIPE).stdout.read().strip()
    if not DOMAINNAME or DOMAINNAME == "(none)":
        fail(MSG_ERR_NONISDOMAIN)

    startService(command="/usr/sbin/ypbind",
                 args=config.get("YPBIND_OPTS", ""),
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink("/var/yp/binding")
    except OSError:
        pass

def status():
    return isServiceRunning(PIDFILE)
