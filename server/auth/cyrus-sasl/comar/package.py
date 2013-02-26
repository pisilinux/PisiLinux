#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/etc/sasl2/sasldb2"):
        os.system("/usr/sbin/saslpasswd2 -f /etc/sasl2/sasldb2 -p login")
        os.system("/usr/sbin/saslpasswd2 -f /etc/sasl2/sasldb2 -d login")

    os.system("/bin/chown root:mail /etc/sasl2/sasldb2")
    os.system("/bin/chmod 0640 /etc/sasl2/sasldb2")
