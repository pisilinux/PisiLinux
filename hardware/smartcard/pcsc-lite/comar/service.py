from comar.service import *

serviceType = "local"
serviceDefault = "on"
serviceDesc = _({"en": "PC/SC SmartCard Reader Service",
                 "tr": "PC/SC Akıllı Kart Okuyucu Servisi"})

PIDFILE = "/var/run/pcscd/pcscd.pid"

@synchronized
def start():
    # pcscd wont start if these exist
    import os
    try:
        os.unlink("/var/run/pcscd/pcscd.comm")
        os.unlink("/var/run/pcscd/pcscd.pub")
    except OSError:
        pass

    startService(command="/usr/sbin/pcscd",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)
