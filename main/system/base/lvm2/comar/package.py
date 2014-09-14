#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/sbin/mudur_tmpfiles.py /usr/lib/tmpfiles.d/lvm2.conf")