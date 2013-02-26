from comar.service import *
import os

serviceType = "local"
serviceDefault = "on"
serviceDesc = _({"en": "Store/Restore Mixer Levels",
                 "tr": "Karıştırıcı Seviyeleri Yönetimi"})

@synchronized
def start():
    # Store mixer levels
    os.system("/sbin/alsactl restore")

@synchronized
def stop():
    # Store mixer levels
    os.system("/sbin/alsactl store")

def status():
    return True
