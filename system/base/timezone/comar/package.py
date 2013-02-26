#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    # Migration 2008->2009
    # Use the timezone script to determine the timezone and write
    # it into /etc/timezone if it doesn't exist.

    # e.g. tz will be 'Europe/Istanbul'
    tz = os.popen("/usr/bin/timezone").read().strip()

    if tz == "Not found":
        if os.path.exists("/etc/timezone"):
            tz = open("/etc/timezone").read()
        else:
            tz = "Europe/Istanbul"

    # This file is used by CRDA to set regulatory domain for WLAN interfaces
    if tz and not os.path.exists("/etc/timezone"):
        open("/etc/timezone", "w").write("%s" % tz)

    # Don't use symlink for /etc/localtime. Replace existing
    # symlinks by the corresponding tz file using zic.
    if tz and os.path.exists(os.path.join("/usr/share/zoneinfo", tz)):
        ret = subprocess.call(["/usr/sbin/zic", "-l", tz])

    """
    if tz and os.path.islink("/etc/localtime"):
        tzfile = os.path.join("/usr/share/zoneinfo", tz)
        if os.path.exists(tzfile):
            try:
                os.unlink("/etc/localtime")
                shutil.copyfile(tzfile, "/etc/localtime")
            except:
                pass
    """
