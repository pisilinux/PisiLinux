#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown gdm:gdm -R /var/lib/gdm")
    os.system("/bin/chown root:gdm -R /var/log/gdm")


