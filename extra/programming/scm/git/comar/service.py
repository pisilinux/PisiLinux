from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "GIT Server",
                 "tr": "GIT Sunucusu"})
serviceDefault = "off"
serviceConf = "git-daemon"

@synchronized
def start():
    startService(command="/usr/bin/git",
                 args="daemon \
                       --base-path=/pub/scm \
                       --pid-file=/run/git-daemon.pid \
                       --user-path=public_git \
                       --detach \
                       --export-all \
                       --syslog \
                       --verbose %s" % config.get("GITDAEMON_OPTS"),
                 pidfile="/run/git-daemon.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/git-daemon.pid",
                donotify=True)

def status():
    return isServiceRunning("/run/git-daemon.pid")
