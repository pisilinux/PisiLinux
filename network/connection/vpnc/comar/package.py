#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for f in ("pid", "defaultroute", "resolv.conf-backup"):
        if not os.path.exists("/var/run/vpnc/%s" % f):
            open("/var/run/vpnc/%s" % f, "w").write("")
