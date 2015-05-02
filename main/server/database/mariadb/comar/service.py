# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType="server"
serviceDesc=_({"en": "MariaDB Database Server",
               "tr": "MariaDB Veritabanı Sunucusu"})

PIDFILE="/run/mysqld/mysqld.pid"
DAEMON="/usr/bin/mysqld"

@synchronized
def start():
    startService(command=DAEMON,
                 pidfile=PIDFILE,
                 detach=True,
                 donotify=True)
    #os.system("pidof mariadb_server + /usr/bin/mysqld > /run/mysqld/mysqld.pid")


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
