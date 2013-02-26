from comar.service import *
import signal

serviceType = "local"
serviceDesc = _({"en": "uShare UPnP A/V Media Server",
                 "tr": "uShare UPnP Ses/Görüntü Ortam Sunucu"})
serviceDefault = "off"

pidfile = "/var/run/ushare.pid"
command = "/usr/bin/ushare"

def check_ushare_dir():
    conf = open("/etc/ushare.conf")

    for line in conf.readlines():
        line = line.strip()
        if line.startswith("USHARE_DIR"):
            ushare_dir = line.split("=")[1]

    if not os.path.exists(ushare_dir):
        fail('uShare directory "%s" doesn\'t exist, please edit your /etc/ushare.conf and set a valid directory.' % ushare_dir)

    conf.close()

@synchronized
def start():
    check_ushare_dir()
    startService(command=command,
                 args="--cfg=/etc/ushare.conf -d",
                 pidfile=pidfile,
                 detach=True,
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidfile,
                donotify=True)

def reload():
    stopService(command=command,
                signal=signal.SIGHUP)

def status():
    return isServiceRunning(pidfile)
