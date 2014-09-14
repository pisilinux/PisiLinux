#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("mkdir -p /var/dansguardian")
    os.system("/bin/chown dansguardian /var/dansguardian")
    os.system("/bin/chown dansguardian:dansguardian /var/log/dansguardian -R")
    os.system("/bin/chmod o-rwx /var/log/dansguardian")
