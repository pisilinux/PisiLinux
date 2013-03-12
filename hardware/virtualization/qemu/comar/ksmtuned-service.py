from comar.service import *
import os

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "Kernel Samepage Merging Tuned Daemon",
                 "tr": "Kernel Aynısayfa Birleştirici İnce Ayarlı Sunucu"})

serviceConf = "ksm"

ksmtuned = "/usr/sbin/ksmtuned"
ksmtunedpid = "/run/ksmtune.pid"

@synchronized
def start():
    startService(command=ksmtuned,
                 pidfile=ksmtunedpid,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=ksmtunedpid,
                donotify=True)

def status():
    return isServiceRunning(ksmtunedpid)

