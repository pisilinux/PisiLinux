#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for f in ("pid", "defaultroute", "resolv.conf-backup"):
        if not os.path.exists("/run/vpnc/%s" % f):
            open("/run/vpnc/%s" % f, "w").write("")
