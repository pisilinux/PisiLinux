serviceType = "server"
serviceDesc = _({"en": "Memory Caching Server",
                 "tr": "Hafıza Önbellekleme Sunucusu"})

from comar.service import *

@synchronized
def start():
    args = (
        config.get("PORT", "11211"),
        config.get("LISTENON", "127.0.0.1"),
        config.get("MEMUSAGE", "64"),
        config.get("MAXCONN", "1024"),
        config.get("MEMCACHED_RUNAS", "memcached"),
    )
    startService(command="/usr/bin/memcached",
                 args="-d -P /run/memcached/memcached.pid -p %s -l %s -m %s -c %s -u %s" % args,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/memcached/memcached.pid",
                donotify=True)
    try:
        os.unlink("/run/memcached/memcached.pid")
    except:
        pass

def status():
    return isServiceRunning(pidfile="/run/memcached/memcached.pid")
