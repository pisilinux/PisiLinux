#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil

ownerships = {
        "/run/avahi-daemon"         : "avahi:avahi",
    }

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for directory,owners in ownerships.items():
        if os.path.exists(directory):
            os.system("/bin/chown %s %s" % (owners, directory))

    if os.path.exists("/etc/localtime"):
        if not os.path.isdir("/etc/avahi/etc"):
            os.makedirs("/etc/avahi/etc")
        shutil.copy("/etc/localtime", "/etc/avahi/etc/localtime")
