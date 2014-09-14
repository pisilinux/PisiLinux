# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "script"
serviceDesc = _({"en": "Serial Port Modifier",
                 "tr": "Seri Port Değiştirici"})

MSG_ERR_STRTSRVC = {"en": "Couldn't start service.",
                    "tr": "Servis başlatılamadı.",
                    }

def start():
    try:
        f = file("/etc/serial.conf")
        d = [a.lstrip() for a in f]
        d = filter(lambda x: not (x.startswith("#") or x == ""), d)
        f.close()

        for k in d:
            ret = run("/bin/setserial -b %s" % k)
            if ret != 0:
                fail("Error setting %s" % k)
        notify("System.Service", "Changed", (script(), "started"))
    except:
        fail(_(MSG_ERR_STRTSRVC))

def stop():
    notify("System.Service", "Changed", (script(), "stopped"))
