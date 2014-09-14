from comar.service import *
import os

serviceType = "local"
serviceConf = "irqbalance"
serviceDefault = "conditional"
serviceDesc = _({"en": "Irqbalance Daemon",
                 "tr": "Irqbalance Servisi"})

@synchronized
def start():
    args = ""
    oneshot = config.get("ONESHOT")
    affinity = config.get("IRQ_AFFINITY_MASK")

    if oneshot == "yes" and os.path.exists("/run/irqbalance.pid"):
        return

    if oneshot == "yes":
        args += ("--oneshot -f")

    if affinity:
        os.environ["IRQBALANCE_BANNED_CPUS"] = affinity

    startService(command="/usr/sbin/irqbalance",
                 args=args, donotify=True)
    os.system("pidof -o %PPID /usr/sbin/irqbalance > /run/irqbalance.pid")

@synchronized
def stop():
    stopService(command="/usr/sbin/irqbalance",
                pidfile="/run/irqbalance.pid",
                donotify=True)

    try:
        os.unlink("/var/lock/subsys/irqbalance")
    except:
        pass

def ready():
    status = is_on()
    if status == "on" or (status == "conditional" and os.path.exists("/sys/devices/system/cpu/cpu1")):
        start()

def status():
    return isServiceRunning("/run/irqbalance.pid")
