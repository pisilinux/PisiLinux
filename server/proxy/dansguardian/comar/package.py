#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown dansguardian:dansguardian /var/log/dansguardian -R")
    os.system("/bin/chmod o-rwx /var/log/dansguardian")
