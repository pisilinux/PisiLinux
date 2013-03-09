from comar.service import *

serviceType="server"
serviceDesc = _({"en": "S.M.A.R.T. monitoring daemon",
                 "tr": "S.M.A.R.T. disk izleme hizmeti"})

serviceConf = "smartd"
PIDFILE = "/run/smartd.pid"


@synchronized
def start():
    args = "-p %s" % PIDFILE
    if config.get("smartd_opts"):
        args = "%s %s" % (args, config.get("smartd_opts"))
    startService(command="/usr/sbin/smartd",
                 args=args,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def reload():
    # FIXME: That's bad.
    run("/usr/bin/killall -HUP smartd")

def status():
    return isServiceRunning(pidfile=PIDFILE)
