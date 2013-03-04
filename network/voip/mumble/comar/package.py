#/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for i in ["/var/lib/mumble-server", "/var/log/mumble-server", "/run/mumble-server", "/usr/sbin/murmurd"]:
        os.system("/bin/chown mumble-server:mumble-server %s" % i)

