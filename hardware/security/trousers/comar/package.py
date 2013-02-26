#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.chmod("/etc/tcsd.conf", 0600)
    os.chmod("/var/lib/tpm", 0700)

    # os.chown only takes numeric uid/gid values
    os.system("/bin/chown tss:tss /etc/tcsd.conf")
    os.system("/bin/chown tss:tss /var/lib/tpm")
