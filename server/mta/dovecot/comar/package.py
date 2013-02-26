#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown root:0 /var/run/dovecot")
    os.system("/bin/chown root:dovecot /var/run/dovecot/login")
    os.system("/bin/chmod 0755 /var/run/dovecot")
    os.system("/bin/chmod 0750 /var/run/dovecot/login")
    os.system("/bin/chmod a+x /etc/dovecot/ssl/mkcert.sh")

    if not os.path.exists("/etc/ssl/certs/dovecot.pem"):
        os.system("/etc/dovecot/ssl/mkcert.sh")
