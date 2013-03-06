from comar.service import *

serviceType = "local"
serviceDesc = _({
    "en": "Display Manager",
    "tr": "Görüntü Yöneticisi",
})
serviceDefault = "on"

pidFile = "/run/dm.pid"

@synchronized
def start(boot=False):
    if status():
        return

    #startDependencies("acpid")

    startService(command="/usr/bin/start-dm",
                 args="--boot" if boot else None,
                 detach=True,
                 pidfile=pidFile,
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidFile,
                donotify=True)

def status():
    return isServiceRunning(pidFile)

def ready():
    from pardus.sysutils import get_kernel_option

    if is_on() == "on" and "off" not in get_kernel_option("xorg"):
        start(boot=True)
