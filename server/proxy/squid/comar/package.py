#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown root:squid /usr/lib/squid/ncsa_auth")
    os.system("/bin/chown root:squid /usr/lib/squid/pam_auth")
    os.system("/bin/chown squid:squid /var/log/squid")
    os.system("/bin/chown squid:squid /var/cache/squid")
    os.system("/bin/chmod 4750 /usr/lib/squid/ncsa_auth")
    os.system("/bin/chmod 4750 /usr/lib/squid/pam_auth")
    os.system("/bin/chmod 0755 /var/log/squid")
    os.system("/bin/chmod 0755 /var/cache/squid")
