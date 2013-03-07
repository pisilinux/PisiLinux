#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for dirs in ("/run/mediatomb", "/etc/mediatomb", "/var/lib/mediatomb", "/var/log/mediatomb"):
        os.system("/bin/chown mediatomb:mediatomb %s" % dirs)
#        os.system("/bin/chmod -R 755 %s" % dirs)
