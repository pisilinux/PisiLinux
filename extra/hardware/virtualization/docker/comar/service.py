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
    os.system("/usr/bin/cgroupfs-mount")

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
    
    os.system("/usr/bin/cgroupfs-umount")

def status():
    return isServiceRunning(pidfile)
