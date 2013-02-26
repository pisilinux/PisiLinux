#!/usr/bin/python

import os

# Update global mime databases, mime database format may change (0.70)
def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/bin/update-mime-database /usr/share/mime")
