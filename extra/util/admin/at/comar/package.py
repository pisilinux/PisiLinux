#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown root:root /var/spool/at")
    os.system("/bin/chmod 1770 /var/spool/at")
    os.system("/bin/chown root:root /var/spool/at/.SEQ")
    os.system("/bin/chmod 0600 /var/spool/at/.SEQ")
    os.system("/bin/chown root:root /var/spool/at/spool")
    os.system("/bin/chmod 1770 /var/spool/at/spool")
