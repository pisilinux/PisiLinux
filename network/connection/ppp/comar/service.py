# -*- coding: utf-8 -*-
from comar.service import *
import os
import shutil

serviceType = "local"
serviceDesc = _({"en": "ppp",
                 "tr": "ppp"})
serviceDefault = "conditional"

MSG_BACKEND_WARNING = _({
                        "en" : "FIXME",
                        "tr" : "FIXME"
                        })

@synchronized
def start():
    if not os.path.isdir("/run/ppp"): os.makedirs("/run/ppp")
    if not os.path.isfile("/run/ppp/resolv.conf"): shutil.copy2("/etc/resolv.conf", "/run/ppp")

@synchronized
def stop():
    pass

def status():
    pass