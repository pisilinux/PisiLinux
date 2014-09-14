#/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -f -R dialout:dialout /var/spool/fax")
    os.system("/usr/bin/mkfifo -m 600 /var/spool/fax/FIFO")
    os.system("/bin/chown dialout:dialout /var/spool/fax/FIFO")
