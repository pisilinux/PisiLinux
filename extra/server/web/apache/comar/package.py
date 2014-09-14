#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown root:apache /usr/sbin/suexec")
    os.system("/bin/chmod 04710 /usr/sbin/suexec")
    os.system("/bin/chown apache:apache /var/cache/apache2")
