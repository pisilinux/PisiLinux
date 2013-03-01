# -*- coding: utf-8 -*-
import os
import subprocess
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Squid Proxy Daemon",
                 "tr": "Squid Vekil Servisi"})

MSG_ERR_CACHEDIRNOTDEF = _({"en": "cache_dir defined in %s doesnt\'t exist, please edit your config file and set a valid directory.",
                            "tr": "%s ayar dosyasında tanımlı olan cache_dir klasörü sistemde bulunmuyor, lütfen geçerli bir yol girin."})

serviceConf = "squid"

PIDFILE = "/run/squid.pid"
SQUIDCONF = "/etc/squid/squid.conf"

def check_cache():
    conf = open(SQUIDCONF)

    for line in conf.readlines():
        line = line.strip()
        if line.startswith("cache_dir"):
            CACHEDIR = line.split()[2]

    if not os.path.exists(CACHEDIR):
        fail(MSG_ERR_CACHEDIRNOTDEF % SQUIDCONF)

    if not os.path.exists("%s/00" % CACHEDIR):
        subprocess.call(["/usr/sbin/squid", "-z", "-F"])

@synchronized
def start():
    check_cache()
    startService(command="/usr/sbin/squid",
                 args="%s" % config.get("SQUID_OPTS"),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/squid",
                args="-k shutdown",
                donotify=True)

def reload():
    stopService(command="/usr/sbin/squid",
                args="-k reconfigure")

def status():
    return isServiceRunning(PIDFILE)
