#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("chown -R ntp:ntp /var/lib/ntp")
    os.system("chown -R root:ntp /etc/ntp/crypto")
    os.chmod("/etc/ntp/crypto", 0750)
