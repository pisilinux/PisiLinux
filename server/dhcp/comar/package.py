#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/var/lib/dhcpd/dhcpd.leases"):
        os.system("/bin/touch /var/lib/dhcpd/dhcpd.leases")

    if not os.path.exists("/var/lib/dhcpd/dhcpd6.leases"):
        os.system("/bin/touch /var/lib/dhcpd/dhcpd6.leases")

