#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chmod 2755 /usr/sbin/mlock")
    os.system("/bin/chown root:mail /usr/sbin/mlock")
