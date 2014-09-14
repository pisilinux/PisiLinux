from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "SVN Server",
                 "tr": "SVN Sunucusu"})
serviceConf = "svnserve"

PIDFILE = "/var/svn/svnserve.pid"

# Note that "/etc/conf.d/svnserve" passes --root=/var/svn by default

@synchronized
def start():
    startService(command="/usr/bin/svnserve",
                 args="--pid-file=%s %s" % (PIDFILE, config.get("SVNSERVE_OPTS")),
                 chuid="%s:%s" % (config.get("SVNSERVE_USER"), config.get("SVNSERVE_GROUP")),
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)
