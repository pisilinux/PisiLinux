#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown clamav:clamav /var/lib/clamav -R")
    os.system("/bin/chown clamav:clamav /run/clamav -R")
    os.system("/bin/chown clamav:clamav /var/log/clamav -R")
