#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    ugstr = "root:utmp"

    os.spawnvp(os.P_NOWAIT, "/bin/chown", ["/bin/chown", ugstr, "/usr/sbin/utempter"])
    os.spawnvp(os.P_NOWAIT, "/bin/chmod", ["/bin/chmod", "2775", "/usr/sbin/utempter"])

    for file in ["/var/log/wtmp", "/run/utmp"]:
        if os.path.exists(file):
            os.spawnvp(os.P_NOWAIT, "/bin/chown", ["/bin/chown", ugstr, file])
            os.spawnvp(os.P_NOWAIT, "/bin/chmod", ["/bin/chmod", "664", file])
