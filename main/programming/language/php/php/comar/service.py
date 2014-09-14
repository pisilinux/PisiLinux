from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "The PHP FastCGI Process Manager",
                 "tr": "The PHP FastCGI Süreç Yöneticisi"})

PIDFILE = "/run/php-fpm.pid"
CONFIG = "/etc/php/ext/php-fpm.conf"

@synchronized
def start():
    startService(command="/usr/sbin/php-fpm",
                 args="-D -y %s" % CONFIG,
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except OSError:
        pass

def status():
    return isServiceRunning(PIDFILE)
