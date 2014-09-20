#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown kdm:kdm -R /var/lib/kdm")
