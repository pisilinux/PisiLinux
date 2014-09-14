from comar.service import *
import signal

serviceType="server"
serviceDesc = _({"en": "Avahi DNS Configuration Daemon",
                 "tr": "Avahi DNS Yapılandırma Hizmeti"})

PIDFILE = "/run/avahi-dnsconfd.pid"
DAEMON = "/usr/sbin/avahi-dnsconfd"

@synchronized
def start():
    startDependencies("avahi")
    startService(command=DAEMON,
                 args="-D",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

@synchronized
def reload():
    stopService(command=DAEMON,
                signal=signal.SIGHUP)

def status():
    return isServiceRunning(pidfile=PIDFILE)
