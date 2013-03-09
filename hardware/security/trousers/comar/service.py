from comar.service import *

import platform
import glob
import os

serviceType = "local"
serviceDesc = _({"en": "TrouSerS TCG Core Services daemon",
                 "tr": "TrouSers TCG Hizmeti",
                })

MSG_NOTPM   = _({"en": "Failed starting trousers",
                 "tr": "trousers hizmeti başlatılamadı",
                })

TCSD = "/usr/sbin/tcsd"
PID_FILE = "/run/tcsd.pid"
DRIVER_DIR = "/lib/modules/%s/kernel/drivers/char/tpm"

def load_drivers():
    if config.has_key("TPM_MODULES"):
        drivers = config.get("TPM_MODULES").split()
    else:
        drivers = glob.glob1(DRIVER_DIR % platform.uname()[2], "tpm_*")

    for driver in drivers:
        os.system("modprobe -q %s" % driver.split(".ko")[0])

def check_drivers():
    return len(glob.glob("/sys/module/tpm_*")) > 0

@synchronized
def start():
    if not check_drivers():
        load_drivers()

    ret = startService(command=TCSD,
                       pidfile=PID_FILE)

    if ret != 0:
        # Probably there aren't any TPM devices
        fail(MSG_NOTPM)

@synchronized
def stop():
    stopService(pidfile=PID_FILE,
                donotify=True)

def status():
    return isServiceRunning(pidfile=PID_FILE)
