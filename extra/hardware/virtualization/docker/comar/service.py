from comar.service import *
import os

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "Docker Management Service",
                 "tr": "Docker Yönetim Hizmeti"})

serviceConf = "docker"
pidfile = "/var/run/docker.pid"
logfile = "/var/log/docker.log"

@synchronized
def start():
    startService(command="/usr/bin/docker",
                args="%s" % (config.get("DOCKER_OPTS", "")),
                pidfile="/var/run/docker.pid",
                chuid="root:docker",
                donotify=True)
                 
@synchronized
def stop():
    stopService(command="/usr/bin/docker",
                pidfile="/var/run/docker.pid",
                donotify=True)

def status():
    return isServiceRunning(pidfile)
