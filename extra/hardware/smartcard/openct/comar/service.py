from comar.service import *

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "OpenCT SmartCard Reader Service",
                 "tr": "OpenCT Akıllı Kart Okuyucu Servisi"})
serviceConf = "openct"

@synchronized
def start():
    startService(command="/usr/sbin/openct-control",
                 args="init",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/openct-control",
                args="shutdown",
                donotify=True)

def status():
    import os.path
    return os.path.exists("/run/openct/status")
