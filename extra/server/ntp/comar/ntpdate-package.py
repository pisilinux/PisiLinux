#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown root:wheel /usr/sbin/ntpdate")
    os.system("/bin/chmod 04710 /usr/sbin/ntpdate")
