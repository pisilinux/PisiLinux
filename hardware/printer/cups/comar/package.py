#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

ownerships = {
        "/run/cups"             : "root:lp",
        "/var/log/cups"         : "root:lp",
    }

CUPSD_CONFIG_FILE = "/etc/cups/cupsd.conf"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for directory,owners in ownerships.items():
        if os.path.exists(directory):
            os.system("chown %s %s" % (owners, directory))

    # Replace possible pnpadmin leftover from cupsd.conf
    if os.path.exists(CUPSD_CONFIG_FILE):
        cupsd = open(CUPSD_CONFIG_FILE, "r").read()
        open(CUPSD_CONFIG_FILE, "w").write(re.sub("pnpadmin", "lpadmin", cupsd))
