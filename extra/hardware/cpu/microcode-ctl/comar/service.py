# -*- coding: utf-8 -*-
serviceConf = "microcode_ctl"
serviceType = "local"
serviceDefault = "conditional"
serviceDesc = _({"en": "Intel IA32 CPU Microcode Updater",
                 "tr": "Intel IA32 İşlemci Mikrokod Güncelleyicisi"
                 })

MSG_ERR_STRTSRVC = {"en": "Unable to start service.",
                    "tr": "Servis başlatılamadı.",
                    }
MSG_ERR_STOPSRVC = {"en": "Unable to stop service.",
                    "tr": "Servis durdurulamadı.",
                    }

from comar.service import *
import time, os

devicenode = config.get("MICROCODE_DEV", "/dev/cpu/microcode")
microcodefile = config.get("MICROCODE_FILE", "/lib/firmware/microcode.dat")

def checkIntel():
    if "Intel" in file("/proc/cpuinfo").read():
        return True
    else:
        return False

@synchronized
def start():
    run("/sbin/modprobe -q microcode")
    # wait for the device node
    time.sleep(3)
    ret = run("/usr/sbin/microcode_ctl -qu -d %s -f %s" % (devicenode, microcodefile))
    if ret == 0:
        notify("System.Service", "Changed", (script(), "started"))
    else:
        fail((MSG_ERR_STRTSRVC))

@synchronized
def stop():
    ret = 0
    if os.path.exists(devicenode):
        ret = run("/sbin/rmmod microcode")
    if ret == 0:
        notify("System.Service", "Changed", (script(), "stopped"))
    else:
        fail(_(MSG_ERR_STOPSRVC))

def ready():
    status = is_on()
    if status == "on" or (status == "conditional" and checkIntel()):
        start()

def status():
    return os.access(devicenode, os.F_OK)
