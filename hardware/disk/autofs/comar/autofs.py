from comar.service import *
import os

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "Automount filesystems on demand",
                 "tr": "Dosya sistemi otomatik bağlayıcı"})
serviceConf = "autofs"

PIDFILE = "/run/autofs/autofs.pid"
AUTOMOUNT = "/usr/sbin/automount"

@synchronized
def start():
    startService(command=AUTOMOUNT,
                 args="%s --pid-file %s" % (config.get("OPTIONS", ""), PIDFILE),
                 donotify=True)

@synchronized
def reload():
    if os.path.exists(PIDFILE):
        # 1 is SIGHUP
        os.kill(int(open(PIDFILE, "r").read().strip()), 1)

@synchronized
def stop():
    stopService(pidfile=PIDFILE, donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)
