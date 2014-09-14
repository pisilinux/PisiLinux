#!/usr/bin/python

import os

UDEV_RULE = "/lib/udev/rules.d/64-iscan.rules"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/lib/iscan-data/make-policy-file --force --mode=udev --out-file=%s" % UDEV_RULE)

def postRemove():
    try:
        os.unlink(UDEV_RULE)
    except OSError, e:
        pass
