#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/var/log/sa/sa21"):
        os.system("/usr/lib/sa/sadc -F -L -")
