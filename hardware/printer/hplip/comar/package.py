#/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # Update hplip queues if any
    os.system("/usr/bin/hpcups-update-ppds")
