#/usr/bin/python
# -*- coding: utf-8 -*-

import os

PUBLIC_FILES = ["hosts.conf", "ups.conf", "upssched.conf", "upsset.conf", "upsstats.html", "upsstats-single.html"]
PRIVATE_FILES = ["upsd.conf", "upsd.users", "upsmon.conf"]

STATE_DIR = "/var/lib/nut"

PRIVATE_USER = "ups"
PRIVATE_GROUP = "ups"


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for _file in PUBLIC_FILES:
        f = "/etc/nut/%s" % _file
        os.chmod(f, 0644)
        os.system("/bin/chown %s:%s %s" % ("root", "root", f))

    for _file in PRIVATE_FILES:
        f = "/etc/nut/%s" % _file
        os.chmod(f, 0640)
        os.system("/bin/chown %s:%s %s" % (PRIVATE_USER, PRIVATE_GROUP, f))

    os.chmod(STATE_DIR, 0770)
    os.system("/bin/chown %s:%s %s" % (PRIVATE_USER, PRIVATE_GROUP, STATE_DIR))

