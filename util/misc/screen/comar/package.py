#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown root:utmp /usr/bin/screen")
    os.system("/bin/chmod 02755 /usr/bin/screen")
    os.system("/bin/chown root:utmp /var/run/screen")
    os.system("/bin/chmod 0755 /var/run/screen")

    # suid
    os.system("/bin/chmod u+s /usr/bin/screen")
    os.system("/bin/chmod go-w /var/run/screen")
