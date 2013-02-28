from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "SMB Network Sharing",
                 "tr": "SMB Ağ Paylaşımı"})

WINBINDD_PIDFILE = "/run/samba/winbindd.pid"
NMBD_PIDFILE = "/run/samba/nmbd.pid"
SMBD_PIDFILE = "/run/samba/smbd.pid"


@synchronized
def start():
    startService(command="/usr/sbin/smbd",
                 args="-D",
                 donotify=True)

    startService(command="/usr/sbin/nmbd",
                 args="-D")

    if config.get("winbind", "no") == "yes":
        startService(command="/usr/sbin/winbindd",
                     args="-D")

@synchronized
def stop():
    stopService(pidfile=WINBINDD_PIDFILE,
                donotify=True)
    stopService(pidfile=NMBD_PIDFILE,
                donotify=True)
    stopService(pidfile=SMBD_PIDFILE,
                donotify=True)

def reload():
    if os.path.exists(WINBINDD_PIDFILE):
        os.kill(int(file(WINBINDD_PIDFILE).read().strip()), signal.SIGHUP)

    if os.path.exists(NMBD_PIDFILE):
        os.kill(int(file(NMBD_PIDFILE).read().strip()), signal.SIGHUP)

    if os.path.exists(SMBD_PIDFILE):
        os.kill(int(file(SMBD_PIDFILE).read().strip()), signal.SIGHUP)

def status():
    result = isServiceRunning(SMBD_PIDFILE) and isServiceRunning(NMBD_PIDFILE)
    if config.get("winbind", "no") == "yes":
        result = result and isServiceRunning(WINBINDD_PIDFILE)
    return result
